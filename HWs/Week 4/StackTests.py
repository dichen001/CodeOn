from Stack1 import Stack

s = Stack()

print s.isEmpty()
s.push("s")

print s.size()
s.push("apple")
print s.isEmpty()

s.push("big")
print s.pop()
print s.pop()
print s.size()
print s.pop()
s.pop()