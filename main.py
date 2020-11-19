import sys, time, random, pygame
from pygame.locals import *

class game:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Snake')
        self.over = False
        self.startScreen = True
        self.block = 10

        # snake position and direction variables

        self.snakePositionX = 300
        self.snakePositionY = 300
        self.snakeDirectionX = 0
        self.snakeDirectionY = 0

        # apple position

        self.applePositionX = random.randrange(110, 690, 10)
        self.applePositionY = random.randrange(110, 590, 10)

        # fix FPS

        self.clock = pygame.time.Clock()

        # list that contains all the positions of the snake

        self.snakePosition = []

        # snake size variable

        self.snakeSize = 1

        # load image

        self.image = pygame.image.load('startScreen.jpg')

        # narrow image

        self.imageTitle = pygame.transform.scale(self.image, (200, 200))

        # score variables

        self.score = 0

    def snakeMovment(self):
        # move snake

        self.snakePositionX += self.snakeDirectionX # move the snake left or right
        self.snakePositionY += self.snakeDirectionY # move the snake up or down

    def showSnake(self):
        # show other parts of the snake

        for snakePart in self.snakePosition:
            pygame.draw.rect(self.screen, (0, 255, 0), (snakePart[0], snakePart[1], self.block, self.block))

    def showElements(self):
        self.screen.fill((0, 0, 0)) # assigns the color black to the screen

        # show snake

        pygame.draw.rect(self.screen, (0, 255, 0), (self.snakePositionX, self.snakePositionY,
                                                    self.block, self.block))

        # show apple

        pygame.draw.rect(self.screen, (255, 0, 0), (self.applePositionX, self.applePositionY,
                                                    self.block, self.block))
        self.showSnake()

    def bitesTail(self, snakeHead):
        # the snake bites its tail

        for snakePart in self.snakePosition[:-1]:
            if snakePart == snakeHead:
                sys.exit()

    def createMessage(self, font, message, rectangle, color):
        if font == 'little':
            font = pygame.font.SysFont('Machine', 20, False)
        elif font == 'medium':
            font = pygame.font.SysFont('Machine', 30, False)
        elif font == 'large':
            font = pygame.font.SysFont('Machine', 40, True)
        message = font.render(message, True, color)
        self.screen.blit(message, rectangle)

    def limits(self):
        # show game limits

        pygame.draw.rect(self.screen, (255, 255, 255), (100, 100, 600, 500), 3)

    def control(self):
        # manage events and show some game components

        while self.startScreen:
            for event in pygame.event.get(): # check events in game
                if event.type == QUIT:
                   sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.startScreen = False
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.imageTitle, (300, 50, 100, 50))
                self.createMessage('little', 'The goal of the game is for the snake to grow',
                                   (250, 300, 200, 5), (240, 240, 240))
                self.createMessage('little', 'for that, he needs apples, eat as many as possible!',
                                   (235, 320, 200, 5), (240, 240, 240))
                self.createMessage('medium', 'Press Enter to start',
                                   (300, 450, 200, 5), (255, 255, 255))

                pygame.display.flip()

        while not self.over:

            # create the start screen, events, display the image ...

            for event in pygame.event.get(): # check events in game
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:

                        # right arrow pressed

                        self.snakeDirectionX = 10
                        self.snakeDirectionY = 0
                    if event.key == K_LEFT:

                        # left arrow pressed

                        self.snakeDirectionX = -10
                        self.snakeDirectionY = 0
                    if event.key == K_UP:

                        # up arrow pressed

                        self.snakeDirectionX = 0
                        self.snakeDirectionY = -10
                    if event.key == K_DOWN:

                        # down arrow pressed

                        self.snakeDirectionX = 0
                        self.snakeDirectionY = 10

            # move snake if it's within the limits of the game

            if self.snakePositionX <= 100 or self.snakePositionX >= 700 \
                or self.snakePositionY <= 100 or self.snakePositionY >= 600:

                # if the snake goes out of bounds the game ends

                sys.exit()
            self.snakeMovment()

            # if the snake eat the apple

            if self.applePositionY == self.snakePositionY and self.applePositionX == self.snakePositionX:
                self.applePositionX = random.randrange(110, 690, 10)
                self.applePositionY = random.randrange(110, 590, 10)

                # increase the size of the snake

                self.snakeSize += 1

                # increase the score

                self.score += 1

            # snake head position list

            snakeHead = []
            snakeHead.append(self.snakePositionX)
            snakeHead.append(self.snakePositionY)

            # add the head of the snake in the list

            self.snakePosition.append(snakeHead)

            # cut extra parts of the snake

            if len(self.snakePosition) > self.snakeSize:
                self.snakePosition.pop(0)
            self.showElements()
            self.bitesTail(snakeHead)
            self.createMessage('large', 'Snake Game', (280, 10, 100, 50), (255, 255, 255))
            self.createMessage('large', format(str(self.score)), (375, 50, 50, 50), (255, 255, 255))

            # show limits

            self.limits()
            self.clock.tick(20)
            pygame.display.flip() # update screen

if __name__ == '__main__':
    pygame.init() # init the game
    game().control()
    pygame.quit()