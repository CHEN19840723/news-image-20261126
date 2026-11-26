"""Draw the 26 November 2026 front page (1024x1024) with Pillow.

No network, no randomness: the same run always produces the same PNG.
Run directly (`python3 render.py`) to write entry.png next to this file.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

NAVY = (22, 35, 63)
NAVY_LIGHT = (31, 48, 84)
RED = (178, 34, 34)
CREAM = (247, 243, 232)
INK = (24, 24, 24)
GREY = (90, 90, 90)
STRIP_BG = (232, 238, 246)
GOLD = (232, 164, 32)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw a wrapped paragraph; returns the y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def draw_tariff_chart(draw, bx, by, bw, bh):
    """Bar chart of the top proposed tariff rates, in box (bx, by, bw, bh)."""
    draw.rectangle([bx, by, bx + bw, by + bh], fill=NAVY_LIGHT)
    d = draw
    # title inside chart
    d.text((bx + 16, by + 12), "TOP PROPOSED RATES",
           font=font(SANS_BOLD, 18), fill=(255, 255, 255))
    base = by + bh - 52
    bars = [("CHINA", 40, RED), ("VIETNAM", 35, GOLD), ("EU", 15, (120, 160, 210))]
    max_h = 96
    slot = bw // 3
    for i, (label, rate, color) in enumerate(bars):
        h = int(max_h * rate / 40)
        x0 = bx + i * slot + 22
        x1 = bx + (i + 1) * slot - 22
        d.rectangle([x0, base - h, x1, base], fill=color)
        d.text(((x0 + x1) // 2, base - h - 26), f"{rate}%",
               font=font(SANS_BOLD, 22), fill=(255, 255, 255),
               anchor="ma")
        d.text(((x0 + x1) // 2, base + 8), label,
               font=font(SANS_BOLD, 16), fill=(255, 255, 255),
               anchor="ma")
    d.line([(bx + 12, base), (bx + bw - 12, base)], fill=(255, 255, 255),
           width=2)


def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    d.rectangle([0, 0, W, 110], fill=NAVY)
    d.text((36, 30), "THE WORLD TODAY",
           font=font(SERIF, 52), fill=(255, 255, 255))
    d.text((988, 24), "THURSDAY", font=font(SANS_BOLD, 32),
           fill=(255, 255, 255), anchor="ra")
    d.text((988, 62), "26 NOVEMBER 2026", font=font(SANS_BOLD, 24),
           fill=(200, 205, 220), anchor="ra")
    d.rectangle([0, 110, W, 118], fill=RED)

    # ---- lead story ----------------------------------------------------
    d.text((36, 142), "LEAD  \u00b7  TRADE", font=font(SANS_BOLD, 21),
           fill=RED)
    d.text((36, 172), "US fires new tariff salvo",
           font=font(SERIF, 46), fill=INK)
    d.text((36, 224), "at 14 trading partners",
           font=font(SERIF, 46), fill=INK)
    lead_body = (
        "President Trump proposed new Section 301 duties on Wednesday "
        "to fight excess factory capacity: China capped at 20%, rising "
        "to 40% if the trade truce unravels; the EU, Japan and South "
        "Korea at 15%.")
    para(d, 36, 292, lead_body, font(SANS, 23), 622, 32)

    draw_tariff_chart(d, 700, 142, 288, 216)
    d.text((700, 368), "Proposed maximum rates, USTR",
           font=font(SANS_ITALIC, 19), fill=(70, 80, 105))

    d.line([(36, 442), (988, 442)], fill=(190, 180, 160), width=2)

    # ---- two middle stories --------------------------------------------
    col_y = 462
    d.text((36, col_y), "UKRAINE  \u00b7  WAR",
           font=font(SANS_BOLD, 20), fill=RED)
    d.text((36, col_y + 28), "Ukraine hits Russian",
           font=font(SERIF, 30), fill=INK)
    d.text((36, col_y + 64), "air base; Kyiv shelled",
           font=font(SERIF, 30), fill=INK)
    ukraine = (
        "Kyiv said its forces struck the Savasleyka air base on "
        "Wednesday, damaging five planes, as Russian ballistic "
        "missiles hit the Ukrainian capital.")
    para(d, 36, col_y + 112, ukraine, font(SANS, 21), 448, 30)

    d.text((520, col_y), "TECHNOLOGY  \u00b7  MICROSOFT",
           font=font(SANS_BOLD, 20), fill=RED)
    d.text((520, col_y + 28), "Microsoft declares",
           font=font(SERIF, 30), fill=INK)
    d.text((520, col_y + 64), "\u201cCode Red\u201d after outage",
           font=font(SERIF, 30), fill=INK)
    msft = (
        "After a 24-hour outage on 12\u201313 November, Microsoft put "
        "reliability ahead of new features, internal memos seen by "
        "Reuters show.")
    para(d, 520, col_y + 118, msft, font(SANS, 22), 468, 31)

    d.line([(36, 706), (988, 706)], fill=(190, 180, 160), width=2)

    # ---- Colombia strip --------------------------------------------------
    d.rectangle([36, 724, 988, 838], fill=STRIP_BG)
    d.rectangle([36, 724, 50, 838], fill=RED)
    d.text((70, 738), "COLOMBIA  \u00b7  WEDNESDAY",
           font=font(SANS_BOLD, 20), fill=RED)
    d.text((70, 766), "All hostages freed in Cartagena siege",
           font=font(SERIF, 30), fill=INK)
    strip_body = (
        "Special forces stormed a supermarket after a 17-hour siege, "
        "freeing the last 20 hostages; one gunman was killed.")
    para(d, 70, 806, strip_body, font(SANS, 19), 900, 26)

    # ---- ticker ----------------------------------------------------------
    d.rectangle([0, 856, W, 972], fill=NAVY)
    ticker = (
        "Egypt highway fire kills 30 \u00b7 Sudan drone strikes kill "
        "19 civilians \u00b7 Poland plans no-fly zone on Ukraine "
        "border \u00b7 BBC appeals Trump $10bn suit \u00b7 Lebanon to "
        "open second airport \u00b7 US jobless claims fall \u00b7 "
        "SpaceX cleared for 1m satellites")
    para(d, 28, 864, ticker, font(SANS_BOLD, 19), 968, 27,
         color=(255, 255, 255))

    # ---- footer ----------------------------------------------------------
    d.text((36, 986),
           "Stories verified against Reuters, Colombia Reports and "
           "Zotpaper  \u00b7  Thursday, 26 November 2026",
           font=font(SANS, 17), fill=GREY)
    return img


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "entry.png")
    build().save(out, "PNG")
    print("wrote", out)
