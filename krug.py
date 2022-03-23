from PIL import Image

img = Image.open("./images/white.jpg")
width, height = img.size


for y in range(height):
    for x in range(width):
        dist = min(abs(x - width), x, abs(y - height), y) # 

        dist = dist / (height / 2) # соотношение от центра к краю

        r = 90 * dist + 0 *(1 - dist)
        g = 0 * dist + 180 * (1 - dist)
        b = 0 * dist + 25 * (1 - dist)
        img.putpixel((x, y), (int(r), int(g), int(b)))

img.save('./images/gradient.jpg')
