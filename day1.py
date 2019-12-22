'''
Fuel required to launch a given module is based on its mass. 
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
'''
# f = ((m / 3) // 1) - 2

# find out how many modules
mod = int(input("How many modules do you have? -> "))


# loop n times of modules
mass_list = []
for i in range(mod):
    # ask for n amount of mass
    mass_value = float(input("What is the mass of this module? -> "))
    mass_list.append(mass_value)

# calculate fuel
fuel_list = [((m / 3) // 1) - 2 for m in mass_list]

# sum & display
print("The amount of fuel required is: ", sum(fuel_list))

# mass = 12 -> fuel = 2
# mass = 14 -> fuel = 2
# mass = 1969 -> fuel = 654
# mass = 100756 -> fuel = 33583
# fuel_sum = 34241
