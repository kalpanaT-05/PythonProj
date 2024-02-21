class Person:
    def __init__(self, firstname, lastname, health, status):
        """initialize attributes to be used in/available for all
        class methods in this class, and for class objects
        created by this class."""

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def intro(self):
        "all people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is very sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 75:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 51:
            print("{} goes to doctor.".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 70, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.health, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.intro()
Rey.intro()
Lee.intro()

Maria.status_change()

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        "reinitializes the attributes from Person class(parent class) to child class"
        self.weapon = weapon

    def intro(self):
        print("You are my mortal enemy!!!")
    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak.".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status=False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Maria)
Alex.steal(Rey)

# Rey.steal(Alex)