class Solution:
    def canConstruct(self, ransomnote: str, magazine: str) -> bool:
        random = {}
        for i in range(len(magazine)):
            if magazine[i] in random:
                random[magazine[i]] += 1
            else:
                random[magazine[i]] = 1
    
        for j in range(len(ransomnote)):
            if ransomnote[j] not in random:
                return False
            else:
                random[ransomnote[j]] -= 1
            
            if random[ransomnote[j]] < 0:
                return False
        return True