from PIL import Image,ImageDraw

img = Image.new("RGB",(500,500),"white")

b=[[(170,235),(160,225)],[(160,225),(153,215)],[(153,215),(147,206)],[(147,206),(143,194)],[(143,194),(139,184)],[(139,184),(137,171)],[(137,171),(137,160)],[(137,160),(136,144)],[(136,144),(137,132)],[(137,132),(141,121)],[(141,121),(145,109)],[(145,109),(150,95)],[(150,95),(157,86)],[(157,86),(165,76)],[(165,76),(172,68)],[(172,68),(181,60)],[(181,60),(191,52)],[(191,52),(201,47)],[(201,47),(210,42)],[(210,42),(222,39)],[(222,39),(233,35)],[(233,35),(244,35)],[(244,35),(255,33)],[(255,33),(266,33)],[(266,33),(277,35)],[(277,35),(287,36)],[(287,36),(296,38)],[(296,38),(306,43)],[(306,43),(316,49)],[(316,49),(324,54)],[(324,54),(322,60)],[(322,60),(340,69)],[(340,69),(349,77)],[(349,77),(355,87)],[(355,87),(362,96)],[(362,96),(367,108)],[(367,108),(372,118)],[(372,118),(374,131)],[(374,131),(374,142)],[(374,142),(376,153)],[(376,153),(374,166)],[(374,166),(373,180)],[(373,180),(370,190)],[(370,190),(365,203)],[(365,203),(354,221)],[(354,221),(348,231)],[(348,231),(342,237)]]
draw = ImageDraw.Draw(img)

for i in b:
    coords = i

    draw.line(coords,fill='black',width=12)

y=[[(171,213),(224,175)],[(224,175),(284,247)]]

for i in y:

    draw.line(i,fill='yellow',width=12)

y1=[[(223,175),(280,126)]]

for i in y1:

    draw.line(i,fill='yellow',width=12)

y2=[[(277,129),(318,181)]]

for i in y2:

    draw.line(i,fill='yellow',width=12)

b2=[(194,284),(316,286)]
draw.line(b2,fill='black',width=12)

b3=[(194,319),(316,320)]
draw.line(b3,fill='black',width=12)

y3=[(215,349),(293,347)]
draw.line(y3,fill='yellow',width=12)

y4=[[(285,349),(281,356)],[(281,356),(275,365)],[(275,365),(269,370)],[(269,370),(262,375)],[(262,375),(255,377)],[(255,377),(245,375)],[(245,375),(238,369)],[(238,369),(232,363)],[(232,363),(227,356)],[(227,356),(222,349)]]

for i in y4:
    draw.line(i,fill='yellow',width=12)

y5=[(232,356),(276,355)]
draw.line(y5,fill='yellow',width=12)

y6=[(242,364),(266,364)]
draw.line(y6,fill='yellow',width=12)

img.save('Output_image.png')

img.show()