import matplotlib.pyplot as plt

t1=500
t2=273


a=0.2
b=10
c=-0.1
d=170

max_rect=0
max_gamma=0
Tf_max=0
Tr_max=0

def range_with_float(start,end,offset):
    while start<end:
        yield start
        start+=offset

for g in range_with_float(0,10,0.00001):
    t_f=((-2*(g*b+d))+((((4*(g*b+d)**2))+(4*(g*a+c)*((g*a*t1*t1)+(c*t2*t2)+(2*g*b*t1)+(2*d*t2))))**0.5))/(2*(g*a+c))
    t_r=((-2*(g*b+d))+((((4*(g*b+d)**2))+(4*(g*a+c)*((g*a*t2*t2)+(c*t1*t1)+(2*d*t1)+(2*g*b*t2))))**0.5))/(2*(g*a+c))
    rect=(((a*t1*t1*0.5)+(b*t1))-((a*t_f*t_f*0.5)+(b*t_f)))/ (((a*t_r*t_r*0.5)+(b*t_r))-((a*t2*t2*0.5)+(b*t2)))
    if rect>max_rect:
        max_rect =rect
        max_gamma=g
        Tf_max=t_f
        Tr_max=t_r
    
   
print("\n\nMaximum rectification ratio=",max_rect,"\nMaximum gamma=",max_gamma,"\nTf_max=",Tf_max,"\nTr_max=",Tr_max)



