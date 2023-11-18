from pythonBasic. game.updown_game inport runUpDown
def menuPrint():
    print("=======GAME=======")
    print("1. 행맨")
    print("2. 업다운")
    print("0. 종료")
    print("==================")

userInput = -1

while userInput != 0:
    menuPrint()
    userInput = int(input("SELECT MENU ::: "))
    if userInput == 1:
        runHangMan()
    elif userInput == 2:
        runUpDown()
    elif userInput == 3:
        run2048()