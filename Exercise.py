#!/usr/bin/env python

def uppercase(str):
    """
    This fucntion prints uppercase followed by a new line
    """
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i)- 32)
            print("{}".format(i),end="")
        print()

    uppercase()        

