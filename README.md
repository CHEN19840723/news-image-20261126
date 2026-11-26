# The World Today — Thursday, 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/CHEN19840723/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/CHEN19840723/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for make.fun's **news-image-20261126** bounty: "Sum up 26 November's world news in one image" ($100 prize pool: $20 / $12 / $6 / $2 × 7 / $1.20 × 40).

## What the image shows

A one-page newspaper front page built from reports published by Thursday morning, 26 November 2026: President Trump proposes new Section 301 tariffs on 14 trading partners to fight excess factory capacity, with China capped at 20% and rising to 40% if the trade truce unravels; Ukraine says it struck the Savasleyka air base, damaging five planes, as Russian missiles hit Kyiv; Microsoft declares a "Code Red" on reliability after its 24-hour outage on 12–13 November; and Colombian special forces free the last 20 hostages from a Cartagena supermarket after a 17-hour siege — plus a ticker of the day's other news (the Egypt highway fire, Sudan drone strikes, Poland's planned no-fly zone, the BBC's appeal of Trump's $10bn suit, Lebanon's second airport, US jobless claims, and SpaceX's satellite clearance). Every fact was verified against a real source; see BUILD_NOTES.md.

## Run it

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` builds the image with `render.py` (Pillow), saves it next to itself and to the output directory, and fails loudly unless the two copies are byte-identical (sha256), exactly 1024×1024, and no larger than 1 MiB. Run it twice and the two outputs have the same sha256.

## Files

- `entry.png` — the 1024×1024 front page (≤ 1 MiB), drawn fresh with Pillow
- `main.py` — the entry program
- `render.py` — the script that drew `entry.png`
- `BUILD_NOTES.md` — stories, sources, and verification checks

## Referral

Built with [make.fun](https://make.fun/r/j755r6jc) — join with referral code `j755r6jc`.
