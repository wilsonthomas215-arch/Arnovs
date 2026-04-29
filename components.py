from PIL import ImageFont
from styles import *

def draw_card(draw, x, y, width, height, color):
    """Draw a rectangle card"""
    draw.rectangle([x, y, x + width, y + height], fill=color, outline=color)

def draw_text(draw, text, x, y, color, size=FONT_SIZE_MEDIUM):
    """Draw text on the image"""
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
    except:
        font = ImageFont.load_default()
    
    draw.text((x, y), text, fill=color, font=font)
