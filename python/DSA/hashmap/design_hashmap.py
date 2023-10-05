class MyHashMap:
    def __init__(self):
      self.map = {}
        
    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        print(self.map.get(key))
        if key in self.map:
          return self.map.get(key) # type: ignore
        else:
          return -1

    def remove(self, key: int) -> None:
      if self.map.get(key):
        self.map.pop(key)
        
a =["MyHashMap","remove","put","put","put","put","put","put","get","put","put"]
b =[[],[2],[3,11],[4,13],[15,6],[6,15],[8,8],[11,0],[11],[1,10],[12,14]]

obj = MyHashMap()
obj.map ={3: 11, 4: 13, 15: 6, 6: 15, 8: 8, 11: 0}
print(obj.get(11))