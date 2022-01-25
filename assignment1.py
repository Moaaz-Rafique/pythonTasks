# vowel = ('a','e','i','o','u')
# flag = "false"
# x = input("Enter String: ")
# y = x.lower()

# for i in y:
#     if i in vowel:
#         flag = "true"

# if flag == "true":
#     print("Valid String")
# else:
#     print("Invalid String")    

count = 0

x = "Compiler construction lab"

for y in x:
    if y.isalpha():
        count = count+1
        print(y,end=',')
   
print(f"{count}")
