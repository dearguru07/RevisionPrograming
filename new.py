# guru='hello to all'
# res=len(guru)
# print(res)



class Person:
    def __init__(self, name, age):
        self.name = name           # Public attribute
        self._age = age            # Protected attribute
        self.__ssn = "123-45-6789" # Private attribute

    # Public method
    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")

    # Getter for the private attribute
    def get_ssn(self):
        return self.__ssn

    # Setter for the private attribute
    def set_ssn(self, ssn):
        self.__ssn = ssn

person = Person("Alice", 30)

# Accessing public attribute
print(person.name)  # Output: Alice

# Accessing protected attribute (conventionally discouraged)
print(person._age)  # Output: 30

# Accessing private attribute directly will raise an AttributeError
# print(person.__ssn)  # Uncommenting this line will raise an error

# Accessing private attribute using getter method
print(person.get_ssn())  # Output: 123-45-6789

# Modifying private attribute using setter method
person.set_ssn("987-65-4321")
print(person.get_ssn())  # Output: 987-65-4321


