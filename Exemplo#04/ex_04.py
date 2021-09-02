import pygame
import os

#define o tamanho da tela
screenSize = (800, 600)
# cria a tela e salva a instância dessa tela em screen
screen = pygame.display.set_mode(screenSize, pygame.DOUBLEBUF)
pygame.display.set_caption("Exemplo#04")

# cria uma instância do time.Clock() - vamos usar para limitar o fps
gameClock = pygame.time.Clock()

# cria uma variavel que verifica se o jogo ainda está rodando
gameRunning = True
FPS = 60

# carrega a imagem da nave
Ship = pygame.image.load(os.path.join("assets", "ship.png"))

x = (screenSize[0] / 2) - (Ship.get_width() / 2)
y = (screenSize[1] / 2) - (Ship.get_height() / 2)

# velocidade será 5 vezes 1 pixel por segundo
velocity = (1 / FPS) * 5

# inicializa o módulo da fonte
pygame.font.init()
# cria uma fonte do tipo Font
font = None
font = pygame.font.SysFont("Arial", 17)

# exibe uma mensagem que não foi possível inicializar a fonte caso ocorra alguma falha
if(font == None):
    print('Não foi possível criar a fonte')


# verifica a cada frame se o jogo está rodando
while gameRunning:
    # limita o FPS em 60 quadros por segundo (deltaTime é o tempo que levou do frame anterior até agora)
    # OBS: A soma deltaTime em 60 frames será 1 segundo
    deltaTime = gameClock.tick(FPS)
    
    # antes de fazer qualquer coisa, limpa a tela para o próximo frame
    screen.fill((0, 0, 0))
    
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
                
    keys = pygame.key.get_pressed()
    
    # OBS: o eixo x cresce da esquerda para direita e o eixo y de cima para baixo, sendo o ponto (0, 0) o canto superior esquerdo
    
    # movimenta a nave para cima
    if(keys[pygame.K_w] or keys[pygame.K_UP]):
        y = y - deltaTime * velocity
    
    # movimenta a nave para baixo
    if(keys[pygame.K_s] or keys[pygame.K_DOWN]):
        y = y + deltaTime * velocity
        
    # movimenta a nave para a direita
    if(keys[pygame.K_d] or keys[pygame.K_RIGHT]):
        x = x + deltaTime * velocity
        
    # movimenta a nave para a esquerda
    if(keys[pygame.K_a] or keys[pygame.K_LEFT]):
        x = x - deltaTime * velocity
            
    screen.blit(Ship, (x, y))
    
    # cria um texto contendo a coordenada X e Y da cor branca usando a técnica de antialias
    textX = font.render(f'X: {x:.2f}', True, (255, 255, 255))
    textY = font.render(f'Y: {y:.2f}', True, (255, 255, 255))
    
    # exibe o primeiro texto (textX) na posição x = 10 e y = 10
    screen.blit(textX, (10, 10))
    
    # exibe o segundo texto (textY) na posição x = 10 e y = 10 + a altura do textY
    screen.blit(textY, (10, 10 + textX.get_height()))
    
    
    howMove = font.render(f'Utilize as teclas WSAD ou as setas do teclado para movimentar a nave', True, (255, 0, 0))
    
    screen.blit(howMove, (10, screenSize[1] - howMove.get_height() - 10))
    
                           
    # depois que você definiu o que desenhar, faça a atualização da tela (chamamos essa parte de double-buffer)
    # o double-buffer evita flicks na tela
    pygame.display.update()
    
# finaliza todos os módulos que foram iniciados
pygame.quit()
