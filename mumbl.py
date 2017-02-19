import random
import itertools
import os
import time

#Lists for shuffling user input:
deck = list(itertools.product(['One','Two','Three','Four','Five','Six','Seven',
                               'Eight','Nine','Ten','Eleven','Twelve','Thirteen'],
                               ['Spades','Clubs','Hearts','Diamonds'],['Blue',
                               'White']))

#List for sorting hearts/diamonds into Uppercase letters:
redLetters = list(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                   'P','Q','R','S','T','U','V','W','X','Y','Z'])

#List for sorting spades/clubs into lowercase letters:
blackLetters = list(['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                     'o','p','q','r','s','t','u','v','w','x','y','z'])

#Binary tables for "Blue back" solutions:
binary = list(['00000','00001','00010','00011','00100','00101','00110','00111',
               '01000','01001','01010','01011','01100','01101','01110','01111',
               '10000','10001','10010','10011','10100','10101','10110','10111',
               '11000','11001','11010','11011','11100','11101','11110','11111'])

#Linking for binary translations:
symbols = list(['0','1','2','3','4','5','6','7','8','9','?','!','@','$','&','*','%',
                '#','.','~','(',')','_','-','+','=','<','>','[',']','^',','])

output = []

#User input for password entering:
print "Enter word for scrambling:"
rawWord = raw_input("> ")

print "Enter Tumbler Code:"
tumbler = raw_input("> ")

#Shuffle for tables to scramble user input:
random.seed(rawWord + tumbler)
random.shuffle(deck)
random.shuffle(redLetters)
random.shuffle(blackLetters)
random.shuffle(binary)
random.shuffle(symbols)

#For Organizing the shuffle of the rawWord & tumbler:
i = 0
while i < 20:
    #For sorting out Symbols through binary sorting:
    if deck[i][2] == 'Blue':
        j = 0
        l = list()
        while j < 5:
            if deck[j + i][2] == "Blue":
                for k in range(1):
                    l.append(0)
                    j = j + 1
            elif deck[j + i][2] == "White":
                for k in range(1):
                    l.append(1)
                    j = j + 1
            else:
                print "There was an error in binary/symbol sorting."
                break
        binResult = [ ''.join(str(x) for x in l) ]
        a = binary.index(binResult[0])
        b = symbols[a]
        output.append(b)
        print a
        print b
        i = i + 1

    #For sorting out Letters through suit sorting:
    elif deck[i][2] == 'White':
        if deck[i][1] == 'Hearts' or deck[i][1] == 'Diamonds':
            output.append(redLetters[i])
            i = i + 1
        elif deck[i][1] == 'Spades' or deck[i][1] == 'Clubs':
            output.append(blackLetters[i])
            i = i + 1
        else:
            print "There was an error in letter sorting."
            break
    else:
        print "There was an error sorting backing color"
        break

os.system('clear')
print ""
print "%s + %s = %s" % (rawWord, tumbler, ''.join(map(str, output)))
print ""
time.sleep(5)
