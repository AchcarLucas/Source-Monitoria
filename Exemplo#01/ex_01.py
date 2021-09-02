import pygame

#define o tamanho da tela
screenSize = (800, 600)
# cria a tela e salva a instância dessa tela em screen
screen = pygame.display.set_mode(screenSize, pygame.DOUBLEBUF | pygame.FULLSCREEN)
pygame.display.set_caption("Exemplo#01")

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
            
    # depois que você definiu o que desenhar, faça a atualização da tela (chamamos essa parte de double-buffer)
    # o double-buffer evita flicks na tela
    pygame.display.update()
    
# finaliza todos os módulos que foram iniciados
pygame.quit()
