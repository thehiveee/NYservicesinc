#!/usr/bin/env python3
"""Build the deployable static site in site/ from the canvas artboards in canvas/.

The canvas/*.dc.html files are the source of truth: they are Design Component
artboards that run inside Claude's Design canvas. This script turns them into
plain HTML that any static host will serve:

  - resolves the {{token}} colour/brand holes to literal values
  - lifts <helmet> into <head> and unwraps <x-dc>
  - drops the Design runtime script block and ./support.js
  - rewrites /_blob/<id> asset URLs to ../assets/*.png
  - rewrites Page.dc.html links to page.html
  - replaces the templated issue picker with CSS-only radio buttons
  - drops the exit-intent pop-up (see README)

Run:  python3 tools/build_site.py
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
CANVAS = os.path.join(REPO, 'canvas')
SITE = os.path.join(REPO, 'site')

# ---------------------------------------------------------------- brand
PHONE = '718-551-2029'
PRIMARY = '#ED1C24'      # logo red
SECONDARY = '#346699'    # logo blue
DARK = '#0D1B2A'         # deep navy ground


def shift(hex_colour, amount):
    m = re.match(r'^#?([0-9a-fA-F]{6})$', hex_colour.strip())
    if not m:
        return hex_colour
    n = int(m.group(1), 16)
    out = []
    for c in ((n >> 16) & 255, (n >> 8) & 255, n & 255):
        v = c + (255 - c) * amount if amount >= 0 else c * (1 + amount)
        out.append(max(0, min(255, round(v))))
    return '#' + ''.join('%02x' % c for c in out).upper()


def rgba(hex_colour, alpha):
    n = int(hex_colour.lstrip('#'), 16)
    return 'rgba(%d,%d,%d,%s)' % ((n >> 16) & 255, (n >> 8) & 255, n & 255, alpha)


TOKENS = {
    'phone': PHONE,
    'name': 'NY HVAC Services',
    'primary': PRIMARY,
    'secondary': SECONDARY,
    'dark': DARK,
    'panelDark': shift(DARK, 0.07),
    'footerDark': shift(DARK, -0.35),
    'primaryDeep': shift(PRIMARY, -0.14),
    'primaryOnLight': shift(PRIMARY, -0.3),
    'primaryOnDark': shift(PRIMARY, 0.42),
    'secondaryOnLight': shift(SECONDARY, -0.28),
    'secondaryOnDark': shift(SECONDARY, 0.45),
    'ringColor': rgba(PRIMARY, '0.3'),
}

BLOB_LIGHT = '/_blob/8d207415a19d3d7a8982fb6d297ef543'
BLOB_DARK = '/_blob/f7bc8f1261a409b0d3f3b2c18c9ffece'

# artboard -> output file. The phone artboard is the same page at 390px, so the
# responsive build covers it and it is not emitted separately.
PAGES = [
    ('NYHVACServices', 'index.html', 'NY HVAC Services — Heating, Cooling &amp; Plumbing in Brooklyn, Queens &amp; Manhattan',
     'Family owned for nearly 30 years. 24-hour emergency heating, cooling and plumbing across Brooklyn, Queens and Manhattan. Call 718-551-2029.'),
    ('Heating', 'heating.html', 'Heating Repair &amp; Installation — NY HVAC Services',
     'Furnace repair, boiler services and emergency heating across Brooklyn, Queens and Manhattan. Answered 24 hours a day.'),
    ('AirConditioning', 'air-conditioning.html', 'Air Conditioning Repair &amp; Installation — NY HVAC Services',
     'AC repair, installation and emergency cooling service in Brooklyn, Queens and Manhattan. Every major brand serviced.'),
    ('Plumbing', 'plumbing.html', 'Plumbing, Drains &amp; Sewer Lines — NY HVAC Services',
     'Emergency plumbing, water heaters, drain cleaning, sewer lines and hydro jetting. One crew for HVAC and plumbing.'),
    ('Commercial', 'commercial.html', 'Commercial HVAC &amp; Plumbing — NY HVAC Services',
     'Commercial heating, cooling and plumbing for restaurants, retail, offices and buildings, scheduled around your opening hours.'),
    ('About', 'about.html', 'About Us — NY HVAC Services',
     'A local, family owned and operated business serving Brooklyn for nearly three decades.'),
    ('Financing', 'financing.html', 'Financing — NY HVAC Services',
     'No-interest and low monthly payment options with a fast online credit decision.'),
    ('Coupons', 'coupons.html', 'Coupons &amp; Current Offers — NY HVAC Services',
     'Seasonal offers on service calls, tune-ups and installations. Mention the offer when you call.'),
    ('Maintenance', 'maintenance.html', 'Maintenance Program — NY HVAC Services',
     'Scheduled seasonal service on the heating and the cooling, so small faults are found early.'),
    ('Contact', 'contact.html', 'Contact — NY HVAC Services',
     'Call 718-551-2029, 24 hours a day. 109 S 5th St, Brooklyn NY 11249. Serving Brooklyn, Queens and Manhattan.'),
]
LINKMAP = {slug + '.dc.html': out for slug, out, _t, _d in PAGES}
LINKMAP['NYHVACServicesPhone.dc.html'] = 'index.html'

# ------------------------------------------------- CSS-only issue picker
PICK_CSS = """
    /* Issue picker — CSS-only replacement for the canvas's templated version */
    .pick { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 5px; overflow: hidden; }
    .pick label { margin: 0; display: block; }
    .pick input { position: absolute; width: 1px; height: 1px; opacity: 0; }
    .pick span { min-height: 52px; padding: 15px 16px; display: flex; align-items: center; gap: 10px; font-family: inherit; font-weight: 600; font-size: 15.5px; cursor: pointer; color: var(--ink-soft); background: var(--surface); transition: background .18s ease, color .18s ease, box-shadow .18s ease; }
    .pick input:focus-visible + span { outline: 2px solid __PRIMARY__; outline-offset: -3px; }
    .pick .i-heat input:checked + span { color: __HEAT_FG__; background: __HEAT_BG__; box-shadow: inset 0 0 0 2px __HEAT_RING__; }
    .pick .i-cool input:checked + span { color: __COOL_FG__; background: __COOL_BG__; box-shadow: inset 0 0 0 2px __COOL_RING__; }
    .pick .i-plumb input:checked + span,
    .pick .i-install input:checked + span { color: var(--ink); background: var(--tint-neutral); box-shadow: inset 0 0 0 2px var(--ink); }
