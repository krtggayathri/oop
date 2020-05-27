class Car:
        sound="Beep Beep"
        
        def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
                if max_speed<0:
                        raise ValueError("Invalid value for max_speed")
                if acceleration<0:
                        raise ValueError("Invalid value for acceleration")
                if tyre_friction<0:
                        raise ValueError("Invalid value for tyre_friction")
                self._color=color
                self._max_speed=max_speed
                self._acceleration=acceleration
                self._tyre_friction=tyre_friction
                self._is_engine_started=False
                self._current_speed=0
                
        
        @property
        def color(self):
                return self._color
        @property
        def max_speed(self):
                return self._max_speed
        @property
        def acceleration(self):
                return self._acceleration
        @property
        def tyre_friction(self):
                return self._tyre_friction
        @property
        def is_engine_started(self):
                return self._is_engine_started
        @property
        def current_speed(self):
                return self._current_speed
        def start_engine(self):
                self._is_engine_started=True
                #self._current_speed=0
        def accelerate(self):
                if self._is_engine_started==True:
                        if self._current_speed>self._max_speed:
                                self._current_speed=self._max_speed
                        elif self._current_speed <self._max_speed:
                        
                                self._current_speed+=self._acceleration
                else:
                        print("Start the engine to accelerate")
                
               
                                
        def stop_engine(self):
                self._is_engine_started=False
                
        def apply_brakes(self):
                if self._current_speed<self._tyre_friction:
                        self._current_speed=0
                else:
                        self._current_speed-=self._tyre_friction
                
        def sound_horn(self):
                if self._is_engine_started==True:
                        print(self.sound)
                else:
                        print("Start the engine to sound_horn")
                
                
        
                
                
                

                
                
                        

        