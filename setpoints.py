import pygame
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import time

# Function to open a file dialog and return the selected file path
def select_file():
    root = tk.Tk()
    root.withdraw()  # Hides the Tkinter root window
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path

# Function to copy the selected file to the program's directory
def copy_file_to_program_directory(file_path):
    base_name = os.path.basename(file_path)
    destination = os.path.join('', base_name)

    # Check if the file exists and create a unique name if it does
    if os.path.exists(destination):
        name, extension = os.path.splitext(base_name)
        destination = os.path.join('', f"{name}_{int(time.time())}{extension}")

    shutil.copy(file_path, destination)
    print(f"Copied file to {destination}")

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('File Upload Example')
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:  # Press 'O' to open file dialog
                file_path = select_file()
                if file_path:  # If a file was selected
                    print(f"File selected: {file_path}")
                    copy_file_to_program_directory(file_path)
                    # Now the file is in your program's directory, and you can handle it as needed

    screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
