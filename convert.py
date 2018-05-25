#date,length,seconds,pulse,weight,weather,notes,shoe 
f = open('Laufergebnisse.txt','r')

for line in f:
    values = line.rstrip().split(';')
    date = values[0]
    length = values[1]
    seconds = values[2]
    pulse = values[3]
    weight = values[4]
    weather = values[5]
    notes = values[6]
    shoe  = values[7]
    print length
    
f.close()