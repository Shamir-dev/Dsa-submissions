from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            distance = sqrt((points[i][0])**2 + (points[i][1])**2)
            distances.append((distance, points[i]))
        
            distances.sort() # converted into array

        print(distances)
        
      #  return [point for distance, point in distances[:k]]
        result = [] 
        for distance, point in distances[:k]:
          result.append(point) 
        return result