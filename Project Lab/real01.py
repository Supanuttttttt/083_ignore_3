import pygame
import requests
import os

WIDTH,HEIGHT = 750,550
background_color = (251,247,245)
original_grid_element_color = (52,31,151)
buffer = 5

gameIcon = pygame.image.load('asdd.png')
pygame.display.set_icon(gameIcon)

response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win,position):
    myfont = pygame.font.SysFont("Comic Sans MS", 35)
    i,j = position[1], position[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (grid_original[i-1][j-1] != 0):
                    return
                if(event.key == 48):
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color,(position[0]*50+buffer, position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    pygame.display.update()
                if(0 < event.key-48 < 10):
                    pygame.draw.rect(win, background_color,(position[0]*50+buffer, position[1]*50+buffer,50-2*buffer,50-2*buffer))
                    value = myfont.render(str(event.key-48),True,(0,0,0))
                    win.blit(value,(position[0]*50+15,position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                return

def main():
    pygame.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 35)
    win = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("SUDOKU")
    win.fill(background_color)
    infofont = pygame.font.SysFont("Comic Sans MS", 20)
    text1 = infofont.render("How to play...",True,original_grid_element_color)
    win.blit(text1,(50,525))
    text2 = infofont.render("Enter the numbers 1-9 in the grid.",True,original_grid_element_color)
    win.blit(text2,(50,550))
    text3 = infofont.render("They must be related by only the numbers 1-9",True,original_grid_element_color)
    win.blit(text3,(50,575))
    text4 = infofont.render("in a vertical, horizontal and 3*3 grid.",True,original_grid_element_color)
    win.blit(text4,(50,600))
    text4 = infofont.render("Use the num key above your keyboard (not numpad)",True,original_grid_element_color)
    win.blit(text4,(50,625))
    text5 = infofont.render("Use 0 key number to erase answer",True,original_grid_element_color)
    win.blit(text5,(50,650))

    
    for i in range(0,10):
        if (i%3 == 0):
            pygame.draw.line(win, (0,0,0),(50+50*i,50),(50+50*i,500),5)
            pygame.draw.line(win, (0,0,0),(50,50+50*i),(500,50+50*i),5)
        pygame.draw.line(win, (0,0,0),(50+50*i,50),(50+50*i,500),2)
        pygame.draw.line(win, (0,0,0),(50,50+50*i),(500,50+50*i),2)
    pygame.display.update()

    for i in range(0,len(grid[0])):
        for j in range(0,len(grid[0])):
            if(0<grid[i][j]<10):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                win.blit(value,((j+1)*50+15,(i+1)*50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button ==1:
                pos = pygame.mouse.get_pos()
                insert(win,(pos[0]//50,(pos[1]//50)))
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()
