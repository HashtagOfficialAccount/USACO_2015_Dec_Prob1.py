x = open("paint.in","r")
farmer = [int(i) for i in x.readline().split()]
bessie = [int(i) for i in x.readline().split()]
count = 0
#sub = 1
farmer_list = []
for i in range(farmer[0],farmer[1]):
    count += 1
    farmer_list.append(i)
for i in range(bessie[0], bessie[1]):
    if i in farmer_list:
        continue
        #sub += 1
    else:
        count+=1
x.close()
x = open("paint.out","w")
x.write(str(count))
x.close()
    
