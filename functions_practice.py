def hello():
    print("Hello User!")

def pack(item1,item2,item3):
    my_list = [item1,item2,item3]
    print(f"The items on my list are: {my_list}")
    return my_list

def eat_lunch(list):
    str_total = len(list)

    if str_total > 0:
        for x in list:
            if list.index(x) == 0:
                print(f"First I eat {x}!")
            else:
                print(f"Next I eat {x}!") 
    else:
        print("My lunchbox is empty!")

hello()
eat_lunch(pack("Steak", "Potatoes", "Roasted Corn"))

print("SOMEONE STOLE MY LUNCH!")
list = []
eat_lunch(list)