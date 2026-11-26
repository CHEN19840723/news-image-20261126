# Build notes — news-image-20261126

Front page "THE WORLD TODAY", Thursday 26 November 2026. Four main stories
plus a seven-item ticker. Every fact below was checked against the linked
source before it went on the page.

## 1. Lead — US fires new tariff salvo at 14 trading partners

President Trump proposed new Section 301 duties on Wednesday, 25 November,
to fight excess factory capacity. China is capped at 20% on top of the
roughly 25% first-term duties, rising to 40% if the trade truce — which
expires 10 January — unravels. Vietnam faces 20% with a deal or 35%
without; India 17% with a deal or 25% without; the EU, Japan, South Korea,
Taiwan and Switzerland 15%. A hearing is set for 25 January 2027. The
Section 301 route follows the Supreme Court striking down the
emergency-powers duties in February. The chart on the page shows the
proposed maximum rates: China 40%, Vietnam 35%, EU 15%.

Source: Reuters via Kitco —
https://www.kitco.com/news/off-the-wire/2026-11-25/trump-unveils-new-tariffs-fight-excess-factory-capacity-undeterred

## 2. Ukraine — Ukraine hits Russian air base; Kyiv shelled

Kyiv said its forces struck the Savasleyka air base in Nizhny Novgorod
Oblast overnight on 24–25 November, damaging five planes. Russian ballistic
missiles hit the Ukrainian capital on Wednesday. Russian drones killed at
least seven people across six Ukrainian regions overnight.

Sources: Reuters world news summary —
https://www.devdiscourse.com/article/international/4012300-reuters-world-news-summary
and https://zot.news/world

## 3. Technology — Microsoft declares "Code Red" after outage

After a 24-hour global outage on 12–13 November hit Exchange Online,
Outlook, Teams and Copilot — the worst email outage in the service's
history — Microsoft put reliability ahead of new features, internal memos
seen by Reuters show. The cause was an undetected Windows scalability
defect from July, not a cyberattack. The overhaul runs across five
workstreams, with a target of worldwide recovery within one hour.

Sources: Reuters via Slashdot —
https://developers.slashdot.org/index2.pl?fhfilter=microsoft
and CoinStats —
https://coinstats.app/news/76b0d5cd65d62494d9b1502a863d11b9edb244e6ccb25f49c2d586988994a59f_Microsofts-24hour-service-outage-prompts-Code-Red-overhaul/

## 4. Colombia — All hostages freed in Cartagena siege

The siege began on Tuesday morning, when gunmen failed to rob an armoured
car and took about 30 people hostage at an Éxito supermarket in Cartagena,
demanding COP 7 billion (about $2 million). About ten hostages were
released on Tuesday. Special forces stormed the supermarket early on
Wednesday after a 17-hour siege, freeing the last 20 hostages; one gunman
was killed and four were detained.

Sources:
https://colombiareports.com/colombias-special-forces-liberate-hostages-cartagena-supermarket/
and
https://newsradio967.iheart.com/content/2026-11-25-colombia-supermarket-hostages-rescued-in-cartagena/

## Ticker

- Egypt highway fire kills 30, injures 25, on the Greater Cairo ring road
  (Zotpaper — https://zot.news/world)
- Sudan drone strikes kill 19 civilians in the southeast, rights group
  (Reuters — https://reuters.buzzing.cc/en/)
- Poland plans a no-fly zone on the Ukraine border by early 2027 (Zotpaper)
- BBC appeals Trump's $10bn defamation suit at the 11th Circuit (Zotpaper)
- Lebanon to open a second airport next month (Reuters summary)
- US weekly jobless claims fell more than expected (Reuters)
- US authorized SpaceX to deploy 1 million satellites for data centers in
  space (Reuters)

## A note on dating

This page was built on Thursday morning, when the UTC day was only about
20 minutes old, so the freshest items are the ones reported on Wednesday —
and they are labelled Wednesday where that is when they happened (the
tariffs, the Ukraine strikes, the Cartagena rescue). The Microsoft story
was reported on Tuesday. Nothing dated before 24 November is presented as
26 November news. Yesterday's stories — Shenzhou-24, the Huawei verdict,
the Houthi strike on Riyadh, the Gulf of Finland confirmation — are not
repeated. BepiColombo's Mercury arrival was 21 November, announced
23 November, so it is left out as stale.

## Verification

- `main.py` run twice into two different output directories: both runs
  produced byte-identical `entry.png` (sha256
  0aeffa1ea44856e79dd5bcf61170d8a63e42feb01f6ab2252bfecec6dcad438f).
- Output is 1024×1024, 131,437 bytes (under the 1 MiB limit).
- The rendered page was viewed and checked: no text crosses a divider
  line or runs outside its box. (The first render had the Ukraine
  headline running into the Microsoft column; the headline was re-split
  and the middle-headline size reduced, then re-verified.)
