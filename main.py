#stress#
print("calculate stress")
#input
force = float(input("input your force/kg:"))
diameter = float(input("diameter:"))
#process
radius = (diameter/2)
area = 3.14*radius**2
stress = (force/area)
#output
print("your stress is:",stress,"kg/mm2")

print()

#strain#
print("calculate satrain")
#input
original_length = float(input("input original length:"))
extension = float(input("input the extension:"))
#process
strain = extension/original_length
#output
print("your satrin:",strain)

print()

#young's modulus#
print("young's law")
#process
youngs_modulus = float(stress/strain)
#output
print("youngs_modulus:",youngs_modulus,"kg/mm2")

print(" BOOM!!!! IN UR FACEEEE")