#!/usr/bin/env python3
"""Render the README "At a Glance" card as dark and light SVGs.

Experience is counted in whole months from START, so the scheduled workflow
keeps it current. Standard library only.

    python3 scripts/glance.py dist                     # writes dist/at-a-glance-{dark,light}.svg
    python3 scripts/glance.py dist --date 2026-10-25   # render as of a given day
"""

import argparse
import datetime as dt
from pathlib import Path
from xml.sax.saxutils import escape

START = dt.date(2024, 3, 1)
COMPANY = "Hansa Solutions India Pvt Ltd"
ROLE = "DevSecOps & Cloud Engineer"
OPEN_TO = [  # one list per chip row
    ["Platform Engineering", "Cloud Architecture"],
    ["DevSecOps", "DevOps Engineer", "Infra Management"],
]
CLOUD = [
    ("NETWORK", "Hub-and-spoke · Firewall"),
    ("SECURITY", "Defender · Entra ID · PIM"),
    ("GOVERN", "Landing zones · Policy"),
]
STACK = [
    ("Platform", ["Landing Zones", "Hub-and-spoke", "Entra ID", "Azure Policy", "PIM"], 1.1),
    ("IaC", ["Terraform", "Bicep", "cloud-init"], 0.75),
    ("Pipelines", ["GitHub Actions", "Azure DevOps", "OIDC federation", "SHA-pinned actions"], 1.2),
    ("Security", ["TFLint", "Trivy", "Checkov", "Gitleaks", "TruffleHog", "Defender for Cloud"], 1.15),
    ("FinOps", ["Infracost", "Retail Prices API", "Rightsizing", "Reservations"], 1.1),
    ("AIOps", ["Python", "LangGraph", "MCP servers", "RAG agents", "Claude Code management"], 1.6),
]

SANS = "Segoe UI, -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "SFMono-Regular, Consolas, Menlo, monospace"

THEMES = {
    "dark": dict(
        bg="#0B1020", border="#1C2747", card="#111A33", text="#F5F7FF", muted="#9AA7C7", soft="#C9D4F2",
        accent="#FF7A1A", accent_text="#FF7A1A", blue="#3B82F6", head="#38BDF8", track="#16213F",
        chip="#18233F", chip_stroke="#3B82F6", chip_text="#C9D4F2", ok="#3FB950",
    ),
    "light": dict(
        bg="#F7F9FD", border="#D9E2F2", card="#FFFFFF", text="#0B1020", muted="#475571", soft="#334155",
        accent="#E8630A", accent_text="#B84A00", blue="#2563EB", head="#0369A1", track="#E2E8F3",
        chip="#EAF0FA", chip_stroke="#2563EB", chip_text="#1D4ED8", ok="#1A7F37",
    ),
}

W, PAD, GAP = 900, 28, 12


def experience(today):
    months = (today.year - START.year) * 12 + today.month - START.month - (today.day < START.day)
    years, months = divmod(max(months, 0), 12)
    parts = []
    if years:
        parts.append(f"{years} {'yr' if years == 1 else 'yrs'}")
    if months or not years:
        parts.append(f"{months} {'mo' if months == 1 else 'mos'}")
    return " ".join(parts)


def text_width(s, size, bold=False):
    """Rough advance width for the sans stack; good enough to size chips."""
    em = 0.0
    for c in s:
        if c in "ijl.,:;'|!·":
            em += 0.27
        elif c in "ft-()/rI ":
            em += 0.34
        elif c in "mwMW":
            em += 0.84
        elif c.isupper():
            em += 0.66
        elif c.isdigit():
            em += 0.56
        else:
            em += 0.54
    return em * size * (1.06 if bold else 1.0)


def t(x, y, s, size, fill, family=SANS, weight=None, anchor=None, spacing=None):
    attrs = [f'x="{x:g}"', f'y="{y:g}"', f'font-family="{family}"', f'font-size="{size}"', f'fill="{fill}"']
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    return f"<text {' '.join(attrs)}>{escape(s)}</text>"


def label(x, y, s, c):
    return t(x, y, s, 11, c["muted"], MONO, spacing="1.5")


def card(x, y, w, h, c):
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="12" fill="{c["card"]}" stroke="{c["border"]}"/>'


def chips(x0, rows, c):
    out = []
    for r, items in enumerate(rows):
        x, y = x0, r * 36
        for item in items:
            w = text_width(item, 13, bold=True) + 20
            out.append(
                f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="28" rx="14" fill="{c["chip"]}" '
                f'stroke="{c["chip_stroke"]}" stroke-opacity=".45"/>'
            )
            out.append(t(round(x + w / 2, 1), y + 18.5, item, 13, c["chip_text"], weight="600", anchor="middle"))
            x += w + 8
    return out, len(rows) * 36 - 8


