# global scope
x = "global variable X"

def func_a():
  # local scope
  y = "local variable y"
  global x
  x = "updated1 global variable X"
  # print(x)
  # print(y)
def func_b():
  global x
  x = "updated2 variable X func b"

# print(y)
# print(x)
# print("------")
func_b()
func_a()
print(x)






