import pygame
import math

#define o tamanho da tela
screenSize = (800, 600)
# cria a tela e salva a instância dessa tela em screen
screen = pygame.display.set_mode(screenSize, pygame.DOUBLEBUF)
pygame.display.set_caption("Exemplo#02")

# cria uma instância do time.Clock() - vamos usar para limitar o fps
gameClock = pygame.time.Clock()

# cria uma variavel que verifica se o jogo ainda está rodando
gameRunning = True

# verifica a cada frame se o jogo está rodando
while gameRunning:
    # limita o FPS em 60 quadros por segundo
    gameClock.tick(60)
    
    # verifica os eventos que estão na pool de eventos
    for event in pygame.event.get():
        # verifica se o X (da janela) foi pressionado, se sim, finalziada o jogo (gameRunning = False)
        if(event.type == pygame.QUIT):
            gameRunning = False
        # verifica se uma tecla foi pressionada
        if(event.type == pygame.KEYDOWN):
            # verifica se a tecla é o ESC, se sim, finaliza o jogo (gameRunning = False)
            if(event.key == pygame.K_ESCAPE):
                gameRunning = False
                
    # cria um retângulo vermelho na coordenada x = 0 e y = 0 com largura = 200 e altura = 200
    pygame.draw.rect(screen, (255, 0, 0), (0, 0, 200, 200))
    # cria um retângulo verde na coordenada x = 250 e y = 0 com largura = 200 e altura = 100
    pygame.draw.rect(screen, (0, 255, 0), (250, 0, 200, 100))
    # cria um circulo de raio 20 pixels na coordenada x = 250 e y = 200 com a cor branco
    pygame.draw.circle(screen, (255, 255, 255), (250, 200), 20)
    # cria um arco de elipse de 0 até (PI / 2) com a = 100 e b = 100 (circuferência) na posição x = 250 e y = 400
    pygame.draw.arc(screen, (0, 0, 255), (250, 400, 100, 100), 0, math.pi / 2)
    # cria uma elipse branca (0 até 2*PI) com a = 100 e b = 200 na posição x = 250 e y = 400
    pygame.draw.arc(screen, (255, 255, 255), (400, 200, 100, 200), 0, 2*math.pi)
    # cria uma roxa com inicio no ponto (250, 250) e com ponto final em (300, 300) com largura 2 da linha
    pygame.draw.line(screen, (255, 0, 255), (250, 250), (300, 300), 2)
            
    # depois que você definiu o que desenhar, faça a atualização da tela (chamamos essa parte de double-buffer)
    # o double-buffer evita flicks na tela
    pygame.display.update()
    
# finaliza todos os módulos que foram iniciados
pygame.quit()
