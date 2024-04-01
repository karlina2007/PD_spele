
from random import randint
import random
  
def generate_sk():
  A = random.sample(range(1, 16), 5)
  B = random.sample(range(16, 31), 5)
  C = random.sample(range(31, 46), 4)
  D = random.sample(range(46, 61), 5)
  E = random.sample(range(61, 76), 5)
  return [A,B,C,D,E]
#No 1 līdz 75
def print_nums(card):
    print ('   B   I   N   G   O   ')
    print (f' {card[0][0]:>3} {card[1][0]:>3} {card[2][0]:>3} {card[3][0]:>3} {card[4][0]:>3}')
    print (f' {card[0][1]:>3} {card[1][1]:>3} {card[2][1]:>3} {card[3][1]:>3} {card[4][1]:>3}')
    print (f' {card[0][2]:>3} {card[1][2]:>3}  -- {card[3][2]:>3} {card[4][2]:>3}')
    print (f' {card[0][3]:>3} {card[1][3]:>3} {card[2][2]:>3} {card[3][3]:>3} {card[4][3]:>3}')
    print (f' {card[0][4]:>3} {card[1][4]:>3} {card[2][3]:>3} {card[3][4]:>3} {card[4][4]:>3}')
#mazāk par 3 nevar, bet var vairāk
def main():
    while True:
        g = input("Kā varu palīdzēt?")
        if g.lower() == "q":
            print("Atā!")
            break
        elif g.lower() == "bingo":
            print("Malacis!")
            break
        elif g.lower() == "s":
            print(randint(1, 76))
        elif g.lower() == "ģ":
            card = generate_sk()
            print_nums(card)

if __name__ == "__main__": #restartē, lai iegūtu kartiņu ar citiem cipariem
    main()
        

        







