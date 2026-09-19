from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       pairs= []
       for point in points:
            x, y = point 
            distance = x*x + y*y
            pairs.append((distance, point)) 
       pairs.sort()
       return [p for dist, p in  pairs[:k]]