# when you remove first element of the queue, the second element becomes the first,
# and the thisr becomes the second, and so on. so the entire queue shiftsto
# the left by one position.
# this takes the O(n) timem complezity, where n is the number of elements in the
# queue. you do this in a loop, so the overall time complexity becomes O(n^2).
# thats why to achieve the O(1) time complexity fo the dequeue operation, 
# we use the pythons built in deque class from teh collectino module. which
# asllows us to add and remove the elements from both ends of the queue
# in O(1) time complexity.
from collections import deque

class RecentCounter:
    def __init__(self):
        # create an empty deque to store the timestamps of the calls
        self.queue = deque()
    
    def ping(self, t: int) -> int:
        # add the current timestamp to the end of the deque
        self.queue.append(t)
        # kick out anyone from the front of the deque that older than 3000 milliseconds
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        # the number of calls in the last 3000 milliseconds is the length of the deque
        return len(self.queue) 

if __name__ == "__main__":
    # 1. Instantiate the counter ONCE so it maintains its history/memory
    counter = RecentCounter()
    
    # 2. Wrap the pings in print statements to output them to the terminal
    print(counter.ping(1))     # Expected Output: 1
    print(counter.ping(100))   # Expected Output: 2
    print(counter.ping(3001))  # Expected Output: 3
    print(counter.ping(3002))  # Expected Output: 3 (The '1' timestamp drops out!)