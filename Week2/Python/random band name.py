import random

band_first = ["The", "A"]

band_second = ["Large", "Crazy", "Wild", "Stinky","Sensitive"
              "Delirious", "Psychotic", "Odd", "Delicious", "Repulsive"]

band_third = ["Buses", "Zapatos", "Diapers", "Babies", "Small Humans",
              "Fetuses", "Placentas", "Crutches", "Lunchboxes", "Waterbottles"]

beginning_name = len(band_first)
middle_name = len(band_second)
last_name = len(band_third)

for i in range(10):
    first_name = random.randint(0, len(band_first)-1)
    second_name = random.randint(0, len(band_second)-1)
    last_name = random.randint(0, len(band_third)-1)

    print(band_first[beginning_name] + band_second[middle_name] + band_third[last_name])
