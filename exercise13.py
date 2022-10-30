#https://edabit.com/challenge/6JNHBeGxY8dhTaPhs
def collatz(a, b):
    steps_a = 0
    while a!=1:
        if a %2 == 0:
            a = a/2
        else: 
            a = 3*a + 1
        steps_a +=1
    steps_b = 0
    while b!=1:
        if b %2 == 0:
            b = b/2
        else: 
            b = 3*b + 1
        steps_b +=1
    if steps_a<steps_b:
        return "a"
    else:
        return "b"

print (collatz(10, 15))
print (collatz(13, 16))
print (collatz(53782, 72534))
