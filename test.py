# 미션 1
#
# star = "*"
#
# while True:
#
#
#     if star == "******":
#         break
#
#     else:
#         print(star)
#         star = star + "*"
#
#
# 미션 2
#
# x = int(input("줄 수를 입력하세요"))
# for i in range(1, x+1):
#     for j in range(x+1 -i):
#         print(" ",end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()



x = int(input("줄 수를 입력하세요"))
x = x + 1
space = x * " "
star = "*"
while True:

    space = x * " "

    if space == " ":
        while True:
            space = x * " "
            if space == x:

    else:
        print(space + star)
        x = x - 1
        star = star + "**"