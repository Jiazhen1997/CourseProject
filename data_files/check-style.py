

import os
import subprocess
import tempfile
import sys
import filecmp
import optparse
import shutil
import difflib
import re

def hg_modified_files():
    files = os.popen ('hg st -nma')
    return [filename.strip() for filename in files]

def copy_file(filename):
    [tmp,pathname] = tempfile.mkstemp()
    src = open(filename, 'r')
    dst = open(pathname, 'w')
    for line in src:
        dst.write(line)
    dst.close()
    src.close()
    return pathname


def uncrustify_config_file(level):
    level2 = 
    level1 = 
    level0 = 
    [tmp,pathname] = tempfile.mkstemp()
    dst = open(pathname, 'w')
    dst.write(level0)
    if level >= 1:
        dst.write(level1)
    if level >= 2:
        dst.write(level2)
    dst.close()
    return pathname

class PatchChunkLine:
    SRC = 1
    DST = 2
    BOTH = 3
    def __init__(self):
        self.__type = 0
        self.__line = ''
    def set_src(self,line):
        self.__type = self.SRC
        self.__line = line
    def set_dst(self,line):
        self.__type = self.DST
        self.__line = line
    def set_both(self,line):
        self.__type = self.BOTH
        self.__line = line
    def append_to_line(self, s):
        self.__line = self.__line + s
    def line(self):
        return self.__line
    def is_src(self):
        return self.__type == self.SRC or self.__type == self.BOTH
    def is_dst(self):
        return self.__type == self.DST or self.__type == self.BOTH
    def write(self, f):
        if self.__type == self.SRC:
            f.write('-%s\n' % self.__line)
        elif self.__type == self.DST:
            f.write('+%s\n' % self.__line)
        elif self.__type == self.BOTH:
            f.write(' %s\n' % self.__line)
        else:
            raise Exception('invalid patch')
    

class PatchChunk:
    def __init__(self, src_pos, dst_pos):
        self.__lines = []
        self.__src_pos = int(src_pos)
        self.__dst_pos = int(dst_pos)
    def src_start(self):
        return self.__src_pos
    def add_line(self,line):
        self.__lines.append(line)
    def src(self):
        src = []
        for line in self.__lines:
            if line.is_src():
                src.append(line)
        return src
    def dst(self):
        dst = []
        for line in self.__lines:
            if line.is_dst():
                dst.append(line)
        return dst
    def src_len(self):
        return len(self.src())
    def dst_len(self):
        return len(self.dst())
    def write(self,f):
        f.write('@@ -%d,%d +%d,%d @@\n' % (self.__src_pos, self.src_len(),
                                           self.__dst_pos, self.dst_len()))
        for line in self.__lines:
            line.write(f)

class Patch:
    def __init__(self):
        self.__src = ''
        self.__dst = ''
        self.__chunks = []
    def add_chunk(self, chunk):
        self.__chunks.append(chunk)
    def chunks(self):
        return self.__chunks
    def set_src(self,src):
        self.__src = src
    def set_dst(self,dst):
        self.__dst = dst
    def apply(self,filename):
        
        return
    def write(self,f):
        f.write('--- %s\n' % self.__src )
        f.write('+++ %s\n' % self.__dst )
        for chunk in self.__chunks:
            chunk.write(f)

def parse_patchset(generator):
    src_file = re.compile('^--- (.*)$')
    dst_file = re.compile('^\+\+\+ (.*)$')
    chunk_start = re.compile('^@@ -([0-9]+),([0-9]+) \+([0-9]+),([0-9]+) @@')
    src = re.compile('^-(.*)$')
    dst = re.compile('^\+(.*)$')
    both = re.compile('^ (.*)$')
    patchset = []
    current_patch = None
    for line in generator:
        m = src_file.search(line)
        if m is not None:
            current_patch = Patch()
            patchset.append(current_patch)
            current_patch.set_src(m.group(1))
            continue
        m = dst_file.search(line)
        if m is not None:
            current_patch.set_dst(m.group(1))
            continue
        m = chunk_start.search(line)
        if m is not None:
            current_chunk = PatchChunk(m.group(1), m.group(3))
            current_patch.add_chunk(current_chunk)
            continue
        m = src.search(line)
        if m is not None:
            l = PatchChunkLine()
            l.set_src(m.group(1))
            current_chunk.add_line(l)
            continue
        m = dst.search(line)
        if m is not None:
            l = PatchChunkLine()
            l.set_dst(m.group(1))
            current_chunk.add_line(l)
            continue
        m = both.search(line)
        if m is not None:
            l = PatchChunkLine()
            l.set_both(m.group(1))
            current_chunk.add_line(l)
            continue
        raise Exception()
    return patchset

