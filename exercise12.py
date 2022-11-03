#https://edabit.com/challenge/LR98GCwLGYPSv8Afb
def pluralize(lst):
    lst_plr = []
    lst_one = []
    for i in lst:
        if lst.count(i) > 1:
            lst_plr.append(i)
        else: lst_one.append(i)
    lst_plr = [x+'s' for x in lst_plr]
    list_answer = lst_one + lst_plr
    answer = set(list_answer)
    return (answer)

print (pluralize(["cow", "pig", "cow", "cow"]))
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))