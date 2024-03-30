import pygame
import sys

def run_game():
    # 初始化pygame
    pygame.init()

    # 设置屏幕尺寸
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame Key Events")

    # 设置背景色
    bg_color = (230, 230, 230)

    # 游戏主循环
    while True:
        # 监听事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 打印按键信息
                print(f"Key pressed: {event.key}")

        # 更新屏幕
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
