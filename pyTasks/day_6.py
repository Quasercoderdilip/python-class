distance_travelled = int(input('Enter the distance travelled : '));
mileage_per_litre = float(input('Enter the mileage of your vehicle (in km/L): '))

fuel = (distance_travelled / mileage_per_litre);
print(f'Fuel : {fuel:.2f} litres');