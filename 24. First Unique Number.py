from collections import deque


class FirstUnique:
    def __init__(self, nums):
        self.queue = deque()
        self.count = {}
        self.unique_order = deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self):
        while self.unique_order and self.count[self.unique_order[0]] > 1:
            self.unique_order.popleft()
        if self.unique_order:
            return self.unique_order[0]
        return -1

    def add(self, value):
        if value in self.count:
            self.count[value] += 1
        else:
            self.count[value] = 1
            self.unique_order.append(value)

        self.queue.append(value)
        self._cleanup_unique_order()

    def _cleanup_unique_order(self):
        while self.unique_order and self.count[self.unique_order[0]] > 1:
            self.unique_order.popleft()


# Example Usage:
firstUnique = FirstUnique([2, 3, 5])
print(firstUnique.showFirstUnique())  # return 2
firstUnique.add(5)  # the queue is now [2, 3, 5, 5]
print(firstUnique.showFirstUnique())  # return 2
firstUnique.add(2)  # the queue is now [2, 3, 5, 5, 2]
print(firstUnique.showFirstUnique())  # return 3
firstUnique.add(3)  # the queue is now [2, 3, 5, 5, 2, 3]
print(firstUnique.showFirstUnique())  # return -1

firstUnique = FirstUnique([7, 7, 7, 7, 7, 7])
print(firstUnique.showFirstUnique())  # return -1
firstUnique.add(7)  # the queue is now [7, 7, 7, 7, 7, 7, 7]
firstUnique.add(3)  # the queue is now [7, 7, 7, 7, 7, 7, 7, 3]
firstUnique.add(3)  # the queue is now [7, 7, 7, 7, 7, 7, 7, 3, 3]
firstUnique.add(7)  # the queue is now [7, 7, 7, 7, 7, 7, 7, 3, 3, 7]
firstUnique.add(17)  # the queue is now [7, 7, 7, 7, 7, 7, 7, 3, 3, 7, 17]
print(firstUnique.showFirstUnique())  # return 17
