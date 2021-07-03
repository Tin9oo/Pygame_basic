import pygame
# 파일인트가 파이게임에 대해서 제대로 이해를 하지 못하고 있으면 잘못된 문제를 알려주기도 한다.
pygame.init() # 초기화(반드시 필요하다)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Joohwan Game")

# 프로그램이 종료되지 않도록 어디선가 대기하고 있어야합니다.
# 이벤트 루프 : 사용자 입력을 검사
# 이벤트 루프가 항상 실행되고 있어야 창이 꺼지지 않습니다.
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():    # pygame을 쓰기위해 무조건 적어야 하는 부분
                                        # 이벤트 루프 : 프로그램이 종료되지 않게 대기
                                        # 사용자 입력을 체크, 입력에 따른 동작을 실행
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님



# pygame 종료
pygame.quit()