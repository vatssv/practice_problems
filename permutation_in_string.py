class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1map = [0] * 26
        s2map = [0] * 26
        
        if len(s2) < len(s1):
            return False
        
        for i in range(0, len(s1)):
            s1map[ord(s1[i])-ord('a')] += 1
            s2map[ord(s2[i])-ord('a')] += 1
            
        count = 0
        for i in range(0, 26):
            if s1map[i] == s2map[i]:
                count += 1
        
        for i in range(0, len(s2)-len(s1)):
            r, l = ord(s2[i + len(s1)])-ord('a'), ord(s2[i])-ord('a')
            if count == 26:
                return True
            s2map[r] += 1
            if s1map[r] == s2map[r]:
                count += 1
            elif s1map[r] + 1 == s2map[r]:
                count -= 1
            s2map[l] -= 1
            if s2map[l] == s1map[l]:
                count += 1
            elif s1map[l] - 1 == s2map[l]:
                count -= 1
        return count == 26