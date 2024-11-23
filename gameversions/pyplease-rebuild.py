from random import randint, choice
from time   import sleep, time

# Names and nations:

namesM      = ('Aaron', 'Abdullah', 'Adam', 'Adamik', 'Adamse', 'Adrian', 'Adriano',
               'Ahmad', 'Aidan', 'Anze', 'Arek', 'Antol', 'Anton', 'Arne', 'Aronovich', 'Arthur','Arttu', 'Arto', 'Arvi', 'Asger',
               'Barbara', 'Barbare', 'Barbora', 'Basiliki', 'Batrisyia', 'Bayarmaa', 'Caleb', 'Calin', 'Cameron', 'Carlos', 'Carter', 'Dan',)

namesF      = ('Dafina', 'Daisy', 'Dalal', 'Damia', 'Camila', 'Camille', 'Carla', 'Carol', 'Carolina')

genders     = ('M', 'F')

namesCorsp  = {'M': namesM, 'F': namesF}

surnames    = ('Arianiti', 'Bushati', 'Beqiri', 'Bogdani', 'Dukagjini', 'Dushku', 'Dervishi', 'Gurakuqi', 'Gjoni', 'Hoti',
               'Hoxha', 'Frasheri', 'Kastrioti', 'Kastrati', 'Leka', 'Gruber', 'Huber', 'Bauer', 'Wagner')

greetings   = ('Hello', 'Hi', 'Afternoon', 'Good Afternoon', 'Hmph, go fast..')

bulletin    = ('\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nWelcome to your new position at East Input Border Checkpoint.\nApprove pythotzkans with valid documents, deny the foreigners.\nGlory to Pythotzka.\n',
               '\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nHenceforth, foreigners with a valid documents are approved. Work hard. Uphold the nation.\nGlory to Pythotzka.\n',
               '\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nEntry for non-citizens is now regulated. All foreigners need a valid \033[34mENTRY TICKET\033[m.\nGlory to Pythotzka',
               '\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nStricter credential requirements have been instituted. Foreigners need an Entry Permit, entry tickets are no long enough.\nGlory to Pythotzka')

nations     = ('Pythotzka', 'Obristan', 'Antegria', 'United Federation', 'Republia', 'Impor', 'Kolechia')

# Initial variables:

day          = 1
credit       = 0
answer       = None
errors       = 0
errorjus     = None
dayremaining = 45


# General functions:

def general_documents():
    # Generating documents (3/4 correctness): 
    # > Universal:  

    gender       = choice(genders)
    apcntName    = choice(namesCorsp[gender])
    apcntSurnam  = choice(surnames)
    apcntNation  = choice(nations)
    
    # > Passport :

    passportNumb = str(randint(00000, 99999)) + '-' +  str(randint(0000, 9999)) 
    passportDate = randint(1, 30)

    # Showing documents:

    # > Passport (always appear):

    print(f'\n\033[34m= Passport - {apcntNation} =\033[m')
    print(f'NAME: {apcntSurnam}, {apcntName}')
    print(f'SEX : {gender}')
    print(f'EXP : {passportDate}.11.1982')
    print(f'NUM : {passportNumb}')

    # > 

    # Checking documents:
    check   = 'A'

    # > Passport :

    if passportDate < day:
        check   = 'D'

        global errorjus
        errorjus = "Passport expired."

    # Universal errorjus:

    errorjus =     'Applicant is alright         .:'

    # > Day-Special Conditions:

    if day == 1 and apcntNation != 'Pythotzka':
        check    = 'D'
        errorjus = "Applicant isn't pythotzkan   .:"

    # Returning Checking result:

    return check

# Main game:

for passtime in range(0, 30):

    # Starting day-clock:

    startservice    = time()
    daytime         = dayremaining = 45

    print(f'\n\033[30mNovember {day}, 1982: Pythotzka, East Input\033[m\n')

    first_answer = None

    while first_answer != 'B' and first_answer != 'S':
        first_answer = input('Type (B) to see the Official Bulletin or (S) to start the work: ').upper().strip()

    if first_answer == 'B':
        print(bulletin[day - 1])

        # Waiting user's reading.

        input('Type anything to continue: ')

    while dayremaining > 0:

        check = general_documents()

        # Player's answer:

        while answer != 'A' and answer != 'D':
            answer = str(input('\nType (A) to approve or (D) to deny the applicant: ')).upper().strip()

        # Checking if player's answer is correct

        if answer == check:
            credit += 5
            sleep(1)
        else:
            errors += 1

            # Showing M.O.A Citation >

            sleep(1)
            print('\n\033[31m======= Protocol Violated. =======\033[m')

            if errors >= 4:
                penalty = (errors - 3) * 5
                print(f'|| Penalty Assessed: {penalty} credits.')

            elif errors == 3:
                print(f'|| Last warning - No penalty.')

            else:
                print(f'|| No penalty.')

            print(f'|| {errorjus}')

            print('========= M.O.A Citation =========')

            # End of the M.O.A Citation <

        endservice = time()
        elapsed = endservice - startservice
        dayremaining = daytime - elapsed

        if dayremaining > 0:
            print(f'\n\033[31mRemaining Time Today:\033[m {dayremaining:.1f} seconds.')

        else:
            sleep(2)
            print(f'End of the day. Come back tomorrow.')

        print('\n... Next!')

        answer = None

    day += 1