#marks =59
#result = " "
#if marks < 34:
 #   result = "fail"
#elif marks < 60:
 #   result = "passed with first class"
#elif marks < 75:
 #   result = "passed with distinction"
#else:
 #   result = "passed"


#print(result)
#match statement
#def checkvowel(n):
 #   match n:
  #      case 'a':
   #         return "Vowel alphabet"
    #    case 'e':
     #       return "Vowel alphabet"
      #  case 'i':
       #     return "Vowel alphabet"
        #case 'o':
         #   return "Vowel alphabet"
        #case 'u':
         #   return "Vowel alphabet"
#print(checkvowel('q'))
#print(checkvowel('e'))
#print(checkvowel('s'))

#while
#i= 1
#while i<6:
 #   print(i)
  #  i+=1
#
#discount =0
#amount = 1000
#if amount >= 2000:
 #   discount = amount * 20/100

#elif amount >= 1000:
 #   discount = amount * 10/100

#print('amount', amount - discount)

#
#age= 17
#print('age', age)
#if age >=18:
 #   print('he/she is major')
#else:
 #   print('he/she is minor')
#
#num=80
#print ("num = ",num)
#if num%2==0:
 #  if num%3==0:
      #print ("Divisible by 3 and 2")
   #else:
    #  print ("divisible by 2 not divisible by 3")
#else:
 #  if num%3==0:
  #    print ("divisible by 3 not divisible by 2")
   #else:
    #  print ("not Divisible by 2 not divisible by 3")
#
#
#import random
#x = "heads"
#y = "tails"
#value = str(input(" Enter u r value x / y "))
#print(random.choice([x,y]))
#if value == random:
# print("You are sucess")
#else:
#  print("You are not sucess")
#
#coin = input("Enter coin value (x, y, z): ")

#coin_values = {'x': 'heads',  'y': 'tails', 'z': 'null'}

#if coin in coin_values:
#  print(coin, "coin is", coin_values[coin])
#else:
#  print("Invalid coin value")
#
#coin = input("Enter coin value (x, y, z): ")  # Use input() directly, no need for str() or extra quotes
#x = 'heads'
#y = 'tails'
#z = 'none'

#if coin == x:  # Use == for equality comparison, not 'is'
   # print(x, "coin is heads")
#elif coin == y:
  #  print(y, "coin is tails")
#elif coin == z:
 #   print(z, "null")  # Changed "i" to "coin" to match variable name
#else:
 #   print("Invalid coin value")
#
#import random

#user_choice = input("Enter your choice (heads or tails): ").lower()

#if user_choice == 'heads' or user_choice == 'tails':
 #   coin_toss = random.choice(['heads', 'tails'])
  #  print("Coin toss result:", coin_toss)

    #if user_choice == coin_toss:
     #   print("Congratulations! You won!")
    #else:
     #   print("Sorry! You didn't win this time.")
#else:
 #   print("Invalid choice. Please enter 'heads' or 'tails'.")
#numbers = range(5)
#print (list(numbers))
# step is 1 by default, range generated from 10 to 19
#numbers = range(10,20)
#print (list(numbers))
# range generated from 1 to 10 increment by step of 2
#numbers = range(15,20)
#print (list(numbers))

fact=1
N =8
for x in range(1, N+1):
   fact=fact*x
print("factorial of {} is {}".format(N, fact))