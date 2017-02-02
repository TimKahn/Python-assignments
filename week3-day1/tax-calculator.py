def taxes(tuple_list, income):
    brackets =  sorted(tuple_list)
    total_tax = 0
    bound = 0
    previous_bound = 0
    rate = 0.0

    for item in brackets:
        bound = item[0]
        rate = item[1]
        if income > bound:
            total_tax += (bound - previous_bound)*rate
            previous_bound = bound
        else:
            break

    total_tax += (income - previous_bound)*rate

    return total_tax, brackets

print taxes([(1000,.1),(3000,.3),(2000,.2)],5000)
print taxes([(1000,.1),(3000,.3),(2000,.2)],500)
print taxes([(20000,.2),(30000,.25),(50000,.5)],100000)
print taxes([(20000,.2),(30000,.25),(50000,.5)],24000)
