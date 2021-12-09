lijst = {}

def add():
    global lijst
    vraag = input('welk item wilt u aan de lijst toevoegen? ')
    amount = input('hoeveel {} wilt u? '.format(vraag))
    meer = input('wilt u nog meer aan uw lijst toevoegen? Y/N ')
    lijst[vraag] = amount
    if meer == 'y' or meer == 'Y':
        return add()
    elif meer == 'n' or meer == 'N':
        return lijst
    else:
        return add()

print(add())