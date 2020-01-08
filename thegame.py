from random import randint
import time
import sys
from termcolor import cprint

options = [1, 3, 4, 7, 8, 9, 10, 11, 12, 14]
win_lose_attack = [1, 2]
win_lose_defence = [1, 2]
one_in_fifteen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
things_in_win_lose_attack = len(win_lose_attack) - 1
random2_attack = randint(0, things_in_win_lose_attack)
use_this2_attack = win_lose_defence[random2_attack]
things_in_win_lose_defence = len(win_lose_defence) - 1
random2_defence = randint(0, things_in_win_lose_defence)
use_this2_defence = win_lose_defence[random2_defence]
money = 100
population = 100
happiness = 100
q = 0
w = 0
e = 0
r = 0
t = 0
y = 0
u = 0
i = 0
p = 0
a = 0
s = 0
d = 0
f = 0
g = 0
h = 0
z = 0
day_cycle = 0
no_repeat = 0
extra_happiness = 0
state_of_emergency_happiness = 0
state_of_emergency_population = 0
warrior_faction = 0
tax_money = 10
moral = 0
soldiers = 'no'
state_of_emergency = 'no'
soldiers_status = 'attacking'
cost = 0
drought_countermeasures = 'no'
capture_reward = 'no'
things_in_options = len(options) - 1
random = randint(0, things_in_options)
use_this = options[random]
true = 'true'
interest = [30, 40, 50, 60]
things_in_interest = len(interest) - 1
random3 = randint(0, things_in_interest)
use_this4 = interest[random3]


def check():
    global money
    global population
    global happiness
    global state_of_emergency_happiness
    global state_of_emergency
    global state_of_emergency_population
    money = round(money)
    population = round(population)
    happiness = round(happiness)
    if population < 1:
        print('All your citizens have left your town.Game over :-(')
        exit()
    elif money < 1:
        state_of_emergency = 'yes'
        state_of_emergency_happiness += 20
        happiness -= state_of_emergency_happiness
        cprint(
            'You are in a state of emergency.'
            'Your happiness has decreased by {} total.'
            'It will continue being decreased by an extra 20 each time until its over'
            .format(state_of_emergency_happiness), 'red')
        cprint('Your money is ={}'.format(money), 'blue')
        time.sleep(1)
        cprint('Your population is ={}'.format(population), 'blue')
        time.sleep(1)
        cprint("Your people's happiness is ={}".format(happiness), 'blue')
        time.sleep(1)
        if happiness < 1:
            state_of_emergency = 'yes'
            state_of_emergency_population += 20
            population -= state_of_emergency_population
            cprint(
                'You are in a state of emergency.Your population has decreased by {}.'
                'It will continue being decreased by an extra 20 each time until its over'
                .format(state_of_emergency_population, ), 'red')
            cprint('Your money is = {}'.format(money), 'blue')
            time.sleep(1)
            cprint('Your population is = {}'.format(population), 'blue')
            time.sleep(1)
            cprint("Your people's happiness is = {}".format(happiness), 'blue')
            time.sleep(1)
    elif happiness < 1:
        state_of_emergency = 'yes'
        state_of_emergency_population += 20
        population -= state_of_emergency_population
        cprint(
            'You are in a state of emergency.Your population has decreased by {}.'
            'It will continue being decreased by an extra 20 each time until its over'
            .format(state_of_emergency_population), 'red')
        cprint('Your money is ={}'.format(money), 'blue')
        time.sleep(1)
        cprint('Your population is ={}'.format(population), 'blue')
        time.sleep(1)
        cprint("Your people's happiness is ={}".format(happiness), 'blue')
        time.sleep(1)
    else:
        state_of_emergency = 'no'
        cprint('Your money is ={}'.format(money), 'blue')
        time.sleep(1)
        cprint('Your population is ={}'.format(population), 'blue')
        time.sleep(1)
        cprint("Your people's happiness is ={}".format(happiness), 'blue')
        time.sleep(1)
    if population < 1:
        print('All your citizens have left your town.Game over :-(')
        exit()    


