import pygame
# 파일인트가 파이게임에 대해서 제대로 이해를 하지 못하고 있으면 잘못된 문제를 알려주기도 한다.
pygame.init() # 초기화(반드시 필요하다)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) # 튜플로 화면 크기를 준다.

# 화면 타이틀 설정
pygame.display.set_caption("Joohwan Game")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:\\OneDrive - 영남대학교\\대학교\\Programing\\Python\\pygame_basic\\background.png") # \\ 혹은 / 을 사용하면 된다.

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:\\OneDrive - 영남대학교\\대학교\\Programing\\Python\\pygame_basic\\character.png")

character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로 크기
character_height = character_size[1] # 캐릭터 세로 크기

character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 중간에 위치
character_y_pos = screen_height - character_height # 화면 세로의 하단에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 프로그램이 종료되지 않도록 어디선가 대기하고 있어야합니다.
# 이벤트 루프 : 사용자 입력을 검사
# 이벤트 루프가 항상 실행되고 있어야 창이 꺼지지 않습니다.
running = True # 게임이 진행중인지 확인
while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수
                        # 프레임의 변화로 게임 속도가 변하면 안된다.
                        # 프레임의 변화로는 이동의 부드러움의 차이가 있을 수는 있다.

# 캐릭터가 1초에 100만큼 이동해야함
# 10 fps : 1초에 10번 동착 -> 1번에 몇 만큼 이동? 10만큼 이동해야한다.
# 20 fps : 1초에 20번 동작 -> 1번에 몇 만큼 이동? 5만큼 이동해야한다.


    # print("FPS : " + str(clock.get_fps())) # fps 확인

    for event in pygame.event.get():    # pygame을 쓰기위해 무조건 적어야 하는 부분
                                        # 이벤트 루프 : 프로그램이 종료되지 않게 대기
                                        # 사용자 입력을 체크, 입력에 따른 동작을 실행
                                        # 해당 반복문은 이벤트 발생 시에만 동작
                                        # 반복문 밖에서는 계속 반복
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN:    # 키가 눌러졌는지 확인
                                            # 대문자면 입력인가??
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키에서 손을 땠는가?
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            
    character_x_pos += to_x * dt # 반복문 안에 들어갔을 때랑 나왔을 때 차이가 뭐냐
    character_y_pos += to_y * dt # 반복문 안 : 이벤트 발생 시에만 동작한다. 따라서, 저장된 to_x, to_y가 한번 character_pos에 반영되어 누르고 있어도 한번 이동된다.
                            # 반복문 밖 : 저장된 to_x, to_y가 계속 character_pos에 반영되어 누르고 있어도 계속 이동 된다.

    # 가로 경계 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경계 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # 배경 그리기
                                    # 좌측 상단에서 우측 하단으로 진행
                                    # (x, y)
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()