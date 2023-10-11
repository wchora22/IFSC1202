values= input("Enter values seperated by spaces: ")
input_list=values.split()
int_list = []
for i in range(len(input_list)):
    int_list.append(int(input_list[i]))
for i in range(1, len(int_list),2):
    print(int_list[i])