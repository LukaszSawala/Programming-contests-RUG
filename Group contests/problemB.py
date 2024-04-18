

n = int(input())
truthVal = [int(i == 'T') for i in input().split()]
logicalOp = ['*','-','+']
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
all = input().split()
array = []
for character in all:
    if character not in logicalOp:
        value = truthVal[alphabet.index(character)]
        array.append(value)
    else:
        last = array.pop()
        if character == '*':
            last2 = array.pop()
            array.append(last*last2)
        elif character == '+':
            last2 = array.pop()
            if last == 1 and last2 == 1:
                array.append(1)
            else:
                array.append(last+last2)
        else:
            if last == 0:
                last = 1
            else:
                last = 0
            array.append(last)

if array[-1] == 0:
    print('F')
else:
    print('T')