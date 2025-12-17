s = "madam"

if s == s[::-1]:
    print("is palindrome")
else:
    print("not palindrome")
    
s = "sos"

flag = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        flg = False
        break
    
if flag:
    print("it is palindrome")
else:
    print("It is not a palindrome")