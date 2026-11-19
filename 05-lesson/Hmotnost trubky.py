def circle_area(d):
    r = d/2
    return 3.1415*(r**2)
def tube_cross_section(d_out, d_in):
    return circle_area(d_out)-circle_area(d_in)

def tube_mass(d_out, d_in, length, density=7850):
    return tube_cross_section(d_out,d_in)*length*density

print(tube_mass(0.060, 0.050, 6))                # ocelová trubka: ≈ 40.69 kg
print(tube_mass(0.060, 0.050, 6, density=2700))  # hliníková: ≈ 14.00 kg