from car import Car
import math

class RaceCar(Car):
        sound="Peep Peep\nBeep Beep"
        def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
                super().__init__(color,max_speed,acceleration,tyre_friction)
                self._nitro=0
                
       
        def accelerate(self):
                
                if self._nitro>0 and (self._is_engine_started==True):
                        
                       #if self._current_speed+math.ceil(self._acceleration*0.3)<=self._max_speed:
                        self._current_speed+=math.ceil(self._acceleration*0.3)
                        
                        self._nitro-=10
                super().accelerate()
               
        def apply_brakes(self):
               
                    
                if self._current_speed>=self.max_speed//2:
                        self._nitro+=10
                super().apply_brakes()     
                
        @property
        def nitro(self):
                return self._nitro
                

               
                
                
                