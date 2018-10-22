import pygame, sys, time
from pygame.locals import *
import random

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700
PLAYER1 = pygame.image.load('글자들/세종대1.png')
PLAYER1 = pygame.transform.scale(PLAYER1,(250,250))
P1_LIFE = int(99)
P1_LIFE_B = P1_LIFE
PLAYER2 = pygame.image.load('글자들/건대1.png')
PLAYER2 = pygame.transform.scale(PLAYER2,(250,250))
P2_LIFE = int(99)
P2_LIFE_B = P2_LIFE
BACKGROUND = pygame.image.load('글자들/배틀 백그라운드.png')
TEXT = pygame.image.load('글자들/배틀씬1.png')

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('건대 코딩 대전')
BASICFONT = pygame.font.Font('freesansbold.ttf',25)
FINISH = False
SCENE_NUM = 1
flag = 0
def Life_sum1(Life): 
    sum =0
    for i in range(0,10):
        for j in range(0,2):
            sum = sum + j
    Life = Life - sum
    return Life

def Life_sum2(Life): 
    sum =0
    for i in range(0,10):
        for j in range(0,2):
            sum = sum + i
    Life = Life - sum
    return Life

while not FINISH:
    for event in pygame.event.get():
        P1_LIFE_TEXT = BASICFONT.render("LIFE: %d" %(P1_LIFE), True, (40,40,40))
        P2_LIFE_TEXT = BASICFONT.render("LIFE: %d" %(P2_LIFE), True, (40,40,40))
        P1_LIFE_TEXT_1 = BASICFONT.render("%d" %(P1_LIFE_B), True, (40,40,40))
        P2_LIFE_TEXT_1 = BASICFONT.render("%d" %(P2_LIFE_B-P2_LIFE), True, (40,40,40))
        P2_LIFE_TEXT_2 = BASICFONT.render("%d" %(P2_LIFE), True, (40,40,40))
        
        if SCENE_NUM==1:
            DISPLAYSURF.fill((255,255,255))
            DISPLAYSURF.blit(BACKGROUND ,(0,0))
            DISPLAYSURF.blit(PLAYER1,(80,250))#세종
            DISPLAYSURF.blit(PLAYER2,(620,60))#건대
            DISPLAYSURF.blit(TEXT,(65,550))
            DISPLAYSURF.blit(P1_LIFE_TEXT,(80,210))
            DISPLAYSURF.blit(P2_LIFE_TEXT,(620,20))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SCENE_NUM+=1
                
        elif SCENE_NUM==2:
            TEXT=pygame.image.load('글자들/배틀씬2.png')
            DISPLAYSURF.blit(BACKGROUND ,(0,0))
            DISPLAYSURF.blit(PLAYER1,(80,250))
            DISPLAYSURF.blit(PLAYER2,(620,60))
            DISPLAYSURF.blit(TEXT,(65,550))
            DISPLAYSURF.blit(P1_LIFE_TEXT,(80,210))
            DISPLAYSURF.blit(P2_LIFE_TEXT,(620,20))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SCENE_NUM+=1
                    
        elif SCENE_NUM%3 == 0:
            TEXT=pygame.image.load('글자들/배틀씬3.png')#상대 라이프를 깎을 수 있는 함수스킬들이다 선택해보자
            SKILL_BACKGROUND = pygame.image.load('글자들/스킬1.png')
            DISPLAYSURF.blit(SKILL_BACKGROUND ,(0,0))
            DISPLAYSURF.blit(TEXT,(65,550))
            if event.type == pygame.KEYDOWN:
                if event.key == ord('1'):
                    P2_LIFE_B = P2_LIFE
                    P2_LIFE = P2_LIFE % 50
                    SCENE_NUM+=1
                elif event.key == ord('2'):
                    P2_LIFE_B = P2_LIFE
                    P2_LIFE = P2_LIFE / 5
                    SCENE_NUM+=1
                elif event.key == ord('3'):
                    P2_LIFE_B = P2_LIFE
                    P2_LIFE = Life_sum1(P2_LIFE)
                    SCENE_NUM+=1
                elif event.key == ord('4'):
                    P2_LIFE_B = P2_LIFE
                    P2_LIFE = Life_sum2(P2_LIFE)
                    SCENE_NUM+=1
                P1_LIFE_B = random.randrange(10,20)
                
                    
        elif SCENE_NUM%3 == 1:
            BACKGROUND = pygame.image.load('글자들/배틀 백그라운드.png')
            TEXT = pygame.image.load('글자들/배틀씬4.png')#데미지 주기
            DISPLAYSURF.fill((255,255,255))
            DISPLAYSURF.blit(BACKGROUND ,(0,0))
            DISPLAYSURF.blit(PLAYER1,(80,250))
            DISPLAYSURF.blit(PLAYER2,(620,60))
            DISPLAYSURF.blit(TEXT,(65,550))
            DISPLAYSURF.blit(P1_LIFE_TEXT,(80,210))
            DISPLAYSURF.blit(P2_LIFE_TEXT,(620,20))
            DISPLAYSURF.blit(P2_LIFE_TEXT_1,(165,550))
            DISPLAYSURF.blit(P2_LIFE_TEXT_2,(350,550))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SCENE_NUM+=1
                    P1_LIFE = P1_LIFE - P1_LIFE_B
                
        elif SCENE_NUM%3 == 2:
            TEXT = pygame.image.load('글자들/배틀씬5.png')#데미지 받음
            DISPLAYSURF.blit(BACKGROUND ,(0,0))
            DISPLAYSURF.blit(PLAYER1,(80,250))
            DISPLAYSURF.blit(PLAYER2,(620,60))
            DISPLAYSURF.blit(TEXT,(65,550))
            DISPLAYSURF.blit(P1_LIFE_TEXT,(80,210))
            DISPLAYSURF.blit(P2_LIFE_TEXT,(620,20))
            DISPLAYSURF.blit(P1_LIFE_TEXT_1,(135,550))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SCENE_NUM+=1

                    
        if (P1_LIFE <= 0 or P2_LIFE <=0) and (SCENE_NUM-1)%3 == 2:
           
                crown = pygame.image.load('글자들/왕관.png')
                crown = pygame.transform.scale(crown,(100,50))
                if(P1_LIFE<=0):
                    DISPLAYSURF.blit(BACKGROUND ,(0,0))
                    DISPLAYSURF.blit(PLAYER1,(80,250))
                    DISPLAYSURF.blit(PLAYER2,(620,60))
                    TEXT=pygame.image.load('글자들/패배.png')
                    DISPLAYSURF.blit(TEXT,(65,550))
                    DISPLAYSURF.blit(crown,(695,10))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            event.type == QUIT
                            FINISH = True
                elif(P2_LIFE<=0):
                    DISPLAYSURF.blit(BACKGROUND ,(0,0))
                    DISPLAYSURF.blit(PLAYER1,(80,250))
                    DISPLAYSURF.blit(PLAYER2,(620,60))
                    TEXT=pygame.image.load('글자들/승리.png')
                    DISPLAYSURF.blit(TEXT,(65,550))
                    DISPLAYSURF.blit(crown,(155,200))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            FINISH = True
            
                    

        
            
                

            
            

            
            













        
    if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
