#Note that sets only keep 1 of each character
s1 = ["a","a","a"]
s2 = ["a", "b", "a"]

#Completes in linear time -> O(n) where n is the length
s1 = set(s1)
print s1

s2 = set(s2)
print s2


#find common value from each set
print s1.intersection(s2)

s = "hello world"
print s, set(s)