import random

choice = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(2)]
choice1 = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(random.randint(1,3))]
choice2 = [random.choice('1234567890')for i in range(random.randint(4,7))]
choice3 = [random.choice('!@#$%^&*()')for i in range(random.randint(3, 3))]

choice4 = choice+choice1
random.shuffle(choice4)
choice5 = choice+choice1+choice2+choice3
random.shuffle(choice5)
choice6 = choice4+choice5
choice8 = 24-len(choice6)
choice7 = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(choice8)]
if len(choice6) < 24:
    print(''.join(choice6+choice7))
    print('aantal characters:', len(choice6+choice7))
else:
    print(choice6)