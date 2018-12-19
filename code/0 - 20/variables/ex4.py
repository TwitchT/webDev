#gives cars a value
cars = 100
 #sets a value for the amount of space in the car
space_in_a_car = 4.0
#gives cars a value
drivers = 30
#gives passengers a value
passengers = 90
#creates a math problem
cars_not_driven = cars - drivers
#makes an equation
cars_driven = drivers
#makes a multiplication equation
carpool_capacity = cars_driven * space_in_a_car
#uses division
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaible.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")