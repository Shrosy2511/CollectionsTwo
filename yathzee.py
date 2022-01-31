import random

dice = []

aces = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

threeOfaKind = 0
fourOfaKind = 0
fullHouse = 0
smallStraight = 0
largeStraight = 0
topScore = 0
chance = 0




def scoreboard():
    totalP1 = aces + twos + threes + fours + fives + sixes
    totalP2 = threeOfaKind + fourOfaKind + fullHouse + smallStraight + largeStraight + topScore + chance
    total = totalP1 + totalP2
    print(f"""
    scoreboard
    -------------------------------------------------
    aces  |total 1's| score: {aces}
    -------------------------------------------------
    twos  |total 2's| score: {twos}
    -------------------------------------------------
    threes|total 3's| score: {threes}
    -------------------------------------------------
    fours |total 4's| score: {fours}
    -------------------------------------------------
    fives |total 5's| score: {fives}
    -------------------------------------------------
    sixes |total 6's| score: {sixes}
    -------------------------------------------------
    EXTRA BONUS| if score is 63 or more | +35 points
    -------------------------------------------------
    total part 1| score: {totalP1}
    -------------------------------------------------



    -------------------------------------------------
    three of a kind| total dice | score: {threeOfaKind}
    -------------------------------------------------
    four of a kind | total dice | score: {fourOfaKind}
    -------------------------------------------------
    full house     | 25 points  | score: {fullHouse}
    -------------------------------------------------
    small straight | 30 points  | score: {smallStraight}
    -------------------------------------------------
    large straight | 40 points  | score: {largeStraight}
    -------------------------------------------------
    top score      | 50 points  | score: {topScore}
    -------------------------------------------------
    chance         | total dice | score: {chance}
    -------------------------------------------------
    total part 2   | score: {totalP2}
    -------------------------------------------------
    total part 1   | score: {totalP1}
    -------------------------------------------------
    total score    | score: {total}
    """)

def chanceQ():
    global chance
    vraag = input('wilt u uw chance gebruiken? Y/N').upper()
    if vraag == 'Y':
        chance = sum(dice)
    else:
        pass

def rollDice():
    for x in range(5):
        dice.append(random.randint(1,6))
    print(dice)

    for i in range(2):
        if chance < 1:
            chanceQ()
            dice.clear()
            rollDice()
        else:
            pass
        throwAgain = input('welke dobbelstenen wil je opnieuw gooien 1 2 3 4 of 5 vergeet geen spatie na elk nummer! ').split()
        print(throwAgain)
        if throwAgain == 'stop':
            scoreboard()
        elif len(throwAgain) > 0:
                for i in throwAgain:
                    randomNummer = random.randint(1,6)
                    dice[int(i)-1] = randomNummer
        print(dice)

def isfullHouse(dice):
    setDice = set(dice)
    diceFullhouse = len(setDice)
    if diceFullhouse == 2:
        if dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3:
            return True
    return False


def chooseType():
    global aces, twos, threes, fours, fives, sixes, threeOfaKind, fourOfaKind, fullHouse, smallStraight, largeStraight, topScore, chance
    choice = input('onder welke categorie wil je je punten toevoegen? schrijf het zoals aces twos threes etc ')
    if choice == 'aces':
        if aces >= 1:
            print('sorry je heb de enen al ingevuld')
            chooseType()
        else:
            aces = (dice.count(1))
    elif choice == 'twos':
        if twos >= 1:
            print('sorry je heb de tweeën al ingevuld')
            chooseType()
        else:
            twos = (dice.count(2))*2
    elif choice == 'threes':
        if threes >= 1:
            print('sorry je heb de tweeën al ingevuld')
            chooseType()
        else:
            threes = (dice.count(3))*3
    elif choice == 'fours':
        if fours >= 1:
            print('sorry je heb de vieren al ingevuld')
            chooseType()
        else:
            fours = (dice.count(4))*4
    elif choice == 'fives':
        if fives >= 1:
            print('sorry je heb de vijfen al ingevuld')
            chooseType()
        else:
            fives = (dice.count(5))*5
    elif choice == 'sixes':
        if sixes >= 1:
            print('sorry je heb de zessen al ingevuld')
            chooseType()
        else:
            sixes = (dice.count(6))*6
    elif choice == 'three of a kind':
        if threeOfaKind >= 1:
            print('sorry u heeft three of a kind al in gevuld')
            chooseType()
        else:
            if dice.count(1) == 3 or dice.count(2) == 3 or dice.count(3) == 3 or dice.count(4) == 3 or dice.count(5) == 3 or dice.count(6) == 3:
                threeOfaKind = sum(dice)
    elif choice == 'four of a kind':
        if fourOfaKind >= 1:
            print('sorry je heb four of a kind al ingevuld')
            chooseType()
        else:
            if dice.count(1) == 4 or dice.count(2) == 4 or dice.count(3) == 4 or dice.count(4) == 4 or dice.count(5) == 4 or dice.count(6) == 4:
                fourOfaKind = sum(dice)
    elif choice == 'fullhouse':
        if isfullHouse(dice) > 1:
            print('sorry je heb fullhouse al ingevuld')
            chooseType()
        else:
            fullHouse = 25
    elif choice == 'small straight':
        if smallStraight > 1:
            print('sorry je heb small straight al in gevuld')
            chooseType()
        else:
            if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
                smallStraight = 30
            elif 2 in dice and 3 in dice and 4 in dice and 5 in dice:
                smallStraight = 30
            elif 3 in dice and 4 in dice and 5 in dice and 6 in dice:
                smallStraight = 30
            else:
                print('sorry je heb geen small straight')
            chooseType()
    elif choice == 'large straight':
        if largeStraight > 1:
            print('sorry je heb large straight al ingevuld')
            chooseType()
        else:
            if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
                largeStraight = 40
            if 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
                largeStraight = 40
            else:
                print('sorry je heb geen large straight')
                chooseType()
    elif choice == 'topscore':
        if topScore > 1:
            print('sorry je heb topscore al ingevuld')
            chooseType()
        else:
            if dice.count(dice[0]) == 5:
                topScore = 50
            else:
                print('sorry je heb geen topscore')
                chooseType()
    else:
        print('sorry dit begrijp ik niet')
    dice.clear()




def isboardnotfull():
    if aces != 0 and twos != 0 and threes != 0 and fours != 0 and fives != 0 and sixes != 0:
        return False
    return True        


def game():
    throw = input('druk op enter om de dobbelstenen te gooien ')
    if throw == '':
        print('')
    elif throw == 'stop':
        quit()
    else:
        print('sorry dit begrijp ik niet')
        game()
    while isboardnotfull():
            rollDice()
            chooseType()
    scoreboard()
     
game()


