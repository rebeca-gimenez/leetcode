"""
1323. Maximum 69 Number
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit 
(6 becomes 9, and 9 becomes 6).
1 <= num <= 104
num consists of only 6 and 9 digits.
"""
def maximum69Number (num):
    letters = str(num)
    if letters == "9"*len(letters):
        return num
    else:
        index = 0
        for letter in letters:
            if letter == "6":
                break
            index += 1
        return int(letters[:index] + "9" + letters[index + 1:])
def maximum69Number2 (num):
    letters = str(num)
    answer = ''
    count = 1
    for letter in letters:
        if letter == "6" and count > 0:
            answer += "9"
            count = 0
        else:
            answer += letter
    return int(answer)
            
        
num = 9669
output = 9969
print(maximum69Number (num) == output)
num = 9996
output = 9999
print(maximum69Number (num) == output)
num = 9999
output = 9999
print(maximum69Number (num) == output)
