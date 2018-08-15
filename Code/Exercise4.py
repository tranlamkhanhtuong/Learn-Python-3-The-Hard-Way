# the number of car
cars=100

# the number of space
space_in_a_car=4.0

#the number of driver
drivers=30

#the number of passenger
passengers=90

# the figure for cars not being driven
cars_not_driven=cars- drivers

# the figure for cars driven
cars_driven=drivers

# the total number of capacity 
carpool_capacity = cars_driven * space_in_a_car

#the mean paseenger per car
average_passengers_per_car=passengers/cars_driven
print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport", carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
