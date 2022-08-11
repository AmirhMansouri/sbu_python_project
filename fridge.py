# Write your code here :-)
import foods
class fridge :
    """ fridge class for making a smart fridge """

    def __init__(self , **fridge_entry):
        """initialize an fridge object"""

        for material, number_of_material in fridge_entry.items():
            if not material.isalpha() :
                raise ValueError("material is not valid")
            elif not (str(number_of_material)).isdigit() :
                raise ValueError("number of material is not valid")
        self.fridge_entry = fridge_entry

    def has(self , food_name):
        """has function checks that your food does exist in fridge or not"""

        if not food_name.isalpha() :
            raise ValueError("entered food is not valid")
        flag = False
        for name in self.fridge_entry.keys() :
            if name == food_name :
                flag = True
        return flag

    def has_various(self , **foods):
        """do something like has but for large number of inputs"""

        result = []
        for key in foods.keys() :
            if has(key):
                result.extend([True])
            else :
                result.extend([False])
        return result

    def add_one(self , food_name , Number = 1 ):
        """add entered foodname to the fridge if it doesnt exist , default number of entered foodname is 1 , if it does
         jOmeletust add the entered number to the last one"""

        if  has(food_name):
            self.fridge_entry[food_name] += Number
        else:
            self.fridge_entry.update({food_name: Number})

    def add_many(self, **foods):
        """like add_one but works on the large number of inputs"""

        for key,value in foods.items() :
            add_one(key,value)

    def get_one(self , food , Number = 1):
        """takes out entered foodname from the fridge if it exists , default number of desired foodname is 1 , if it doesnt
         exist sends error"""
        if not has(food_name):
            raise ValueError("entered food doesn't exist")
        else:
            self.fridge_entry[food] -= Number

    def get_many(self , **foods):
        """do something like get_one but for large number of inputs"""

        for key,value in foods.items() :
            get_one(key,value)

    def can_make_food(self , desired_omelet) :
        """return True if we can make omelet using materials """

        if desired_omelet.mix(self) :
            return True
        return False





