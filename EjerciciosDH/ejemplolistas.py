animales=["Leon", "Vaca","Dinosaurio","Chacal","Gallina"]

for animal in animales:
    print(animal)

def esLeon(animales):
    for animal in animales:
        if animal == "Leon":
            print("Hay un leon")
            break
        else:
            continue
        
esLeon(animales)
