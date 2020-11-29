import random
bet = 30
money = 100
num = random.randint(1, 10)
#Write your game of chance functions here
def coin_flip(guess, bet):
  global money
  coin_flip = random.choice(['Heads', 'Tails']) #randomly generates heads or tails choice.
  
  if guess != "Heads" and guess != "Tails":
      return "Whoops! you have entered your choice incorrectly! try entering either Heads or Tails to continue"

  elif bet <= 0:
    return "You cannot bet a negative amount of money, please select a higher amount."

  elif money < 0:
    return "You have run out of money, please deposit more to continue."

  elif coin_flip == guess:
    money = money + bet
    return "Congratulations, you guessed correctly! You have won £" + str(bet) +"!\n" + "You now have £" + str(money) + " in your account."

  else:
    money = money - bet
    return "Unfortunately you have lost £" + str(bet) + " better luck next time\n" + "You now have £" + str(money) + " in your account."
    
def cho_han(guess, bet):
  global money
  dice_roll_1 = random.randint(1, 6)
  dice_roll_2 = random.randint(1, 6)
  dice_result = dice_roll_1 + dice_roll_2
  print("You have guessed " + str(guess) + " best of luck!")

  if guess != "even" and guess != "odd":
      return "Whoops! you have entered your choice incorrectly! try entering either odd or even to continue"

  elif bet <= 0:
    return "You cannot bet a negative amount  of money, please select a higher amount."

  elif money < 0:
    return "You have run out of money, please deposit more to continue."

  elif dice_result % 2 == 0 and guess ==     "even":
    money = money + bet
    return "The combined dice rolls were even, congratulations! You have won £" + str(bet) + "!\n" + "You now have £" + str(money) + " in your account."

  elif dice_result % 2 <= 0 and guess == "odd":
    money = money + bet
    return "The combined dice rolls were odd, congratulations! You have won £" + str(bet) + "!\n" + "You now have £" + str(money) + " in your account."
  
  else:
    money = money - bet
    return "Unfortunately you have guessed incorrectly, better luck next time.\n" + "You now have £" + str(money) + " in your account."

def higher_lower(guess, bet):
  global money
  List1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  result = random.choice(List1)

  if guess < 1 or guess > 13:
      return "Whoops! you have entered your choice incorrectly! Try entering a number between 1 to 13 to continue"

  elif bet <= 0:
    return "You cannot bet a negative amount of money, please select a higher amount."

  elif money < 0:
    return "You have run out of money, please deposit more to continue."

  elif guess > result:
    money = money + bet
    return "Congratulations, you have picked the higher card and won!\n" + "You now have £" + str(money) + " in your account." 

  elif guess < result:
    money = money - bet
    return "Unfortunately you haven't picked the higher card and lost this time!\n" + "You now have £" + str(money) + " in your account." 

  else:
    money
    return "You have picked a card with the same value as your opponent, it is a tie!\n" + "You now have £" + str(money) + " in your account." 

def roulette_odd_or_even(guess, bet):
    global money
    number = random.randint(1,36)
    
    if guess != "even" and guess != "odd":
      return "Whoops! you have entered your choice incorrectly! Try entering either odd or even to continue"

    elif bet <= 0:
      return "You cannot bet a negative amount of money, please select a higher amount."

    elif money < 0:
      return "You have run out of money, please deposit more to continue."

    elif number % 2 == 0 and guess == "even":
      money = money + bet
      return "Congratulations! you guessed even and was correct!\n" + "You now have £" + str(money) + " in your account."
    
    elif number % 2 == 1 and guess == "odd":
      money = money + bet
      return "Congratulations! you guessed odd and was correct!\n" + "You now have £" + str(money) + " in your account."

    else:
      money = money - bet
      return "Unfortunately you have guessed incorrectly this time!\n" + "You now have £" + str(money) + " in your account."

def roulette_red_or_black(guess, bet):
  global money
  colour = random.choice(["red","black"])

  if guess != "red" and guess != "black":
      return "Whoops! you have entered your choice incorrectly! Try entering either red or black to continue"

  elif bet <= 0:
    return "You cannot bet a negative amount of money, please select a higher amount."
    
  elif money < 0:
    return "You have run out of money, please deposit more to continue."

  elif colour == "red" and guess == "red":
      money = money + bet
      return "Congratulations! you guessed red and was correct!\n" + "You now have £" + str(money) + " in your account."
  
  elif colour == "black" and guess == "black":
      money = money + bet
      return "Congratulations! you guessed black and was correct!\n" + "You now have £" + str(money) + " in your account."

  else:
    money = money - bet
    return "Unfortunately you have guessed incorrectly this time!\n" + "You now have £" + str(money) + " in your account."

def roulette_0_36(guess, bet):
  global money
  number = random.randint(0,36)

  if guess < 0 or guess > 36:
      return "Whoops! you have entered your choice incorrectly! Try entering a number between 0 to 36 to continue."

  elif bet <= 0:
    return "You cannot bet a negative amount of money, please select a higher amount."

  elif money < 0:
    return "You have run out of money, please deposit more to continue."

  elif number == guess:
      money = money + bet*36
      return "Congratulations! you guessed correctly!\n" + "You now have £" + str(money) + " in your account."

  else:
    money = money - bet
    return "Unfortunately you have guessed incorrectly this time!\n" + "You now have £" + str(money) + " in your account."
#Call your game of chance functions here
print(money_deposit)
print(coin_flip('Heads', 30))
print(cho_han("odd", 30))
print(higher_lower(2, 30))
print(roulette_odd_or_even("odd", 30))
print(roulette_red_or_black("red", 30))
print(roulette_0_36(4, 30))
print(money_withdrawal)