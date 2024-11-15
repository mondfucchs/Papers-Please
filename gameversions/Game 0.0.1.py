from random import randint, choice
from time import sleep, time
from enum import Enum

# Declaring big-event functions:

def end_game(endreason):
    print(f'\n\033[31m== Your whole family {endreason} ==\033[m')
    quit()

# Declaring classes and dictionaries.

class famstate(Enum):
    good        = 2
    hungry      = 1
    v_hungry    = 0
    dead        = -1

class famheat(Enum):
    good        = 2
    sick        = 1
    dead        = -1

dictstate_string = {famstate.good: 'OK', famstate.hungry: 'Hungry',
                    famstate.v_hungry: 'Very Hungry', famstate.dead: "YOU'RE A HORRIBLE FATHER!",
                    famheat.good: 'OK', famheat.sick: 'Sick', famheat.dead: "THE DEATH COME BECAUSE OF YOU!"}

# Declaring the dialogue tuples

names       = ('Aaron', 'Abdullah', 'Adam', 'Adamik', 'Adamse', 'Adrian', 'Adriano',
               'Ahmad', 'Aidan', 'Anze', 'Arek', 'Antol', 'Anton', 'Arne', 'Aronovich', 'Arthur','Arttu', 'Arto', 'Arvi', 'Asger',
               'Barbara', 'Barbare', 'Barbora', 'Basiliki', 'Batrisyia', 'Bayarmaa', 'Camila', 'Camille', 'Carla', 'Carol',
               'Carolina', 'Caleb', 'Calin', 'Cameron', 'Carlos', 'Carter', 'Dafina', 'Daisy', 'Dalal', 'Damia', 'Dan',)

surnames     = ('Arianiti', 'Bushati', 'Beqiri', 'Bogdani', 'Dukagjini', 'Dushku', 'Dervishi', 'Gurakuqi', 'Gjoni', 'Hoti',
               'Hoxha', 'Frasheri', 'Kastrioti', 'Kastrati', 'Leka', 'Gruber', 'Huber', 'Bauer', 'Wagner')

greetings   = ('Hello', 'Hi', 'Afternoon', 'Good Afternoon', 'Hmph, go fast..')
bulletin    = ('\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nWelcome to your new position at East Input Border Checkpoint.\nApprove pythotzkans with valid documents, deny the foreigners.\nGlory to Pythotzka.\n',
               '\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nHenceforth, foreigners with a valid documents are approved. Work hard. Uphold the nation.\nGlory to Pythotzka.\n',
               '\nPythotzka,\nMinistry of Admission,\nOfficial Bulletin.\n\nInspector,\nEntry for non-citizens is now regulated. All foreigners need a valid \033[34mENTRY TICKET\033[m.\n')

nations     = ('Pythotzka', 'Obristan', 'Antegria', 'United Federation', 'Republia', 'Impor', 'Kolechia')

# Declaring the general variables

errors          = 0
works           = 0
credit          = 0
day             = 0
hunger_time     = 3
heat_time       = 2
food_family    = famstate.good
heat_family     = famheat.good
familymembers   = ('Son', 'Wife', 'Uncle')

