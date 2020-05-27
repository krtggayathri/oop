from car import Car
class Truck(Car):
        
        def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
                super().__init__(color,max_speed,acceleration,tyre_friction)
                self._max_cargo_weight=max_cargo_weight
                self._load=0
                
        @property                
        def max_cargo_weight(self):
                return self._max_cargo_weight
      
        def load(self,load1):
                if load1<0:
                        raise ValueError("Invalid value for cargo_weight")
                
                if self.current_speed!=0:
                        print("Cannot load cargo during motion")
                elif self._load+load1>self._max_cargo_weight:
                        print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))

                else:                                                         
                        self._load+=load1
                        
                
        
        def unload(self,load3):
                if load3<0:
                        raise ValueError("Invalid value for cargo_weight")
                else:
                        if self._is_engine_started==True and self.current_speed!=0:
                                print("Cannot unload cargo during motion")
                                
                        elif self.current_speed==0 or self.current_speed!=0:
                                self._load-=load3
        def sound_horn(self):
                if self._is_engine_started==True:
                        print("Honk Honk")
                else:
                        print("Start the engine to sound_horn")
                