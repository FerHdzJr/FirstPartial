#Quien es el ciervo raton???
i1=15
i2=17
i3=21
v1=2/i1
v2=2/i2
v3=2/i3
print("Velocity of iteration #1: "+str(v1)+" m/s")
print("Velocity of iteration #2: "+str(v2)+" m/s")
print("Velocity of iteration #3: "+str(v3)+" m/s\n")

print("The avarge velocity is: "+str((v1+v2+v3)/3)+" m/s\n------------")

n=int(input("Insert the distance covered (in meters):\n"))
v4=n/i1
v5=n/i2
v6=n/i3
av=(v4+v5+v6)/3
at=(i1+i2+i3)/3
print("The avarage acceleration is: "+str(av/at)+ "\n")
print("Velocity of iteration #1: "+str(v4)+" m/s")
print("Velocity of iteration #2: "+str(v5)+" m/s")
print("Velocity of iteration #3: "+str(v6)+" m/s\n")
print("Rate change between iteration #1 and #2 is: "+str(v5-v4))
print("Rate change between iteration #2 and #3 is: "+str(v6-v5))
