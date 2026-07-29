score = int(input('score = '))

if 0 <= score <= 100 :
    if 100 >= score >= 90 :
        print ('A')
    elif score >= 80 :
        print ('B')
    elif score >= 70 :
        print ('C')
    elif score >= 60 :
        print ('D')
    else :
        print ('F')
else :
    print ('input data error')

""""""

score = int(input('score: '))

if 0<= score <= 100 :
    print ('Pass' if score >= 60 else 'Fail')
else:
    print("input out of range")


