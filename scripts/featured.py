#!/usr/bin/env python3
"""Render the README "Featured Engineering" case-study cards as dark and light SVGs.

The content is static, so the output is committed to assets/ like the banner:

    python3 scripts/featured.py            # writes assets/featured-{drift,landing-zone}-{dark,light}.svg
"""

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

from glance import MONO, SANS, text_width

THEMES = {
    "dark": dict(
        bg="#0B1020", border="#1C2747", tile="#111A33", panel="#0D1530", node="#16213F", node_border="#26355E",
        text="#F5F7FF", muted="#9AA7C7", soft="#C9D4F2", accent="#FF7A1A", accent_text="#FF7A1A", head="#38BDF8",
        ok="#3FB950", chip="#18233F", chip_stroke="#3B82F6", focus_fill="#1C2A55", focus_stroke="#3B82F6",
        hot_fill="#2A1A0E", hot_stroke="#FF7A1A", chevron="#5B6B95",
    ),
    "light": dict(
        bg="#F7F9FD", border="#D9E2F2", tile="#FFFFFF", panel="#FFFFFF", node="#F2F6FC", node_border="#D9E2F2",
        text="#0B1020", muted="#475571", soft="#334155", accent="#E8630A", accent_text="#B84A00", head="#0369A1",
        ok="#1A7F37", chip="#EAF0FA", chip_stroke="#2563EB", focus_fill="#EAF0FA", focus_stroke="#2563EB",
        hot_fill="#FFF1E6", hot_stroke="#E8630A", chevron="#94A3B8",
    ),
}

W, PAD = 900, 28


def t(x, y, content, size, fill, family=SANS, weight=None, anchor=None, spacing=None):
    """A <text>; `content` is either a string or a list of (text, fill, weight) runs."""
    attrs = [f'x="{x:g}"', f'y="{y:g}"', f'font-family="{family}"', f'font-size="{size}"', f'fill="{fill}"']
    if weight:
        attrs.append(f'font-weight="{weight}"')
    if anchor:
        attrs.append(f'text-anchor="{anchor}"')
    if spacing:
        attrs.append(f'letter-spacing="{spacing}"')
    if isinstance(content, str):
        body = escape(content)
    else:
        body = "".join(
            f'<tspan fill="{run_fill}"{f" font-weight={chr(34)}{run_weight}{chr(34)}" if run_weight else ""}>{escape(s)}</tspan>'
            for s, run_fill, run_weight in content
        )
    return f"<text {' '.join(attrs)}>{body}</text>"


def box(x, y, w, h, fill, stroke, rx=8, stroke_opacity=None):
    op = f' stroke-opacity="{stroke_opacity}"' if stroke_opacity else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx}" fill="{fill}" stroke="{stroke}"{op}/>'


def label(x, y, s, fill):
    return t(x, y, s, 11, fill, MONO, spacing="1.5")