def day_thing():
    global state_of_emergency
    global day_cycle
    global money
    global tax_money
    global population
    global happiness
    global no_repeat
    global extra_happiness
    day_cycle = round(day_cycle, 1)
    if day_cycle % 1 == 0:
        if no_repeat != day_cycle:
            no_repeat = day_cycle
            if day_cycle != 0:
                if state_of_emergency == 'no':
                    money += tax_money
                    happiness += extra_happiness
                    population += 5 + (happiness / 10)
                    money = round(money)
                    population = round(population)
                    happiness = round(happiness)
                    daily_happiness = round(happiness / 10) + 5
                    cprint('End of day {}'.format(day_cycle), 'blue')
                    time.sleep(1)
                    cprint('+{} money'.format(tax_money), 'green')
                    time.sleep(1)
                    cprint('+{} population'.format(daily_happiness), 'green')
                    time.sleep(1)
                    if extra_happiness > 0:
                        cprint('+{} happiness'.format(extra_happiness),
                               'green')
                    elif extra_happiness != 0:
                        cprint('{} happiness'.format(extra_happiness), 'red')
                    check()
                else:
                    cprint('End of day {}'.format(day_cycle), 'blue')
                    time.sleep(1)
                    cprint('+{} money'.format(tax_money), 'green')
                    money += tax_money
                    time.sleep(1)
                    check()


YN = input(
    'You control a village. Answer with yes or no unless'
    ' otherwise prompted. Only use lower case. Press enter to continue ')
