from PIL import Image, ImageDraw, ImageFont
import os

out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'images'))
os.makedirs(out_dir, exist_ok=True)

# attempt to load a TTF font; fall back to default
def get_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        try:
            return ImageFont.truetype("DejaVuSans.ttf", size)
        except Exception:
            return ImageFont.load_default()

placeholders = [
    ("placeholder-1.png", (1200,800), "#e6f2fb", "Sistema de gestão integrado"),
    ("placeholder-2.png", (1200,800), "#fff8ea", "Portal de atendimento ao cliente"),
    ("placeholder-3.png", (1200,800), "#f3fff4", "App móvel para vendas"),
]

persons = [
    ("person-1.png", (400,400), "#f4f7fb", "Maria Silva"),
    ("person-2.png", (400,400), "#fbfbff", "João Pereira"),
    ("person-3.png", (400,400), "#fff9fb", "Ana Costa"),
]

# helper for centered text
def draw_centered_text(draw, text, font, box, fill="#334"):
    w, h = draw.textsize(text, font=font)
    x = box[0] + (box[2]-box[0]-w)/2
    y = box[1] + (box[3]-box[1]-h)/2
    draw.text((x,y), text, font=font, fill=fill)

# create placeholders
for name, size, bg, label in placeholders:
    img = Image.new('RGB', size, bg)
    draw = ImageDraw.Draw(img)
    # inner white card
    pad = 40
    inner = (pad, pad, size[0]-pad, size[1]-pad)
    draw.rectangle(inner, fill="#ffffff", outline="#dbeefc", width=2)
    # text
    font = get_font(40)
    draw_centered_text(draw, label, font, inner, fill="#4b6b86")
    path = os.path.join(out_dir, name)
    img.save(path, optimize=True)
    print("Wrote", path)

# create person avatars
for name, size, bg, label in persons:
    img = Image.new('RGB', size, bg)
    draw = ImageDraw.Draw(img)
    # head circle
    cx, cy = size[0]//2, size[1]//3
    r = min(size)//6
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill="#cfe6ff")
    # body card
    body_y = cy + r + 10
    draw.rectangle((size[0]//6, body_y, size[0]*5//6, size[1]-20), fill="#fff", outline="#e6f2fb")
    # name
    font = get_font(20)
    w, h = draw.textsize(label, font=font)
    draw.text(((size[0]-w)/2, body_y + 20), label, font=font, fill="#334")
    path = os.path.join(out_dir, name)
    img.save(path, optimize=True)
    print("Wrote", path)
