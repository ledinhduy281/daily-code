class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # num = [0] * 100
        # ret = 0
        # for x, y in dominoes:
        #     val = x * 10 + y if x <= y else y * 10 + x
        #     ret += num[val]
        #     num[val] += 1
        # return ret
        # seen = collections.Counter()
        # equal_pairs = 0
        # for a, b in dominoes:
        #     k = frozenset((a, b))
        #     if k in seen:
        #         equal_pairs += seen[k]
        #     seen[k] += 1
        # return equal_pairs
        # time: O(n)
        # space: O(n)

        seen = [0] * 100
        equal_pairs = 0
        for a, b in dominoes:
            val = a * 10 + b if a <= b else b * 10 + a
            equal_pairs += seen[val]
            seen[val] += 1
        return equal_pairs
        # time: O(n)
        # space: O(n)