#Creator: XRomoYT
print('Calculator 3n+1')
num =  int(input("You'r number: "))
biggest_num = []
while True:
    if num == 1:
        print('1')
        print(' ')
        print('Biggest num: ', max_big)
        print(' ')
        biggest_num.clear()
        print('Calculator 3n+1')
        num =  int(input("You'r number: "))
    if num == 0:
        print('Chose another number')
        print('Calculator 3n+1')
        num =  int(input("You'r number: "))
    if num >= 2:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num)
    biggest_num.append(num)
    max_big = max(biggest_num)
    
