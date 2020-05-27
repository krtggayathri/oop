class Pokemon:
        sound=''
        running=''
        swimming=''
        flying=''
        def __init__(self,name,level=1):
                if name=='':
                        raise ValueError("name cannot be empty")
                if level<=0:
                        raise ValueError("level should be > 0")
                self._name=name
                self._level=level
                self._master=None
        
        @property
        def name(self):
                return self._name
        @property
        def level(self):
                return self._level
        @property     
        def master(self):
                if self._master==None:
                        print("No Master")
                else:
                        return self._master
        @classmethod
        def make_sound(cls):
                print(cls.sound)
        @classmethod
        def run(cls):
                print(cls.running)
        @classmethod
        def fly(cls):
                print(cls.flying)

        def __str__(self):
                return f'{self.name} - Level {self.level}'
        @classmethod
        def swim(cls):
                if len(cls.swimming)==0:
                        print("NOT SWIM")
                else:
                        print(cls.swimming)


        
class swim(Pokemon):
        @classmethod
        def swim(cls):
                print("not swim")
                                                     

class Electric(Pokemon):
        def attack(self):
                print("Electric attack with {} damage".format(10*self.level))

class Water(Pokemon):
        def attack(self):
                print("Water attack with {} damage".format(9*self.level))
class Air(Pokemon):
        def attack(self):
                print("Air attack with {} damage".format(5*self.level))
        
class WaterAir(Pokemon):
        def attack(self):
                print("Water attack with {} damage".format(9*self.level))
                print("Air attack with {} damage".format(5*self.level))
class ElectricAir(Pokemon):
        def attack(self):
                print("Electric attack with {} damage".format(10*self.level))
        
                print("Air attack with {} damage".format(5*self.level))

class Pikachu(Electric):
        sound='Pika Pika'
        running='Pikachu running...'

class Squirtle(Water):
        sound='Squirtle...Squirtle'
        running='Squirtle running...'
        swimming='Squirtle swimming...'

class Pidgey(Air):
        sound='Pidgey...Pidgey'
        flying='Pidgey flying...'
        
class Swanna(WaterAir):
        sound='Swanna...Swanna'
        flying='Swanna flying...'
        swimming='Swanna swimming...'
        
class Zapdos(ElectricAir):
        sound='Zap...Zap'
        flying='Zapdos flying...'
        
class Island:
        add_list=[]
        def __init__(self,name,max_no_of_pokemon=0,total_food_available_in_kgs=0):
                self._name=name
                self._max_no_of_pokemon=max_no_of_pokemon
                self._total_food_available_in_kgs=total_food_available_in_kgs
                self._pokemon_left_to_catch=0
                Island.add_list.append(self)
        @property
        def name(self):
                return self._name
        @property
        def max_no_of_pokemon(self):
                return self._max_no_of_pokemon
        @property
        def total_food_available_in_kgs(self):
                return self._total_food_available_in_kgs
        @property
        def pokemon_left_to_catch(self):
                return self._pokemon_left_to_catch

        def __str__(self):
                return f'{self.name} - {self._pokemon_left_to_catch} pokemon - {self.total_food_available_in_kgs} food'

        def add_pokemon(self,poke):
                if self._pokemon_left_to_catch<self._max_no_of_pokemon:
                        self._pokemon_left_to_catch+=1
                        
                else:
                        print("Island at its max pokemon capacity")
        @classmethod
        def get_all_islands(cls):
                return cls.add_list

class Trainer(Island):
        
        def __init__(self,name):
                self._name=name
                self._experience=100
                self._max_food_in_bag=10*self._experience
                self._food_in_bag=0
                self._current_island=None
                self.get_pokemon_list=[]
                #self.master=self._name
               
               
        @property
        def name(self):
                return self._name  
        @property
        def experience(self):
                return self._experience
        @property
        def max_food_in_bag(self):
                return self._max_food_in_bag
        @property
        def food_in_bag(self):
                return self._food_in_bag
        @property
        def current_island(self):
                if self._current_island==None:
                        print("You are not on any island")
                else:
                        return self._current_island
        
        def __str__(self):
                
                return f'{self._name}'
        
        def move_to_island(self,island):
                
                self._current_island=island
                
        def collect_food(self):
                if self._current_island!=None:
                        if self._current_island._total_food_available_in_kgs>self._max_food_in_bag:
                                if self._food_in_bag<self._max_food_in_bag:
                                        self._food_in_bag+=self._max_food_in_bag
                                        self._current_island._total_food_available_in_kgs-=self._food_in_bag
                                else:
                                       self._food_in_bag=self._max_food_in_bag
                        else:
                                self._food_in_bag=self._current_island._total_food_available_in_kgs
                                self._current_island._total_food_available_in_kgs=0

                                
                else:
                        print("Move to an island to collect food")
                
        def catch(self,poke1):
                self.get_pokemon_list.append(poke1)
                poke1._master=self
               # print(self)
                #print(poke1.master)
                if self._experience>=100*poke1.level:
                
                        print(f'You caught {poke1.name}')
                        self._experience+=20*poke1.level
                       
                else:
                        print(f'You need more experience to catch {poke1.name}')
                        
                        
                        
        def get_my_pokemon(self):
                return self.get_pokemon_list
                
       
                        
       
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
                        
                
                

                
        
        

        
        
        
        
        
        
