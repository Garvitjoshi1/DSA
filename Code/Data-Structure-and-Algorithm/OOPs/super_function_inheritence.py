class Vehicle():

    def __init__(self, make, model, fuel):
        self.make = make
        # private
        self.__model = model
        self.__fuel = fuel

    def _private_method_parent(self):
        print("This is Private")


class Car(Vehicle):
    def __init__(self, make, model, fuel, air_conditioner, sunroof):
        super(Car, self).__init__(self, make, model)
        # These 3 lines not required if super class used
        # parent class
        # Vehicle.make = make
        # Vehicle.__model = model
        # Vehicle.__fuel = fuel

        self.air_conditioner = air_conditioner
        self.sunroof = sunroof

    def show_parent_attribute(self):
        print(Vehicle.make, " ", Vehicle.__model, " ", Vehicle.__fuel)

    def show_private_method_of_parent(self):
        self._Vehicle_private_method_parent()


myobj = Car("Tesla", 2019, "Electric", True, True)
print(myobj.__dict__)
