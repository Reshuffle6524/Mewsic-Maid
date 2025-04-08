import time
from rich.console import Console
from rich_pixels import Pixels

# Initialize the console object
console = Console()

# Path to your images (adjust with your actual path)
image_folder = "./luckystar-pics/"
image_files = [f"{image_folder}/out{i + 1}.png" for i in range(4)]  # Modify the image names if necessary

# Preload the images into memory (so you don't load them every time)
images = [Pixels.from_image_path(image_path) for image_path in image_files]

# The fps you want to display (24 frames per second)
fps = 24
frame_duration = 1 / fps

# Loop through each image and display it
while True:
    for pixels in images:
        # Print the pre-loaded image to the console
        console.print(pixels)

        # Wait for the next frame
        time.sleep(frame_duration)

        # Clear the console screen for the next frame
        console.clear()

