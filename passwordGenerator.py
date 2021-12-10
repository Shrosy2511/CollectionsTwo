import random

choice = [random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(3)]
choice1 = [random.choice('1234567890') for i in range(7)]
choice2 = [random.choice('!@#$%^&*()') for i in range(3)]
choice3 = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(8)]
choice4 = [random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for i in range(3)]
choices = choice1+choice2+choice3
random.shuffle(choices)
print('hier is uw wachtwoord met 24 characters:',''.join(choice+choices+choice4))
