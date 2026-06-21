from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_count = Counter(t)  # what we need
        window_count = {}
        
        left = 0
        min_len = float('inf')
        min_window = ""
        have, need = 0, len(t_count)
        
        for right, c in enumerate(s):
            window_count[c] = window_count.get(c, 0) + 1
            
            if c in t_count and window_count[c] == t_count[c]:
                have += 1  # one character fulfilled
            
            while have == need:
                # update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right+1]
                
                # shrink from left
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                left += 1
        
        return min_window