import matplotlib.pyplot as plt

t1=500
t2=273


a=0.2
b=10
c=-0.1
d=170

Tf=[]
Tr=[]

print("max_rectification            Gamma                Tf                   Tr")

def range_with_float(start,end,offset):
    while start<end:
        yield start
        start+=offset
for k in range(1,90):
    a=0.2+(0.1*k)
    b=10+(2*k)
    c=-0.1-(0.001*k)
    d=200

    max_rect=0
    max_gamma=0
    Tf_max=0
    Tr_max=0

    for g in range_with_float(0,5,0.00001):
        t_f=((-2*(g*b+d))+((((4*(g*b+d)**2))+(4*(g*a+c)*((g*a*t1*t1)+(c*t2*t2)+(2*g*b*t1)+(2*d*t2))))**0.5))/(2*(g*a+c))
        t_r=((-2*(g*b+d))+((((4*(g*b+d)**2))+(4*(g*a+c)*((g*a*t2*t2)+(c*t1*t1)+(2*d*t1)+(2*g*b*t2))))**0.5))/(2*(g*a+c))
        rect=(((a*t1*t1*0.5)+(b*t1))-((a*t_f*t_f*0.5)+(b*t_f)))/ (((a*t_r*t_r*0.5)+(b*t_r))-((a*t2*t2*0.5)+(b*t2)))
        if rect>max_rect:
            max_rect =rect
            max_gamma=g
            Tf_max=t_f
            Tr_max=t_r
    Tf.append(Tf_max)
    Tr.append(Tr_max)

plt.plot(Tf,Tr)
plt.xlabel("T_f")
plt.ylabel("T_r")
plt.show()

