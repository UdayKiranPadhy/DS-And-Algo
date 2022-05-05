freq = 5*10**9
di_ele = 4.4
height = 1.6
c = 3*(10**8)*(10**3)
lamb = c/freq


width = c/(2*freq*pow(((di_ele+1)/2), 0.5))
print("Width of the antenna is : ", width)

e_eff = ((di_ele+1)/2) + ((di_ele-1)/2)*pow(1 + (12*height/width), -0.5)


part1 = c/(2*freq*(e_eff**0.5))
length = part1 - 0.824*height * \
    (e_eff+0.3)*((width/height) + 0.264)/((e_eff-0.258)*((width/height)+0.8))
print("Length of the patch antenna is ", length)

length_ground = 6*height + length
width_ground = 6*height + width
print("Length of Ground : ", length_ground)
print("Width of Ground : ", width_ground)