def render(theme, today):
    c = THEMES[theme]
    exp = experience(today)
    col = (W - 2 * PAD - 3 * GAP) / 4
    xs = [PAD + i * (col + GAP) for i in range(4)]
    span2 = 2 * col + GAP
    body = []

    # Header
    body.append(t(PAD, 47, "$ kubectl describe engineer harsh-agarwal", 13, c["accent_text"], MONO, spacing="1"))
    pill_w = text_width("Open to new roles", 12, bold=True) + 44
    px = W - PAD - pill_w
    body.append(
        f'<rect x="{px:.1f}" y="30" width="{pill_w:.1f}" height="28" rx="14" fill="{c["chip"]}" '
        f'stroke="{c["chip_stroke"]}" stroke-opacity=".45"/>'
    )
    body.append(f'<circle cx="{px + 16:.1f}" cy="44" r="4" fill="{c["ok"]}"/>')
    body.append(t(round(px + 28, 1), 48, "Open to new roles", 12, c["soft"], weight="600"))

    # Row 1: Now + Building
    y1, h1 = 70, 136
    x = xs[0] + 18
    body.append(card(xs[0], y1, span2, h1, c))
    body.append(label(x, y1 + 28, "NOW", c))
    body.append(t(x, y1 + 58, COMPANY, 20, c["text"], weight="700"))
    body.append(t(x, y1 + 82, ROLE, 14, c["muted"]))
    body.append(f'<rect x="{x}" y="{y1 + 96}" width="{span2 - 36:g}" height="1" fill="{c["border"]}"/>')
    body.append(label(x, y1 + 120, "EXPERIENCE", c))
    body.append(t(x + 96, y1 + 121, exp, 15, c["text"], weight="700"))
    right = xs[0] + span2 - 18
    since = "Mar 2024 – Present"
    body.append(t(right, y1 + 120, since, 12, c["muted"], anchor="end"))
    dot_x = right - text_width(since, 12) - 10
    body.append(f'<circle class="ping" cx="{dot_x:.1f}" cy="{y1 + 116}" r="3.5" fill="{c["ok"]}"/>')
    body.append(f'<circle cx="{dot_x:.1f}" cy="{y1 + 116}" r="3.5" fill="{c["ok"]}"/>')

    bx, bw = xs[2] + 18, span2 - 36
    body.append(card(xs[2], y1, span2, h1, c))
    body.append(f'<circle class="ping" cx="{bx + 3.5}" cy="{y1 + 24}" r="3.5" fill="{c["accent"]}"/>')
    body.append(f'<circle cx="{bx + 3.5}" cy="{y1 + 24}" r="3.5" fill="{c["accent"]}"/>')
    body.append(t(bx + 15, y1 + 28, "BUILDING", 11, c["accent_text"], MONO, spacing="1.5"))
    body.append(t(bx, y1 + 58, "ai-terraform-drift-detector", 16, c["text"], MONO, weight="600"))
    seg = (bw - 4) / 2
    by = y1 + 80
    body.append(f'<rect x="{bx}" y="{by}" width="{seg:g}" height="6" rx="3" fill="{c["blue"]}"/>')
    l2 = bx + seg + 4
    body.append(f'<clipPath id="l2"><rect x="{l2:g}" y="{by}" width="{seg:g}" height="6" rx="3"/></clipPath>')
    body.append(f'<rect x="{l2:g}" y="{by}" width="{seg:g}" height="6" rx="3" fill="{c["track"]}"/>')
    body.append(
        f'<g clip-path="url(#l2)"><rect class="scan" x="{l2 - 70:g}" y="{by}" width="70" height="6" rx="3" '
        f'fill="{c["accent"]}"/></g>'
    )
    body.append(t(bx, y1 + 108, "Level 1 · v1.0.0 shipped", 12, c["muted"]))
    body.append(t(bx + bw, y1 + 108, "Level 2 · local-first CLI · in progress", 12, c["muted"], anchor="end"))

    # Row 2: Education, Open to, Cloud (own widths: the chips and cloud details need the room)
    ex, ew = PAD, 168
    ox, ow = ex + ew + GAP, 404
    cx, cw = ox + ow + GAP, W - PAD - (ox + ow + GAP)
    chip_parts, _ = chips(ox + 18, OPEN_TO, c)
    y2 = y1 + h1 + GAP
    h2 = 18 + 14 + 10 + 3 * 22 + 30
    for x0, w0 in ((ex, ew), (ox, ow), (cx, cw)):
        body.append(card(x0, y2, w0, h2, c))
    x = ex + 18
    body.append(label(x, y2 + 28, "EDUCATION", c))
    body.append(t(x, y2 + 54, "B.Tech CSE", 17, c["text"], weight="700"))
    body.append(t(x, y2 + 76, "DIT University · 2024", 13, c["muted"]))
    body.append(
        f'<rect x="{x}" y="{y2 + 94}" width="{ew - 36}" height="30" rx="8" fill="{c["chip"]}" '
        f'stroke="{c["chip_stroke"]}" stroke-opacity=".45"/>'
    )
    body.append(t(x + 12, y2 + 113, "CGPA", 11, c["muted"], MONO, spacing="1.5"))
    body.append(t(ex + ew - 30, y2 + 114, "8.56 / 10", 15, c["text"], weight="700", anchor="end"))
    body.append(label(ox + 18, y2 + 28, "OPEN TO", c))
    body.append(f'<g transform="translate(0 {y2 + 42})">{"".join(chip_parts)}</g>')
    x = cx + 18
    body.append(label(x, y2 + 28, "PRIMARY CLOUD", c))
    body.append(t(x, y2 + 54, "Microsoft Azure", 17, c["head"], weight="700"))
    for i, (key, value) in enumerate(CLOUD):
        body.append(t(x, y2 + 80 + i * 22, key, 10, c["muted"], MONO, spacing="1"))
        body.append(t(x + 66, y2 + 80 + i * 22, value, 12.5, c["soft"]))

    # Row 3: Stack
    y3 = y2 + h2 + GAP + 2
    rows = max(len(items) for _, items, _ in STACK)
    h3 = 18 + 14 + 22 + 22 + (rows - 1) * 19 + 22
    body.append(card(PAD, y3, W - 2 * PAD, h3, c))
    body.append(label(PAD + 18, y3 + 28, "STACK", c))
    inner = W - 2 * PAD - 36
    gap = 14
    unit = (inner - gap * (len(STACK) - 1)) / sum(weight for *_, weight in STACK)
    x = PAD + 18
    for name, items, weight in STACK:
        head = c["accent_text"] if name == "AIOps" else c["head"]
        body.append(t(round(x, 1), y3 + 54, name, 13, head, weight="700"))
        for i, item in enumerate(items):
            body.append(t(round(x, 1), y3 + 76 + i * 19, item, 12.5, c["soft"]))
        x += unit * weight + gap

    h = y3 + h3 + PAD
    desc = (
        f"Now: {ROLE} at {COMPANY}, {exp} since March 2024. "
        "Building ai-terraform-drift-detector Level 2. Education: B.Tech CSE, DIT University (2024), CGPA 8.56/10. "
        f"Open to: {', '.join(sum(OPEN_TO, []))}. Primary cloud: Microsoft Azure "
        f"({'; '.join(f'{k.lower()}: {v}' for k, v in CLOUD)}). "
        + " ".join(f"{name}: {', '.join(items)}." for name, items, _ in STACK)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="title desc">
  <title id="title">Harsh Agarwal at a glance</title>
  <desc id="desc">{escape(desc)}</desc>
  <style>
    .fade {{ animation: fade .8s ease-out both; }}
    .ping {{ transform-box: fill-box; transform-origin: center; animation: ping 2.4s ease-out infinite; }}
    .scan {{ animation: scan 2.2s ease-in-out infinite; }}
    @keyframes fade {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ping {{ 0% {{ transform: scale(1); opacity: .7; }} 100% {{ transform: scale(3.2); opacity: 0; }} }}
    @keyframes scan {{ from {{ transform: translateX(0); }} to {{ transform: translateX({seg + 70:g}px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .fade, .ping, .scan {{ animation: none; }} .ping {{ opacity: 0; }} }}
  </style>
  <rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="16" fill="{c["bg"]}" stroke="{c["border"]}"/>
  <g class="fade">
    {chr(10).join("    " + part for part in body).lstrip()}
  </g>
</svg>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--date", type=dt.date.fromisoformat, default=dt.date.today())
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for theme in THEMES:
        path = args.out_dir / f"at-a-glance-{theme}.svg"
        path.write_text(render(theme, args.date), encoding="utf-8")
        print(f"wrote {path} ({experience(args.date)})")


if __name__ == "__main__":
    main()
