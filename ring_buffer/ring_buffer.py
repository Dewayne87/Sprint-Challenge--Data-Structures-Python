class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if len(self.storage) < self.capacity:
      self.storage.append(item)
    else:
      self.storage[self.current] = item
      if self.current == self.capacity - 1:
        self.current = 0
      else:
        self.current += 1  

  def get(self):
    noneRemoved = []
    for i in self.storage:
      if i != None:
        noneRemoved.append(i)
    return noneRemoved
    

ex = RingBuffer(2)
ex.append(1)
print(ex.get())




