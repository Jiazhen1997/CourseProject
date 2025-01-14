
__author__ = 'Danyang'

class Point:
    def __init__(self, a=0, b=0):
        
        self.x = a
        self.y = b

class Solution:
    def maxPoints_complicated(self, points):
        

        hash_map = {}  

        length = len(points)
        for i in xrange(length):
            for j in xrange(i+1, length):
                point1 = points[i]
                point2 = points[j]
                if point1.x == point2.x:
                    key = (1 << 32, point1.x)
                else:
                    slope = float(point1.y-point2.y)/(point1.x-point2.x)
                    intersection = slope*point1.x - point1.y

                    slope = int(slope*1000) 
                    intersection = int(intersection*1000) 

                    key = (slope, intersection)  

                if key not in hash_map:
                    hash_map[key] = [0 for _ in points]
                hash_map[key][i] = 1  
                hash_map[key][j] = 1


        if (length<=1):
            return length

        if(len(hash_map)==0):
            return 0

        maxa = -1<<32
        for key, item in hash_map.items():
            
            current = item.count(1)
            if current>maxa:
                maxa = current

        return maxa

    def maxPoints(self, points):
        
        maxa = -1<<32
        length = len(points)
        if (length<=1):
            return length

        for i in xrange(length):
            hash_map = {}
            duplicate = 1 
            for j in xrange(length):
                if i==j:
                    continue

                point1 = points[i]
                point2 = points[j]
                if point1.x==point2.x and point1.y==point2.y:
                    duplicate += 1
                    continue
                if point1.x==point2.x:
                    key = 1<<32
                else:
                    slope = float(point1.y-point2.y)/(point1.x-point2.x)
                    slope = int(slope*10000) 
                    
                    key = slope

                if key not in hash_map:
                    hash_map[key] = 0
                hash_map[key]+=1


            if hash_map:
                max_key = max(hash_map, key=hash_map.get)
                max_value = hash_map[max_key]
            else:
                max_value  = 0
            maxa = max(maxa, max_value+duplicate)

        return maxa






