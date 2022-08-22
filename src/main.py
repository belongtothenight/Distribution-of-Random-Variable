from os import system

print("choose type")
print("1.Uniform  2.Bernuoulli 3.Geometric 4.Poisson ")
pick=input()
if pick==1:
    print("輸入L")
    l1=input("")
    l=float (l1)
    print("Uniform RV")
    print("期望值E="+((l+1)/2))
else:
    print("a")
#Bernuoulli RV
#Geometric  RV
#Poisson    RV

system('cmd \k')