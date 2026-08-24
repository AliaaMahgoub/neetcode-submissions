class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        groups_dict = {}
        for s in strs:
            tup = (0,)*26
            for c in list(s):
                tup = tup[:alphabet.index(c)] + (tup[alphabet.index(c)]+1,) + tup[alphabet.index(c) + 1:]
            if tup in groups_dict.keys():
                groups_dict[tup].append(s)
            else:
                groups_dict[tup] = [s]
        return list(groups_dict.values())