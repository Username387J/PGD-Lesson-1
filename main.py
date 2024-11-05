#Datatypes

#string
name="Joshua"

#integer
age = 13

#boolean
chocolates = True
hockey = False

#Float
height = 5.4

#input
#subject=input("Enter your fav subject : ")
#print("My fav subject is ", subject)

#list - save multiple values
pets=["Dog","cat","parrot","rat"]
print(pets)

#index - starts with 0
print(pets[0])
print(pets[3])
#Dictionary-key valie pair
student= {
  "name": "Joshua",
  "age" : 13,
  "height" : 5.4
  }
print(student)
#name : Joshua ,age : 13, height : 5.4
print(student.keys())
#name age height
print(student.values())
#joshua 13 5.4

#Acess values
print(student["age"])
print(student["height"])

#for loop in dict
for i in range(5):
  print(i)
  #0, 1 , 2, 3, 4, 5, 
  
for i in student.keys():
  print(i, ':', student[i])
  
if "marks" in student: 
  print("Key is available")
else:
  print("Key is not available")


student["favSub"]="Math"
print(student)

del(student["age"])
print(student)

subject=input("What is your fav subject?")
student["favSub"] = subject
print(student)
    
    
