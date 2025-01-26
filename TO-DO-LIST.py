while True:
    print("1-Enter a task\n2-View Tasks\n3-Delete Tasks\n4-Quit")
    x = int(input("pick a choise: "))
    if x == 1 or x == 2 or x == 3 or x == 4:
        break
    else:
        print("\n\n\n\nplease enter a valid number")
        continue
tasks = []
while x == 1:
    j = input("enter the tasks you want to do: ")
    tasks.append(j)
    print("when done enter (done)")
    if j == 'done':
        break
tasks.pop(-1)
print(tasks)



    