while true == 'true':
    if use_this == 1:  # Bartender
        day_cycle += 0.2
        cprint('Bartender:', 'yellow')
        YN = input(
            "Can I borrow some money to start a bar?I'll pay you back with interest "
        )
        if YN == 'yes':
            options.remove(1)
            options.append(2)
            print("Thanks.You won't regret this!")
            time.sleep(1)
            cprint('-20 money', 'red')
            extra_happiness += 2
            time.sleep(1)
            money -= 20
            happiness += 10
            check()
            q += 1
        else:
            print("I understand")
            time.sleep(1)
            cprint('-20 happiness', 'red')
            time.sleep(1)
            happiness -= 20
            check()
    if use_this == 2:  # Pay back
        day_cycle += 0.2
        options.remove(2)
        cprint('Bartender:', 'yellow')
        YN = input('Thanks for the loan.Do you want some of my profit?')
        if YN == 'yes':
            print('here you go')
            time.sleep(1)
            cprint('+{} money'.format(use_this4), 'green')
            time.sleep(1)
            money += use_this4
            check()
        else:
            print('As you wish')
            time.sleep(1)
            cprint('+20 happiness', 'green')
            time.sleep(1)
            happiness += 20
            check()
    if use_this == 3:  # Soldiers
        day_cycle += 0.2
        cprint('army of soldiers from outside the city:', 'yellow')
        YN = input(
            "Want to hire us?We'll protect your city against attacking cities and internal threats. "
        )
        if YN == 'yes':
            print('Thanks')
            options.remove(3)
            options.append(5)
            time.sleep(1)
            cprint('-50 money', 'red')
            time.sleep(1)
            money -= 50
            soldiers = 'yes'
            check()
        else:
            print('Ok.See you around.')
            time.sleep(1)
    if use_this == 4:  # War alert
        day_cycle += 0.2
        cprint('Adviser:', 'yellow')
        options.append(6)
        options.remove(4)
        if soldiers == 'yes':
            YN = input(
                "An neighbouring city is soon going to attacking.Should we attack or defend?"
            )
            if YN == 'attack' or 'Attack':
                print("(You choose attack)")
                time.sleep(1)
                print('yes sir')
                time.sleep(1)
                soldiers_status = 'attacking'
            else:
                YN = input
                if YN == 'yes':
                    print("(You choose defend)")
                    time.sleep(1)
                    print('yes sir')
                    soldiers_status = 'defending'
        else:
            print(
                "An neighbouring city is soon going to attacking.You might want soldiers"
            )
            time.sleep(1)
    if use_this == 5:  # Witch
        day_cycle += 0.2
        cprint('Witch:', 'yellow')
        YN = input('I can make your soldiers stronger for 70 gold.Want me to?')
        if YN == 'yes':
            options.remove(5)
            print('Your soldiers are now stronger')
            time.sleep(1)
            win_lose_attack.insert(1, 1)
            things_in_win_lose_attack = len(win_lose_attack) - 1
            random2_attack = randint(0, things_in_win_lose_attack)
            use_this2_attack = win_lose_attack[random2_attack]
            cprint('-70 money', 'red')
            money -= 70
            time.sleep(1)
            check()
        else:
            print('As you wish')
    if use_this == 6:  # War
        day_cycle += 0.2
        options.remove(6)
        if soldiers == 'yes':
            if (use_this2_attack == 2 and soldiers_status == 'attacking') or (
                    use_this2_defence == 2 and soldiers_status == 'defending'):
                print("You were raided.Your soldiers died.")
                happiness -= 100
                time.sleep(1)
                cprint('-100 happiness', 'red')
                time.sleep(1)
                if money>30:
                 cprint('-{} money'.format(money - 30), 'red')
                 money = 30
                time.sleep(1)
                check()
                soldiers = 'no'
            elif (use_this2_attack == 1 and soldiers_status == 'attacking'
                  ) or (use_this2_defence == 1
                        and soldiers_status == 'defending'):
                print('You won the battle')
                time.sleep(1)
                time.sleep(1)
                cprint('+300 money', 'green')
                money += 300
                time.sleep(1)
                cprint('+100 happiness', 'green')
                happiness += 100
                time.sleep(1)
                check()
        else:
            cprint('Your city was raided.Your soldiers stood down', 'red')
            happiness -= 100
            time.sleep(1)
            cprint('-100 happiness', 'red')
            time.sleep(1)
            cprint('-{} money'.format(money - 30), 'red')
            money = 30
            time.sleep(1)
            check()
    if use_this == 7 and money < 51:  # Increase tax
        day_cycle += 0.2
        cprint('Advisers', 'yellow')
        options.remove(7)
        if money > 0:
            YN = input('Should we increase taxes?.We only have {} gold '.
                       format(money))
            if YN == 'yes':
                print('Yes sir')
                time.sleep(1)
                tax_money += 10
                cprint('-50 happiness', 'red')
                time.sleep(1)
                happiness -= 50
                check()
            else:
                print('as you wish')
        else:
            YN = input("Should we increase taxes?.We're bankrupt!")
            if YN == 'yes':
                print('Yes sir')
                time.sleep(1)
                tax_money += 10
                cprint('-30 happiness', 'red')
                time.sleep(1)
                happiness -= 30
                check()
            else:
                print('You better have a plan')
                time.sleep(1)
    if use_this == 8:  # Clown
        if z > 2:
            day_cycle += 0.2
            z += 1
            cprint('Clown:', 'yellow')
            YN = input('Hey man,can I set up a circus in your town? ')
            if YN == 'yes':
                YN = input('Is there a fee? ')
                time.sleep(1)
                if YN == 'yes':
                    cost = int(input('How much? '))
                    if cost <= 50:
                        print('here you go')
                        time.sleep(1)
                        cprint('+{} money'.format(cost), 'green')
                        time.sleep(1)
                        hpness = (70 - cost)
                        happiness += hpness
                        money += cost
                        cprint('+{} happiness'.format(hpness), 'green')
                        time.sleep(1)
                        check()
                    else:
                        print("That's too much.I guess we'll go else where")
                        time.sleep(1)
                else:
                    print('Nice!')
                    time.sleep(1)
                    happiness += 70
                    cprint('+70 happiness', 'green')
                    time.sleep(1)
                    check()
            else:
                time.sleep(1)
                print('*sad clown noises*')
                time.sleep(1)
                y += 1
        else:
            options.remove(8)
    if use_this == 9:  # Drunk man
        day_cycle += 0.2
        options.remove(9)
        cprint('Royal guard', 'yellow')
        YN = input(
            'We arrested a very drunk man got into a fight at the bar.Should we through him into the dungeon?'
        )
        if YN == 'no':
            print('yes sir')
            time.sleep(1)
            print('*your people will remember that*')
            time.sleep(1)
        else:
            print('Yes sir')
    if use_this == 10:  # Devil
        if p < 4:
            day_cycle += 0.2
            p += 1
            cprint('The devil', 'yellow')
            YN = input(
                'Want to flip a coin?'
                'If you win,I free some souls but if I win I kill some of your people.What do you say?'
            )
            if YN == 'yes':
                coin_toss = randint(1, 5)
                heads_or_tails = input('Heads or tails? ')
                moral -= 1
                if (coin_toss % 2 == 0 and heads_or_tails == 'heads') or (
                        coin_toss % 2 != 0 and heads_or_tails == 'tails'):
                    time.sleep(1)
                    if coin_toss % 2 == 0:
                        print('Heads')
                    else:
                        print('Tails')
                    time.sleep(1)
                    print('You win.Here you go')
                    time.sleep(1)
                    population += 50
                    cprint('+50 population', 'green')
                    time.sleep(1)
                    check()
                elif (coin_toss % 2 != 0 and heads_or_tails == 'heads') or (
                        coin_toss % 2 == 0 and heads_or_tails == 'tails'):
                    time.sleep(1)
                    if coin_toss % 2 == 0:
                        print('Heads')
                    else:
                        print('Tails')
                    print("I win.I'll be taking those souls")
                    time.sleep(1)
                    cprint('-50 population', 'red')
                    time.sleep(1)
                    cprint('-10 happiness', 'red')
                    happiness -= 10
                    population -= 50
                    check()
                else:
                    cprint("answer not valid", 'red')
            else:
                print('Your loss')
        else:
            options.remove(10)
    if use_this == 11:  # Holiday
        cprint("Citizen", 'yellow')
        day_cycle += 0.2
        YN = input(
            "I think we should have a national holiday,like some of the other countries."
            "It will only cost 10 gold.What do you think?should we?")
        if YN == 'yes':
            print("Thanks")
            options.remove(11)
            time.sleep(1)
            cprint('-10 money', 'red')
            money -= 10
            time.sleep(1)
            cprint('+50 happiness', 'green')
            happiness += 50
            time.sleep(1)
            check()
        else:
            time.sleep(1)
            check()
    if use_this == 12:  # Escapist
        cprint('Royal guard', 'yellow')
        day_cycle += 0.2
        options.remove(12)
        options.append(13)
        YN = input('A prisoner has escaped.Should we put up posters?')
        if YN == 'yes':
            money -= 10
            cprint('-10 money', 'red')
            time.sleep(1)
            YN = input('Should we add a reward for her capture?')
            extra_happiness -= 5
            if YN == 'yes':
                print('Yes Sir')
                time.sleep(1)
                capture_reward = 'yes'
                time.sleep(1)
                a = 3
                check()
            else:
                a = 1
                print('Yes sir')
                time.sleep(1)
                check()
        else:
            print('As you wish')
            time.sleep(1)
            moral -= 1
            a = 2
    if use_this == 13:  # Capture
        cprint('Royal guard', 'yellow')
        day_cycle += 0.2
        options.remove(13)
        if a == 1:  # put up posters no reward
            print(
                'We have recaptured the criminal unfortunately.She attacked someone but they will recover.'
            )
            extra_happiness += 5
            time.sleep(1)
            cprint('Inner self', 'yellow')
            YN = input('Should I pay his medical bills?')
            if YN == 'yes':
                moral += 1
                cprint('-30 money', 'red')
                money -= 30
                time.sleep(1)
            else:
                moral -= 1
                time.sleep(1)
        elif a == 2:  # no posters
            print(
                'We have recaptured the criminal unfortunately,'
                'due to the lack of awareness about her,she struck again,Killing 10.'
            )
            a += 5
            time.sleep(3)
            cprint('-10 population', 'red')
            extra_happiness += 5
            population -= 10
            a += 5
            check()
            money -= 30
            cprint("-30 money", "red")
            time.sleep(1)
        else:  # both posters and reward
            print(
                'Thanks to the posters and the rewards,we were able to recapture the criminal.She is now in jail'
            )
            time.sleep(1)
            cprint("-30 money", "red")
            time.sleep(1)
        a += 5
    if use_this == 14:  # Better defences
        day_cycle += 0.2
        cprint('Adviser:', 'yellow')
        YN = input(
            "We have noticed flaws in our city's defences.Want us to fix them?"
        )
        if YN == 'yes':
            print('Our defences are now stronger')
            options.remove(14)
            time.sleep(1)
            win_lose_defence.insert(1, 1)
            things_in_win_lose_defence = len(win_lose_defence) - 1
            random2_attack = randint(0, things_in_win_lose_defence)#probmlem here?
            use_this2_defence = options[random2_attack]
            cprint('-70 money', 'red')
            money -= 70
            time.sleep(1)
            h += 1
            check()
        else:
            print('As you wish')
    if len(options)==0:
        print("looks like you've finished the game.")
        check()
        true='false'


     
    use_this3 = use_this
    day_thing()
    things_in_options = len(options) - 1
    random = randint(0, things_in_options)
    use_this = options[random]
    if use_this == use_this3 and g <= 10:
        things_in_options = len(options) - 1
        random = randint(0, things_in_options)
        use_this = options[random]
        g += 1
    g = 0