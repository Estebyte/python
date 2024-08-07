my_list = [9, 2, 4, 7, 3, 8, 1, 3, 0, 5]
my_list.sort() #Kinda boring, huh?
print(my_list) 

def my_sort(my_list):
    for i in my_list:
        if my_list[i] > my_list[i + 1]:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            print(my_list)
    

my_sort(my_list)
print(my_list)