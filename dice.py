import random


print("Dice 1.0 is built for Python3. Failure to utilize Python3 \
may result in buggy behavior.")


def roll():
    roll1 = getroll()
    roll2 = getroll()
    total = (roll1 + roll2)
    print("Dice 1 = " + str(roll1))
    print("Dice 2 = " + str(roll2))
    print("Therefore you rolled a " + str(total))
    return total


def end(amount):
    if amount <= 0:
        print("You are out of money please go get some more")
        exit()
    if amount > 0:
        while True:
            try:
                play_again = int(input("1.) Place a bet\n2.) Quit\nMake your Selection: "))
                if play_again == 1:
                    break
                elif play_again == 2:
                    exit()
            except ValueError:
                print("Please enter either 1 to play again or 2 to exit")
                continue


def determinewinnings(bet, c, total, amount):
    if c == 'h' and total >= 8:
        print("You have won " + str(bet))
        return amount + bet
    elif c == 'l' and total <= 6:
        print("You have won " + str(bet))
        return amount + bet
    elif c == 's' and total == 7:
        print("You have won " + str(bet*4))
        return amount + bet*4
    else:
        print("You have lost " + str(bet))
        return amount - bet


def getroll():
    rolla = random.randint(1, 6)
    return rolla


def getbet(amount):
    while True:
        try:
            print("You have $" + str(amount) + " dollars to bet with: Good Luck!")
            bet = int(input("Place your bet "))
            if bet < 0 or bet > amount:
                print("Please enter a reasonable bet:")
                continue
            elif bet == 0:
                print("goodbye")
                exit(0)
            elif bet > 0 or bet <= amount:
                return bet
        except ValueError:
            print("please enter a valid number")


def gethighlow():
    while True:
        try:
            c = input("Enter H for high, S for sevens and L for low: ").lower()
            if c == "s" or c == "h" or c == "l":
                if c == "h":
                    print("You bet high")
                    return c
                elif c == "l":
                    print("You bet low")
                    return c
                elif c == "s":
                    print("You bet sevens")
                    return c
                else:
                    print("please enter a valid character")
                    continue
        except ValueError:
            print("please enter a valid character")


def game():
    #  Below is the initial amount of money alloted to the player
    amount = 100
    while True:
        bet = getbet(amount)
        c = gethighlow()
        print("You have " + str(amount) + " dollars")
        total = roll()
        amount = determinewinnings(bet, c, total, amount)
        print("You now have $" + str(amount) + " dollars")
        end(amount)


game()
