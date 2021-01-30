from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("blur.png", 'png')
