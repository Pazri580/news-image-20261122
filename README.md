# news-image-20261122 — "THE WORLD IN ONE PAGE"

A one-page newspaper front page summing up Sunday 22 November 2026's
world news, drawn entirely in code with Pillow. Masthead "THE WORLD IN ONE
PAGE", dated "Sunday 22 November 2026".

## The five stories

1. **COP31 talks run into overtime as fossil fuels divide the summit** (lead,
   Antalya) — Negotiations ran past their Friday deadline into a second day
   of overtime on Sunday; a third draft released in the early hours of Sunday
   points back to the COP28 pledge to move away from fossil fuels but sets no
   firm date; ~130 countries demand phase-out language, Saudi Arabia and oil
   producers oppose it; a $120bn adaptation-finance target was dropped.
   Sources: Reuters, AP, KLSE Screener, IndiaVerve.
2. **Magnitude 4.1 quake shakes Myanmar in the early hours** — Struck at
   02:35 local time on Sunday, 95 km deep, epicentre in the north-west; no
   damage or casualties reported. Source: India's National Centre for
   Seismology, via ANI.
3. **China condemns US ban on its telecoms firms** — Beijing said on Sunday
   it firmly opposes the FCC vote barring Chinese telecom companies from
   direct access to US phone numbers. Source: Reuters, 22 Nov.
4. **Australia hits back at US report on AUKUS submarines** — Defence
   Minister Richard Marles criticised a US Congressional Budget Office report
   on Sunday saying AUKUS would leave the US Navy with fewer attack
   submarines. Source: Reuters, 22 Nov.
5. **Pant ton powers India to record total in New Zealand** — Rishabh Pant's
   century carried India to 629 for 6 in Wellington, their highest Test total
   in New Zealand, leading by 261 on day four. Source: Reuters, 22 Nov.

Ticker: ATP Finals — Alcaraz meets Zverev in Sunday's title decider in
Turin; Germany — IG Metall calls a 24-hour strike for Monday; North Korea —
Pyongyang marathon moved to October 2027.

Every story was verified by web search as having happened, or first been
reported, on Sunday 22 November 2026. Stories first reported on 21 November
or earlier (Bahrain attack, El Chapo Isidro capture, Al-Shabaab ambush of
26 October, Norway's 13 November court ruling, Kenya's 11 November Ebola
discharge, the FBI database breach, the Hormuz plan, the Kryvyi Rih strike,
Voyager 1's light-day, the Lisbon march, the UN killer-robots talks, the
Basra fire) were checked and left out. See news22-log-2026-11-22.md.

## Files

- `entry.png` — the image, 1024x1024 RGB PNG, 145,454 bytes.
- `render.py` — the Pillow script that draws it (run `python3 render.py`
  to regenerate entry.png). All art is drawn in code; no external images.
- `main.py` — the entrypoint (Python 3.13, standard library only): copies
  entry.png to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and
  verifies the copy by sha256. Deterministic: two runs write identical bytes.

## Run

```
python3 render.py          # regenerate entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
