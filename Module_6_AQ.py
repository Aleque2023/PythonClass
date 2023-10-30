###Alex Quezada, 8/30/2023, Module 6 Assignment
###Working with dictionaries

Videogames = {
    1: 'Borderlands',
    2: 'Resident Evil',
    3: 'Dark Souls',
    4: 'Elden Ring',
    5: 'Halo',
    6: 'Hitman',
    7: 'Batman',
    8: 'Star Wars',
    9: 'Street Fighter',
    10: 'The Forest',
    }

print(f"{Videogames}")
chosen = int(input(f"Please select one out of the 10 from the list: "))
print(f"You have selected {Videogames[chosen].title()}.")
