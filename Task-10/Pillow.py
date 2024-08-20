from PIL import  Image,ImageDraw

img = Image.new("RGB",(500,500),"white")

draw = ImageDraw.Draw(img)

coords = [(170,235),(160,225)]

draw.line(coords,fill = 'black',width=2)

img.save("output_image.png")

img.show()