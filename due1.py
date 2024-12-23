def due(given):
    num=given-12.56
    if given==12.56:
        return print("your purchase is completed✅")
    elif given>12.56:
        return print("you gave",given,"so we will give",num)
    else:
        return print("Your purchase is not completed❗❌")
num=float(input("You have gone shopping,your total is 12.56$ how much wil you give : "))
call=due(num)
print(call)