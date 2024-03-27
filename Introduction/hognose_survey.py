# Import required modules.
import csv
from datetime import datetime

# Create the "Hognose" class.
class Hognose:
# Define the attributes that make up the class.
    def __init__(self, name, age, snoot, goodness, good_eater, last_fed):
        self.name = name
        self.age = float(age)  # Convert age to a float number (to account for ages between 0 and 1).
        self.snoot = snoot
        self.goodness = goodness == 'Yes'  # Convert goodness to a boolean.
        self.good_eater = good_eater == 'True'  # Convert good_eater to a boolean.
        self.last_fed = datetime.strptime(last_fed, '%m/%d/%Y')  # Convert last_fed to a datetime object.

# Define the "official" string that is the snake object.
# The return string is broken up to stay maintain shorter lines per PEP 8
    def __repr__(self):
        return (f"Hognose(name='{self.name}', age={self.age}, snoot='{self.snoot}', "
                f"goodness={self.goodness}, good_eater={self.good_eater}, "
                f"last_fed='{self.last_fed.strftime('%m/%d/%Y')}')")


# Mapping between CSV headers and class attribute names.
header_mapping = {
    'Snake Name': 'name',
    'How old are they': 'age',
    'What kind of snout': 'snoot',
    'Are they good': 'goodness',
    'Are they a good eater': 'good_eater',
    'When were they last fed': 'last_fed'
}

# Read the CSV file and create Hognose instances.
hognose_snakes = []
with open('hognose_snakes.csv', 'r') as file:  # The 'r' stands for "read", as opposed to "write".
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Rename the keys based on the mapping.
        renamed_row = {header_mapping[key]: value for key, value in row.items()}
        # Create the Hognose object with the renamed keys.
        snake = Hognose(**renamed_row)
        hognose_snakes.append(snake)

# Print the list of Hognose objects.
for snake in hognose_snakes:
    print(snake)