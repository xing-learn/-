import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
# 定义屏幕尺寸
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 定义字体
font_path = "STXINWEI.ttf"  # 字体文件路径
font_size = 36  # 字体大小
font = pygame.font.Font(font_path, font_size)


# 定义贪吃蛇和食物的大小
BLOCK_SIZE = 20

# 定义贪吃蛇的初始位置和速度
snake_x = SCREEN_WIDTH / 2
snake_y = SCREEN_HEIGHT / 2
snake_x_change = 0
snake_y_change = 0

# 定义食物的初始位置
food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

# 定义贪吃蛇的身体
snake_body = []
snake_length = 1
score = 0

# 定义游戏结束标志
game_over = False

# 定义游戏时钟
clock = pygame.time.Clock()

# 初始化玩家名字

player_name = ""
#while not game_over:
 #   for event in pygame.event.get():
  #      if event.type == pygame.QUIT:
   #         game_over = True
    #    elif event.type == pygame.KEYDOWN:
     #       if event.key == pygame.K_RETURN:
                # 玩家按下回车键，开始游戏
               # if player_name:
                #    game_over = False
            #elif event.key == pygame.K_BACKSPACE:
                # 处理退格键，删除最后一个字符
             #   player_name = player_name[:-1]
           # else:
                # 处理其他字符输入
            #    player_name += event.unicode

screen.fill(BLUE)
#输入玩家姓名
text = f"玩家名字: {player_name}"
text_surface = font.render(text, True, RED)
text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
screen.blit(text_surface, text_rect)    
# 游戏主循环
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -BLOCK_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = BLOCK_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -BLOCK_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = BLOCK_SIZE
                snake_x_change = 0

    # 更新贪吃蛇的位置
    snake_x += snake_x_change
    snake_y += snake_y_change

    # 检查贪吃蛇是否撞到边界
    if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
        game_over = True

    # 绘制背景
    screen.fill(BLUE)
    
    #message = font_style.render("Xing Qichen, Please start the Game by Pressing Up, Down, left and Right ", True, RED)
    #screen.blit(message, [SCREEN_WIDTH/12 , SCREEN_HEIGHT / 3])
    # 显示汉字
   # text = "邢起尘，请开始游戏"
    # text_surface = font.render(text, True, BLACK)
    # text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    # screen.blit(text_surface, text_rect)

    # 更新屏幕
    pygame.display.flip()

    # 绘制食物
    pygame.draw.rect(screen, YELLOW, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

    scoretext = f" {score} "
    scoretext_surface = font.render(scoretext, True, RED)
    scoretext_rect = scoretext_surface.get_rect(center=(20, 20))
    screen.blit(scoretext_surface, scoretext_rect)
    # 更新贪吃蛇的身体
    snake_head = []
   # if snake_x == food_x and snake_y == food_y:
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    # if snake_x == food_x and snake_y == food_y:
    snake_body.append(snake_head)

    # 如果贪吃蛇的长度超过了当前长度，则删除最早的身体部分
    if len(snake_body) > snake_length:
       del snake_body[0]

    # 检查贪吃蛇是否撞到自己
    for block in snake_body[:-1]:
        if block == snake_head:
            game_over = True

    # 绘制贪吃蛇
    for block in snake_body:
    #    i = 0
     #   count = 0
      #  if snake_x == food_x and snake_y == food_y:
       #     count = + 1
        #    snake_body.append(snake_x)
         #   snake_body.append(snake_y)
          #  if i <= count: 
           #     pygame.draw.rect(screen, WHITE, [block[i], block[i+1], BLOCK_SIZE, BLOCK_SIZE])
            #    i = i-1
          #  else: 
           # else :
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

    # 如果贪吃蛇吃到了食物，则增加长度并重新生成食物
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / 20.0) * 20.0
        food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    # 更新贪吃蛇的长度
        snake_length += 1
        score += 1
       
    # 更新屏幕
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(3)

# 游戏结束后显示消息
text = f"游戏结束！邢起尘的得分： {score} 分"
text_surface = font.render(text, True, RED)
text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
screen.blit(text_surface, text_rect)
#message = font_style.render("GAME OVER", True, RED)
#screen.blit(message, [SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3])
pygame.display.update()

# 等待玩家退出游戏
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            pygame.quit()
            quit()