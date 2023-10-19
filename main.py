from PIL import Image
from PIL import ImageFilter

# Open an Image
def open_image(path):
    return Image.open(path)

# Save Image
def save_image(image, path):
    image.save(path, 'png')

# Create a new image with filter
def create_image_with_filter(image):
    return image.filter(ImageFilter.EMBOSS)

# Create a new image with rotation
def create_image_with_rotate(image):
    return image.rotate(90)

# Main function to run the program
def main():
    # Open the image file
    img = open_image('original.png')
    # Apply filter to the image
    img_with_filter = create_image_with_filter(img)
    # Save the filtered image
    save_image(img_with_filter, 'filtered.png')
    # Apply rotation to the image
    img_with_rotate = create_image_with_rotate(img)
    # Save the rotated image
    save_image(img_with_rotate, 'rotated.png')

if __name__ == '__main__':
    main()
