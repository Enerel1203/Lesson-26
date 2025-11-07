class Dog:
    
    species = "Canine"
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def show_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")

dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("Bulldog", "Rocky")

dog1.show_details()
dog2.show_details()
