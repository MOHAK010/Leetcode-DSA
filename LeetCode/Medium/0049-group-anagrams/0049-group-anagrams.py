class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        group = {}

        for word in strs:
            key = sorted(word)
            keys = "".join(key)
        
            if keys in group:
                group[keys].append(word)
            else:
                group[keys] = [word]
        return list(group.values())