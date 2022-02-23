def parent_function():
    def child_function():
        return "this is gg"
    return child_function()

#print(parent_function())

def print_all_elements(list_of_things):
    def print_each_element(things):
        print("things : ", things, "types : ", type(things))
        for thing in things:
            print("thing : ",thing)

    if len(list_of_things) > 0:
        print_each_element(list_of_things)
    
    else:
        print("empty things")


def print_each_element2(things):
    for thing in things:
        print(thing)

def print_all_elements2(list_of_things):
    if len(list_of_things) > 0:
        print_each_element2(list_of_things)
    
    else:
        print("empty things")

print_all_elements2(list_of_things=[1,2,4])

def is_paid_user(func):
    user_paid = True # 간단화 하기 위해 무조건 True

    def wrapper(*args, **kwargs):
        if user_paid:
            func() 
        else:
            return

    return wrapper