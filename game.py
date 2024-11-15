from random import randint

# Generate the original document:

# Passport:

passport_one = []

for i in range(1, 7):
    passport_one.append(randint(0, 9))

passport_one.insert(3, '-')

passport_one = ''.join(str(o) for o in passport_one)

print(passport_one)