

import numpy as np
import cv2
import os
from contextlib import contextmanager
import itertools as it

image_extensions = ['.bmp', '.jpg', '.jpeg', '.png', '.tif', '.tiff', '.pbm', '.pgm', '.ppm']

class Bunch(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)
    def __str__(self):
        return str(self.__dict__)

def splitfn(fn):
    path, fn = os.path.split(fn)
    name, ext = os.path.splitext(fn)
    return path, name, ext

def anorm2(a):
    return (a*a).sum(-1)
def anorm(a):
    return np.sqrt( anorm2(a) )

def homotrans(H, x, y):
    xs = H[0, 0]*x + H[0, 1]*y + H[0, 2]
    ys = H[1, 0]*x + H[1, 1]*y + H[1, 2]
    s  = H[2, 0]*x + H[2, 1]*y + H[2, 2]
    return xs/s, ys/s

def to_rect(a):
    a = np.ravel(a)
    if len(a) == 2:
        a = (0, 0, a[0], a[1])
    return np.array(a, np.float64).reshape(2, 2)

def rect2rect_mtx(src, dst):
    src, dst = to_rect(src), to_rect(dst)
    cx, cy = (dst[1] - dst[0]) / (src[1] - src[0])
    tx, ty = dst[0] - src[0] * (cx, cy)
    M = np.float64([[ cx,  0, tx],
                    [  0, cy, ty],
                    [  0,  0,  1]])
    return M


def lookat(eye, target, up = (0, 0, 1)):
    fwd = np.asarray(target, np.float64) - eye
    fwd /= anorm(fwd)
    right = np.cross(fwd, up)
    right /= anorm(right)
    down = np.cross(fwd, right)
    R = np.float64([right, down, fwd])
    tvec = -np.dot(R, eye)
    return R, tvec

def mtx2rvec(R):
    w, u, vt = cv2.SVDecomp(R - np.eye(3))
    p = vt[0] + u[:,0]*w[0]    
    c = np.dot(vt[0], p)
    s = np.dot(vt[1], p)
    axis = np.cross(vt[0], vt[1])
    return axis * np.arctan2(s, c)

def draw_str(dst, (x, y), s):
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.CV_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.CV_AA)

class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv2.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv2.imshow(self.windowname, self.dests[0])

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.line(dst, self.prev_pt, pt, color, 5)
            self.dirty = True
            self.prev_pt = pt
            self.show()
        else:
            self.prev_pt = None



_jet_data =   {'red':   ((0., 0, 0), (0.35, 0, 0), (0.66, 1, 1), (0.89,1, 1),
                         (1, 0.5, 0.5)),
               'green': ((0., 0, 0), (0.125,0, 0), (0.375,1, 1), (0.64,1, 1),
                         (0.91,0,0), (1, 0, 0)),
               'blue':  ((0., 0.5, 0.5), (0.11, 1, 1), (0.34, 1, 1), (0.65,0, 0),
                         (1, 0, 0))}

cmap_data = { 'jet' : _jet_data }

def make_cmap(name, n=256):
    data = cmap_data[name]
    xs = np.linspace(0.0, 1.0, n)
    channels = []
    eps = 1e-6
    for ch_name in ['blue', 'green', 'red']:
        ch_data = data[ch_name]
        xp, yp = [], []
        for x, y1, y2 in ch_data:
            xp += [x, x+eps]
            yp += [y1, y2]
        ch = np.interp(xs, xp, yp)
        channels.append(ch)
    return np.uint8(np.array(channels).T*255)

def nothing(*arg, **kw):
    pass

def clock():
    return cv2.getTickCount() / cv2.getTickFrequency()

@contextmanager
def Timer(msg):
    print msg, '...',
    start = clock()
    try:
        yield
    finally:
        print "%"."2"f" "m"s"" ""%"" ""(""(""c""l""o""c""k""("")""-""s""t""a""r""t"")""*""1""0""0""0"")""
