import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from PIL import ImageFont
from bank_names import bank_names

def get_colour(i):
    if 5 <= i <= 13: #Gears
        return 'red'
    elif 19 <= i <= 34:
        return 'green'
    elif 35 <= i <= 47:
        return 'blue'
    return 'white'

def get_name(i):
    return ''

def render_template_image(coords, width, height, box_width):

    filename="template.png"
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # draw each box
    for i, box in enumerate(coords):
        # extract corner coordinates
        x1, x2, x3, x4, y1, y2, y3, y4 = box[1:]
        # y is flipped
        y1=abs(y1 -1)
        y2=abs(y2 - 1)
        y3=abs(y3 - 1)
        y4=abs(y4 - 1)
        # non abs coords
        y1 = height - y1 * height
        y2 = height - y2 * height
        y3 = height - y3 * height
        y4 = height - y4 * height

        # create box polygon
        poly = [(x1 * width, y1), (x2 * width - box_width, y2), (x4 * width - box_width, y4 - box_width), (x3 * width, y3 - box_width)]

        # draw box polygon
        draw.polygon(poly, outline=get_colour(i), width=box_width)

    # save image
    img.save(filename)
    
def render_template_labels(coords, width, height, font_sz):
    filename="template_labels.png"
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', font_sz) # create font instance with size 24
    for i, box in enumerate(coords):
        # extract corner coordinates
        x1, x2, x3, x4, y1, y2, y3, y4 = box[1:]
        if x1 >= 1.0 and y1 >= 1.0:
            continue
        # y is flipped
        y1=abs(y1 -1)
        y2=abs(y2 - 1)
        y3=abs(y3 - 1)
        y4=abs(y4 - 1)
        # non abs coords
        y1 = height - y1 * height
        y2 = height - y2 * height
        y3 = height - y3 * height
        y4 = height - y4 * height
        # calculate center point
        cx = (x1 + x2 + x3 + x4) / 4 * width
        cy = (y1 + y2 + y3 + y4) / 4
        # render text in center of box
        text = "{}".format(bank_names[i])
        text_width, text_height = draw.textsize(text, font=font) # pass font instance to get correct text size
        draw.text((cx - text_width/2, cy - text_height/2), text, font=font) # pass font instance to use larger font
    img.save(filename)