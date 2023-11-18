import pygame

colors = {
    'white': ( 255, 255, 255),
    'black': (0, 0, 0),
    '-1': (200, 200, 200),
    '2': (236, 239, 241),
    '4': (207, 216, 220),
    '8': (176, 190, 197),
    '16': (144, 164, 174),
    '32': (120, 144, 156),
    '64': (96, 125, 139),
    '128': (84, 110, 122),
    '256': (69, 90, 100),
    '512': (55, 71, 79),
    '1024': (38, 50, 56),
    '2048': (29, 37, 41),
}

board = [[-1, -1, -1, -1],
         [-1, -1, -1, -1],
         [-1, -1, -1, -1],
         [-1, -1, -1, -1]]

isGameRunning = True

size = (500, 500)
screen = pygame.display.set_mode(size)

def initScreen():
    screen = fill(colors['white'])
    pygame.display.update()


def setEventListener():
    global isGameRunning
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                isGameRunning = False
            elif event == pygame.K_DOWN:
                print("아래")
            elif event == pygame.K_UP:
                print("위")
            elif event == pygame.K_RIGHT:
                print("오른쪽")
            elif event == pygame.K_LEFT:
                print("왼쪽")


def drawDisplay():
    global screen

    baseX = 35
    baseY = 35
    blockHeight = 100
    blockWidth = 100
    margin = 10

    for i in range(4):
        for j in range(4):
            x = (blockWidth + margin) * j + baseX
            y = (blockHeight + margin) * i + baseY
            data = str(board[i][j])
            if data == '-1':
                pygame.draw.rect(screen, colors[data], [x, y, baseX, baseY, blockWidth, blockHeight], 2)
            else:
                pygame.draw.rect(screen, colors[data], [x, y, baseX, baseY, blockWidth, blockHeight],)


    pygame.display.flip()



def run2048():
    pygame.init()
    initScreen()
    print("2048 게임 시작")

    while isGameRunning:
        setEventListener()
        drawDisplay()



    pygame.quit()

run2048()






'''  
         2048 규칙
    #### #### #### ####
    #### #### #### ####
    #### #### #### ####
    #### #### #### ####

    0008 0016 #### ####
    0008 0004 0004 0008
    0512 0128 0064 0008
    2048 1024 0512 0128

    1. 화면출력 모두 ####이고, 2와 4가 랜덤 위치에 뜨게
    #### #### 0004 ####
    #### 0002 #### ####
    #### #### #### ####
    #### #### #### ####

    2. 사용자의 움직임이 있으면 그 방향으로 숫자를 밀고 빈칸 중 하나(랜덤위치)에 2, 4 중에서 하나가 뜨게
    3. 블럭이 한방향으로 모일때 해당 방향에 같은 숫자가 있으면 블럭 합치기

    (아랫방향 입력시)
    #### #### #### ####
    #### #### 0002 ####
    #### #### #### ####
    #### 0002 0004 ####

    (왼쪽방향 입력시)
    #### #### #### ####
    0002 #### 0002 ####
    #### #### #### ####
    0002 0004 #### ####

    (아랫방향 입력시)
    #### #### #### ####
    0002 #### #### ####
    #### #### #### ####
    0004 0004 #### ####


    4. 최종적으로 2048이 만들어졌으면 WIN.
'''