my_pikachu = Pikachu(name='ryan',level=1)
print(my_pikachu.name)
#my_pikachu = Pikachu(level=1)
print(my_pikachu)
#print(my_pikachu)
my_pikachu.make_sound()
my_pikachu.run()
my_pikachu.swim()
        
        
        
'''      
trainer = Trainer(name="Bot")  
print(trainer)
pokemon= Pikachu(name="Ryan", level=1)       
print(pokemon.name)

print(pokemon.level)

print(pokemon.master)  # Print

trainer.catch(pokemon)
print(pokemon.master)
print(pokemon.master == trainer)




my_squirtle = Squirtle(name="Ryan")
print(my_squirtle.name)

print(my_squirtle.level)

print(my_squirtle)
my_squirtle.make_sound()  # Print


my_squirtle.run()  # Print


my_squirtle.swim()  # Print


print(my_squirtle.level)
my_squirtle.attack()  # Print

my_squirtle2 = Squirtle(name="Ryan",level=2)
my_squirtle2.level

my_squirtle2.attack()  # Print
#Water Attack with 18 damage

my_pidgey = Pidgey(name="Tom")
print(my_pidgey.name)

print(my_pidgey.level)

print(my_pidgey)
#Tom - Level 1

my_pidgey.make_sound()  # Print
#Pidgey...Pidgey

my_pidgey.fly()  # Print
#Pidgey flying...

print(my_pidgey.level)

my_pidgey.attack()  # Print
#Air attack with 5 damage


my_swanna = Swanna(name="Misty")
print(my_swanna.name)

print(my_swanna.level)

print(my_swanna)
#Misty - Level 1

my_swanna.make_sound()  # Print
#Swanna...Swanna

my_swanna.fly()  # Print
#Swanna flying...

my_swanna.swim()  # Print
#Swanna swimming...

print(my_swanna.level)

my_swanna.attack()  # Print


my_swanna2= Swanna(name="Misty",level=2)
print(my_swanna2.level)
my_swanna2.attack()  #

island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
print(island.name)

print(island.max_no_of_pokemon)

print(island.total_food_available_in_kgs)

print(island.pokemon_left_to_catch)

print(island)
#Island1 - 0 pokemon - 10000 food 
print(island.pokemon_left_to_catch)
pokemon= Pikachu(name="Ryan", level=1)
island.add_pokemon(pokemon)
pokemon= Pikachu(name="Ryan", level=1)
island.add_pokemon(pokemon)
pokemon= Pikachu(name="Ryan", level=1)
island.add_pokemon(pokemon)
pokemon= Pikachu(name="Ryan", level=1)
island.add_pokemon(pokemon)
pokemon= Pikachu(name="Ryan", level=1)
#island.add_pokemon(pokemon)

#my_pikachu = Pikachu(name="Ryan", level=1)

print(island.pokemon_left_to_catch)
print(island.max_no_of_pokemon)
pokemon= Pikachu(name="Ryan", level=1)'''
'''
trainer = Trainer(name="Bot") 

print(trainer.name)

print(trainer.experience)

print(trainer)

print(trainer.max_food_in_bag)

print(trainer.food_in_bag)
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
#trainer.move_to_island(island1)
#print(trainer.current_island == island1)
trainer.current_island
print(island.total_food_available_in_kgs)  
trainer.move_to_island(island)
island.total_food_available_in_kgs

print(trainer.food_in_bag)
trainer.collect_food()
print(island.total_food_available_in_kgs)

print(trainer.food_in_bag)
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
pokemon= Pikachu(name="Ryan", level=1)
print(pokemon.name)

print(pokemon.level)

print(trainer.experience)

trainer.catch(pokemon)  # Print
print(trainer.experience)'''
'''
trainer = Trainer(name="Bot") 
island1 = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
print(island)
print(Island.get_all_islands())
trainer.move_to_island(island)

trainer.current_island
#Island1 - 0 pokemon - 10000 - food
#If trainer is not on any island current_island should return the message mentioned below.
trainer.current_island # Print
#You are not on any island
pokemon= Pikachu(name="Ryan", level=1)
trainer.catch(pokemon) 
print(trainer.get_my_pokemon())'''








