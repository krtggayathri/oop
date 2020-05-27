class Item:
        def __init__(self,name=None,price=0,category=0):
                if price<=0:
                        raise ValueError("Invalid value for price, got {}".format(price))
                        
               
                self._name=name
                self._price=price
                self._category=category
                
               
        @property
        def name(self):
                return self._name
        @property
        def price(self):
                return self._price
        @property
        def category(self):
                return self._category
                
        def __str__(self):
                return f'{self.name}@{self.price}-{self.category}'
        
        
class Query:
        operation_list=['EQ','IN','GT','LT','GTE','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        def __init__(self,field=None,operation=None,value=None):
                if operation not in self.operation_list:
                        raise ValueError("Invalid value for operation, got {}".format(operation))
                self._field=field
                self._operation=operation
                self._value=value
        @property
        def field(self):
                return self._field
                
        @property
        def operation(self):
                return self._operation
                
        @property
        def value(self):
                return self._value
                
        def __str__(self):
                return f'{self._field} {self._operation} {self._value}'
       
class Store(Item,Query):
        def __init__(self):
                self.AddItem=[]
        
       
        def add_item(self,item):
                self.AddItem.append(item)

                 
          
        def __str__(self):
                if not len(self.AddItem):
                        return "No items"
                        
                else:        
                        return '\n'.join(map(str,self.AddItem))
                        
       
                                                
        def filter(self,query):
                obj=Store()
                
                if query.operation=='EQ':
                        for i in self.AddItem: 
                                
                                if i.name==query.value:
                                        obj.add_item(i)

                                if i.price==query.value:
                                        
                                        obj.add_item(i)
                                
                                if i.category==query.value:
                                        obj.add_item(i)
                
                if query.operation=='GT':
                        for i in self.AddItem:
                                if i.price>query.value:
                                         obj.add_item(i)
                        
  
                if query.operation=='LT':
                        for i in self.AddItem:
                                if i.price<query.value:
                                         obj.add_item(i)


                        
                if query.operation=='GTE':
                        for i in self.AddItem:
                                if i.price>=query.value :
                                         obj.add_item(i)
                                       

                        
                if query.operation=='LTE':
                        for i in self.AddItem:
                                if i.price<=query.value:
                                         obj.add_item(i)
                        
                if query.operation=='STARTS_WITH':
                        for i in self.AddItem:
                                if i.name.startswith(query.value):
                                        obj.add_item(i)
                        for i in self.AddItem:

                                if i.category.startswith(query.value):
                                        obj.add_item(i)
                                
                if query.operation=='ENDS_WITH':
                        for i in self.AddItem:
                                if i.name.endswith(query.value):
                                        obj.add_item(i)
                        
                        for i in self.AddItem:

                                if i.category.endswith(query.value):
                                        obj.add_item(i)
                                        
                if query.operation=='CONTAINS':
                        
                        for i in self.AddItem:
                                if query.field == 'name' and query.value in i.name:
                                        obj.add_item(i)
                                elif query.field == 'category' and i.category.__contains__(query.value):
                                        obj.add_item(i)
                
                if query.operation=='IN':
                        if query.field=='name':
                                for i in range(len(query.value)):
                                        for j in self.AddItem:
                                                if j.name==query.value[i]:
                                                        obj.add_item(j)
                        if query.field=='category':
                                for i in range(len(query.value)):
                                        for j in self.AddItem:
                                                if j.category==query.value[i]:
                                                        obj.add_item(j)
                        if query.field=='price':
                                for i in range(len(query.value)):
                                        for j in self.AddItem:
                                                if j.price==query.value[i]:
                                                        obj.add_item(j)
                return obj

        def count(self):
                return len(self.AddItem)                
              
        def exclude(self,query):
                obj2=Store()
                r=self.filter(query)
               
                for i in self.AddItem:
                        if i not in r.AddItem:
                                obj2.add_item(i)
                                
                                
                return obj2
  
        def __add__(self,other):
                obj3=Store()
                for j in other.AddItem:
                        obj3.add_item(j)
                for i in self.AddItem:
                        obj3.add_item(i)
                
                return obj3
                        


                
                
                
                
        
        
  
            
        
        
        
        
                                
                                
        

                
'''      
store = Store()  

item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
#item = Item(name="butter", price=10, category="Food")  
#store.add_item(item)  
query = Query(field="name", operation="IN", value=["Oreo Biscuits", "Boost Biscuits" ])  
results = store.filter(query) 
print(results)  

query = Query(field="name", operation="CONTAINS", value='cuits')  
results = store.filter(query)  
print(results) 

'''
'''
store = Store()  
item = Item(name="Oreo Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=10, category="Food")  
store.add_item(item)  
item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item)  


query = Query(field="price", operation="GT", value=15)  
results = store.exclude(query)  # exclude all items whose price is greater than 15 
print(results)
'''

'''
store=Store()
item=Item()'''

store = Store()
item = Item(name="Oreo Biscuits", price=30, category="Food")
store.add_item(item)
item = Item(name="Boost Biscuits", price=20, category="Food")
store.add_item(item)
item = Item(name="ParleG Biscuits", price=10, category="Food")
store.add_item(item)


query = Query(field="price", operation="GT", value=15)
#results = store.filter(query)
#print(results)

#query = Query(field="price", operation="GT", value=15)  
#results = store.exclude(query)
#print(results)

results = store.exclude(query) + store.filter(query) # OR Operation
print(results)

                
                
                
         
 
 
  







                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

        
                
                
                
                


                
                
                
                


                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        