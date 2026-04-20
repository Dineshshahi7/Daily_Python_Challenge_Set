'''
Group Anagrams

Problem:
Given a list of strings, group the anagrams together.
'''

def group_anagrams(words):
    anagram_dict = {}

    for word in words:
        key = "".join(sorted(word))
        
        if key not in anagram_dict:
            anagram_dict[key] = []
        
        anagram_dict[key].append(word)

    return list(anagram_dict.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))