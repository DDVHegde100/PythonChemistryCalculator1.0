print("Welcome to Dhruv's Chemistry Calculator")
chem=str(input('Enter the calculation(no capital letters(single word)): '))

if(chem=='density'):
    mass=float(input('Enter the mass:'))
    volume=float(input('Enter the volume:'))
    density=mass/volume
    print('%0.3f is the density.' %(density))
