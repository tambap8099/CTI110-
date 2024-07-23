#Peter Tamba
#6/27/2024
#P2LAB2
#a program that creates a dictionary where the key and value pairs are as follows.

#Create dictionary
#create dictionary
cars={"camaro":18.21, "Prius": 52.36, "Model S":110, "Silverado":26}
#Dispay keys
keys= cars. keys ()
print (keys)
print ()
#get intput from user
car_input=input ("Enter a vehicle to see it's mpg:")
print ()
# Get the mpg associated with the vechicle
mpg_output = cars [car_input]
print (f'the { car_input} gets {mpg_output} mpg. \n')
#Get the distance
distance = float (input (f'How many miles will you drive the {car_input}?'))
print ()
#Calculate gallons of gas needed
gallons = distance/mpg_output
# Print gallons needed to drive the car
print (f' {gallons: .2f}gallons (s) of gas are needed to drive the car {car_input} {distance} miles.')
