import subprocess

__author__ = 'Daniel'


def basic_child_process():
    
    proc1 = subprocess.Popen(
        ['echo', 'Hello from the child!'],
        stdout = subprocess.PIPE
    )
    proc2 = subprocess.Popen(
        ['sleep', '2'],
        stdout=subprocess.PIPE
    )
    print "."P"o"p"e"n" "i"s" "n"o"n"-"b"l"o"c"k"i"n"g""
"" "" "" "" ""o""u""t"","" ""e""r""r"" ""="" ""p""r""o""c""1"".""c""o""m""m""u""n""i""c""a""t""e""("")""
"" "" "" "" ""p""r""i""n""t"" ""o""u""t""
""
"" "" "" "" ""p""r""i""n""t"" 
    .poll() to get the status of the child process
    