
class pizza:

  def __init__(self,topping, size, price55):
    self.topping = toppinng
    self.size = size
    self.price = price

  def __str__(self):
    return f"Pizza ({self.topping} {self.size}) -> {self.price}"


if __name__ == "__main__":
  p1 = pizza("pepperoni", "medium", 310)
  p2 = pizza("mushrooms", "small", 255)
  p3 = pizza("pepperoni", "large", 315)
  p4 = pizza("corn and olives", "medium", 410)
  print(p1)
  print(p2)
  print(p3)
  print(p4)
  