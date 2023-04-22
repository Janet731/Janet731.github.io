'''
Implement a game of Tetris using pygame.
'''
import pygame
import random

GAME_WIDTH = 10
GAME_HEIGHT = 20
BLOCK_SIZE_PX = 32
FRAME_RATE = 5

I_SHAPE = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

S_SHAPE = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0]
]

Z_SHAPE = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 0]
]

O_SHAPE = [
    [1, 1],
    [1, 1]
]

L_SHAPE = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 1]
]

J_SHAPE = [
    [0, 0, 0],
    [1, 1, 1],
    [1, 0, 0]
]

T_SHAPE = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 0]
]

SHAPES = [ I_SHAPE, S_SHAPE, Z_SHAPE, O_SHAPE, L_SHAPE, J_SHAPE, T_SHAPE ]

EMPTY_BLOCK_COLOR = (0, 0, 0)
FIXED_BLOCK_COLOR = (150, 150, 150)
BLOCK_COLOR = (0, 255, 150)


TETRIS_SHAPES = []

class TetrisBlock:
    def __init__(self, shape):
        self.shape = shape
        self.x = 0
        self.y = 0

class TetrisState:
    def __init__(self):
        self.grid = [[0 for _ in range(GAME_WIDTH)] for _ in range(GAME_HEIGHT)]
        self.current_block = None
        self.next_block = self.create_new_block()
        self.score = 0

    def update(self):
        if self.current_block is None:
            # print('enter update func')
            self.current_block = self.next_block
            self.next_block = self.create_new_block()
        else:
            self.move_block()
            # update the grid
            removed_rows = []
            for row in range(GAME_HEIGHT):
                moved = True
                for col in range(GAME_WIDTH):
                    if self.grid[row][col] == 0:
                        moved = False
                        break
                if moved:
                    removed_rows.append(row)

            for row in removed_rows:
                self.grid.pop(row)
                self.grid.insert(0, [0 for _ in range(GAME_WIDTH)])
                self.score += 1
                print('score: ', self.score)

    def create_new_block(self):
        random_shape = random.choice(SHAPES)
        block = TetrisBlock(random_shape)
        block.x = GAME_WIDTH // 2 - len(random_shape[0]) // 2
        return block

    def is_colliding(self, block: TetrisBlock) -> bool:
        #Check if the block is colliding with another block.
        for y, row in enumerate(block.shape):
            for x, cell in enumerate(row):
                if cell == 1:
                    # Check if the block is outside the grid.
                    if(
                        block.y + y >= GAME_HEIGHT
                        or block.x + x >= GAME_WIDTH
                        or block.x + x < 0
                    ):
                        return True
                    if self.grid[block.y + y][block.x + x] == 1:
                        return True
        return False

    def fix_block_into_grid(self): 
        for y, row in enumerate(self.current_block.shape):
            for x, cell in enumerate(row):
                if cell == 1:
                    self.grid[self.current_block.y + y][self.current_block.x + x] = 1

        self.current_block = None

    def rotate_shape(self, shape, reverse=False):
        # Rotate the shape 90 degrees.
        if reverse:
            return [list(reversed(row)) for row in zip(*shape)]
        else:
            return [list(row) for row in zip(*shape[::-1])]

    def move_block(self):
        # Move the block left or right.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.current_block.x -= 1
            if self.is_colliding(self.current_block):
                self.current_block.x += 1
        elif keys[pygame.K_RIGHT]:
            self.current_block.x += 1
            if self.is_colliding(self.current_block):
                self.current_block.x -= 1
        elif keys[pygame.K_DOWN]:
            self.current_block.y += 1
            if self.is_colliding(self.current_block):
                self.current_block.y -= 1

        # Use A and D to rotate the block.
        if keys[pygame.K_a]:
            self.current_block.shape = self.rotate_shape(self.current_block.shape)
            if self.is_colliding(self.current_block):
                self.current_block.shape = self.rotate_shape(
                    self.current_block.shape, reverse=True
                )
        elif keys[pygame.K_d]:
            self.current_block.shape = self.rotate_shape(self.current_block.shape, reverse=True)
            if self.is_colliding(self.current_block):
                self.current_block.shape = self.rotate_shape( self.current_block.shape)

        # Move the block down 1 row each update.
        self.current_block.y += 1 

        # Check if the block is colliding with another block.
        if self.is_colliding(self.current_block):
            self.current_block.y -= 1
            self.fix_block_into_grid()

def main():
    # Create the pygame context and screen.
    pygame.init()
    screen = pygame.display.set_mode((GAME_WIDTH * BLOCK_SIZE_PX, GAME_HEIGHT * BLOCK_SIZE_PX))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    
    # Create the game state.
    state = TetrisState()
    
    # Main game loop.
    while True:
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]):
            pygame.quit()
            return
        if (keys[pygame.K_r]):
            state = TetrisState()

        # Update the game state.
        state.update()

        # Draw the game state.
        screen.fill((0, 0, 0))
        for y in range(GAME_HEIGHT):
            for x in range(GAME_WIDTH):
                if state.grid[y][x] == 0:
                    pygame.draw.rect(
                        screen, 
                        EMPTY_BLOCK_COLOR, 
                        (
                            x * BLOCK_SIZE_PX, 
                            y * BLOCK_SIZE_PX, 
                            BLOCK_SIZE_PX, 
                            BLOCK_SIZE_PX
                        ),
                    )
                else:
                    pygame.draw.rect(
                        screen, 
                        FIXED_BLOCK_COLOR, 
                        (
                            x * BLOCK_SIZE_PX, 
                            y * BLOCK_SIZE_PX, 
                            BLOCK_SIZE_PX, 
                            BLOCK_SIZE_PX
                        ),
                    )

        #Draw the current block.
        if state.current_block is not None:
            for y in range(len(state.current_block.shape)):
                for x in range(len(state.current_block.shape[y])):
                    if state.current_block.shape[y][x] == 1:
                        pygame.draw.rect(
                            screen, 
                            BLOCK_COLOR, 
                            (
                                (x + state.current_block.x) * BLOCK_SIZE_PX, 
                                (y + state.current_block.y) * BLOCK_SIZE_PX, 
                                BLOCK_SIZE_PX,
                                BLOCK_SIZE_PX
                            ),
                        )
        
        pygame.display.flip()

if __name__ == "__main__":
    main()