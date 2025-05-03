class Solution:
    # def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #     res = float('inf')
    #     for x in range(1, 7):
    #         res = min(res, self.getRotation(tops, bottoms, x))
    #         res = min(res, self.getRotation(bottoms, tops, x))
    #     return -1 if res == float('inf') else res

    # def getRotation(self, tops, bottoms, target):
    #     rotations = 0
    #     for i in range(len(tops)):
    #         if tops[i] == target:
    #             continue
    #         if bottoms[i] == target:
    #             rotations += 1
    #         else:
    #             return float('inf')
    #     return rotations  
    def minDominoRotations(self, A, B):
        for x in [A[0],B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1