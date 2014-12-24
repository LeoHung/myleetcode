# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def gcd(self, a, b):
        if a < b: 
            return self.gcd(b, a)

        y = a % b 
        if y == 0:
            return b 
        else:
            return self.gcd(b, y)

    def gen_pair(self, v1, v2):
        if v1 == 0 :
            return (0, 1)
        if v2 == 0:
            return (1, 0)
        if v1 < 0 and v2 < 0:
            return self.gen_pair(-v1, -v2)
        if v1 > 0 and v2 < 0:
            return self.gen_pair(-v1, -v2)

        if v1 < 0:
            v1 = -v1
            base = self.gcd(v1, v2)
            v1, v2 = v1/base, v2/base
            return (-v1, v2)
        else:
            base = self.gcd(v1, v2)
            v1, v2 = v1/base, v2/base
            return (v1, v2)

    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        p_l = len(points)
        if p_l <= 2:
            return p_l

        max_points = 0 
        for i in range(p_l):
            p1 = points[i]
            cache = {}
            same = 0 
            for j in range(i+1, p_l):
                p2 = points[j]
                v1, v2 = (p1.x - p2.x), (p1.y - p2.y)
                if v1 == 0 and v2 == 0:
                    same += 1
                    continue 

                v1, v2 = self.gen_pair(v1, v2)


                if (v1, v2) not in cache:
                    cache[(v1, v2)] = 0

                cache[(v1, v2)] += 1

            # print cache

            if len(cache) > 0:
                max_points = max(max(cache.values())+same +1, max_points)
            else:
                max_points = max(same + 1, max_points)

        return max_points

if __name__ == "__main__":
    print Solution().maxPoints([Point(1, 1), Point(2, 2), Point(1,1), Point(1, -1)])
    print Solution().maxPoints([Point(0, 0), Point(-1, -1), Point(2, 2)])
    print Solution().maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)])
    print Solution().maxPoints([Point(0, 0), Point(1, 1), Point(0, 0)])
    print Solution().maxPoints([Point(0, 0), Point(0, 0), Point(0, 0)])