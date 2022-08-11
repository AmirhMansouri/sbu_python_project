import fridge

class omelet :
    """class for a Omelet"""

    def __init__(self , status , kind = "simple"):
        """ initialize an omelet object """

        if not (status =="cooked" or status == "ingredients"):
            raise ValueError("entered status isn't valid ")
        self.status = status
        self.needs = {"egg":1}
        self.omelet_type = kind

    def __ingredients__(self, **material_dict) :
        """private methode for making dict of materials"""

        self.needs.update(material_dict)

    def set_kind(self,kind_name,**kind):
        """ add desired name and material to your Omelet """

        if not kind_name.isalpha():
            raise ValueError("Omelet type is not valid")
        for key, value in kind.items() :
            if not key.isalpha() :
                raise ValueError("entred material  is not valid")
            if not (str(value)).isdigit() :
                raise ValueError("entred number  is not valid")
        self.omelet_type = kind_name
        self.__ingredients__(kind)

    def mix(self, my_fridge ) : # if one of material doesnt exist in fridge get_one in fridge will stop the program
        """take ingrediants from the fridge """

        for key,value in self.needs.items() :
            my_fridge.get_one(key,value)
        print( "materials mixed seccusfully " )
        return True

    def cook(self) :
        """cook omelet afte mixing"""

        if self.mix(my_fridge)  and self.status=="ingrediants":
            print("cooked seccusfully")
            self.status = "cooked"
        elif self.status=="cooked":
            print("this food already cooked")
        else :
            raise ValueError("cannot cook food")














