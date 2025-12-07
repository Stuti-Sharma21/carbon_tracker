print("Welcome To Daily Carbon Tracker !!!")
print("Hi what do u want for today")
print("1) Add a new record for today ")
print("2) View history")
print("3) Exit")
print("4) ")
choicee=int(input("Please enter your choice : "))
if choicee==1:
    carbon_emission=0.2 # (1 km = 0.2 kg CO₂)
    daily_limit=20
    unit=0.8 # (1 electricity unit = 0.8 kg CO₂)
    while True:
        #travel
        km=float(input("Enter the number of kilometers u traveled today : "))
        travel_emission=km*carbon_emission
        print("Travel emission:", travel_emission, "kg CO2")
        
        #electricity
        electricity=float(input("enter the number of electricity units used today : "))
        electricity_emission=electricity*unit
        print("Electricity emission:", electricity_emission, "kg CO2")
    
        #food
        food=input("did u eat a veg or non_veg meal : ").lower()
        if food=="veg":
            food_emission=1
        else:
            food_emission=3
        print("Food emission:", food_emission, "kg CO2")

        #total daily emission
        total_emission=travel_emission+electricity_emission+food_emission
    
        print("Your total emission for today are", total_emission, "kg CO2")

        #credits
        if total_emission<=20:
            credits_earned=(daily_limit-total_emission)*0.5
            print("You are under the limit :)")
            print("you earn a total of ",credits_earned,"credits ")
            credits_info=credits_earned

        else:
            extra=(total_emission-daily_limit)
            print("you excedded the limit by",extra,"kg CO2 :( ")
            print("you need to buy",extra*0.3,"amount of credits ")
            credits_info=extra*0.3

        with open("carbon_history.txt", "a") as file:
            file.write(f"{km}km, {electricity}units, {food}, {total_emission:.2f}kg, {credits_info}\n")

        choice=input("do u want to enter a record for another day (yes/no)")
        if choice.lower()!= "yes":
            break

elif choicee==2:
    print("\n--- Your Saved History ---")
    with open("carbon_history.txt", "r") as file:
        data = file.read()
        if data.strip() == "":
            print("No records yet.")
        else:
            print(data)

elif choicee:
    print("Exiting The Program ")

else:
    print("Invalid Choice ")