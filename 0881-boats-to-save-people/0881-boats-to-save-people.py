class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        s=0
        e=len(people)-1
        boats=0
        people.sort()
        while s <= e:
            if(people[s]+people[e]<=limit):
                s+=1
                e-=1
            else:
                e-=1
            boats+=1
        return boats
        