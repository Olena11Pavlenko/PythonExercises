#https://edabit.com/challenge/LR98GCwLGYPSv8Afb
def pluralize(lst):
    lst_plr = []
    lst_one = []
    for i in lst:
        if lst.count(i) > 1:
            lst_plr.append(i)
        else: lst_one.append(i)
    lst_plr_one = lst_plr
    lst_plr = [x+'s' for x in lst_plr]
    
    return (lst_plr, lst_one)

print (pluralize(["cow", "pig", "cow", "cow"]))