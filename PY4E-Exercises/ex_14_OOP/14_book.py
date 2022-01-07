stuff = list()
stuff.append('Python')
stuff.append('Gustavo')
stuff.sort()
print(stuff[0])

print (stuff.__getitem__(0))
print(list.__getitem__(stuff,0))
# ------------------------------------------------------------------------------------------
# These 3 prints statements above or line of code are the same things, print the same result
# ------------------------------------------------------------------------------------------
dir(stuff)
"""
An object can contain a number of functions (which we call "methods") as well as data
that is used by those functions. We call data items that are part of the object "attributes".

We use the class keyword to define the data and code that will make up each of the
objects. The class keyword includes the name of the class and begins an indented
block of code where we include the attributes (data) and methods (code).
"""

class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1 # This syntax using the 'dot' operator is saying 'the x within self'.
                         # So each time party() is called, the internal x value is incremented by 1 and the value is printed out.
     print("So far",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an) # In this variation, we are accessing the code from within the class
                      # and explicitly passing the object pointer an in as the first
                      # parameter (i.e. self within the method).
                      # You can think of an.party() as shorthand for the above line.

"""
An object can contain a number of functions (which we call "methods") as well
as data that is used by those functions.
We call data items that are part of the object "attributes".

Each method looks like a function, starting with the def keyword and consisting of an
indented block of code. This example has one attribute (x) and one method (party).
The methods have a special first parameter that we name by convention self.

"""
print ("Type", type(an))
print ("Dir ", dir(an))
print ("Type", type(an.x))
print ("Type", type(an.party))
# You can see that using the class keyword, we have created a new type.
# From the dir output, you can see both the x integer attribute and the
# party method are available in the object.
