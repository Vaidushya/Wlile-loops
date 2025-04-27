#--homework--#

num = 12345 

re_num = 0

while num > 0:
    digit = num % 10
    re_num = re_num * 10 + digit
    num //= 10

print("The reversed number is:", re_num)
