"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""
a=input("What is  your name with a full sentence: ")

def ask_user(a):
    s = a.split()[::-1]
    l=[]
    for i in s:
        l.append(i)
    print(" ".join(l))
ask_user(a)
    



    
