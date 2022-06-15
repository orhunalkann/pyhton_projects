import random
from game_data import data

def oyun():
     ##Chose data randomly
     degerler =[]
     for a in range(2):
          bilgi_random = data[random.randint(0, len(data) - 1)]
          degerler.append(bilgi_random)

     data1 = degerler[0]
     data2 = degerler[1]

     print(f"\nCompare A : {data1['name']}, {data1['description']} from {data1['country']}  ")
     print(f"\nCompare B : {data2['name']}, {data2['description']} from {data2['country']}  ")
     def user_pick():
          pick = input("Who has more followers? Type 'A' or 'B':")
          if pick == "a":
               return "data1"
          elif pick == "b":
               return "data2"
     userpick = user_pick()

     def dogru_cevap(insta1, insta2):
          """Take 2 input and return higher answer"""
          if insta1 < insta2:
               return "data2"
          else:
               return "data1"
     dogrucevap = dogru_cevap(data1['follower_count'], data2['follower_count'])

     def is_user_picked_true(answer, target):
          """dogru cevap ile user cevabini karsilastirir"""
          if answer == target:
               return "dogru"

          else:
               return "yalnis"


     sonuc = is_user_picked_true(userpick, dogrucevap)

     if sonuc == "dogru":
          print("\nYou got this, next one is : ")
          oyun()
     else:
          print("Wrong answer Game over")
          again = input("Do you wanna play again ? Y/N ")
          if again == "y":
               oyun()
          elif again == "n":
               print("THANKS FOR PLAYING")

oyun()

