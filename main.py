import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH, HEIGHT = 600, 600  # Window dimensions
GRID_SIZE = 15
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 30

 # Setup display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labyrinth Game")

# Setup clock
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        self.energy = 100
        self.keys = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.energy = max(0, self.energy - 10)

    def draw(self, win):
        pygame.draw.rect(win, BLUE, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def handle_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.move(dx=-1, dy=0)
        if keys[pygame.K_RIGHT]:
            self.move(dx=1, dy=0)
        if keys[pygame.K_UP]:
            self.move(dx=0, dy=-1)
        if keys[pygame.K_DOWN]:
            self.move(dx=0, dy=1)

    def add_key(self):
        self.keys += 1

    def use_key(self):
        if self.keys > 0:
            self.keys -= 1
            return True
        return False

def redraw_window(win, player, key_position):
    win.fill(WHITE)

    # Draw key
    pygame.draw.rect(win, GREEN, (key_position[0] * CELL_SIZE, key_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw player
    player.draw(win)

    # Update display
    pygame.display.update()

def main():
    player = Player(GRID_SIZE // 2, GRID_SIZE // 2)
    key_position = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    floor = 1

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.handle_keys()

        # Check if player found the key
        if (player.x, player.y) == key_position:
            player.add_key()
            print("Key found! Proceeding to the next level.")
            floor += 1
            key_position = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))  # New key position

            # Add health if more than one key
            if player.keys > 1:
                player.health = min(100, player.health + 20)

            # Reset player position
            player.x, player.y = GRID_SIZE // 2, GRID_SIZE // 2

        # Check if player is out of energy
        if player.energy <= 0:
            print("You ran out of energy! Game Over.")
            run = False

        redraw_window(win, player, key_position)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


