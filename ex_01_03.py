hrs = input("enter hours:")
rate = input ("enter rate :")
h= float (hrs)
r= float (rate)
if h> 40 :
    py= 40*r
    pyo= (h-40)*1.5*r
    pay = py+ pyo
    print (pay)
else :
    pay = h*r
    print (pay)
