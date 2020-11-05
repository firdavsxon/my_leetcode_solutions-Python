"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

"""


class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []

	def push(self, x: int) -> None:
		if self.stack == []:
			self.stack.append([x,x])
		else:
			self.stack.append([x, min(x, self.stack[-1][1])])

	def pop(self) -> None:
		self.stack.pop()

	def top(self) -> int:
		return self.stack[-1][0]

	def getMin(self) -> int:
		return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.push(-2))
print(obj.push(0))
print(obj.push(-3))
print(obj.getMin())
print(obj.pop())
print(obj.top())
print(obj.getMin())
#
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

