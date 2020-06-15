from PIL import Image, ImageDraw, ImageFont
#opens Images
img=Image.open("D:\Python\pillow\d.png").convert("RGB")

images=[]
info=[]

for i in range(3):
    for j in [0.1, 0.5, 0.9]:

        split_img=img.split()   #splits to RGB
        change_img=split_img[i].point(lambda value:value*j)    #changes the RGB value
        split_img[i].paste(change_img) #paste the returned image to source file
        merge_img=Image.merge(img.mode, split_img)   #merge the list of RGB Images
        info.append(f"Channel {i} Intensity {j}")   #info
        images.append(merge_img)    #append image to list


#image font
font=ImageFont.truetype("arial.ttf",size=75)

first=images[0]

#3x3 Grid
c_sheet=Image.new(first.mode, (first.width * 3, (first.height * 3)+(3*85) ) )
x=0
y=0

draw=ImageDraw.Draw(c_sheet)

for no,i in enumerate(images):
    c_sheet.paste(i, (x,y))
    draw.text((x, y+first.height+5), font=font, text=info[no])

    if x+first.width == c_sheet.width:
        x=0
        y+=first.height+85

    else:
        x+=first.width

#Resize final image
final=c_sheet.resize( ( (int(c_sheet.width/2)), (int(c_sheet.width/2)) ))

#save the object
final.save("final.png")