print("\n** For-Each Loop ** ")
marks=[28,38,48,58]
for mark in marks:
    print(mark)
    
print("\n** For Loop ** ")
for i in range(5):
    print("Iteration : ",i)    

print("\n** While Loop **")
count=0
while count<5:
    print("Count : ",count)
    count+=1
    
print("\n** Break **")
for i in range(5):
    if i==2:
        break
    print("Iteration : ",i)
    
print("\n** Continue **")
for i in range(5):
    if i==2:
        continue
    print("Iteration : ",i)
    
print("\n** Do-While loop simulation **")
count=0
while True:
    print("Count : ",count)
    count += 1
    if count >= 5:
        break