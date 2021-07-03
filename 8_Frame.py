import pygame
# 파일인트가 파이게임에 대해서 제대로 이해를 하지 못하고 있으면 잘못된 문제를 알려주기도 한다.

# 기본 초기화 (반드시 해야하는 것들) #########################################################################################################################################
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # 튜플로 화면 크기를 준다.

# 화면 타이틀 설정
pygame.display.set_caption("Dreamer")

# FPS
clock = pygame.time.Clock()
#############################################################################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
            
    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()

pygame.quit()