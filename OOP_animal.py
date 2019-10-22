class animal():
    # def __init__(self):
    #     print("animal created")
    def who_am_i (self):
        print("i am an animal")
    def eat(self):
        print("I am eating")


class dog(animal):
    def __init__(self,name):
        self.name = name
        animal.__init__(self)
        print('dog created')

    def say(self):
        return self.name + " says WOOF!!"

    def who_am_i(self):
        print("I am a dog!!")




class cat(animal):
    def __init__(self,name):
        animal.__init__(self)
        self.name = name
        print('cat created')

    def say(self):
        return  self.name + " says MEOW!!"

chapo = dog('chapo')
fils = cat('fils')

# print(chapo.say())
# print(fils.say())

# for pet in [chapo,fils]:
#     print(type(pet))
#     print(pet.say())

def pet_speak(pet):
   print(pet.say())

#pet_speak(chapo)
