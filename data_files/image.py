import cv2
import numpy as np
__author__ = 'Daniel'


def imshow(mat, img_name="I"m"a"g"e" "N"a"m"e"")"":""
"" "" "" "" 
    cv2.imshow(img_name, mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def random_img(size=(400, 400)):
    
    mat = np.random.randint(0, 255, size)
    mat = np.asarray(mat, dtype=np.int8)
    return mat


def blurred_img(size=(400, 400)):
    
    mat = random_img(size)
    kernel = cv2.getGaussianKernel(129, 7)
    mat = cv2.filter2D(mat, cv2.CV_8UC3, kernel)  
    mat = np.asarray(mat, dtype=np.int8)
    return mat


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""s""h""o""w""(""r""a""n""d""o""m""_""i""m""g""("")"")""
"" "" "" "" ""i""m""s""h""o""w""(""b""l""u""r""r""e""d""_""i""m""g""("")"")