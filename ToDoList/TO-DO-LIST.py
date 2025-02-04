tasks = []
while True:
    print("\n")
    print("Welcome to my life organize app\n")
    print("------------------\n")
    
    print("1-Enter a task\n2-View Tasks\n3-Delete Tasks\n4-Quit")
    x = int(input("pick a choise: "))
    print()
    if x ==4:
        break
    if x != 1 and x !=2 and x !=3 and x !=4:
        print("\n\n\n\nplease enter a valid number")
        continue
    while x == 1:
        j = input("enter the tasks you want to do: ")
        print("when done enter (done)")
        if j == 'done':
            break
        tasks.append(j)
        with open('tasks.txt','w') as file:
            for item in tasks:
                file.write(item+'\n')       
    while x == 2:
        print("------------------\n")
        print("Your tasks are:\n")
        with open('tasks.txt','r') as file:
            reading = file.readlines()
        for num,task in enumerate(reading, start=1):
            print(num,'-',task)
        print("------------------")
        break
    while x == 3:
        if not tasks:
            print("there's no tasks to delete")
            break
        try:
            v = int(input("enter the number of the task you wanna delete: "))
            with open('tasks.txt','r') as file:
                reading = file.readlines()
            if 0 < v <= len(reading):
                tasks.pop(v-1)
                deleted_task = reading.pop(v-1)
                with open('tasks.txt','w') as file:
                    file.writelines(reading)
                print("Task deleted")
            else:
                print("Invalid Task number")
        except ValueError:
            print("Please enter a valid number.")
        except IndexError:
            print("Task number out of range.")
        break
#
        
    

        
        










    
