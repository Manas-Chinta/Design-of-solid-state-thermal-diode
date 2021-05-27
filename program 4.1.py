import matplotlib.pyplot as plt

t1=473
t2=300


a=0.39
b=1
c=-0.34
d=170

x=[]
y=[]

def range_with_float(start,end,offset):
    while start<end:
        yield start
        start+=offset

for g in range_with_float(0,1,0.01):
    t_f=((-2*(g*b+d))+((((4*(g*b+d)**2))+(4*(g*a+c)*((g*a*t1*t1)+(c*t2*t2)+(2*g*b*t1)+(2*d*t2))))**0.5))/(2*(g*a+c))
    t_r=((-2*(g*b+d))+((((4*(g*b+d)**2))+(4*(g*a+c)*((g*a*t2*t2)+(c*t1*t1)+(2*d*t1)+(2*g*b*t2))))**0.5))/(2*(g*a+c))
    
    x.append(g)
    rect=(((a*t1*t1*0.5)+(b*t1))-((a*t_f*t_f*0.5)+(b*t_f)))/ (((a*t_r*t_r*0.5)+(b*t_r))-((a*t2*t2*0.5)+(b*t2)))
    y.append(rect)
       


plt.plot(x,y,label="rect")

plt.xlabel("gamma(L2/L1)")
plt.ylabel("rectification ratio")

plt.legend()
plt.show()


