import numpy as np
import cv2
from time import clock
from numpy import pi, sin, cos
import common

class VideoSynthBase(object):
    def __init__(self, size=None, noise=0.0, bg = None, **params):
        self.bg = None
        self.frame_size = (640, 480)
        if bg is not None:
            self.bg = cv2.imread(bg, 1)
            h, w = self.bg.shape[:2]
            self.frame_size = (w, h)
            
        if size is not None:
            w, h = map(int, size.split('x'))
            self.frame_size = (w, h)
            self.bg = cv2.resize(self.bg, self.frame_size)

        self.noise = float(noise)

    def render(self, dst):
        pass
        
    def read(self, dst=None):
        w, h = self.frame_size

        if self.bg is None:
            buf = np.zeros((h, w, 3), np.uint8)
        else:
            buf = self.bg.copy()

        self.render(buf)

        if self.noise > 0.0:
            noise = np.zeros((h, w, 3), np.int8)
            cv2.randn(noise, np.zeros(3), np.ones(3)*255*self.noise)
            buf = cv2.add(buf, noise, dtype=cv2.CV_8UC3)
        return True, buf

class Chess(VideoSynthBase):
    def __init__(self, **kw):
        super(Chess, self).__init__(**kw)

        w, h = self.frame_size

        self.grid_size = sx, sy = 10, 7
        white_quads = []
        black_quads = []
        for i, j in np.ndindex(sy, sx):
            q = [[j, i, 0], [j+1, i, 0], [j+1, i+1, 0], [j, i+1, 0]]
            [white_quads, black_quads][(i + j) % 2].append(q)
        self.white_quads = np.float32(white_quads)
        self.black_quads = np.float32(black_quads)

        fx = 0.9
        self.K = np.float64([[fx*w, 0, 0.5*(w-1)],
                        [0, fx*w, 0.5*(h-1)],
                        [0.0,0.0,      1.0]])

        self.dist_coef = np.float64([-0.2, 0.1, 0, 0])
        self.t = 0

    def draw_quads(self, img, quads, color = (0, 255, 0)):
        img_quads = cv2.projectPoints(quads.reshape(-1, 3), self.rvec, self.tvec, self.K, self.dist_coef) [0]
        img_quads.shape = quads.shape[:2] + (2,) 
        for q in img_quads:
            cv2.fillConvexPoly(img, np.int32(q*4), color, cv2.CV_AA, shift=2)

    def render(self, dst):
        t = self.t
        self.t += 1.0/30.0
        
        sx, sy = self.grid_size
        center = np.array([0.5*sx, 0.5*sy, 0.0])
        phi = pi/3 + sin(t*3)*pi/8
        c, s = cos(phi), sin(phi)
        ofs = np.array([sin(1.2*t), cos(1.8*t), 0]) * sx * 0.2
        eye_pos = center + np.array([cos(t)*c, sin(t)*c, s]) * 15.0 + ofs
        target_pos = center + ofs

        R, self.tvec = common.lookat(eye_pos, target_pos)
        self.rvec = common.mtx2rvec(R)

        self.draw_quads(dst, self.white_quads, (245, 245, 245))
        self.draw_quads(dst, self.black_quads, (10, 10, 10))



classes = dict(chess=Chess)

def create_capture(source):
    
    try: source = int(source)
    except ValueError: pass
    else:
        return cv2.VideoCapture(source)
    source = str(source).strip()
    if source.startswith('synth'):
        ss = filter(None, source.split(':'))
        params = dict( s.split('=') for s in ss[1:] )
        try: Class = classes[params['class']]
        except: Class = VideoSynthBase

        return Class(**params)
    return cv2.VideoCapture(source)


presets = dict(
    empty = 'synth:',
    lena = 'synth:bg=../cpp/lena.jpg:noise=0.1',
    chess = 'synth:class=chess:bg=../cpp/lena.jpg:noise=0.1:size=640x480'
)

if __name__ == '__main__':
    import sys
    import getopt

    print 'USAGE: video.py [--shotdir <dir>] [source0] [source1] ...'
    print "s"o"u"r"c"e":" "'"<"i"n"t">"'" "o"r" "'"<"f"i"l"e"n"a"m"e">"'" "o"r" "'"s"y"n"t"h":"<"p"a"r"a"m"s">"'""
"" "" "" "" ""p""r""i""n""t""
""
"" "" "" "" ""a""r""g""s"","" ""s""o""u""r""c""e""s"" ""="" ""g""e""t""o""p""t"".""g""e""t""o""p""t""(""s""y""s"".""a""r""g""v""[""1"":""]"","" ""'""'"","" ""'""s""h""o""t""d""i""r""=""'"")""
"" "" "" "" ""a""r""g""s"" ""="" ""d""i""c""t""(""a""r""g""s"")""
"" "" "" "" ""s""h""o""t""d""i""r"" ""="" ""a""r""g""s"".""g""e""t""(""'""-""-""s""h""o""t""d""i""r""'"","" ""'"".""'"")""
"" "" "" "" ""i""f"" ""l""e""n""(""s""o""u""r""c""e""s"")"" ""=""="" ""0"":""
"" "" "" "" "" "" "" "" ""s""o""u""r""c""e""s"" ""="" ""["" ""p""r""e""s""e""t""s""[""'""c""h""e""s""s""'""]"" ""]""
""
"" "" "" "" ""p""r""i""n""t"" ""'""P""r""e""s""s"" ""S""P""A""C""E"" ""t""o"" ""s""a""v""e"" ""c""u""r""r""e""n""t"" ""f""r""a""m""e""'""
""
"" "" "" "" ""c""a""p""s"" ""="" ""m""a""p""(""c""r""e""a""t""e""_""c""a""p""t""u""r""e"","" ""s""o""u""r""c""e""s"")""
"" "" "" "" ""s""h""o""t""_""i""d""x"" ""="" ""0""
"" "" "" "" ""w""h""i""l""e"" ""T""r""u""e"":""
"" "" "" "" "" "" "" "" ""i""m""g""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"","" ""c""a""p"" ""i""n"" ""e""n""u""m""e""r""a""t""e""(""c""a""p""s"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"","" ""i""m""g"" ""="" ""c""a""p"".""r""e""a""d""("")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""m""g""s"".""a""p""p""e""n""d""(""i""m""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""v""2"".""i""m""s""h""o""w""(""'""c""a""p""t""u""r""e"" ""%""d""'"" ""%"" ""i"","" ""i""m""g"")""
"" "" "" "" "" "" "" "" ""c""h"" ""="" ""c""v""2"".""w""a""i""t""K""e""y""(""1"")""
"" "" "" "" "" "" "" "" ""i""f"" ""c""h"" ""=""="" ""2""7"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
"" "" "" "" "" "" "" "" ""i""f"" ""c""h"" ""=""="" ""o""r""d""(""'"" ""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""i"","" ""i""m""g"" ""i""n"" ""e""n""u""m""e""r""a""t""e""(""i""m""g""s"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""n"" ""="" ""'""%""s""/""s""h""o""t""_""%""d""_""%""0""3""d"".""b""m""p""'"" ""%"" ""(""s""h""o""t""d""i""r"","" ""i"","" ""s""h""o""t""_""i""d""x"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""v""2"".""i""m""w""r""i""t""e""(""f""n"","" ""i""m""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""f""n"","" ""'""s""a""v""e""d""'""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""h""o""t""_""i""d""x"" ""+""="" ""1""
