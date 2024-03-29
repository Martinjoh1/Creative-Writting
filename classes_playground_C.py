class Person:
    """
    A class to represent a person
    """

    def __init__(self, height, weight, age, color, alive = True):
        """
        An initializer method to represent a person, including all of their initial attributes
        :param height: the person's height
        :param weight: the person's weight
        :param age: the person's age
        :param color: the person's eye color
        :param alive: A boolean representing if the person is alive or dead
        """
        self.height = height
        self.weight = weight
        self.alive = alive
        self.age = age
        self.eye_color = color

    def walk(self):
        """
        Takes the person for a walk
        :return: None
        """
        print("Go forward")

    def die(self):
        """
        Kills the person
        :return: None
        """
        self.alive = False
        print("You ded")

    def eat(self):
        """
        Let's the person eat
        :return: None
        """
        print("Yum")

    def dance(self):
        """
        Makes the person dance
        :return: None
        """
        print("Look away")

    def resurrect(self, alive):
        """
        Resurrects the person if they are dead. If they are alive, kills them.
        :param alive: Boolean representing if the person is alive or dead
        :return: None
        """
        if alive:
            self.alive = False
        else:
            self.alive = True
        print("You are {0}".format("alive" if self.alive else "dead"))

def main():
    scott = Person(5*12+8, 195, 35, "brown")        # creates the person scott
    print("Scott is {0}".format("alive" if scott.alive else "dead"))
    print("Scott is {0} years old".format(scott.age))
    scott.walk()
    scott.die()

    jacob = Person(5*12+10, 205, 18, "green", True)     # creates the person jacob
    print("Jacob is {0}".format("alive" if jacob.alive else "dead"))
    jacob.resurrect(jacob.alive)      # Tries to resurrect jacob. Since he's alive, he dies. You can't resurrect the living!


main()
