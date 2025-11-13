import pygame as pg
import secrets

def getNum():
    secure_random = secrets.SystemRandom()
    return secure_random.randint(1, 2)

def getCol(i):
    match i:
        case 1: return (173, 0, 0)
        #case 2: return (189, 186, 15)
        case 2: return (18, 181, 0)
        #case 2: return (0, 21, 179)
        #case 2: return (112, 0, 168)

def click(klast,streak,maxstreak):
    k=getNum()
    color=getCol(k)
    if k==klast:
        streak+=1
        maxstreak=max(streak,maxstreak)
    else:
        streak=1
    klast=k
    return klast,streak,maxstreak,color

pg.init()
screen = pg.display.set_mode((800,500)) #, flags=pg.NOFRAME
pg.display.set_caption('Click royale')
icon = pg.image.load("images/PYGAMEICON.jpg")
pg.display.set_icon(icon)

color='Black'
font_large = pg.font.Font(None, 48)
font_medium = pg.font.Font(None, 34)

streak = 1
maxstreak = 1
klast=0
k=1

run=True
while run:
    
    screen.fill(color)
    
    showScore = font_large.render(f"Счёт: {streak}", True, (255,255,255))
    showScore_rect = showScore.get_rect(center = (395, 180))
    screen.blit(showScore, showScore_rect)

    showmaxScore = font_medium.render(f"Рекорд: {maxstreak}", True, (255,255,255))
    showmaxScore_rect = showmaxScore.get_rect(center = (80,50))
    screen.blit(showmaxScore, showmaxScore_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key in [pg.K_SPACE, pg.K_RETURN]:
                klast,streak,maxstreak,color=click(klast,streak,maxstreak)

        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 - левая кнопка мыши
                klast,streak,maxstreak,color=click(klast,streak,maxstreak)

    pg.display.update()

pg.quit() #метод выхода
print(maxstreak)
            
'''match i:
        case 1: return (173, 0, 0)
        case 2: return (201, 107, 0)
        case 3: return (189, 186, 15)
        case 4: return (18, 181, 0)
        case 5: return (15, 107, 255)
        case 6: return (0, 21, 179)
        case 7: return (112, 0, 168)'''
'''k=getNum()
color=getCol(k)
if k==klast:
    streak+=1
    maxstreak=max(streak,maxstreak)
else:
    streak=1
klast=k'''