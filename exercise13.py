# 3n + 1 Problem (Collatz Conjecture)
# https://edabit.com/challenge/6JNHBeGxY8dhTaPhs
def count_steps (num):
    steps = 0
    while num!=1:
        if num %2 == 0:
            num = num/2
        else: 
            num = 3*num + 1
        steps +=1
    return steps
def collatz(a, b):
    if count_steps(a)<count_steps(b):
        return "a"
    else:
        return "b"

print (collatz(10, 15))
print (collatz(13, 16))
print (collatz(53782, 72534))
