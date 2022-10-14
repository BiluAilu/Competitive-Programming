class Solution:
    def sortSentence(self, s: str) -> str:
        str_list = list(s.split())
        new_list = []
        str_list.sort(key = lambda x: x[-1])
        for i in str_list:
            new_list.append(i[:-1])
        stri = " ".join(new_list)
        return stri