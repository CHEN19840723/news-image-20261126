# The World Today — Thursday, 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/CHEN19840723/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/CHEN19840723/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for make.fun's **news-image-20261126** bounty: "Sum up 26 November's world news in one image" ($100 prize pool: $20 / $12 / $6 / $2 × 7 / $1.20 × 40).

## What the image shows

Built from reports published by Thursday morning, 26 November 2026: President Trump proposes new Section 301 tariffs on 14 trading partners — China capped at 20%, rising to 40% if the trade truce unravels, the EU, Japan and South Korea at 15%; Ukraine strikes Russia's Savasleyka air base, damaging five planes, as Russian ballistic missiles hit Kyiv; Microsoft declares a "Code Red" overhaul after its 24-hour global outage on 12–13 November; and Colombian special forces free the last 20 hostages from a Cartagena supermarket after a 17-hour siege — plus a ticker of the day so far (Egypt highway fire kills 30, Sudan drone strikes kill 19 civilians, Poland's planned no-fly zone, the BBC's appeal against Trump's $10bn suit, Lebanon's second airport, US jobless claims falling, and SpaceX cleared for 1m satellites). Every fact was verified against a real source; see BUILD_NOTES.md.

## Run it

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) draws `entry.png` with
`render.py` and fails loudly unless the two copies are byte-identical
(sha256). Run it twice and the two outputs have the same sha256.

## Files

- `entry.png` — the 1024×1024 front page (≤ 1 MiB), drawn fresh with PIL
- `main.py` — the entry program
- `render.py` — the script that drew `entry.png`
- `BUILD_NOTES.md` — stories, sources, and verification checks

## Referral

Built with [make.fun](https://make.fun/r/j755r6jc) — join with referral code `j755r6jc`.
