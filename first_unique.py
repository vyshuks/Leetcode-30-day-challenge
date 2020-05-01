"""
You have a queue of integers, you need to retrieve the
first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer
of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.


Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique",
"add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

"""
from typing import List
from collections import OrderedDict, Counter


class FirstUnique:

    def __init__(self, nums: List[int]):
        self._map = OrderedDict()
        self.counter = Counter(nums)
        for num in nums:
            if self.counter[num] == 1:
                self._map[num]=1

    def showFirstUnique(self) -> int:
        if not self._map:
            return -1
        return next(iter(self._map))



    def add(self, value: int) -> None:
        if self.counter[value] > 1:
            return
        elif self.counter[value]==1:
            self._map.pop(value)
        else:
            self._map[value] = 1
        self.counter[value] += 1




obj = FirstUnique([2,3,5])
obj.add(5)
obj.add(2)
print(obj.showFirstUnique())
obj.add(3)
print(obj.showFirstUnique())

