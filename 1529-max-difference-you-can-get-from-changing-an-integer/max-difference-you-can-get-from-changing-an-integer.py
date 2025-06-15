class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # Maximize: replace first non-9 digit with 9
        for ch in num_str:
            if ch != '9':
                a = int(num_str.replace(ch, '9'))
                break
        else:
            a = num  # already all 9s
        
        # Minimize: replace first digit with 1 or others with 0
        if num_str[0] != '1':
            b = int(num_str.replace(num_str[0], '1'))
        else:
            for i in range(1, len(num_str)):
                if num_str[i] not in ['0', num_str[0]]:
                    b = int(num_str.replace(num_str[i], '0'))
                    break
            else:
                b = num  # already minimal
        
        return a - b