def chevron(x, cy, c, i):
    return (
        f'<path class="flow" style="animation-delay:{i * 0.35:.2f}s" d="M{x:g} {cy - 6:g}l6 6-6 6" fill="none" '
        f'stroke="{c["chevron"]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def check(x, cy, c):
    return (
        f'<path d="M{x:g} {cy + 0.5:g}l4.5 4.5 9-9.5" fill="none" stroke="{c["ok"]}" stroke-width="2.4" '
        f'stroke-linecap="round" stroke-linejoin="round"/>'
    )


def repo_pill(right, y, c):
    """'View repo' pill ending at x=right; the whole card is the link in the README."""
    w = text_width("View repo", 13, bold=True) + 46
    x = right - w
    return [
        box(x, y, w, 30, c["chip"], c["chip_stroke"], rx=15, stroke_opacity=".45"),
        t(x + 14, y + 20, "View repo", 13, c["soft"], weight="600"),
        f'<path d="M{x + w - 25:g} {y + 19:g}l8-8m-6 0h6v6" fill="none" stroke="{c["soft"]}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round"/>',
    ]


def frame(c, h, title, desc, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(desc)}</desc>
  <style>
    .fade {{ animation: fade .8s ease-out both; }}
    .flow {{ animation: flow 1.75s ease-in-out infinite; }}
    @keyframes fade {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes flow {{ 0%, 100% {{ opacity: .35; }} 30% {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{ .fade, .flow {{ animation: none; }} }}
  </style>
  <rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="16" fill="{c["bg"]}" stroke="{c["border"]}"/>
  <g class="fade">
    {chr(10).join("    " + part for part in body).lstrip()}
  </g>
</svg>
"""


def render_drift(theme):
    c = THEMES[theme]
    body = []
    body.append(t(PAD, 46, [
        ("FLAGSHIP", c["accent_text"], None),
        ("  /  ", c["chevron"], None),
        ("level1-v1.0.0 released · Level 2 in progress", c["muted"], None),
    ], 11, c["muted"], MONO, spacing="1.5"))
    body += repo_pill(W - PAD, 28, c)
    body.append(t(PAD, 82, "AI-Powered Terraform Drift Detection & Remediation Platform", 22, c["text"], weight="800"))
    body.append(t(PAD, 110, [
        ("Finds out when Azure no longer matches Terraform, explains ", c["muted"], None),
        ("who changed what, when, and what it costs,", c["text"], "700"),
    ], 14, c["muted"]))
    body.append(t(PAD, 130, "and raises it before it becomes an incident.", 14, c["muted"]))

    x = PAD
    for chip in ["Python", "Terraform", "Azure", "GitHub Actions", "LangGraph"]:
        w = text_width(chip, 12) + 20
        body.append(box(x, 146, w, 24, c["node"], c["node_border"], rx=6))
        body.append(t(x + w / 2, 162, chip, 12, c["soft"], anchor="middle"))
        x += w + 6

    # Flow: Azure → plan → engine → outputs → dashboard
    py, ph = 186, 146
    body.append(box(PAD, py, W - 2 * PAD, ph, c["panel"], c["border"], rx=10))
    cy = py + ph / 2
    nodes = [
        (44, 96, "Azure", "live state", c["node"], c["node_border"], None),
        (170, 140, "Scheduled plan", "GitHub Actions + OIDC", c["node"], c["node_border"], None),
        (340, 136, "Drift engine", "deterministic Python", c["focus_fill"], c["focus_stroke"], ".7"),
        (760, 96, "Dashboard", "local-first", c["hot_fill"], c["hot_stroke"], ".6"),
    ]
    for x, w, name, sub, fill, stroke, op in nodes:
        body.append(box(x, cy - 26, w, 52, fill, stroke, stroke_opacity=op))
        body.append(t(x + 10, cy - 4, name, 12.5, c["text"], weight="700"))
        body.append(t(x + 10, cy + 14, sub, 11, c["muted"] if fill == c["node"] else c["soft"]))
    outputs = [
        "GitHub Issue per drifted resource",
        "Activity Log: who / when / what",
        "LangGraph analysis (LLM opt-in)",
        "Infracost + unmanaged resources",
    ]
    oy = cy - (4 * 24 + 3 * 6) / 2
    for i, out in enumerate(outputs):
        body.append(box(506, oy + i * 30, 224, 24, c["node"], c["node_border"], rx=6))
        body.append(t(515, oy + i * 30 + 16, out, 11.5, c["soft"]))
    for i, x in enumerate([152, 322, 488, 742]):
        body.append(chevron(x, cy, c, i))

    # Proof tiles
    stats = [("2,885", "tests passing", c["ok"]), ("98.85%", "drift-engine coverage", c["head"]),
             ("135", "e2e cases, failure injection", c["text"]), ("6", "required checks on main", c["text"])]
    sy, gap = 346, 10
    sw = (W - 2 * PAD - 3 * gap) / 4
    for i, (num, what, fill) in enumerate(stats):
        x = PAD + i * (sw + gap)
        body.append(box(x, sy, sw, 64, c["tile"], c["border"], rx=10))
        body.append(t(x + 14, sy + 32, num, 24, fill, weight="800"))
        body.append(t(x + 14, sy + 52, what, 12, c["muted"]))

    # Guardrails
    guards = [
        [("OIDC trust limited to ", c["soft"], None), ("main", c["text"], "700"), (", no client secrets", c["soft"], None)],
        "Every action pinned by full commit SHA",
        "TFLint · Trivy · TruffleHog in CI",
        "Human-in-the-loop remediation, no write access",
    ]
    for i, g in enumerate(guards):
        x, y = PAD + (i % 2) * 432, 440 + (i // 2) * 24
        body.append(check(x, y - 5, c))
        body.append(t(x + 22, y, g, 13, c["soft"]))

    # Live test callout
    body.append(box(PAD, 482, W - 2 * PAD, 40, c["hot_fill"], c["hot_stroke"], rx=10, stroke_opacity=".45"))
    body.append(label(PAD + 16, 506, "LIVE TEST", c["accent_text"]))
    body.append(t(PAD + 100, 507, "Flagged 5 resources created outside Terraform in a live Azure subscription: "
                                  "≈ $44.85/mo at list price.", 13, c["text"]))

    desc = (
        "Flagship project, level1-v1.0.0 released, Level 2 in progress. Finds out when Azure no longer matches "
        "Terraform, explains who changed what, when, and what it costs, and raises it before it becomes an incident. "
        "Flow: Azure live state, scheduled plan in GitHub Actions with OIDC, deterministic Python drift engine, then a "
        "GitHub Issue per drifted resource, Activity Log attribution, LangGraph analysis (LLM opt-in) and Infracost "
        "with unmanaged resources, into a local dashboard. 2,885 tests passing, 98.85% drift-engine coverage, "
        "135 end-to-end cases with failure injection, 6 required checks on main. OIDC trust limited to main with no "
        "client secrets, actions pinned by commit SHA, TFLint, Trivy and TruffleHog in CI, human-in-the-loop "
        "remediation. A live Azure test flagged 5 resources created outside Terraform, about $44.85 a month."
    )
    return frame(c, 550, "AI-Powered Terraform Drift Detection & Remediation Platform", desc, body)


def render_landing_zone(theme):
    c = THEMES[theme]
    body = []
    left_w = 536
    body.append(label(PAD, 46, "INFRASTRUCTURE AS CODE", c["head"]))
    body += repo_pill(PAD + left_w, 28, c)
    body.append(t(PAD, 82, "Azure Infrastructure Landing Zone", 20, c["text"], weight="800"))
    body.append(t(PAD, 108, "A modular, fully automated Azure landing zone in Terraform.", 14, c["muted"]))

    modules = ["VNet", "Subnet", "App Gateway", "Load Balancer", "Bastion", "Key Vault", "VM", "Public IP",
               "Resource Group"]
    mw = (left_w - 12) / 3
    for i, name in enumerate(modules):
        x, y = PAD + (i % 3) * (mw + 6), 126 + (i // 3) * 38
        body.append(box(x, y, mw, 32, c["node"], c["node_border"], rx=6))
        body.append(t(x + mw / 2, y + 21, name, 12, c["soft"], anchor="middle"))
    body.append(t(PAD, 256, "9 reusable modules · Terraform · Azure · GitHub Actions · Gitleaks", 12, c["muted"]))

    rx = PAD + left_w + 24
    body.append(f'<rect x="{rx - 24}" y="28" width="1" height="236" fill="{c["border"]}"/>')
    body.append(label(rx, 46, "PIPELINE", c["muted"]))
    rw = W - PAD - rx
    steps = [
        ("1 · Bootstrap", "Remote state · TLS 1.2 · no public blob", False),
        ("2 · init · validate · plan", "Gitleaks secret scanning", False),
        ("3 · apply", "preprod and prod, same modules", True),
    ]
    for i, (name, sub, focus) in enumerate(steps):
        y = 60 + i * 66
        fill, stroke, op = (c["focus_fill"], c["focus_stroke"], ".7") if focus else (c["node"], c["node_border"], None)
        body.append(box(rx, y, rw, 56, fill, stroke, stroke_opacity=op))
        body.append(t(rx + 12, y + 23, name, 13, c["text"], weight="700"))
        body.append(t(rx + 12, y + 42, sub, 11.5, c["soft"] if focus else c["muted"]))

    desc = (
        "A modular, fully automated Azure landing zone in Terraform with 9 reusable modules: VNet, Subnet, "
        "Application Gateway, Load Balancer, Bastion, Key Vault, VM, Public IP and Resource Group. Pipeline: "
        "bootstrap remote state (TLS 1.2, no public blob access), then init, validate and plan with Gitleaks secret "
        "scanning, then apply to preprod and prod, which compose the same modules with their own variables."
    )
    return frame(c, 292, "Azure Infrastructure Landing Zone", desc, body)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("out_dir", type=Path, nargs="?", default=Path(__file__).resolve().parent.parent / "assets")
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, render in (("drift", render_drift), ("landing-zone", render_landing_zone)):
        for theme in THEMES:
            path = args.out_dir / f"featured-{name}-{theme}.svg"
            path.write_text(render(theme), encoding="utf-8")
            print(f"wrote {path}")


if __name__ == "__main__":
    main()
