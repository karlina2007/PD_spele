from random import randint

# atslegas = list(valstis.keys())





while True:
 
    g = input("Kā varu palīdzēt?")
    if g.lower() == "q":
        print("Paldies par spēli!")
        break
    elif g.lower() == "ģ":
        print(randint(1, 100))


       
    elif g.lower() =="bingo":
        print("Malacis!")
        break
    elif g.lower() =="s":
       print(randint(1, 100))
    else:
        print("Nesapratu")





