class Animal:
        food=0
        sound=''
        breath=''
        
        def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
                if age_in_months!=1:
                        raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
                if type(breed) !=str:
                        raise ValueError("Invalid value for field breed: {}".format(breed))
                if required_food_in_kgs<=0:
                         raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
                self._age_in_months=age_in_months
                self._breed=breed
                self._required_food_in_kgs=required_food_in_kgs
          
        @property
        def age_in_months(self):
                return self._age_in_months
        @property
        def breed(self):
                return self._breed
        @property
        def required_food_in_kgs(self):
                return self._required_food_in_kgs
               
        def grow(self):
                self._required_food_in_kgs+=self.food
                self._age_in_months+=1
        @classmethod
        def make_sound(cls):
                print(cls.sound)
        @classmethod
        def breathe(cls):
                print(cls.breath)
class Land_animals(Animal):
        breath='Breathe in air'
class Water_animals(Animal):
        breath='Breathe oxygen from water'

''' 
               # print(type(self).__name__ )
                if type(self).__name__ == 'Lion' or type(self).__name__ == 'Snake':
                                
                                #print(zoo._add_animal_list)
                                if  zoo._add_animal_list.count('Deer')>0:
                                        zoo._add_animal_list.remove('Deer')
                   
                else:
                        print("No deers to hunt")
                if type(self).__name__ == 'Shark':
                                
                                #print(zoo._add_animal_list)
                                if zoo._add_animal_list.count('GoldFish')>0:
                                        zoo._add_animal_list.remove('GoldFish')
                                               
                else:
                        print("No GoldFish to hunt")'''
class HuntingAnimal:
        def hunt(self,zoo):
                
                if 'Deer' in zoo.add_animal_list:
                        zoo.add_animal_list.remove('Deer')
                else:
                        print("No deers to hunt")
                      

class Deer(Land_animals):
        food=2
        sound='Buck Buck'
        
       
class Lion(Land_animals,HuntingAnimal):
        food=4
        sound='Roar Roar'
       
        
class Shark(Water_animals):
        food=8
        sound='Shark Sound'
        def hunt(self,zoo):       
                if 'GoldFish' in zoo.add_animal_list:
                        zoo.add_animal_list.remove('GoldFish')
                else:
                        print("No GoldFish to hunt")
                       

class GoldFish(Water_animals):
        food=0.2
        sound='Hum Hum'
      
class Snake(Land_animals,HuntingAnimal):
        food=0.5
        sound='Hiss Hiss'
        


class Zoo(Snake,GoldFish,Shark,Lion,Deer):
        total_animals_in_all_zoo=0
        def __init__(self):
              self._reserved_food_in_kgs=0
              self.add_animal_list=[]
             
            
        @property
        def reserved_food_in_kgs(self):
                return self._reserved_food_in_kgs
        def add_animal(self,Animal):
                self.add_animal_list.append(type(Animal).__name__)
               
                Zoo.total_animals_in_all_zoo+=1
               
                
                
                
        def add_food_to_reserve(self,food1):
                self._reserved_food_in_kgs+=food1
       
                
        def count_animals(self):
                return len(self.add_animal_list)

        def feed(self,Animal):
                
                
                if self._reserved_food_in_kgs>0:
                        self._reserved_food_in_kgs-=Animal.required_food_in_kgs
                        Animal.grow()
                
        @classmethod
        def count_animals_in_all_zoos(cls):
                 return  cls.total_animals_in_all_zoo
        
        @staticmethod
        def count_animals_in_given_zoos(zoo):
                c=0
                for i in zoo:
                        c=c+i.count_animals()
                return c
 
                  
                  


zoo = Zoo()
print(zoo.reserved_food_in_kgs)
zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)
print(zoo.count_animals())
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
print(zoo.count_animals())
print(zoo.reserved_food_in_kgs)
zoo.feed(gold_fish)
print(zoo.reserved_food_in_kgs)
print(gold_fish.age_in_months)
nehru_zoological_park = Zoo()
zoo.add_food_to_reserve(10000000)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
nehru_zoological_park.add_animal(lion)
print(nehru_zoological_park.count_animals())
print(Zoo.count_animals_in_all_zoos())
print(Zoo.count_animals_in_given_zoos([zoo]))
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
nehru_zoological_park.add_animal(deer)
print(nehru_zoological_park.count_animals())
lion.hunt(nehru_zoological_park)
print(nehru_zoological_park.count_animals())
lion.hunt(nehru_zoological_park)

        