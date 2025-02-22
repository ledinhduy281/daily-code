class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = []
        for i, word in enumerate(S.split()):
            if word[0].lower() not in 'aeiou':
                word = word[1:]+word[0]
                
            ans.append(word + 'ma' + 'a'*(i+1))
            
        return ' '.join(ans)