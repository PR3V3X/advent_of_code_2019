'''
Fuel required to launch a given module is based on its mass. 
Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

f = ((m / 3) // 1) - 2

mass = 12 -> fuel = 2
mass = 14 -> fuel = 2
mass = 1969 -> fuel = 654
mass = 100756 -> fuel = 33583
fuel_sum = 34241

A module of mass 1969 requires 654 fuel. 
This fuel requires 216 more fuel (654 / 3 - 2).
216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel.
So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
'''

def fuel_eq(m):
    return ((m / 3) // 1) - 2

# reads mass data .txt
with open('day1_mod_mass.txt') as md:
    data = md.read().splitlines()

# converts mass data into int.
data = [int(md) for md in data]

md.close()

# calculates fuel.
fuel_list = [((m / 3) // 1) - 2 for m in data]

# sum & display
print("The amount of fuel required is: ", sum(fuel_list))

# makes sub total of required fuel.
sub_fuel = sum(fuel_list)

# total fuel from manual calculations should be *** units. should...


# sub total fuel = 3271095 units

# !!!DO NOT CONTINUE WITHOUT MAKING ORIGINAL CODE!!!
# Credit to TristoKrempita for figuring this out!
# fuel calculations for fuel needed to launch fuel mass.
with open("day1_mod_mass.txt", "r") as file:
    masses = file.readlines()

def calc_fuel(mass):
    if mass//3-2 < 0:
        return mass
    else:
        return mass + calc_fuel(mass//3-2)

print(sum(calc_fuel(int(m))-int(m) for m in masses))
