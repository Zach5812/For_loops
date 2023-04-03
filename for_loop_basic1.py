# for x in range(0, 151):
#     print (x)


# for x in range(5, 1005, 5):
#     print (x)


# for x in range(1, 100):
#     if x%10 and x%5 !=0:
#         print(x)
#     if x%10 == 0:
#         print("Coding")
#     elif x%5 == 0:
#         print("Coding Dojo")

# sum=0
# for x in range(0, 500000):
#     if x % 2 != 0:
#         sum = sum + x
# print(sum)


# for x in range(2018, 0, -4):
#     if x%2 == 0:
#         print(x)


lowNum = 4
highNum = 20
mult = 4
for x in range(lowNum-1, highNum+1):
    if x%mult == 0:
        print(x)