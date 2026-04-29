from PIL import Image, ImageDraw
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
from styles import *
from components import *

def create_home_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Balance Card
    draw_card(draw, 20, 60, 350, 120, CARD_COLOR)
    draw_text(draw, "Balance: $12.45", 40, 90, TEXT_COLOR)
    draw_text(draw, "1,245 pts", 40, 120, TEXT_COLOR)

    # Buttons
    draw_card(draw, 20, 200, 160, 60, ACCENT)
    draw_text(draw, "Earn Now", 50, 220, TEXT_COLOR)

    draw_card(draw, 210, 200, 160, 60, CARD_COLOR)
    draw_text(draw, "Cash Out", 240, 220, TEXT_COLOR)

    # Quick Earn Section
    draw_text(draw, "Quick Earn", 20, 300, TEXT_COLOR, FONT_SIZE_LARGE)

    options = ["Videos", "Surveys", "Games", "Tasks"]
    y = 340
    for opt in options:
        draw_card(draw, 20, y, 350, 60, CARD_COLOR)
        draw_text(draw, opt, 40, y+20, TEXT_COLOR)
        y += 80

    img.save("home_screen.png")
    print("✓ home_screen.png created")

def create_wallet_screen():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    draw_text(draw, "Wallet", 20, 40, TEXT_COLOR, FONT_SIZE_LARGE)
    draw_text(draw, "Balance: $12.45", 20, 80, TEXT_COLOR)

    methods = ["PayPal", "Cash App", "Bank"]
    y = 150
    for m in methods:
        draw_card(draw, 20, y, 350, 60, CARD_COLOR)
        draw_text(draw, m, 40, y+20, TEXT_COLOR)
        y += 80

    img.save("wallet_screen.png")
    print("✓ wallet_screen.png created")

if __name__ == "__main__":
    create_home_screen()
    create_wallet_screen()
    print("\nScreens generated successfully!")
