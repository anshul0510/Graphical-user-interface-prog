picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for item in picture :
  for a in item:
    if (a == 0):
     print(" ", end="")
    else:
     print("*", end="")
  print("")
         
