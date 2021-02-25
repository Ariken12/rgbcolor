import PIL
from PIL import Image, ImageDraw

print("введите две буквы из набора {r, g, b}")

while True:
    name = ".\\rgbcolor\\{0}_in_rgb_without_alpha.png".format(input())
    print("13 ", name[13])
    print("14 ", name[14])
    if (name[11] == "r" or name[11] == "g" or name[11] == "b") and (name[12] == "r" or name[12] == "g" or name[12] == "b"):
        break
    else:
        print("введите две буквы из набора {r, g, b}")

h = 8192
w = 8192
r = 30
white = (255, 255, 255)

img = Image.new('RGB', (h, w), white)
draw = ImageDraw.Draw(img)

def tup(name, x, y):
    if name[11] == "r":
        if name[12] == "g":
            return (x//32, y//32, 0)
        elif name[12] == "b":
            return (y//32, 0, x//32)
    elif name[11] == "g":
        if name[12] == "r":
            return (y//32, x//32, 0)
        elif name[12] == "b":
            return (0, y//32, x//32)
    elif name[11] == "b":
        if name[12] == "r":
            return (y//32, 0, x//32)
        if name[12] == "g":
            return(0, y//32, x//32)

for y in range(0, 8160, 32):
    for x in range(0, 8160, 32):
        draw.ellipse((x + 1, y + 1, x + r - 1, y + r - 1), tup(name, x, y), tup(name, x, y))

img.show(img)