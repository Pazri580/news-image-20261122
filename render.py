# Draws the newspaper front page for Sunday 22 November 2026 and saves it
# as entry.png (1024x1024 RGB). All art is drawn in code with Pillow; no
# external images, no photographs, no copied artwork. Run:
#   python3 render.py
# and it writes entry.png beside this file.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (26, 26, 26)
RED = (178, 38, 30)
NAVY = (31, 58, 95)
BLUE = (52, 110, 168)
GREEN = (74, 140, 82)
LIGHT = (233, 226, 208)
GREY = (110, 104, 90)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w, word by word."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, max_w, fill, spacing=6):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def letter_spaced(draw, cx, y, text, fnt, fill, extra=4):
    """Draw text centred on cx with extra space between letters."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + extra * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + extra


def globe(draw, cx, cy, r):
    """A simple globe: blue disc, green land blobs, latitude arcs."""
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE, outline=NAVY, width=3)
    # land blobs
    draw.ellipse([cx - r * 0.62, cy - r * 0.55, cx - r * 0.05, cy - r * 0.05], fill=GREEN)
    draw.ellipse([cx + r * 0.08, cy + r * 0.05, cx + r * 0.62, cy + r * 0.55], fill=GREEN)
    draw.ellipse([cx - r * 0.15, cy + r * 0.42, cx + r * 0.35, cy + r * 0.72], fill=GREEN)
    # latitude arcs
    for k, ry in ((0.55, r * 0.55), (0.0, r * 0.92), (-0.55, r * 0.55)):
        y = cy + k * r
        half = (r * r - (k * r) ** 2) ** 0.5
        draw.arc([cx - half, y - ry, cx + half, y + ry], 0, 180, fill=(255, 255, 255), width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=2)
    draw.arc([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], 90, 270, fill=(255, 255, 255), width=2)
    draw.arc([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], 270, 90, fill=(255, 255, 255), width=2)


def thermometer(draw, x, y, w, h):
    """A red thermometer, mercury near the top."""
    bulb_r = w
    # stem
    draw.rounded_rectangle([x + w // 2 - 7, y, x + w // 2 + 7, y + h - bulb_r], radius=7, fill=(255, 255, 255), outline=INK, width=2)
    # mercury in stem (high)
    draw.rounded_rectangle([x + w // 2 - 4, y + 14, x + w // 2 + 4, y + h - bulb_r], radius=4, fill=RED)
    # bulb
    draw.ellipse([x, y + h - 2 * bulb_r, x + 2 * bulb_r, y + h], fill=RED, outline=INK, width=2)
    # tick marks
    for i in range(5):
        ty = y + 12 + i * (h - bulb_r - 24) // 4
        draw.line([x + w // 2 + 10, ty, x + w // 2 + 18, ty], fill=INK, width=2)


def seismo(draw, x, y, w, h):
    """A seismograph trace over cracked ground."""
    mid = y + h // 2
    draw.line([x, mid, x + w, mid], fill=GREY, width=1)
    pts = []
    n = 26
    for i in range(n + 1):
        px = x + i * w // n
        if i in (9, 10, 11, 12, 13, 14):
            amp = (h // 2 - 6) * (1 if i % 2 else -1) * (0.5 + 0.5 * ((i * 7) % 3) / 2)
        elif i in (7, 8, 15, 16):
            amp = (h // 4) * (1 if i % 2 else -1)
        else:
            amp = 2 * (1 if i % 2 else -1)
        pts.append((px, mid + amp))
    draw.line(pts, fill=RED, width=3, joint="curve")
    # cracked ground
    gy = y + h - 8
    draw.line([x, gy, x + w, gy], fill=INK, width=2)
    draw.line([x + w // 3, gy, x + w // 3 + 8, gy + 7], fill=INK, width=2)
    draw.line([x + 2 * w // 3, gy, x + 2 * w // 3 - 8, gy + 7], fill=INK, width=2)


def phone_ban(draw, x, y, w, h):
    """A phone handset with a red prohibition ring, and a signal tower."""
    # tower
    tx = x + 14
    draw.line([tx, y + h - 6, tx + 16, y + 6], fill=INK, width=3)
    draw.line([tx + 16, y + 6, tx + 32, y + h - 6], fill=INK, width=3)
    draw.line([tx + 2, y + h - 14, tx + 30, y + h - 14], fill=INK, width=3)
    for r in (10, 18, 26):
        draw.arc([tx + 16 - r, y + 6 - r, tx + 16 + r, y + 6 + r], 300, 240, fill=BLUE, width=2)
    # phone
    px = x + w - 66
    draw.rounded_rectangle([px, y + 4, px + 44, y + h - 4], radius=8, fill=(255, 255, 255), outline=INK, width=3)
    draw.rectangle([px + 8, y + 12, px + 36, y + h - 16], fill=NAVY)
    draw.line([px + 18, y + h - 10, px + 26, y + h - 10], fill=INK, width=2)
    # prohibition ring over the phone
    cx, cy, r = px + 22, y + h // 2, 30
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED, width=5)
    draw.line([cx - r * 0.7, cy + r * 0.7, cx + r * 0.7, cy - r * 0.7], fill=RED, width=5)


def submarine(draw, x, y, w, h):
    """A submarine above wavy sea lines."""
    # sea
    for i, wy in enumerate((y + h - 16, y + h - 8)):
        pts = []
        for px in range(x, x + w + 1, 12):
            pts.append((px, wy + (4 if (px // 12) % 2 else -4)))
        draw.line(pts, fill=BLUE, width=2)
    # hull
    hx, hy = x + 30, y + 12
    hw, hh = w - 60, 30
    draw.rounded_rectangle([hx, hy, hx + hw, hy + hh], radius=15, fill=NAVY)
    draw.polygon([(hx + hw - 14, hy + hh), (hx + hw + 16, hy + hh + 8), (hx + hw - 2, hy + hh)], fill=NAVY)
    # conning tower + periscope
    draw.rectangle([hx + hw // 2 - 14, hy - 14, hx + hw // 2 + 14, hy + 4], fill=NAVY)
    draw.line([hx + hw // 2 + 8, hy - 14, hx + hw // 2 + 8, hy - 24], fill=INK, width=3)
    # portholes
    for i in range(4):
        px = hx + 26 + i * (hw - 52) // 3
        draw.ellipse([px - 5, hy + hh // 2 - 5, px + 5, hy + hh // 2 + 5], fill=(255, 255, 255), outline=INK, width=1)


def cricket(draw, x, y, w, h):
    """Stumps, a bat and a red ball."""
    # stumps
    sx = x + 26
    for i in range(3):
        draw.line([sx + i * 12, y + 10, sx + i * 12, y + h - 14], fill=(222, 178, 90), width=5)
    draw.line([sx + 2, y + 6, sx + 10, y + 6], fill=(222, 178, 90), width=4)
    draw.line([sx + 14, y + 6, sx + 22, y + 6], fill=(222, 178, 90), width=4)
    # bat: a flat blade with a handle, leaning on the stumps
    bx = x + w - 88
    draw.polygon([(bx, y + h - 6), (bx + 30, y + h - 6), (bx + 38, y + 30), (bx + 8, y + 30)], fill=(222, 178, 90), outline=INK, width=2)
    draw.line([bx + 23, y + 30, bx + 32, y + 8], fill=INK, width=6)
    # ball
    draw.ellipse([x + w // 2 - 12, y + h - 26, x + w // 2 + 12, y + h - 2], fill=RED, outline=INK, width=2)
    draw.arc([x + w // 2 - 12, y + h - 26, x + w // 2 + 12, y + h - 2], 200, 340, fill=(255, 255, 255), width=2)


def story_card(draw, x, y, w, h, kicker, headline, body, art):
    """One small story: an illustration band on top, then headline and body."""
    draw.rectangle([x, y, x + w, y + h], outline=INK, width=1)
    # art band
    draw.rectangle([x + 1, y + 1, x + w - 1, y + 60], fill=LIGHT)
    art(draw, x + 14, y + 4, w - 28, 52)
    draw.line([x, y + 60, x + w, y + 60], fill=INK, width=1)
    tx = x + 14
    ty = y + 70
    draw.text((tx, ty), kicker, font=font(SANS_BOLD, 13), fill=RED)
    ty += 20
    ty = draw_wrapped(draw, tx, ty, headline, font(SANS_BOLD, 21), w - 28, INK, spacing=3)
    ty += 4
    draw_wrapped(draw, tx, ty, body, font(SANS, 15), w - 28, INK, spacing=4)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28
    CW = W - 2 * M  # 968

    # ---- masthead ----
    d.text((W // 2, 30), "THE WORLD IN ONE PAGE", font=font(SERIF_BOLD, 56),
           fill=INK, anchor="ma")
    letter_spaced(d, W // 2, 100, "SUNDAY 22 NOVEMBER 2026", font(SANS_BOLD, 19), RED, extra=5)
    d.line([M, 130, W - M, 130], fill=INK, width=2)
    d.line([M, 134, W - M, 134], fill=INK, width=1)

    # ---- lead story: COP31 ----
    ly = 146
    d.text((M, ly), "CLIMATE  •  ANTALYA, TURKEY", font=font(SANS_BOLD, 14), fill=RED)
    hl = "COP31 talks run into overtime as fossil fuels divide the summit"
    hy = draw_wrapped(d, M, ly + 24, hl, font(SANS_BOLD, 33), 580, INK, spacing=4)
    body = (
        "Negotiators in Antalya worked past their Friday deadline into a second "
        "day of overtime on Sunday, after a draft deal stripped out every mention "
        "of coal, oil and gas. A third draft, released in the early hours of Sunday, "
        "points back to the COP28 pledge to move away from fossil fuels — but sets "
        "no firm date. Around 130 countries demand phase-out language; Saudi Arabia "
        "and other oil producers oppose it. A $120bn target for adaptation finance "
        "was also dropped."
    )
    draw_wrapped(d, M, hy + 6, body, font(SANS, 16), 580, INK, spacing=5)
    # lead illustration panel
    px, py, pw, ph = 640, 146, 356, 300
    d.rectangle([px, py, px + pw, py + ph], fill=LIGHT, outline=INK, width=1)
    globe(d, px + 118, py + 118, 92)
    thermometer(d, px + 262, py + 52, 34, 190)
    d.text((px + 24, py + 232), "OVERTIME", font=font(SANS_BOLD, 20), fill=RED)
    d.text((px + 24, py + 260), "Day 2 past the deadline —",
           font=font(SANS, 15), fill=INK)
    d.text((px + 24, py + 280), "no deal yet in Antalya.",
           font=font(SANS, 15), fill=INK)
    d.line([M, 458, W - M, 458], fill=INK, width=2)

    # ---- rows of two stories ----
    col_w = (CW - 16) // 2
    y2 = 470
    story_card(d, M, y2, col_w, 220,
               "EARTHQUAKE  •  MYANMAR",
               "Magnitude 4.1 quake shakes Myanmar in the early hours",
               "A magnitude 4.1 earthquake struck Myanmar at 02:35 local time on "
               "Sunday, India's National Centre for Seismology said. The tremor was "
               "95 km deep. No damage or casualties were reported.",
               seismo)
    story_card(d, M + col_w + 16, y2, col_w, 220,
               "TECH  •  WASHINGTON",
               "China condemns US ban on its telecoms firms",
               "China said on Sunday it firmly opposes a US decision to bar Chinese "
               "telecom companies from direct access to American phone numbers — "
               "the latest step in a widening technology rift.",
               phone_ban)
    y3 = 702
    story_card(d, M, y3, col_w, 220,
               "DEFENCE  •  CANBERRA",
               "Australia hits back at US report on AUKUS submarines",
               "Australia's defence minister criticised a US budget office report "
               "on Sunday, after it said AUKUS would leave the US Navy with fewer "
               "attack submarines. Canberra called it wrong.",
               submarine)
    story_card(d, M + col_w + 16, y3, col_w, 220,
               "CRICKET  •  WELLINGTON",
               "Pant ton powers India to record total in New Zealand",
               "Rishabh Pant's century carried India to 629 for 6 in Wellington on "
               "Sunday — their highest Test total in New Zealand. The tourists led "
               "by 261 runs on day four of the first Test.",
               cricket)

    # ---- ticker ----
    ty = 934
    d.rectangle([M, ty, W - M, ty + 56], fill=INK)
    ticker = (
        "ATP FINALS: Alcaraz meets Zverev in Sunday's title decider in Turin    •    "
        "GERMANY: IG Metall calls a 24-hour strike for Monday    •    "
        "NORTH KOREA: Pyongyang marathon moved to October 2027"
    )
    tfont = font(SANS_BOLD, 16)
    lines = wrap(d, ticker, tfont, CW - 32)
    yy = ty + 7
    for line in lines:
        d.text((W // 2, yy), line, font=tfont, fill=(255, 255, 255), anchor="ma")
        yy += 21

    img.save("entry.png", format="PNG")
    print("saved entry.png")


if __name__ == "__main__":
    main()
