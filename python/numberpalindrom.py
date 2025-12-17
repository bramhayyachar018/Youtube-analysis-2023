# n = 121

# s = str(n)

# if s == s[::-1]:
#     print("is palindrome")
# else:
#     print("not palindrome")

s = "madam"
flag = True

for i in range(len(s)//2):
    if s[i] != s[len(s) - i - 1]:
        flag = False
        break
    
if flag:
    print("It is a palindrome")
else:
    print("Not a palindrome")