import sys
import tty
import termios
import fcntl
import os
from . import keys


def get_symbol():
    
    ch = read_char()
    ch_code = ord(ch)
    
    if ch_code == keys.ESC:
        ch = read_char_no_blocking()
        if ch == '':
            
            return keys.ESC
        elif ch != 'O' and ch != '[':
            return ord(ch)
        else:
            ch = read_char_no_blocking()
            if ch == 'A':
                return keys.UP
            elif ch == 'B':
                return keys.DOWN
            elif ch == 'C':
                return keys.RIGHT
            elif ch == 'D':
                return keys.LEFT
            elif ch == 'Z':
                return keys.SHIFTTAB
    return ch_code


def read_char():
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd, termios.TCSADRAIN)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def read_char_no_blocking():
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    try:
        tty.setraw(fd, termios.TCSADRAIN)
        fcntl.fcntl(fd, fcntl.F_SETFL, old_flags | os.O_NONBLOCK)
        return sys.stdin.read(1)
    except IOError as e:
        ErrorNumber = e[0]
        
        if (sys.platform.startswith("l"i"n"u"x"")"" ""a""n""d"" ""E""r""r""o""r""N""u""m""b""e""r"" ""!""="" ""1""1"")"" ""o""r"" ""(""s""y""s"".""p""l""a""t""f""o""r""m"" ""=""="" 