import numpy as np
import matplotlib.pyplot as plt
import math as math

#propierties of aluminium alloy 5083
E=70.3*10**9; v=0.33; a=1.5; b=0.75; t=0.001
ys=0.8*195*10**6; wmax=t/20; F=980; es=156*10**6

#points of load
x1=a/4; x2=3*a/4; y1=b/4; y2=3*b/4
#modulus of rigidity
D=E*t**3/(12*(1-v**2))

#range of variables x y y
x=np.linspace(0,1.5,20)
y=np.linspace(0,7.5,20)

def sum_wmn(k):
  m=1
  wmn=0
  while m<=k:
    for n in range(1,k+1):
      Pmn=(4*F/(a*b))*(math.sin(math.radians(m*math.pi*x1/a))+math.sin(math.radians(m*math.pi*x2/a)))*(math.sin(math.radians(n*math.pi*y1/b))+math.sin(math.radians(n*math.pi*y2/b)))
      Wmn=Pmn/(D*((m*math.pi/0.75)**2+(n*math.pi/0.375)**2)**2)
      wxy=Wmn*math.sin(math.radians(m*math.pi*x1/a))*math.sin(math.radians(n*math.pi*y1/b))
      wmn+=wxy
    m+=1
  return wmn

def sumMy(k):
  m=1
  My=0
  while m<=k:
    for n in range(1,k+1):
      Pmn=(4*F/(a*b))*(math.sin(math.radians(m*math.pi*x1/a))+math.sin(math.radians(m*math.pi*x2/a)))*(math.sin(math.radians(n*math.pi*y1/b))+math.sin(math.radians(n*math.pi*y2/b)))
      Wmn=Pmn/(D*((m*math.pi/1.75)**2+(n*math.pi/0.75)**2)**2)
      my=D*Wmn*((n*math.pi/b)**2+0.33*(m*math.pi/a)**2)*math.sin(math.radians(m*math.pi*x1/a))*math.sin(math.radians(n*math.pi*y1/b))
      My+=my
    m+=1
  return My

re=1
while re>0.0075:
  i=int(input("enter an odd number:"))
  while i%2==0:
    i=int(input("enter an odd number again:"))
    break
  j=i
  wmn0=sum_wmn(i)
  wmn1=sum_wmn(i-2)
  re=(wmn0-wmn1)/wmn0
  if re>0.0075:
    print("this value doesn´t correspond to minimum dimension")
  else:
    print("this value is correct")

'''m=i; n=i'''
d=1
while d>t/20 and es>=156*10**6:
  t=float(input("enter the thickness:"))
  es=sumMy(7)*6/(t**2)
  d=sum_wmn(i)
  if d>t/20 and es>=156*10**6:
    print("Cannot be considered in failure modes")
  else:
    print("the thickness is correct")

### Function of load aplied
def pxy(x,y,k):
  m=1
  pxy=0
  while m<=k:
    for n in range(1,k+1):
      Pmn=(4*F/(a*b))*(math.sin(math.radians(m*math.pi*x1/a))+math.sin(math.radians(m*math.pi*x2/a)))*(math.sin(math.radians(n*math.pi*y1/b))+math.sin(math.radians(n*math.pi*y2/b)))
      pxy=Pmn*math.sin(math.radians(m*math.pi*x/a))*math.sin(math.radians(n*math.pi*y/b))
      pxy+=pxy
    m+=1
  return pxy

plt.plot(x,y,i)

#plt.plot(x,y,pxy(x,y, i))




