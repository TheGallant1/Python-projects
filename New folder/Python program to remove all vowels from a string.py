text = input("Enter a string of text: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char not in vowels:
        result += char

print("Text without vowels:", result)