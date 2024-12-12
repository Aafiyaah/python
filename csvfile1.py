import csv

field_name = ['no', 'company', 'car model']
car = [
    {'no' : 1, 'company': 'Ferrari', 'car model': 'GH'},
    {'no' : 2, 'company': 'BMW', 'car model': 'X5'},
    {'no' : 3, 'company': 'Maruti Suzuki', 'car model': 'Swift'},
    {'no' : 4, 'company': 'Audi', 'car model': 'RS7'},
    {'no' : 5, 'company': 'Toyota', 'car model': 'Fortuner'},
]
with open('car.csv', 'w', newline='') as csvfile:
    write = csv.DictWriter(csvfile, fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('car.csv', newline='') as csvfile:
    d = csv.reader(csvfile)
    for r in d:
        print(','.join(r))


