class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # az=n*2-1
        # ans=[0]*az
        # def dfs(pos, viz=0):
        #     if pos==az:
        #         return viz.bit_count()==n
        #     if ans[pos]!=0:
        #         return dfs(pos+1, viz)
        #     for j in range(n, 0, -1):
        #         if (viz>>j)&1==1: 
        #             continue
        #         next_pos=pos+j if j>1 else pos

        #         if next_pos>=az or ans[next_pos]!=0:
        #             continue
        #         ans[pos]=ans[next_pos]=j
        #         viz|=(1<<j)

        #         if dfs(pos+1, viz):
        #             return True
        #         ans[pos]=ans[next_pos]=0
        #         viz&=(~(1<<j))
        #     return False

        # dfs(0)
        # return ans 
        res = [0] * (2 * n - 1)
        seen = set()
        def backtrack(i):
            if i == len(res):
                return True
            if res[i]:
                return backtrack(i+1)
            for j in range(n,0,-1):
                if j in seen:
                    continue
                seen.add(j)
                res[i] = j
                if j == 1:
                    if backtrack(i+1):
                        return True
                elif j + i < len(res) and res[i+j] == 0:
                    res[i+j] = j
                    if backtrack(i+1):
                        return True
                    res[i+j] = 0
                res[i] = 0
                seen.remove(j)
            return False
        backtrack(0)
        return res 
        