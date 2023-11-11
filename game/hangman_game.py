import random

def getRandomWord():
    words = ["hang", "pretty", "apple", "ant", "water", "samsung", "mcdonalds", "fluent", "voca", "galaxy"]
    return words[random.randrange(0, len(words))]
hangman_input_history = []
def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isalpha()): # 알파벳인지 확인
            alphabet = user_input[0].lower()
            if(alphabet in hangman_input_history ): # 이미 입력된 알파벳인지 확인
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet
def runHangMan():
    global hangman_input_history
    # 초기화용 코드
    hangman_input_history = []
    chance = 7
    correct = 0

    word = getRandomWord()
    wordSet = set(word)

    while chance > 0:
        alphabet = str(getHangmanInput())

        hangman_input_history.append(alphabet)

        if word.find(alphabet) != -1:  # alphabet이 word에 속해있으면 정답이라고 알려주고, 아니면 기회를 깎기.
            correct = correct +1
            print("CORRECT!")
        else:
            chance = chance - 1
            print("LEFT CHANCE : ", chance)

    # 1. 모든 정답을 맞췄을때 게임이 끝나지 않음
    # -> 맞추면 alive  출력해주고 그만하기 (break문을 사용)
        if correct >= len(wordSet): # 정답을 맞췄을때 게임 종료
            print("Alive!")
            break