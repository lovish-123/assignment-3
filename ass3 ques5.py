# Assignment 3
# Question 5
n = 10

for i in range(6):
    a = 65
    for j in range(11):

        if j < i or j > (n - i):
            print(' ', end=''),
        else:
            print(chr(a), end='')
        a += 1
    print()