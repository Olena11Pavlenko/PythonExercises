# Majority Vote
# https://edabit.com/challenge/pQavNkBbdmvSMmx5x

def majority_vote(lst):
    for i in lst:
        if lst.count(i) > len(lst)/2:
            return i

print (majority_vote(["A", "A", "B"]))
print (majority_vote(["A", "A", "A", "B", "C", "A"]))
print (majority_vote(["A", "B", "B", "A", "C", "C"]))
print (majority_vote(["A", "B", "B", "B", "C", "B"]))
print (majority_vote([]))