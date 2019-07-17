"""
Create a function that simulates two players picking a card randomly from a deck of cards. The higher number wins.

Once again, this function should have a parameter that allows a player to bet an amount of money on whether they have a higher card. In this game, there can be a tie. What should be returned if there is a tie?

Check the hint to see an additional challenge for this game.If the game is a tie, you should return 0. The player doesn’t win or lose any money.

It’s possible that your solution doesn’t really simulate drawing two cards from the same deck. For example, if I draw a 4, it is less likely that you will draw a 4 when you draw a card. As a challenge, think about how you might create a system that knows which cards have already been draw.

Hint: if you’re familiar with lists, this would be a good place to use them!



Create a function that simulates some of the rules of roulette. A random number should be generated that determines which space the ball lands on.

When we wrote our function, we allowed the user to guess "Odd", "Even", or a specific number. We also implemented the logic associated with the 0 and 00 spots. For example, the player loses if they guess either "Odd" or "Even" and either 0 or 00 comes up.

Implement as many rules of roulette as you’d like. Make sure to consider the different ways roulette rewards a win. Check the hint to see more about this!

The amount of money you get back from roulette changes depending on what kind of guess you make. For example, if you bet 1 dollar on a specific number, and you win, you will get 35 dollars back. But if you bet 1 dollar on "Even" and win, you will only get one dollar back. The return value of your function should reflect the different ways roulette rewards its winners.


Call each of your functions at least once. Below is an example of betting $10 on a coin flip and updating the amount of money you have based on whether you win or lose :

money += coin_flip("Heads", 10)
Make sure there are enough print statements so you can understand what games were played, what happened during those games, and the amount of money you have after each game is played.

8.
Expand your program to check for edge cases. What should happen if a player tries to bet more money than they have? What should happen if a player bets a negative amount of money? What should happen if a player calls "heads" or "Heads!" rather than “Heads".

Try to make it very difficult to someone to break your program.

"""

#user starts with 100$
# user needs to choose heads or tails
#computer flips coin
# if user = comp, user wins and gain money, else computer wins and user loses
# money, keep track of money
# play again? yes? play again if money > 50 else: not enough money
# no, play next game 

#Heads or Tails:

import random

def begin_game_one(money_g1):
    print("You begin with $" + str(money_g1))

    user_guess = input("Choose Heads or Tails :")
    while user_guess.lower() != 'heads' and user_guess.lower() != 'tails':
        print("Invalid Choice.")
        user_guess = input("Choose Heads or Tails :")

    user_bet = input("How much of your available money would you like to bet: eg format(2350) ")
    while user_bet.isdigit() != True or int(user_bet) > money_g1:
        print("Sorry you can't bet that.  Try again.")
        user_bet = input("How much of your available money would you like to bet: ")

    user_guess = user_guess.lower()
    user_bet = int(user_bet)

    winnings = heads_or_tails(user_guess, user_bet)
    now_have = money_g1 + winnings
    print("You now have $" + str(now_have))
    return now_have
            


def heads_or_tails(guess, bet):
    coin_flip = random.randint(1,2)
    if coin_flip == 1:
        flip = 'heads'
    else:
        flip = 'tails'
        
    print("And the flip is ", flip.upper())
    if ((flip == 'heads' and guess == 'heads') or (flip == 'tails' and guess == 'tails')):
        print("Winner!")
        return bet
    else:
        print("Loser.")
        return 0-bet


def play_cho_han(money_g2):
    print("You begin with $" + str(money_g2))
    print("Rolling Dice...\n")
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)



    print("Guess if the sum of the 2 dice will be even or odd.")
    user_guess_2 = input("Choose Even or Odd :")
    while user_guess_2.lower() != 'even' and user_guess_2.lower() != 'odd':
        print("Invalid Choice.")
        user_guess_2 = input("Choose Even or Odd :")

    user_bet_2 = input("How much of your available money would you like to bet: eg format(2350) ")
    while user_bet_2.isdigit() != True or int(user_bet_2) > money_g2:
        print("Sorry you can't bet that.  Try again.")
        user_bet_2 = input("How much of your available money would you like to bet: ")

    user_guess_2 = user_guess_2.lower()
    user_bet_2 =int(user_bet_2)
    dice_sum = dice_1 + dice_2

    print("1st roll =", dice_1, "    2nd roll =", dice_2)
    print("Sum of dice =", dice_sum)
    

    if dice_sum % 2 == 0:
        ans = 'even'
    else:
        ans = 'odd'

    if ((ans == 'even' and user_guess_2 == 'even') or (ans == 'odd' and user_guess_2 == 'odd')):
        print ("Winner!")
        winnings = money_g2 + user_bet_2
        print ("You now have $" + str(winnings))
        
        return winnings

    else:
        print("Loser.")
        winnings = money_g2 - user_bet_2
        print ("You now have $" + str(winnings))
        
        return winnings

    

def main():
    print("Let's play Heads or Tails!")
    money = 100;
    g1_total = begin_game_one(money)

    again = play_again(g1_total)

    while again == "yes" and g1_total > 10:
        g1_total = begin_game_one(g1_total)
        again = play_again(g1_total)

    if g1_total < 10:
        print("Sorry, you don't have enough money to continue playing.")
    print("----------\n ")


    print("Let's play Cho Han")
    money_2= g1_total + money

    g2_total = play_cho_han(money_2)

    again_2 = play_again(g2_total)

    while again_2 == "yes" and g2_total > 10:
        g2_total = play_cho_han(g2_total)
        again = play_again(g2_total)

    if g2_total < 10:
        print("Sorry, you don't have enough money to continue playing.")
    print("----------\n ")

    
    



    
    
def play_again(money_to_bet):
    print("Do you want to play again?")
    play_another = input("Enter 'Y' for yes, anything else for no: ")

    if play_another == 'Y' or play_another == 'y' or play_another.lower() == "yes":
        return "yes"
    else:
        return "no"
    

main()
