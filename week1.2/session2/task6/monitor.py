# Week 1.2, Session 2: Task 6
temperature = int(input("Enter the machine temperature in Celsius: "))
pressure = int(input("Enter the machine pressure in PSI: "))
opperational_status = int(input("Enter opperational status (1 = operating, 0 = stopped): "))

if temperature > 80:
    print ("Temperature is too high.Shut down the machine.")
elif temperature >= 50:
    