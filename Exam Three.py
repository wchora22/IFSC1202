import math
from math import pi
class Triangle():
    def __init__(self,side1,side2,side3):
        self.Side1=side1
        self.Side2=side2
        self.Side3=side3
    def triangle_type(self):
        if(self.Side1==self.Side2 and self.Side2==self.Side3):
            return "Equilateral"
        elif(self.Side1==self.Side2 or self.Side2==self.Side3 or self.Side3==self.Side1):
            return "Isoceles"
        else:
            return "Scalene"
    def perimeter(self):
        return self.Side1+self.Side2+self.Side3
    def area(self):
        if (self.triangle_type()=="Equilateral"):
            return (math.sqrt(3)/4)*(self.Side1*self.Side1)
        elif (self.triangle_type()=="Isoceles"):
            a=0.00
            b=0.00
            if (self.Side1==self.Side2):
                a=self.Side1
                b-self.Side3
            else:
                a=self.Side1
                b=self.Side2
            return (b*math.sqrt((4*a*a)-(b*b)))/4
        else:
            s=self.perimeter()/2
            return (s*(s-self.Side1)*(s-self.Side2)*(s-self.Side3))**0.5
    def angles(self):
        if(self.triangle_type()=="Equilateral"):
            return [60,60,60]
        elif(self.triangle_type=="Isoceles"):
            b=0.00
            if (self.Side1==self.Side2):
                b=self.Side3
                h= math.sqrt(math.pow(self.Side1,2)-math.pow(b/2,2))
                angle1= (math.acos((b/2*b/2+self.Side1*self.Side1-h*h)/(b*self.Side1)))*180/pi;
                angle2=angle1
                angle3=180-angle1-angle2
                return [angle1,angle2,angle3]
            elif (self.Side2==self.Side3):
                b=self.Side1
                h= math.sqrt(math.pow(self.Side2,2)-math.pow(b/2,2))
                angle1= (math.acos((b/2*b/2+self.Side2*self.Side2-h*h)/(b*self.Side1)))*180/pi;
                angle2=angle1
                angle3=180-angle1-angle2
                return [angle1,angle2,angle3]
            else:
                b=self.Side2
                h=math.sqrt(math.pow(self.Side1,2)-math.pow(b/2,2))
                angle1= (math.acos((b/2*b/2+self.Side1*self.Side1-h*h)/(b*self.Side1)))*180/pi;
                angle2=angle1
                angle3=180-angle1-angle2
                return [angle2,angle1,angle3]
        else:
            b=self.Side3
            h=2*(self.area()/b)
            a1= math.sqrt(math.pow(self.Side1,2)-math.pow(h,2))
            a2=b-a1
            angle1=(math.acos((a1*a1+self.Side1*self.Side1-h*h)/(2*a1*self.Side1)))*180/pi;
            angle2=angle1
            angle3=180-angle1-angle2
            return [angle1,angle2,angle3]

obj=[]
filename=open("Exam Three Triangles.txt", 'r')
for x in filename:
    values= x.split(',')
    s1= float(values[0])
    s2= float(values[1])
    s3= float(values[2])
    obj.append(Triangle(s1,s2,s3))
print('{:>20}{:>12}{:>12}{:>12}{:>12}{:>8}{:>13}{:>12}{:>12}'.format('Type','Side 1','Side 2','Side 3', 'Perimeter', 'Area', 'Angle 1', 'Angle 2', 'Angle 3'))
for item in obj:
    print('{:>20}{:>12}{:>12}{:>12}{:>12}{:>8}{:>13}{:>12}{:>12}'.format(item.triangle_type(),item.Side1, item.Side2, item.Side3, item.perimeter(), round(item.area(),3), round(item.angles()[0],3), round(item.angles()[1],3),round(item.angles()[2],3)))