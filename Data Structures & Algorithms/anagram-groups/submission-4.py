class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        groups_dict = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tup = tuple(count)
            if tup in groups_dict:
                groups_dict[tup].append(s)
            else:
                groups_dict[tup] = [s]
        return list(groups_dict.values())