import pygame as pg


WIN_SIZE = (900, 600)
WIDTH, HEIGHT = WIN_SIZE
BLACK = (0, 0, 0)
GREY = (192, 192, 192)
WHITE = (255, 255, 255)


class Display_Dyn():
    def __init__(self, game):
        pg.font.init()
        self.game = game
        self.screen = game.screen


    def run(self):
        mouseX, mouseY = pg.mouse.get_pos()
        font = pg.font.SysFont(None, 40)

        text1 = font.render("Mouse", True, BLACK)
        text2 = font.render("Position: ", True, BLACK)
        text3 = font.render(f"X: {mouseX} " + f"Y: {mouseY}", True, BLACK)
        text1_rect = text1.get_rect()
        text2_rect = text2.get_rect()
        text3_rect = text3.get_rect()
        text1_rect.center = (WIDTH // 2, HEIGHT //2)
        text2_rect.center = (WIDTH // 2, HEIGHT //2)
        text3_rect.center = (WIDTH // 2, HEIGHT //2)
        text1_rect.top = 150
        text2_rect.top = 200
        text3_rect.top = 250
        self.screen.blit(text1, text1_rect)  
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text3, text3_rect)

        font_i = pg.font.SysFont(None, 20)
        intr = font_i.render("Click any key to change mode", True, GREY)
        intr_rect = intr.get_rect()
        intr_rect.center = (WIDTH // 2, HEIGHT // 2)
        intr_rect.top = 300
        self.screen.blit(intr, intr_rect)

class Display_Click():
    def __init__(self, game):
        pg.font.init()
        self.game = game
        self.screen = game.screen


    def run(self):
        mouseX, mouseY = self.game.mouseX, self.game.mouseY
        font = pg.font.SysFont(None, 40)

        text1 = font.render("Mouse", True, BLACK)
        text2 = font.render("Position: ", True, BLACK)
        text3 = font.render(f"X: {mouseX} " + f"Y: {mouseY}", True, BLACK)
        text1_rect = text1.get_rect()
        text2_rect = text2.get_rect()
        text3_rect = text3.get_rect()
        text1_rect.center = (WIDTH // 2, HEIGHT //2)
        text2_rect.center = (WIDTH // 2, HEIGHT //2)
        text3_rect.center = (WIDTH // 2, HEIGHT //2)
        text1_rect.top = 150
        text2_rect.top = 200
        text3_rect.top = 250
        self.screen.blit(text1, text1_rect)  
        self.screen.blit(text2, text2_rect)
        self.screen.blit(text3, text3_rect)

        font_i = pg.font.SysFont(None, 20)
        intr = font_i.render("Click any key to change mode", True, GREY)
        intr_rect = intr.get_rect()
        intr_rect.center = (WIDTH // 2, HEIGHT // 2)
        intr_rect.top = 300
        self.screen.blit(intr, intr_rect)

        
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.Display_Dyn = Display_Dyn(self)
        self.mouseX, self.mouseY = "000", "000"
        self.Display_Click = Display_Click(self)
        self.current_display = 0


    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
            if event.type == pg.KEYDOWN:
                self.current_display += 1
            
            if self.current_display % 2 != 0 and event.type == pg.MOUSEBUTTONDOWN:
                self.mouseX, self.mouseY = pg.mouse.get_pos()


    def run(self):
        while True:
            self.screen.fill(WHITE)

            if self.current_display % 2 == 0:
                self.Display_Dyn.run()
            elif self.current_display % 2 != 0:
                self.Display_Click.run()

            self.event_handler()
            pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()