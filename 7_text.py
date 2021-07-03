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

# 적 캐릭터
enemy = pygame.image.load("D:\\OneDrive - 영남대학교\\대학교\\Programing\\Python\\pygame_basic\\enemy.png")

enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터 가로 크기
enemy_height = enemy_size[1] # 캐릭터 세로 크기

enemy_x_pos = (screen_width - enemy_width) / 2 # 화면 가로의 중간에 위치
enemy_y_pos = (screen_height - enemy_height) / 2 # 화면 세로의 하단에 위치

# 폰터 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생서 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴

# 프로그램이 종료되지 않도록 어디선가 대기하고 있어야합니다.
# 이벤트 루프 : 사용자 입력을 검사
# 이벤트 루프가 항상 실행되고 있어야 창이 꺼지지 않습니다.
running = True # 게임이 진행중인지 확인
while running:
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수
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

    # 충돌 처리를 위한 rect 정보 최신화
    character_rect = character.get_rect()   # 실제 위치는 변하지 않고 자리를 유지한다.
                                            # 그리는 위치만 바꿔주는거다.
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos # 이부분을 주석처리하게 되면 위치 정보를 가지고는 있지만 실제로 rect에 적이 반영되지는 않은 상태가 된다.
    enemy_rect.top = enemy_y_pos

    # 충돌 처리
    if character_rect.colliderect(enemy_rect): # colliderect : 사각형 기준으로 충돌이 있었는지 확인(캐릭터가 적과 충돌했는지 확인)
        print("충돌했어요")
        running = False

    # 그리기 : 이 동작은 그리기만 할 뿐 실제 객체들의 동작에는 반영되지 않는다.
    screen.blit(background, (0, 0)) # 배경 그리기
                                    # 좌측 상단에서 우측 하단으로 진행
                                    # (x, y)
    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # 시간 단위를 초로 변환 (기존 : ms)

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))    # render : 글자를 실제로 그린 것, 문자열이어야한다.
                                                                                            # (시간, True, 글자 색상)
    screen.blit(timer, (10, 10))

    # 시간이 0 이하면 게임 종료
    if total_time - elapsed_time <= 0:
        print("Time Out")
        running =False

    pygame.display.update() # 게임화면 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # ms 단위라서 2000

# pygame 종료
pygame.quit()