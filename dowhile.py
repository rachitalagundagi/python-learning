# DO WHILE LOOP WITH CONTINUE
i=0
while True:
    print(i)
    i+=1
    if(i%100==0):
        break

i=0
while True:
    for i in range(12):
       
        if(i==10):
            continue
            print(i)