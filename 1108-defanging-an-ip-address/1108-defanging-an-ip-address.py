class Solution:
    def defangIPaddr(self, address: str) -> str:
        word=address.split('.')
        s="[.]".join(word)
        return s
        