def calculate_volume_of_sphere(radius):
    pi = 3.14
    return (4 / 3) * pi * radii ** 3

radii1 = 30
radii2 = 40

volume1 = calculate_volume_of_sphere(radius1)
print(f"The volume of the sphere with radii {radii1} is {volume1:.2f}")

volume2 = calculate_volume_of_sphere(radius2)
print(f"The volume of the sphere with radii {radii2} is {volume2:.2f}")
