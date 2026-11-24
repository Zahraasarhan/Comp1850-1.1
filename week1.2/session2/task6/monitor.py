# Week 1.2, Session 2: Task 6
temperature = int(input("Enter the machine temperature in Celsius: "))
pressure = int(input("Enter the machine pressure in PSI: "))
opperational_status = int(input("Enter opperational status (1 = operating, 0 = stopped): "))

if temperature > 80:
    print ("Temperature is too high.Shut down the machine.")
elif temperature >= 50:
    print ("Temperature is within safe limits.")
else:
    print ("The machine temperature is low and no action is needed.")


if pressure > 100:
    print ("High pressure is detected and recommend maintenance.")
elif pressure >= 70:
    print ("The pressure is stable.")
else:
    print (" The pressure is low and the system is operating normally.")

if opperational_status == 1:
    if temperature > 80 or pressure > 100 :
        print(" The machine is running in unsafe conditions and recommend shutting it down")
    else:
        print("The machine is running normally")
else:
    print("The machine is stopped and no immediate action is needed.")