if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""o""i""n""t""s"" ""="" ""[""(""5""6""0"","" ""2""4""8"")"","" ""(""0"","" ""1""6"")"","" ""(""3""0"","" ""2""5""0"")"","" ""(""9""5""0"","" ""1""8""7"")"","" ""(""6""3""0"","" ""2""7""7"")"","" ""(""9""5""0"","" ""1""8""7"")"","" ""(""-""2""1""2"","" ""-""2""6""8"")"","" ""(""-""2""8""7"","" ""-""2""2""2"")"","" ""(""5""3"","" ""3""7"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""-""2""8""0"","" ""-""1""0""0"")"","" ""(""-""1"","" ""-""1""4"")"","" ""(""-""5"","" ""4"")"","" ""(""-""3""5"","" ""-""3""8""7"")"","" ""(""-""9""5"","" ""1""1"")"","" ""(""-""7""0"","" ""-""1""3"")"","" ""(""-""7""0""0"","" ""-""2""7""4"")"","" ""(""-""9""5"","" ""1""1"")"","" ""(""-""2"","" ""-""3""3"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""3"","" ""6""2"")"","" ""(""-""4"","" ""-""4""7"")"","" ""(""1""0""6"","" ""9""8"")"","" ""(""-""7"","" ""-""6""5"")"","" ""(""-""8"","" ""-""7""1"")"","" ""(""-""8"","" ""-""1""4""7"")"","" ""(""5"","" ""5"")"","" ""(""-""5"","" ""-""9""0"")"","" ""(""-""4""2""0"","" ""-""1""5""8"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""-""4""2""0"","" ""-""1""5""8"")"","" ""(""-""3""5""0"","" ""-""1""2""9"")"","" ""(""-""4""7""5"","" ""-""5""3"")"","" ""(""-""4"","" ""-""4""7"")"","" ""(""-""3""8""0"","" ""-""3""7"")"","" ""(""0"","" ""-""2""4"")"","" ""(""3""5"","" ""2""9""9"")"","" ""(""-""8"","" ""-""7""1"")"","" ""(""-""2"","" ""-""6"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""8"","" ""2""5"")"","" ""(""6"","" ""1""3"")"","" ""(""-""1""0""6"","" ""-""1""4""6"")"","" ""(""5""3"","" ""3""7"")"","" ""(""-""7"","" ""-""1""2""8"")"","" ""(""-""5"","" ""-""1"")"","" ""(""-""3""1""8"","" ""-""3""9""0"")"","" ""(""-""1""5"","" ""-""1""9""1"")"","" ""(""-""6""6""5"","" ""-""8""5"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""3""1""8"","" ""3""4""2"")"","" ""(""7"","" ""1""3""8"")"","" ""(""-""5""7""0"","" ""-""6""9"")"","" ""(""-""9"","" ""-""4"")"","" ""(""0"","" ""-""9"")"","" ""(""1"","" ""-""7"")"","" ""(""-""5""1"","" ""2""3"")"","" ""(""4"","" ""1"")"","" ""(""-""7"","" ""5"")"","" ""(""-""2""8""0"","" ""-""1""0""0"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""7""0""0"","" ""3""0""6"")"","" ""(""0"","" ""-""2""3"")"","" ""(""-""7"","" ""-""4"")"","" ""(""-""2""4""6"","" ""-""1""8""4"")"","" ""(""3""5""0"","" ""1""6""1"")"","" ""(""-""4""2""4"","" ""-""5""1""2"")"","" ""(""3""5"","" ""2""9""9"")"","" ""(""0"","" ""-""2""4"")"","" ""(""-""1""4""0"","" ""-""4""2"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""-""7""6""0"","" ""-""1""0""1"")"","" ""(""-""9"","" ""-""9"")"","" ""(""1""4""0"","" ""7""4"")"","" ""(""-""2""8""5"","" ""-""2""1"")"","" ""(""-""3""5""0"","" ""-""1""2""9"")"","" ""(""-""6"","" ""9"")"","" ""(""-""6""3""0"","" ""-""2""4""5"")"","" ""(""7""0""0"","" ""3""0""6"")"","" ""(""1"","" ""-""1""7"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""0"","" ""1""6"")"","" ""(""-""7""0"","" ""-""1""3"")"","" ""(""1"","" ""2""4"")"","" ""(""-""3""2""8"","" ""-""2""6""0"")"","" ""(""-""3""4"","" ""2""6"")"","" ""(""7"","" ""-""5"")"","" ""(""-""3""7""1"","" ""-""4""5""1"")"","" ""(""-""5""7""0"","" ""-""6""9"")"","" ""(""0"","" ""2""7"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""-""7"","" ""-""6""5"")"","" ""(""-""9"","" ""-""1""6""6"")"","" ""(""-""4""7""5"","" ""-""5""3"")"","" ""(""-""6""8"","" ""2""0"")"","" ""(""2""1""0"","" ""1""0""3"")"","" ""(""7""0""0"","" ""3""0""6"")"","" ""(""7"","" ""-""6"")"","" ""(""-""3"","" ""-""5""2"")"","" ""(""-""1""0""6"","" ""-""1""4""6"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""5""6""0"","" ""2""4""8"")"","" ""(""1""0"","" ""6"")"","" ""(""6"","" ""1""1""9"")"","" ""(""0"","" ""2"")"","" ""(""-""4""1"","" ""6"")"","" ""(""7"","" ""1""9"")"","" ""(""3""0"","" ""2""5""0"")""]""
""
"" "" "" "" ""p""o""i""n""t""s"" ""="" ""[""P""o""i""n""t""(""p""o""i""n""t""[""0""]"","" ""p""o""i""n""t""[""1""]"")"" ""f""o""r"" ""p""o""i""n""t"" ""i""n"" ""p""o""i""n""t""s""]""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""o""i""n""t""s""(""p""o""i""n""t""s"")""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""o""i""n""t""s""(""p""o""i""n""t""s"")""=""=""2""2