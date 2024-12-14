"""
Prompt:
I want to create a Snake Game using Python. What steps would I need to do that?

=========================================================================
Answer:

Steps to Create a Snake Game
1. Set Up the Environment
Install pygame:
pip install pygame
Create a new Python file for your project (e.g., snake_game.py).

2. Initialize pygame
Import pygame and initialize it using pygame.init().

3. Define Game Settings
Set the screen size (e.g., 800x600).
Define colors for the snake, food, and background.
Choose the snake's speed and size.

4. Create the Game Window
Use pygame.display.set_mode() to create the game window.
Set a title using pygame.display.set_caption().

5. Implement the Snake
Represent the snake as a list of blocks.
Define movement logic based on keyboard inputs (pygame.KEYDOWN events).

6. Add Food for the Snake
Place food at random positions using random.randint() within the screen boundaries.

7. Detect Collisions
Check if the snake collides with the food.
If yes, grow the snake and reposition the food.
Check if the snake collides with itself or the boundaries.
If yes, end the game.

8. Display the Score
Keep track of the player's score and display it on the screen using pygame.font.Font.

9. Game Loop
Continuously update the game state.
Redraw the snake, food, and score on each frame.
Use pygame.time.Clock to control the frame rate.
10. Handle Game Over
Display a "Game Over" message when the snake dies.
Provide an option to restart or exit.
=======================================================

Prompt:
Provide the code for a Snake Game in Python. The code should include all details and features described above.

======================================================================================================

import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
block_size = 20
snake_speed = 15

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display the score
def display_score(score):
    value = score_font.render(f"Your Score: {score}", True, blue)
    screen.blit(value, [0, 0])

# Draw the snake
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

# Message on Game Over
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width // 6, height // 3])

# Main game function
def game_loop():
    game_over = False
    game_close = False

    x1, y1 = width // 2, height // 2  # Initial position
    x1_change, y1_change = 0, 0  # Movement

    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:
        while game_close:
            screen.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = block_size
                    x1_change = 0

        # Check boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake collides with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

===============================================================================================

Prompt:
I want to change the background color from blue to purple. Where in the code can I do that?

==================================================================================================

To change the background color of the game, you need to modify the color used when filling the screen in the game_loop function. Specifically, replace the screen.fill(black) line with your desired color.

Here’s what you need to do:

Define a purple color at the top of the script:
purple = (128, 0, 128)

Locate the lines where screen.fill(black) is used. These are the lines responsible for filling the background with black. Replace black with purple.

For example, modify these lines in the game_loop function:
screen.fill(black)

Change them to:
screen.fill(purple)

Full Example of the Relevant Changes
At the top of the code, add the new color definition:
purple = (128, 0, 128)

In the game_loop function, replace both occurrences of screen.fill(black) with:
screen.fill(purple)

Now, the game’s background will be purple instead of black. Let me know if you need further assistance!

===============================================================================================================

Prompt:
Where in the code can I adjust the speed of the snake?

==============================================================================================================

You can adjust the speed of the snake by modifying the snake_speed variable, which is defined near the top of the code:
snake_speed = 15

This variable controls how many frames per second (fps) the game runs, which directly affects how fast the snake moves. A higher value will make the snake move faster, while a lower value will slow it down.

Steps to Adjust Snake Speed:
Find the snake_speed Variable: Locate this line near the top of the code:
snake_speed = 15

Change Its Value:

Increase speed: Set a higher number, such as 20 or 25, for a faster snake.
Decrease speed: Set a lower number, such as 10 or 5, for a slower snake.
Dynamic Speed Adjustment (Optional): If you want the snake to get faster as the game progresses (e.g., as the player’s score increases), you can adjust snake_speed dynamically in the game loop. For example:

Replace:
clock.tick(snake_speed)

With:
clock.tick(snake_speed + length_of_snake // 5)

This example makes the snake speed increase slightly as it grows larger, adding more challenge.

"""
