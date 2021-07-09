#TASK
#the provided code stub reads two integers,  and , from STDIN.
#add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
#no rounding or formatting is necessary.

#CODE
from __future__ import division

def new_func(a, b):
    print(a // b)
    print(a / b)

if __name__ == "__main__":
    a = int(raw_input())
    b = int(raw_input())
    new_var = new_func(a, b)
    new_var