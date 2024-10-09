def makes10(a, b):
  if a + b == 10:
    return True
  
  elif a == 10 or b == 10:
    return True
    
  else:
    return False

print(makes10(6,4))
print(makes10(5,5))
print(makes10(1,10))
print(makes10(1,3))
