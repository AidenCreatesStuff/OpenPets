import pygame
import os

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OpenPets")

# Load fonts (Define font before using it)
pygame.font.init()
font = pygame.font.Font(None, 60)  # Default font, size 36

# Load sprite frames dynamically
sprite_folder = "assets\imgs\sprites"  # Change to your actual folder name
bestfriend_sprite_folder = os.path.join(sprite_folder, "bestfriend")
frames = []

for i in range(14):  # Assuming 14 frames
    filename = f"bestfriend_{i:02d}.png"  # Formats as bestfriend_00, bestfriend_01, etc.
    img_path = os.path.join(bestfriend_sprite_folder, filename)
    image = pygame.image.load(img_path).convert_alpha()
    frames.append(image)

expressions = {
    0: "default",
    1: "look_right",
    2: "look_left",
    3: "look_right_alt",
    4: "look_left_alt",
    5: "eyesclosed_half",
    6: "eyesclosed",
    7: "sassy",
    8: "happy",
    9: "winking_left",
    10: "winking_right",
    11: "angry",
    12: "disappointed",
    13: "neutral"
}

# Function to display a specific sprite with its expression name
def display_expression(expression_index):
    screen.fill((144,213,255))

    # Ensure valid index
    if 0 <= expression_index < len(frames):
        scaled_sprite = pygame.transform.scale(frames[expression_index], (WIDTH, HEIGHT))
        screen.blit(scaled_sprite, (0, 0))

    # Draw text for the expression name
    expression_text = expressions.get(expression_index, "Unknown")  # Default to "Unknown"
    text_surface = font.render(expression_text, True, (0, 0, 0))  # Black text

    text_x = (WIDTH - text_surface.get_width()) // 2  # Center X
    text_y = 20  # Keep it near the top

    screen.blit(text_surface, (text_x, text_y))  # Draw at top-left

    pygame.display.update()  # Update display

running = True
current_expression = 7

while running:
    display_expression(current_expression)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
