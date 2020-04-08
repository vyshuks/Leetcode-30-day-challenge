# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


from collections import defaultdict
def group_anagrams(anagrams):
    d = {}
    result = defaultdict(list)
    for anagram in anagrams:
        sorted_str = "".join(sorted(anagram))
        result[sorted_str].append(anagram)
        
    final = []
    for lst in result:
        final.append(result[lst])
    return final

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

