class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if(i not in magazine):
                return False
            else:
                if(ransomNote.count(i)>magazine.count(i)):
                    return False
        return True
        