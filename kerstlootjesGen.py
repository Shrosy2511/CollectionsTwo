import random
lootjes = []
fillname = True
while fillname:
    naam = input('geef hier de namen(type: stop als je klaar bent): ')
    if naam == 'stop':
        fillname = False
    else:
        lootjes.append(naam)

def trekking():
    check = True
    namecheck = []
    namecheck2 = []
    while check == True:
        lootje1 = random.choice(lootjes)
        lootje2 = random.choice(lootjes)
        trekkingLootjes1 = lootje1
        trekkingLootjes2 = lootje2
        looting = trekkingLootjes1, trekkingLootjes2
        if trekkingLootjes1 in namecheck or trekkingLootjes2 in namecheck2:
            pass
        elif lootje1 != lootje2:
            print(looting)
            namecheck.append(trekkingLootjes1)
            namecheck2.append(trekkingLootjes2)
            if len(namecheck) == len(lootjes):
                check = False
        else:
            pass
trekking()
