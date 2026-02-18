from PIL import Image, ImageFilter

# ///////////for blur pikachu///////////
# img = Image.open("./Pokedex/pikachu.jpg")
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur_pikachu.png", "png")
# print(img)


# /////////for gray pikachu/////////
img = Image.open("./Pokedex/pikachu.jpg")
filtered_img = img.convert("L")
crooked = filtered_img.rotate(90)
crooked.save("gray_pikachu.png", "png")
# filtered_img.show()

# ///////////for resize pikachu/////////
# img = Image.open("./Pokedex/pikachu.jpg")
# filtered_img = img.convert("L")
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("gray_pikachu.png", "png")

img = Image.open("./scenery.jpg")
img.thumbnail((400, 400)) 
''' thumbnail method is used to resize the image while maintaining the aspect ratio. It takes a tuple as an argument which specifies the maximum width and height of the thumbnail. The image will be resized to fit within these dimensions while preserving the aspect ratio.
'''
img.save("thumbnail.jpg")