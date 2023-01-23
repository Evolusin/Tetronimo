from settings import *
import sys
from tetris import Tetris


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pg.display.flip()

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.anim_triger = False
        pg.time.set_timer(self.user_event, ANIMATION_INTERWAL)

    def check_events(self):
        self.anim_triger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_triger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App()
    app.run()
