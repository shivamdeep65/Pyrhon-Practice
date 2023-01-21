command =""
started = False
while True:
    command= input(">").lower()
    if command == "start":
        if started:
            print("Car Already started")
        else:
            started = True
            print("Car Started")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print ("Car Stopped")
    elif command== "help":
        print(''' start- to start the car
        stop- to stop the car
        quit- to quit''')
    elif command== "quit":
        print("Game Exited")
        break
    else:
        print('"Sorry could not understand the command"')