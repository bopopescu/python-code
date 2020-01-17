from PIL import Image,ImageDraw,ImageFont

#add num to image
def addnum(image,num):
    with Image.open(image) as head:
        w,h = head.size
        font = ImageFont.truetype('arial.ttf',25)
        draw = ImageDraw.Draw(head)
        draw.text((0.8*w,0.1*h),str(num),fill=(255,0,0),font=font)
        head.save('head2.jpg')

if __name__ =='__main__':
    addnum('head.jpg',68)
