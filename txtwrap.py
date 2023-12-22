#Want to divide your consecutive text? 
#With this code you can input a string (eg: ABCDEFG) and the number of letters of the wrap (eg: 3)
#It will divide your string by as many characters you chose

import textwrap

def wrap(string, max_width):
    i = 0
    stringa = []
    for x in range(10):
        if (len(string)- i - max_width) > 0:
            stringa = string[i:i+max_width]
            print(stringa)
            i+=max_width
        else:
            return string[i:]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
