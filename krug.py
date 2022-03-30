from PIL import Image
img = Image.open("./images/white.jpg")
width, height = img.size


for y in range(height):
    for x in range(width):
        dist = ((x - width/2) ** 2 + (y - height/2) ** 2) ** (1/2)

        
        dist = dist / ((2**(1/2) * (height / 2))) # соотношение от центра к краю

        r = 0 * dist + 150 *(1 - dist)
        g = 30 * dist + 80 * (1 - dist)
        b = 0 * dist + 125 * (1 - dist)
        img.putpixel((x, y), (int(r), int(g), int(b)))

img.save('./images/gradient.jpg')
