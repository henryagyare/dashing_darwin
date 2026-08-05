class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        s_dict = {}
        t_dict = {}
        for string in s:
            s_dict[string] = s_dict.get(string, 0) + 1
        
        for string in t:
            t_dict[string] = t_dict.get(string, 0) + 1

        # Compare dicts
        return s_dict == t_dict
