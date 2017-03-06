"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction: Hiding details unneed
   Encaptulation: Keeping everything together
   Polymorphism: Interchangablility of components

2. What is a class?

   Code that encaptulates definitions of similar type of things.

3. What is an instance attribute?

   A characteristic that is defined for an individual occurence 
   of a class 

4. What is a method?

   A function that defined on a class

5. What is an instance in object orientation?

   A manifestation of a class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   Class attribute is a character that will inherit to the 
   instances. Instance attribute is a character that defines
   the occurence.
   For example, in "animal" class, there may be a quality that
   is "with blood". In "reptile" which is an instance of the
   class "animal", "with blood" attribute will be inherited,
   but the reptile also may have "cold blood" attribute which
   is different from the "mannal" instance that will have
   the attribute of "warm blood"
"""

# Parts 2 through 5:
# Create your classes and class methods

# two classes and two methods added
class AbstractHousehold(object): # Parent (super class)
    """ An abstract parent class of all households """

    alive = True # parent class attribute

    def __init__(self): # parnet class method that initializes child class attribute
        self.added_to_household = True
        print "Type print from parent init, att in child: %s" %self.type_of

class Human(AbstractHousehold):
    """A class that defines human household members"""

    type_of = "human" # Child class attribute

    def __init__(self, name):
      self.name = name
      print "Name from child init input: %s" %self.name
      print "Status_alive from parent attribute:", self.alive
      print self.num_legs(2)
      return super(Human, self).__init__()
      
    def num_legs(self, number):
      return "Num leg inside child module: %s" %number

print
myself = Human("Morine") # when the initiation occurs, the type is set to human
print "Parent init accessible from instance: %s" %myself.added_to_household # check if init super is in the instance
print