import os
import subprocess
import sys 

class CVSHandler():
    
    def __init__(self, cvs):
        self._roots_cache = {}
        self._not_tracked_cache = set()
        self.cvs = cvs

    def _get_root_from_cache(self, directory):
        
        if directory in self._roots_cache:
            return directory
        if os.path.dirname(directory) == directory:
            return None
        return self._get_root_from_cache(os.path.dirname(directory))

    def get_source_files(self, directory):
        if directory in self._not_tracked_cache:
            return None

        root_dir = self._get_root_from_cache(directory)
        if not root_dir:
            try:
                
                root_dir = self.cvs._get_root(directory)
                self._roots_cache[root_dir] = self.cvs._get_tracked_files(root_dir)
            except Exception as e:
                
                self._not_tracked_cache.add(directory)
                return None

        files = self._roots_cache[root_dir]
        
        if directory != root_dir:
            rel_dir = os.path.relpath(directory, root_dir)
            files = [f[len(rel_dir)+1:] for f in files if f.startswith(rel_dir)]
        return files
 

class Git():
    @staticmethod
    def _get_root(directory):
        return run_command("c"d" "%"s" "&"&" "g"i"t" "r"e"v"-"p"a"r"s"e" "-"-"s"h"o"w"-"t"o"p"l"e"v"e"l"" ""%"" ""d""i""r""e""c""t""o""r""y"")"".""s""t""r""i""p""("")""
"" "" "" "" ""@""s""t""a""t""i""c""m""e""t""h""o""d""
"" "" "" "" ""d""e""f"" ""_""g""e""t""_""t""r""a""c""k""e""d""_""f""i""l""e""s""(""d""i""r""e""c""t""o""r""y"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""u""n""_""c""o""m""m""a""n""d""( The default directory handler uses the 'find' external program to return all the files inside a given directory up to MAX_depth depth (ie, if maxdepth=2, returns all files inside that dir, and all files in a subdir of that directory) check first if the given directory is inside a git tracked project, if no, check with mercurial, if no, fallback to the default handler 