""
""c""l""a""s""s"" ""S""t""a""t""V""a""l""u""e"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""s""m""o""o""t""h""_""c""o""e""f"" ""="" ""0"".""5"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""v""a""l""u""e"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""s""m""o""o""t""h""_""c""o""e""f"" ""="" ""s""m""o""o""t""h""_""c""o""e""f""
"" "" "" "" ""d""e""f"" ""u""p""d""a""t""e""(""s""e""l""f"","" ""v"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""v""a""l""u""e"" ""i""s"" ""N""o""n""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""v""a""l""u""e"" ""="" ""v""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c"" ""="" ""s""e""l""f"".""s""m""o""o""t""h""_""c""o""e""f""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""v""a""l""u""e"" ""="" ""c"" ""*"" ""s""e""l""f"".""v""a""l""u""e"" ""+"" ""(""1"".""0""-""c"")"" ""*"" ""v""
""
""c""l""a""s""s"" ""R""e""c""t""S""e""l""e""c""t""o""r"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""w""i""n"","" ""c""a""l""l""b""a""c""k"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""i""n"" ""="" ""w""i""n""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""c""a""l""l""b""a""c""k"" ""="" ""c""a""l""l""b""a""c""k""
"" "" "" "" "" "" "" "" ""c""v""2"".""s""e""t""M""o""u""s""e""C""a""l""l""b""a""c""k""(""w""i""n"","" ""s""e""l""f"".""o""n""m""o""u""s""e"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""s""t""a""r""t"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t"" ""="" ""N""o""n""e""
"" "" "" "" ""d""e""f"" ""o""n""m""o""u""s""e""(""s""e""l""f"","" ""e""v""e""n""t"","" ""x"","" ""y"","" ""f""l""a""g""s"","" ""p""a""r""a""m"")"":""
"" "" "" "" "" "" "" "" ""x"","" ""y"" ""="" ""n""p"".""i""n""t""1""6""(""[""x"","" ""y""]"")"" ""#"" ""B""U""G""
"" "" "" "" "" "" "" "" ""i""f"" ""e""v""e""n""t"" ""=""="" ""c""v""2"".""E""V""E""N""T""_""L""B""U""T""T""O""N""D""O""W""N"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""s""t""a""r""t"" ""="" ""(""x"","" ""y"")""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""d""r""a""g""_""s""t""a""r""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""f""l""a""g""s"" ""&"" ""c""v""2"".""E""V""E""N""T""_""F""L""A""G""_""L""B""U""T""T""O""N"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""x""o"","" ""y""o"" ""="" ""s""e""l""f"".""d""r""a""g""_""s""t""a""r""t""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""x""0"","" ""y""0"" ""="" ""n""p"".""m""i""n""i""m""u""m""(""[""x""o"","" ""y""o""]"","" ""[""x"","" ""y""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""x""1"","" ""y""1"" ""="" ""n""p"".""m""a""x""i""m""u""m""(""[""x""o"","" ""y""o""]"","" ""[""x"","" ""y""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""x""1""-""x""0"" "">"" ""0"" ""a""n""d"" ""y""1""-""y""0"" "">"" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t"" ""="" ""(""x""0"","" ""y""0"","" ""x""1"","" ""y""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""c""t"" ""="" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""s""t""a""r""t"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""r""e""c""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""c""a""l""l""b""a""c""k""(""r""e""c""t"")""
"" "" "" "" ""d""e""f"" ""d""r""a""w""(""s""e""l""f"","" ""v""i""s"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
"" "" "" "" "" "" "" "" ""x""0"","" ""y""0"","" ""x""1"","" ""y""1"" ""="" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t""
"" "" "" "" "" "" "" "" ""c""v""2"".""r""e""c""t""a""n""g""l""e""(""v""i""s"","" ""(""x""0"","" ""y""0"")"","" ""(""x""1"","" ""y""1"")"","" ""(""0"","" ""2""5""5"","" ""0"")"","" ""2"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
"" "" "" "" ""@""p""r""o""p""e""r""t""y""
"" "" "" "" ""d""e""f"" ""d""r""a""g""g""i""n""g""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""d""r""a""g""_""r""e""c""t"" ""i""s"" ""n""o""t"" ""N""o""n""e""
""
""
""d""e""f"" ""g""r""o""u""p""e""r""(""n"","" ""i""t""e""r""a""b""l""e"","" ""f""i""l""l""v""a""l""u""e""=""N""o""n""e"")"":""
"" "" "" "" ""'""'""'""g""r""o""u""p""e""r""(""3"","" ""'""A""B""C""D""E""F""G""'"","" ""'""x""'"")"" ""-""-"">"" ""A""B""C"" ""D""E""F"" ""G""x""x""'""'""'""
"" "" "" "" ""a""r""g""s"" ""="" ""[""i""t""e""r""(""i""t""e""r""a""b""l""e"")""]"" ""*"" ""n""
"" "" "" "" ""r""e""t""u""r""n"" ""i""t"".""i""z""i""p""_""l""o""n""g""e""s""t""(""f""i""l""l""v""a""l""u""e""=""f""i""l""l""v""a""l""u""e"","" ""*""a""r""g""s"")""
""
""d""e""f"" ""m""o""s""a""i""c""(""w"","" ""i""m""g""s"")"":""
"" "" "" "" ""'""'""'""M""a""k""e"" ""a"" ""g""r""i""d"" ""f""r""o""m"" ""i""m""a""g""e""s"".""
""
"" "" "" "" ""w"" "" "" "" ""-""-"" ""n""u""m""b""e""r"" ""o""f"" ""g""r""i""d"" ""c""o""l""u""m""n""s""
"" "" "" "" ""i""m""g""s"" ""-""-"" ""i""m""a""g""e""s"" ""(""m""u""s""t"" ""h""a""v""e"" ""s""a""m""e"" ""s""i""z""e"" ""a""n""d"" ""f""o""r""m""a""t"")""
"" "" "" "" ""'""'""'""
"" "" "" "" ""i""m""g""s"" ""="" ""i""t""e""r""(""i""m""g""s"")""
"" "" "" "" ""i""m""g""0"" ""="" ""i""m""g""s"".""n""e""x""t""("")""
"" "" "" "" ""p""a""d"" ""="" ""n""p"".""z""e""r""o""s""_""l""i""k""e""(""i""m""g""0"")""
"" "" "" "" ""i""m""g""s"" ""="" ""i""t"".""c""h""a""i""n""(""[""i""m""g""0""]"","" ""i""m""g""s"")""
"" "" "" "" ""r""o""w""s"" ""="" ""g""r""o""u""p""e""r""(""w"","" ""i""m""g""s"","" ""p""a""d"")""
"" "" "" "" ""r""e""t""u""r""n"" ""n""p"".""v""s""t""a""c""k""(""m""a""p""(""n""p"".""h""s""t""a""c""k"","" ""r""o""w""s"")"")""
""
""d""e""f"" ""g""e""t""s""i""z""e""(""i""m""g"")"":""
"" "" "" "" ""h"","" ""w"" ""="" ""i""m""g"".""s""h""a""p""e""["":""2""]""
"" "" "" "" ""r""e""t""u""r""n"" ""w"","" ""h""
""
""d""e""f"" ""m""d""o""t""(""*""a""r""g""s"")"":""
"" "" "" "" ""r""e""t""u""r""n"" ""r""e""d""u""c""e""(""n""p"".""d""o""t"","" ""a""r""g""s"")""
""
""d""e""f"" ""d""r""a""w""_""k""e""y""p""o""i""n""t""s""(""v""i""s"","" ""k""e""y""p""o""i""n""t""s"","" ""c""o""l""o""r"" ""="" ""(""0"","" ""2""5""5"","" ""2""5""5"")"")"":""
"" "" "" "" ""f""o""r"" ""k""p"" ""i""n"" ""k""e""y""p""o""i""n""t""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""x"","" ""y"" ""="" ""k""p"".""p""t""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""v""2"".""c""i""r""c""l""e""(""v""i""s"","" ""(""i""n""t""(""x"")"","" ""i""n""t""(""y"")"")"","" ""2"","" ""c""o""l""o""r"")""
""
