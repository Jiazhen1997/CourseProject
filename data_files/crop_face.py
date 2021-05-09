
































import sys, math, Image

def Distance(p1,p2):
  dx = p2[0] - p1[0]
  dy = p2[1] - p1[1]
  return math.sqrt(dx*dx+dy*dy)

def ScaleRotateTranslate(image, angle, center = None, new_center = None, scale = None, resample=Image.BICUBIC):
  if (scale is None) and (center is None):
    return image.rotate(angle=angle, resample=resample)
  nx,ny = x,y = center
  sx=sy=1.0
  if new_center:
    (nx,ny) = new_center
  if scale:
    (sx,sy) = (scale, scale)
  cosine = math.cos(angle)
  sine = math.sin(angle)
  a = cosine/sx
  b = sine/sx
  c = x-nx*a-ny*b
  d = -sine/sy
  e = cosine/sy
  f = y-nx*d-ny*e
  return image.transform(image.size, Image.AFFINE, (a,b,c,d,e,f), resample=resample)

def CropFace(image, eye_left=(0,0), eye_right=(0,0), offset_pct=(0.2,0.2), dest_sz = (70,70)):
  
  offset_h = math.floor(float(offset_pct[0])*dest_sz[0])
  offset_v = math.floor(float(offset_pct[1])*dest_sz[1])
  
  eye_direction = (eye_right[0] - eye_left[0], eye_right[1] - eye_left[1])
  
  rotation = -math.atan(float(eye_direction[1])/float(eye_direction[0]))
  
  dist = Distance(eye_left, eye_right)
  
  reference = dest_sz[0] - 2.0*offset_h
  
  scale = float(dist)/float(reference)
  
  image = ScaleRotateTranslate(image, center=eye_left, angle=rotation)
  
  crop_xy = (eye_left[0] - scale*offset_h, eye_left[1] - scale*offset_v)
  crop_size = (dest_sz[0]*scale, dest_sz[1]*scale)
  image = image.crop((int(crop_xy[0]), int(crop_xy[1]), int(crop_xy[0]+crop_size[0]), int(crop_xy[1]+crop_size[1])))
  
  image = image.resize(dest_sz, Image.ANTIALIAS)
  return image
  
if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" ""i""m""a""g""e"" ""="" "" ""I""m""a""g""e"".""o""p""e""n""(