def remove_trailing_whitespace_changes(patch_generator):
    whitespace = re.compile('^(.*)([ \t]+)$')
    patchset = parse_patchset(patch_generator)
    for patch in patchset:
        for chunk in patch.chunks():
            src = chunk.src()
            dst = chunk.dst()
            try:
                for i in range(0,len(src)):
                    s = src[i]
                    d = dst[i]
                    m = whitespace.search(s.line())
                    if m is not None and m.group(1) == d.line():
                        d.append_to_line(m.group(2))
            except:
                return patchset
    return patchset


def indent(source, debug, level):
    output = tempfile.mkstemp()[1]
    
    cfg = uncrustify_config_file(level)
    if debug:
        sys.stderr.write('original file=' + source + '\n')
        sys.stderr.write('uncrustify config file=' + cfg + '\n')
        sys.stderr.write('temporary file=' + output + '\n')
    try:
        uncrust = subprocess.Popen(['uncrustify', '-c', cfg, '-f', source, '-o', output],
                                   stdin = subprocess.PIPE,
                                   stdout = subprocess.PIPE,
                                   stderr = subprocess.PIPE)
        (out, err) = uncrust.communicate('')
        if debug:
            sys.stderr.write(out)
            sys.stderr.write(err)
    except OSError:
        raise Exception ('uncrustify not installed')
    
    src = open(source, 'r')
    dst = open(output, 'r')
    diff = difflib.unified_diff(src.readlines(), dst.readlines(), 
                                fromfile=source, tofile=output)
    src.close()
    dst.close()
    if debug:
        initial_diff = tempfile.mkstemp()[1]
        sys.stderr.write('initial diff file=' + initial_diff + '\n')
        tmp = open(initial_diff, 'w')
        tmp.writelines(diff)
        tmp.close()
    final_diff = tempfile.mkstemp()[1]
    if level < 3:
        patchset = remove_trailing_whitespace_changes(diff);
        dst = open(final_diff, 'w')
        if len(patchset) != 0:
            patchset[0].write(dst)
        dst.close()
    else:
        dst = open(final_diff, 'w')
        dst.writelines(diff)
        dst.close()
            
            
    
    if debug:
        sys.stderr.write('final diff file=' + final_diff + '\n')
    shutil.copyfile(source,output)
    patch = subprocess.Popen(['patch', '-p1', '-i', final_diff, output],
                             stdin = subprocess.PIPE,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)
    (out, err) = patch.communicate('')
    if debug:
        sys.stderr.write(out)
        sys.stderr.write(err)
    return output
 


def indent_files(files, diff=False, debug=False, level=0, inplace=False):
    output = []
    for f in files:
        dst = indent(f, debug=debug, level=level)
        output.append([f,dst])

    
    if inplace:
        for src,dst in output:
            shutil.copyfile(dst,src)
        return True

    
    failed = []
    for src,dst in output:
        if filecmp.cmp(src,dst) == 0:
            failed.append([src, dst])
    if len(failed) > 0:
        if not diff:
            print 'Found %u badly indented files:' % len(failed)
            for src,dst in failed:
                print '  ' + src
        else:
            for src,dst in failed:
                s = open(src, 'r').readlines()
                d = open(dst, 'r').readlines()
                for line in difflib.unified_diff(s, d, fromfile=src, tofile=dst):
                    sys.stdout.write(line)
        return False
    return True

def run_as_hg_hook(ui, repo, **kwargs):
    
    from mercurial import lock, error
    lock.LockError = error.LockError
    
    files = hg_modified_files()
    if not indent_files(files, inplace=False):
        return True
    return False

def run_as_main():
    parser = optparse.OptionParser()
    parser.add_option('--debug', action='store_true', dest='debug', default=False,
                      help='Output some debugging information')
    parser.add_option('-l', '--level', type='int', dest='level', default=0,
                      help="L"e"v"e"l" "o"f" "s"t"y"l"e" "c"o"n"f"o"r"m"a"n"c"e":" "h"i"g"h"e"r" "l"e"v"e"l"s" "i"n"c"l"u"d"e" "a"l"l" "l"o"w"e"r" "l"e"v"e"l"s"." ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" 