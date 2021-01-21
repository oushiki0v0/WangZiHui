import sys



import pygame

from alien import Alien

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

from ship import Ship

import game_functions as gf






# 音乐的路径
file=r'music\bgm.mp3'
# 初始化
pygame.mixer.init()
# 加载音乐文件
track = pygame.mixer.music.load(file)
# 开始播放音乐流
pygame.mixer.music.play()



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("CSGO")

    #创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)




    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()


    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)



    #创建一个外星人
    alien = Alien(ai_settings, screen)



    #开始游戏的主循环
    while True:






        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)



run_game()





