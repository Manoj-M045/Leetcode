class Solution:
    def average(self, salary: list[int]) -> float:
        salary.sort()
        x=len(salary)-2
        s=sum(salary[1:len(salary)-1])
        return s/x
        
        