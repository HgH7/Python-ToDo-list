tasks = []
while True:
    print("\n")
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
    while x == 2:
        for num,task in enumerate(tasks, start=1):
            print(num,'-',task)
        break
    while x == 3:
        v = int(input("enter the number of the task you wanna delete: "))
        tasks.pop(v-1)
        break









    
