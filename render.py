"""Render the front page of THE WORLD TODAY for Thursday, 26 November 2026.

Deterministic: no randomness, no clock, no network. Every value is fixed,
so two runs produce byte-identical PNGs.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

CREAM = (247, 242, 231)
NAVY = (20, 38, 76)
RED = (176, 42, 48)
GOLD = (212, 160, 40)
LIGHT_BLUE = (140, 185, 220)
INK = (30, 30, 30)
GREY = (110, 110, 110)
STRIP_BG = (220, 232, 245)
WHITE = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, color, max_width, line_h):
    lines = wrap(draw, text, fnt, max_width)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += line_h
    return y


def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.text((32, 22), "THE WORLD TODAY",
           font=font(SERIF, 52), fill=WHITE)
    f_day = font(SANS_BOLD, 24)
    f_date = font(SANS_BOLD, 20)
    d.text((W - 32 - d.textlength("THURSDAY", font=f_day), 20),
           "THURSDAY", font=f_day, fill=WHITE)
    d.text((W - 32 - d.textlength("26 NOVEMBER 2026", font=f_date), 52),
           "26 NOVEMBER 2026", font=f_date, fill=WHITE)
    d.rectangle([0, 96, W, 100], fill=RED)

    # ---- Lead story (left) ----------------------------------------------
    x0 = 32
    y = 122
    d.text((x0, y), "LEAD · TRADE", font=font(SANS_BOLD, 20), fill=RED)
    y += 34
    f_head = font(SERIF, 42)
    d.text((x0, y), "US fires new tariff salvo", font=f_head, fill=INK)
    y += 52
    d.text((x0, y), "at 14 trading partners", font=f_head, fill=INK)
    y += 60
    lead_body = ("President Trump proposed new Section 301 duties on "
                 "Wednesday to fight excess factory capacity: China capped "
                 "at 20%, rising to 40% if the trade truce unravels; the "
                 "EU, Japan and South Korea at 15%.")
    y = draw_wrapped(d, x0, y, lead_body, font(SANS, 20), INK, 600, 28)

    # ---- Lead graphic (right): bar chart on navy panel ------------------
    px0, py0, px1, py1 = 668, 122, 992, 388
    d.rectangle([px0, py0, px1, py1], fill=NAVY)
    d.text((px0 + 20, py0 + 14), "TOP PROPOSED RATES",
           font=font(SANS_BOLD, 18), fill=WHITE)
    bars = [
        ("CHINA", 40, RED),
        ("VIETNAM", 35, GOLD),
        ("EU", 15, LIGHT_BLUE),
    ]
    by = py0 + 56
    f_lab = font(SANS_BOLD, 16)
    f_val = font(SANS_BOLD, 16)
    for label, pct, color in bars:
        d.text((px0 + 20, by), label, font=f_lab, fill=WHITE)
        d.text((px1 - 20 - d.textlength(f"{pct}%", font=f_val), by),
               f"{pct}%", font=f_val, fill=WHITE)
        by += 26
        bar_w = int(264 * pct / 40)
        d.rectangle([px0 + 20, by, px0 + 20 + bar_w, by + 20], fill=color)
        by += 36
    d.text((px0, py1 + 10), "Proposed maximum rates, USTR",
           font=font(SANS, 15), fill=GREY)

    # ---- Divider ----------------------------------------------------------
    d.line([32, 452, 992, 452], fill=(190, 180, 160), width=2)

    # ---- Middle stories ---------------------------------------------------
    mid_y = 472
    col_w = 464
    f_kick = font(SANS_BOLD, 17)
    f_mid_head = font(SERIF, 27)
    f_mid_body = font(SANS, 18)

    # Left: Ukraine
    mx = 32
    d.text((mx, mid_y), "UKRAINE · WAR", font=f_kick, fill=RED)
    d.text((mx, mid_y + 28), "Ukraine hits Russian", font=f_mid_head, fill=INK)
    d.text((mx, mid_y + 64), "air base; Kyiv shelled", font=f_mid_head, fill=INK)
    draw_wrapped(d, mx, mid_y + 106,
                 "Kyiv said its forces struck the Savasleyka air base on "
                 "Wednesday, damaging five planes, as Russian ballistic "
                 "missiles hit the Ukrainian capital.",
                 f_mid_body, INK, col_w, 25)

    # Right: Microsoft
    mx = 528
    d.text((mx, mid_y), "TECHNOLOGY · MICROSOFT", font=f_kick, fill=RED)
    d.text((mx, mid_y + 28), "Microsoft declares 'Code Red'", font=f_mid_head, fill=INK)
    d.text((mx, mid_y + 64), "after outage", font=f_mid_head, fill=INK)
    draw_wrapped(d, mx, mid_y + 106,
                 "After a 24-hour outage on 12–13 November, Microsoft put "
                 "reliability ahead of new features, internal memos seen "
                 "by Reuters show.",
                 f_mid_body, INK, col_w, 25)

    d.line([32, 700, 992, 700], fill=(190, 180, 160), width=2)

    # ---- Colombia strip ---------------------------------------------------
    sy0, sy1 = 720, 828
    d.rectangle([32, sy0, 992, sy1], fill=STRIP_BG)
    d.rectangle([32, sy0, 44, sy1], fill=RED)
    d.text((64, sy0 + 10), "COLOMBIA · WEDNESDAY",
           font=font(SANS_BOLD, 17), fill=RED)
    d.text((64, sy0 + 34), "All hostages freed in Cartagena siege",
           font=font(SERIF, 27), fill=INK)
    draw_wrapped(d, 64, sy0 + 72,
                 "Special forces stormed a supermarket after a 17-hour "
                 "siege, freeing the last 20 hostages; one gunman was "
                 "killed.",
                 font(SANS, 18), INK, 900, 24)

    # ---- Ticker band ------------------------------------------------------
    ty0, ty1 = 856, 940
    d.rectangle([0, ty0, W, ty1], fill=NAVY)
    ticker = ("Egypt highway fire kills 30 · Sudan drone strikes kill 19 "
              "civilians · Poland plans no-fly zone on Ukraine border · "
              "BBC appeals Trump $10bn suit · Lebanon to open second "
              "airport · US jobless claims fall · SpaceX cleared for 1m "
              "satellites")
    draw_wrapped(d, 32, ty0 + 12, ticker, font(SANS_BOLD, 19), WHITE, 960, 27)

    # ---- Footer -----------------------------------------------------------
    d.text((32, 962),
           "Stories verified against Reuters, Colombia Reports and Zotpaper "
           "· Thursday, 26 November 2026",
           font=font(SANS, 15), fill=GREY)

    return img


if __name__ == "__main__":
    build().save("entry.png")