# Amount of days
for i in range(1, 30):
    #Start of the day:

    print(f'\n\033[30mNovember {day + 20}, 1982: Pythotzka, East Input\033[m\n')

    # Amount of works p/day

    # Start of the day:
    first_answer = None
    while first_answer != 'B' and first_answer != 'S':
        first_answer = input('Type (B) to see the Official Bulletin or (S) to start the work: ').upper().strip()

    if first_answer == 'B':
        print(bulletin[day])

        # Waiting user's reading.

        input('Type anything to continue: ')

    # Configuration of the service-clock:
    startservice    = time()
    daytime         = dayremaining = 60

    # Work:
    while dayremaining > 0:

        # Initial dialogue:

        print(f'\033[34mApplicant:\033[m {choice(greetings)}.')

        sleep(1)

        print(f'\033[34mInspector:\033[m Python, please-- I mean, papers, please...\n')
        
        # True documents

        nation                  = choice(nations)
        passport_true           = str(randint(0000, 9999)) + '-' + chr(randint(65, 90)) + chr(randint(65, 90)) + chr(randint(65, 90))
        identcard_true          = str(randint(000, 999)) + '-' + str(randint(00, 99)) + '.' + str(randint(0, 9))

        if day > 1 and nation   != 'Pythotzka':
            entryticket         = str(randint(0000, 9999)) + '-' + str(randint(0000, 9999))
            ticket_until        = randint(0, 30)

        name                    = choice(names) + ' ' + choice(surnames)

        # Actual documents

        trueness    = randint(0, 2)
        correct     = 'D'

        if trueness == 0:
            passport_actual     = str(randint(0000, 8888)) + '-' + chr(randint(66, 90)) + chr(randint(66, 90)) + chr(randint(65, 90))
            identcard_actual    = str(randint(000, 999)) + '-' + str(randint(00, 99)) + '.' + str(randint(0, 9))

        elif trueness == 1:
            passport_actual     = passport_true
            identcard_actual    = str(randint(000, 999)) + '-' + str(randint(00, 99)) + '.' + str(randint(0, 9))
            correct             = 'D'

        else:
            passport_actual     = passport_true
            identcard_actual    = identcard_true

            correct = 'A'

            if day == 0 and nation != 'Pythotzka':
                correct         = 'D'
            
            if day > 1 and nation != 'Pythotzka' and ticket_until >= day:
                correct         = 'A'
            
            elif day > 1 and nation != 'Pythotzka' and ticket_until <= day:
                correct         = 'D'


        # Player evaluation

        sleep(1)

        print('Applicant Passport   : ====')
        print(f'Nationality          : {nation}')
        print(f'Name                 : {name}')
        print(f'Passport Number      : {passport_actual}')
        print(f'Personal ID          : {identcard_true}\n')

        print('Identification Card  : ====')
        print(f'Name                 : {name}')
        print(f'Passport Number      : {passport_true}')
        print(f'Personal ID          : {identcard_actual}\n')

        if day > 1 and nation != 'Pythotzka':
            print('Entry Ticket         : ====')
            print(f'Valid Until          : 1982.11.{ticket_until}\n')

        # Player approvation

        p_answer = ''

        while p_answer != 'A' and p_answer != 'D':
            p_answer = input('Type (A) for \033[32mApproved\033[m or (D) for \033[31mDenied\033[m: ').upper().strip()

        # Player's answer check:

        print('...')
        sleep(2)

        works += 1

        if p_answer != correct:
            errors += 1
            print(f'\033[31mM.O.A. Citation: Protocol Violated.\033[m.', end=' ')
            if errors > 3:
                print(f'Penalty Assessed - {(errors - 3) * 5} Credits')
                credit -= (errors - 3) * 5
            elif errors == 3:
                print(f'Last Warning - No Penalty')
            else:
                print(f'No Penalty')
            
            print('... Next!\n')

        else:
            print('Next!\n')
            credit += 5

        # Using service-clock:

        endservice = time()
        elapsed = endservice - startservice
        dayremaining = daytime - elapsed

        if dayremaining > 0:
            print(f'\033[31mRemaining Time Today:\033[m {dayremaining:.1f} seconds\n')
            
    # End of the day:

    print('= End of the Day =\n')
    print(f'\033[32mTotal of Credits:\033[m {credit}\n')
    works = 0

    pay_food    = 10
    pay_heat    = 10
    pay_rent    = 20
    confirm     = None

    while confirm != 'Y' and confirm != 'N':
        # Food managment

            # Shows family members at the time states.

        for person in familymembers:
            print(f'\033[34m{person:6}:\033[m (Food: {dictstate_string[food_family]}) (Heat: {dictstate_string[heat_family]})')

            # Actual chooses
        
        confirm = input(f'\n\033[32mPay Food\033[m ({pay_food} credits) [Y/N]: ').strip().upper()

        if confirm == 'Y':
            credit -= pay_food
            hunger_time = 3

            food_family = famstate.good

        else:
            hunger_time -= 1
            if hunger_time == 3:
                food_family = famheat.good

            if hunger_time == 2:
                food_family = famstate.hungry
            
            if hunger_time == 1:
                food_family = famstate.v_hungry

            if hunger_time == 0:
                food_family = famstate.dead
                endreason = 'starved to death'

        confirm = None

            # Heat managment

        confirm = input(f'\n\033[32mPay Heat\033[m ({pay_heat} credits) [Y/N]: ').strip().upper()
        
        if confirm == 'Y':
            credit -= pay_heat
            heat_time = 2

            heat_family = famheat.good

        else:
            heat_time -= 1
            if hunger_time == 2:
                heat_family = famheat.good
            
            if heat_time == 1:
                heat_family = famheat.sick

            if heat_time == 0:
                heat_family = famstate.dead
                endreason = 'died of cold'

    print(f"\n\033[32mPay Rent\033[m ({pay_rent} credits) [No Choice]")
    credit -= pay_rent

    print(f'\n\033[32mTotal of Credits:\033[m {credit}')

    # Checking if your family died of hunger or cold.

    if food_family == famstate.dead or heat_family == famheat.dead:
        end_game(endreason)

    day += 1
