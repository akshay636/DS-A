# A hashmap in Python is a data structure that maps keys to values. It is implemented as a dictionary, which is a built-in data type in Python. 
# Hashmaps are very efficient for storing and retrieving data, especially when the keys are unique and the data is frequently accessed.

# Hashmaps work by using a hash function to convert each key into a unique index. This index is then used to store the value associated 
# with the key in an array. When a value is retrieved, the hash function is used to generate the index of the value, and the value is then 
# retrieved from the array.

# Hashmaps are a very efficient way to store and retrieve data because they allow constant-time lookups.
# This means that the time it takes to retrieve a value from a hashmap does not depend on the size of the hashmap.

class hash_map:
  def __init__(self):
    self.data ={}
    
  def _add(self, key, val):
    self.data[key] =val
  
  def _get(self, key):
    return self.data.get(key,None)
  
  def _list(self):
    for i in self.data:
      print(self.data[i])
      
hm = hash_map()
hm._add(1,20)
hm._add(3,10)
hm._add(2,21)
hm._list()