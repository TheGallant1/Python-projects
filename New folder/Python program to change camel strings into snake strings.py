snake_str = ""
camel_case= input("Enter a camel case variable name: ")
for char in camel_case:
 if char.isupper():
       snake_str += '_' + char.lower()
 else:
      snake_str += char

print( "Snake case:" , snake_str) 
