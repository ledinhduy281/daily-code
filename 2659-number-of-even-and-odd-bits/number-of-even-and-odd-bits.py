class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bin_ = bin(n)[2:]
        bin_n = bin_[::-1]
        odd_indexed= []
        even_indexed =[]
        for i in range(len(bin_n)):
            if i%2==0 and bin_n[i]=='1':
                even_indexed.append(bin_n[i])
            elif i%2!=0 and bin_n[i]=='1':
                odd_indexed.append(bin_n[i])
        return [len(even_indexed), len(odd_indexed)]
            
        
        