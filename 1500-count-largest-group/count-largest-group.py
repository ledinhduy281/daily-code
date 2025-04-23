class Solution:
    def countLargestGroup(self, n: int) -> int:
        # hashMap = collections.Counter()
        # for i in range(1, n + 1):
        #     key = sum([int(x) for x in str(i)])
        #     hashMap[key] += 1
        # maxValue = max(hashMap.values())
        # count = sum(1 for v in hashMap.values() if v == maxValue)
        # return count

        categorii=[0]*37 #ignor 0. am 36 de categorii
        tablouSumaCifrelor=[0]*(n+1)
        for i in range(1,n+1):
            sc=i%10+tablouSumaCifrelor[i//10]
            tablouSumaCifrelor[i]=sc
            categorii[sc] += 1
        valMax=max(categorii)
        nrGrupuri=categorii.count(valMax)
        return nrGrupuri