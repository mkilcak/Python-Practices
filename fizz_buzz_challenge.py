fizz_buzz_challenge = int(input('Enter Number: '))
a= fizz_buzz_challenge % 3 == 0  
b= fizz_buzz_challenge % 5 == 0
if a and b:
    print("Fizz_Buzz") 
elif a:
        print("Fizz")
elif b:
    print("Buzz")
else:
    print(fizz_buzz_challenge)



#Define a function called "fizz_buzz_challenge"
#and assign "input" as a parameter
#then follow the statements below
#if the input we give is divisible by 3 and 5 return "FizzBuzz"
#If the input we give is divisible by 3, retur "Fizz"
#If the input we give is divisible by 5, return "Buzz"
#If none of the statements are true, print input
# 