try:
    import pygame
    import time
    import math
    from pygame.locals import *
    pygame.init()

    screen = pygame.display.set_mode((500, 600))

    GREY = (120, 120, 120)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    running = True
    running_hai = True
    #Cac nut bam
    font = pygame.font.SysFont('sans', 50)
    text_1 = font.render('+', True, BLACK)
    text_2 = font.render('-', True, BLACK)
    text_3 = font.render('+', True, BLACK)
    text_4 = font.render('-', True, BLACK)
    text_5 = font.render('Start', True, BLACK)
    text_6 = font.render('Reset', True, BLACK)
    #in thong bao
    font = pygame.font.SysFont('sans', 30)
    text_7 = font.render('Het Gio (BY Kiet Hacker)', True, RED)
    font = pygame.font.SysFont('sans', 20)
    text_12 = font.render('12', True, BLACK)
    text_mot = font.render('1', True, BLACK)
    text_hai = font.render('2', True, BLACK)
    text_ba = font.render('3', True, BLACK)
    text_bon = font.render('4', True, BLACK)
    text_nam = font.render('5', True, BLACK)
    text_sau = font.render('6', True, BLACK)
    text_bay = font.render('7', True, BLACK)
    text_tam = font.render('8', True, BLACK)
    text_chin = font.render('9', True, BLACK)
    text_muoi = font.render('10', True, BLACK)
    text_muoimot = font.render('11', True, BLACK)

    font = pygame.font.SysFont('sans', 50)

    total_secs = 15
    total = 0
    is_start = False
    secs = 0
    mins = 0

    r_sec = 90
    r_min = 50

    start = False
    sound = pygame.mixer.Sound('ting.wav')
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        screen.fill(GREY)
        sound = pygame.mixer.Sound('ting.wav')
        sound2 = pygame.mixer.Sound('hettg.wav')
        mouse_x, mouse_y = pygame.mouse.get_pos()
        #print(mouse_x)
        #ve Button
        pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
        pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
        pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
        pygame.draw.rect(screen, WHITE, (300, 150, 150, 50))
        # ve Groress bar
        pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
        pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))
        # them chu
        screen.blit(text_1, (115, 45))
        screen.blit(text_2, (115, 195))
        screen.blit(text_3, (215, 45))
        screen.blit(text_4, (215, 195))
        screen.blit(text_5, (315, 45))
        screen.blit(text_6, (315, 145))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #running_hai = False
                running = False
                #pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.pause()
                    if(100 < mouse_x < 150) and (50 < mouse_y < 100):
                        total_secs = total_secs + 60
                        total = total_secs
                        print("press + minutes")
                    if (100 < mouse_x < 150) and (200 < mouse_y < 250):
                        total_secs = total_secs - 60
                        total = total_secs
                        print("press - minutes")

                    if (200 < mouse_x < 250) and (50 < mouse_y < 100):
                        total_secs = total_secs + 1
                        total = total_secs
                        print("press + seconds")
                    if (200 < mouse_x < 250) and (200 < mouse_y < 250):
                        total_secs = total_secs - 1
                        total = total_secs
                        print("press - seconds")
                    if (300 < mouse_x < 400) and (50 < mouse_y < 100):
                        is_start = True
                        total = total_secs
                        print("total_secs: " + str(total_secs))
                        print("press Start")
                    if (300 < mouse_x < 400) and (150 < mouse_y < 200):
                        running_hai = False
                        total_secs = 0
                        is_start = False
                        print("press Reset")
            if is_start:
                total_secs = total_secs - 1
                pygame.mixer.Sound.play(sound)
                if total_secs == 0:
                    print("Het Gio")

                    pygame.mixer.Sound(sound2)
                    #while running_hai
                    screen.blit(text_7, (70, 525))
                    pygame.display.flip()
                        #running_hai = False

                    #while running:
                        #pygame.display.flip()
                time.sleep(1)
            if total_secs < 0:
                is_start = False
                total_secs = 0
                total = 0
            secs = total_secs % 60
            mins = (total_secs - secs) / 60
            mins = int(mins)
            time_str = str(mins) + " : " + str(secs)

            text_min = font.render(time_str, True, BLUE)
            screen.blit(text_min, (120, 120))
            #screen.blit(text_7, (60, 520))
            # ve
            pygame.draw.circle(screen, BLACK, (250, 400), 100)
            pygame.draw.circle(screen, WHITE, (250, 400), 95)
            pygame.draw.circle(screen, WHITE, (250, 400), 5)
            #ve kim
            #pygame.draw.line(screen, BLACK, (250, 400), (250 + int(r_sec * math.sin((secs/180)*6))))
            #pygame.draw.line(screen, RED, (250, 400), (250 + int(r_min * math.sin((secs/180)*6))))
            #pygame.draw.line(screen, BLACK, (250, 400), (250, 350))
            x_sec = 250 + 90 * math.sin(6 * secs * math.pi/180)
            y_sec = 400 - 90 * math.cos(6 * secs * math.pi / 180)
            pygame.draw.line(screen, BLACK, (250, 400), ((int(x_sec)), (int(y_sec))))

            x_min = 250 + 40 * math.sin(6 * secs * math.pi / 180)
            y_min = 400 - 40 * math.cos(6 * secs * math.pi / 180)
            pygame.draw.line(screen, RED, (250, 400), ((int(x_min)), (int(y_min))))

            # pygame.draw.line(screen, BLACK, (250, 400), (250 + int(r_sec * math.sin((secs/180)*6))))
            # pygame.draw.line(screen, RED, (250, 400), (250 + int(r_min * math.sin((secs/180)*6))))

            screen.blit(text_12, (240, 305))
            screen.blit(text_mot, (290, 318))
            screen.blit(text_hai, (320, 350))
            screen.blit(text_ba, (330, 390))
            screen.blit(text_bon, (320, 430))
            screen.blit(text_nam, (290, 460))
            screen.blit(text_sau, (245, 470))
            screen.blit(text_bay, (200, 460))
            screen.blit(text_tam, (170, 430))
            screen.blit(text_chin, (160, 390))
            screen.blit(text_muoi, (170, 350))
            screen.blit(text_muoimot, (190, 320))

            pygame.display.flip()


    if total != 0:
            pygame.draw.rect(screen, RED, (60, 530, 380 * int((total_secs / total)), 30))
            #screen.blit(text_7, (60, 520))
            #pygame.display.flip()
    pygame.QUIT
except Exception as bug:
    print(bug)
input()



