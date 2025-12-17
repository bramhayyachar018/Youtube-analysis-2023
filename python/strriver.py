#approach 1
s = "hello"
print(s[::-1])

# #approach 2
s = "hello"

rev ="".join(reversed(s))
print(rev)

# appproach 3
s = "hello"
rev = ""

for i in s:
    rev = i + rev
    
# print(rev)

# approach 4

s = "hello"
rev = ''

i = len(s) - 1

while i >= 0:
    rev += s[i]
    i -=1
    
print(rev)