"""
PICK_CSS = (PICK_CSS
            .replace('__PRIMARY__', PRIMARY)
            .replace('__HEAT_FG__', shift(PRIMARY, -0.34))
            .replace('__HEAT_BG__', shift(PRIMARY, 0.9))
            .replace('__HEAT_RING__', PRIMARY)
            .replace('__COOL_FG__', shift(SECONDARY, -0.3))
            .replace('__COOL_BG__', shift(SECONDARY, 0.88))
            .replace('__COOL_RING__', SECONDARY))

ICONS = {
    'heat': 'M12 2.7c.6 4 3 5.6 4.4 7.6a6.9 6.9 0 1 1-11.5 4.6c0-3 1.7-4.8 2.8-6.3.3 1.9 1.1 2.8 2.1 3.2-.6-3.6.3-7.1 2.2-9.1z',
    'cool': 'M12 2.6v18.8M3.9 7.3l16.2 9.4M3.9 16.7l16.2-9.4',
    'plumb': 'M12 2.8s5.6 5.7 5.6 9.4a5.6 5.6 0 1 1-11.2 0C6.4 8.5 12 2.8 12 2.8z',
    'install': 'M4.5 7h15a1.5 1.5 0 0 1 1.5 1.5v7a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 15.5v-7A1.5 1.5 0 0 1 4.5 7zM6 11h12M6 14h12',
}
LABELS = [('heat', 'No heat'), ('cool', 'Not cooling'),
          ('plumb', 'Leak or blockage'), ('install', 'Install or replace')]


def picker_html():
    rows = []
    for i, (key, label) in enumerate(LABELS):
        checked = ' checked' if i == 0 else ''
        rows.append(
            '            <label class="i-%s"><input type="radio" name="issue" value="%s"%s>'
            '<span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
            'style="flex: none; width: 18px; height: 18px"><path d="%s"></path></svg>%s</span></label>'
            % (key, key, checked, ICONS[key], label))
    return ('          <div role="group" aria-label="What\'s going on?" class="pick">\n'
            + '\n'.join(rows) + '\n          </div>')


def convert(src):
    s = open(src, encoding='utf-8').read()

    # 1. drop the Design runtime logic block and support.js
    s = re.sub(r'<script type="text/x-dc".*?</script>\s*', '', s, flags=re.S)
    s = s.replace('<script src="./support.js"></script>\n', '')

    # 2. drop the exit-intent pop-up (needs the runtime's state)
    s = re.sub(r'\s*<!-- Lead pop-up \(exit intent\) -->\s*<sc-if.*?</sc-if>', '', s, flags=re.S)

    # 3. templated issue picker -> CSS-only radios
    s = re.sub(r'[ ]*<div role="group" aria-label="What\'s going on\?".*?</sc-for>\s*</div>',
               picker_html(), s, flags=re.S)
    s = s.replace('{{submitLabel}}', 'Get my free estimate')

    # 4. resolve brand tokens (before the helmet is lifted, so its CSS is covered too)
    def tok(m):
        key = m.group(1)
        if key not in TOKENS:
            raise SystemExit('unresolved token {{%s}} in %s' % (key, src))
        return TOKENS[key]
    s = re.sub(r'\{\{\s*([A-Za-z_]\w*)\s*\}\}', tok, s)

    # 5. lift <helmet> into <head>, unwrap <x-dc>
    helmet = re.search(r'<helmet>(.*?)</helmet>', s, re.S)
    head_extra = helmet.group(1) if helmet else ''
    head_extra = head_extra.replace('</style>', PICK_CSS + '  </style>')
    s = re.sub(r'<helmet>.*?</helmet>\s*', '', s, flags=re.S)
    s = s.replace('<x-dc>', '').replace('</x-dc>', '')

    # 6. assets and inter-page links
    s = s.replace(BLOB_LIGHT, '../assets/nyhvac-logo.png')
    s = s.replace(BLOB_DARK, '../assets/nyhvac-logo-dark.png')
    for a, b in LINKMAP.items():
        s = s.replace('href="' + a + '"', 'href="' + b + '"')

    body = re.search(r'<body>(.*?)</body>', s, re.S).group(1).strip()
    return head_extra.strip(), body


def main():
    os.makedirs(SITE, exist_ok=True)
    for slug, out, title, desc in PAGES:
        head_extra, body = convert(os.path.join(CANVAS, slug + '.dc.html'))
        html = (
            '<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>' + title + '</title>\n'
            '<meta name="description" content="' + desc + '">\n'
            '<meta name="theme-color" content="' + DARK + '">\n'
            '<link rel="icon" href="../assets/nyhvac-logo.png">\n'
            + head_extra + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')

        leftovers = re.findall(r'\{\{[^}]*\}\}|<sc-\w+|<x-dc|<helmet', html)
        if leftovers:
            raise SystemExit('template leftovers in %s: %s' % (out, set(leftovers)))

        open(os.path.join(SITE, out), 'w', encoding='utf-8').write(html)
        print('  %-24s %5d KB' % (out, len(html) // 1024))
    print('built %d pages into site/' % len(PAGES))


if __name__ == '__main__':
    main()
