class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        return len(d := [i for i, (c1, c2) in enumerate(zip(s1, s2)) if c1 != c2]) == 0 or (len(d) == 2 and s1[d[0]] == s2[d[1]] and s1[d[1]] == s2[d[0]])