
import pygame

from data import Data

class MainLoop:
    def __init__(self):
        data = Data()
        data.load()
        self.config = data.config['config']
        self.window = data.config['config']['window']

        self.RUN = True

        # Window =
        self.window_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.window_rect = self.window_display.get_rect()
        self.window_width, self.window_height = self.window_rect.size
        self.window_title = pygame.display.set_caption(self.window['title'])
        self.window_icon = pygame.display.set_icon(pygame.image.load(self.window['icon_path']))
        self.window_clock = pygame.time.Clock()

    def set(self):
        pass

    def run(self):
        while self.RUN:
            window_width, window_height = pygame.display.get_surface().get_size()
            # self.C['window']['size'][2] = (window_width, window_height)
            if  self.window['full_screen'] == 'True':
                self.window_display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            if self.window['full_screen'] == 'False':
                self.window_display = pygame.display.set_mode((tuple(self.window['size'])[1][0],tuple(self.window['size'])[1][1]), pygame.RESIZABLE)
            self.window_rect = self.window.get_rect()
            self.window_width, self.window_height = self.window_rect.size
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.RUN = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.RUN = False

            pygame.display.update()
            self.window_clock.tick(60)

if __name__ == '__main__':
    main = MainLoop()
    print(main.config)
    main.run()