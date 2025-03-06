import pygame

colors = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "BROWN": (139, 69, 19),
    "BLUE": (30, 144, 255),
    "GREEN": (34, 139, 34),
    "YELLOW": (255, 255, 0),
}


class Game:
    def __init__(self, width=800, height=600, title="House Drawing with Game Class"):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.ground = Ground(width, height, colors)
        self.house = House(width // 3, height // 2, width // 3, height // 3, colors)

        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.screen.fill(colors["WHITE"])
        self.ground.draw(self.screen)
        self.house.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(self.fps)

        pygame.quit()


class House:
    def __init__(self, x, y, width, height, colors):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walls = Wall(x, y, width, height, colors)
        self.roof = Roof(x, y, width, height, colors)
        self.door = Door(
            x + width // 3, y + height // 2, width // 4, height // 2, colors
        )
        self.windows = [
            Window(x + width // 10, y + height // 5, width // 6, height // 6, colors),
            Window(
                x + width - width // 10 - width // 6,
                y + height // 5,
                width // 6,
                height // 6,
                colors,
            ),
        ]
        self.chimney = Chimney(
            x + width - width // 4, y - height // 8, width // 10, height // 4, colors
        )

    def draw(self, surface):
        self.walls.draw(surface)
        self.roof.draw(surface)
        self.door.draw(surface)
        for window in self.windows:
            window.draw(surface)
        self.chimney.draw(surface)


class Wall:
    def __init__(self, x, y, width, height, colors):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, colors["BROWN"], self.rect)
        pygame.draw.rect(surface, colors["BLACK"], self.rect, 2)  # Border


class Roof:
    def __init__(self, x, y, width, height, colors):
        self.points = [(x, y), (x + width // 2, y - height // 2), (x + width, y)]

    def draw(self, surface):
        pygame.draw.polygon(surface, colors["RED"], self.points)
        pygame.draw.polygon(surface, colors["BLACK"], self.points, 2)  # Border


class Door:
    def __init__(self, x, y, width, height, colors):
        self.rect = pygame.Rect(x, y, width, height)
        self.knob_pos = (x + width - width // 6, y + height // 2)
        self.knob_radius = width // 12

    def draw(self, surface):
        pygame.draw.rect(surface, colors["BLACK"], self.rect)
        pygame.draw.circle(surface, colors["YELLOW"], self.knob_pos, self.knob_radius)


class Window:
    def __init__(self, x, y, width, height, colors):
        self.rect = pygame.Rect(x, y, width, height)
        self.panes = [
            pygame.Rect(x, y, width // 2, height // 2),
            pygame.Rect(x + width // 2, y, width // 2, height // 2),
            pygame.Rect(x, y + height // 2, width // 2, height // 2),
            pygame.Rect(x + width // 2, y + height // 2, width // 2, height // 2),
        ]

    def draw(self, surface):
        pygame.draw.rect(surface, colors["BLUE"], self.rect)
        pygame.draw.rect(surface, colors["BLACK"], self.rect, 2)  # Border

        for pane in self.panes:
            pygame.draw.rect(surface, colors["BLACK"], pane, 1)  # Pane dividers


class Chimney:
    def __init__(self, x, y, width, height, colors):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, colors["BLACK"], self.rect)


class Ground:
    def __init__(self, width, height, colors):
        self.rect = pygame.Rect(0, height - height // 4, width, height // 4)

    def draw(self, surface):
        pygame.draw.rect(surface, colors["GREEN"], self.rect)


def main():
    # Create and run the game
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
