# image-processing-tool
A new repository created via Python script


---

I'm sorry for the confusion but there is a contradiction in your request. You asked for the final code without any explanation but then requested a step by step explanation. I'm assuming you want the final code with explanation so here it is:

```python
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
```

Just replace 'original.png' with the path of your image. This code will create and save two images. One with an emboss filter applied to it and another one that is rotated 90 degrees.

Please ensure that you have installed the Pillow library in Python, which is a fork of PIL (Python Image Library). It adds some user-friendly features. You can install it using pip:

```bash
pip install pillow
```