# Majority Vote
# https://edabit.com/challenge/pQavNkBbdmvSMmx5x

def majority_vote(lst):
    for vote in set(lst):
        if lst.count(vote) > len(lst)/2:
            return vote

print (majority_vote(["A", "A", "B"]))
print (majority_vote(["A", "A", "A", "B", "C", "A"]))
print (majority_vote(["A", "B", "B", "A", "C", "C"]))
print (majority_vote(["A", "B", "B", "B", "C", "B"]))
print (majority_vote([]))