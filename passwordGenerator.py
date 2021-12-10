import random

choiceLC = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(2)]
choiceUP = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(random.randint(1,3))]
choiceNUM = [random.choice('1234567890')for i in range(random.randint(4,7))]
choiceSYM = [random.choice('!@#$%^&*()')for i in range(3)]

choice_LW_UP = choiceLC+choiceUP
random.shuffle(choice_LW_UP)
choiceALL = choiceLC+choiceUP+choiceNUM+choiceSYM
random.shuffle(choiceALL)
choiceTotall = choice_LW_UP+choiceALL
choiceSUM = 24-len(choiceTotall)
choiceADD = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(choiceSUM)]
if len(choiceTotall) < 24:
    print(''.join(choiceTotall+choiceADD))
    print('aantal characters:', len(choiceTotall+choiceADD))
else:
    print(choiceTotall)