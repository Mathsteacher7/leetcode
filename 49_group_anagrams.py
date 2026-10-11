class Solution:  # solution for O(n x k log k)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict_of_anagrams_keys = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in dict_of_anagrams_keys:
                dict_of_anagrams_keys[sorted_string].append(string)
            else:
                dict_of_anagrams_keys[sorted_string] = [string]
        return list(dict_of_anagrams_keys.values())
