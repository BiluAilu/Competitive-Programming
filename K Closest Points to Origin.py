class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp=[]
        minK=[]
        for i in points:
            temp.append((abs(i[0])**2 + abs(i[1])**2,(i[0], i[1])))
        temp=sorted(temp)
        for i in range (k):
            minK.append(temp[i][1])
        return minK