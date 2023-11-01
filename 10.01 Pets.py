class Pet():
    def __init__(self):
        self.Name = ""
        self.Type = ""
        self.Age = 0
f = open('10.01 Pets.txt')
list = []
for i in f:
    line = i.replace('\n','')
    data = line.split(', ')

    temp = Pet()

    temp.Name = data[0]
    temp.Type = data[1]
    temp.Age = int (data[2])

    list.append(temp)
for obj in list:
    print("{:>10} {:>10} {:>10}".format(obj.Name, obj.Type, obj.Age))
f.close()