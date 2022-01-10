with open('Perepis.txt') as f:
    x=int(input())
    y=int(input())
    k=0
    L={}
    for i in f:
        c=i[0:i.find(' ')]
        L[c] = i[len(i)-5:len(i)-1]
        if int(i[len(i)-5:len(i)]) < 1978: #Проверка даты
            k+=1
        if int(i[len(i)-5:len(i)]) < y and int(i[len(i)-5:len(i)]) > x: #Диапазон
            print(i)
    print('Жителей до 1978 - ',k)
    print(L)

