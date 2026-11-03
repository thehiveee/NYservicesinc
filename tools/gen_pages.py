import json, os

ROOT = '/tmp/claude-0/-home-claude/e8a34c17-06b4-5615-96e9-ae989328367f/scratchpad/nyhvac/project/'
HELMET = open('/tmp/claude-0/-home-claude/e8a34c17-06b4-5615-96e9-ae989328367f/scratchpad/_helmet.txt', encoding='utf-8').read()

LOGO_L = '/_blob/8d207415a19d3d7a8982fb6d297ef543'
LOGO_D = '/_blob/f7bc8f1261a409b0d3f3b2c18c9ffece'
TEL = 'tel:+17185512029'

PAGES = [
    ('Heating',         'Heating'),
    ('AirConditioning', 'Air conditioning'),
    ('Plumbing',        'Plumbing'),
    ('Commercial',      'Commercial'),
    ('About',           'About'),
    ('Financing',       'Financing'),
    ('Coupons',         'Coupons'),
    ('Maintenance',     'Maintenance program'),
    ('Contact',         'Contact'),
]

NAV_L = [('Heating.dc.html', 'Heating'), ('AirConditioning.dc.html', 'Air conditioning'), ('Plumbing.dc.html', 'Plumbing')]
NAV_R = [('Commercial.dc.html', 'Commercial'), ('Financing.dc.html', 'Financing'), ('About.dc.html', 'About')]
NAV_ALL = [('NYHVACServices.dc.html', 'Home')] + NAV_L + NAV_R + [
    ('Coupons.dc.html', 'Coupons'), ('Maintenance.dc.html', 'Maintenance program'), ('Contact.dc.html', 'Contact')]


def navlinks(items, active, align):
    out = []
    for href, label in items:
        on = (href == active)
        style = ('text-decoration: none; padding-bottom: 3px;'
                 ' border-bottom: 2px solid {{primary}}' if on else 'text-decoration: none')
        out.append('<a href="' + href + '" style="' + style + '">' + label + '</a>')
    just = 'flex-start' if align == 'l' else 'flex-end'
    return '\n        '.join(out), just


def masthead(active, home_href):
    left, _ = navlinks(NAV_L, active, 'l')
    right, _ = navlinks(NAV_R, active, 'r')
    mob = '\n          '.join(
        '<a href="' + h + '">' + l + '</a>' for h, l in NAV_ALL if h != active)
    return '''
  <!-- Masthead: logo centred -->
  <header style="position: relative; background: var(--surface); border-bottom: 1px solid var(--line)">
    <div class="mast" style="max-width: 1280px; margin: 0 auto; padding: 18px 40px; display: flex; flex-wrap: wrap; gap: 16px 32px; align-items: center; justify-content: center">
      <nav class="nav-l" aria-label="Main" style="flex: 1 1 300px; display: flex; flex-wrap: wrap; gap: 26px; justify-content: flex-start; font-size: 15.5px; font-weight: 600; color: var(--ink)">
        ''' + left + '''
      </nav>
      <a class="brand lg-swap" href="''' + home_href + '''" aria-label="NY HVAC Services — home" style="flex: none; display: block; text-decoration: none">
        <img class="lg-light" src="''' + LOGO_L + '''" alt="NY HVAC Services" style="height: 58px; width: auto; display: block">
        <img class="lg-dark" src="''' + LOGO_D + '''" alt="NY HVAC Services" style="height: 58px; width: auto">
      </a>
      <div class="nav-r" style="flex: 1 1 300px; display: flex; flex-wrap: wrap; gap: 22px; align-items: center; justify-content: flex-end; font-size: 15.5px; font-weight: 600; color: var(--ink)">
        <nav aria-label="More" style="display: flex; flex-wrap: wrap; gap: 22px">
          ''' + right + '''
        </nav>
        <a href="Contact.dc.html" style="display: inline-block; padding: 14px 20px; border: 1.5px solid var(--ink); border-radius: 4px; color: var(--ink); font-weight: 700; font-size: 15.5px; text-decoration: none">Book your service</a>
      </div>
      <a class="mobcall" href="''' + TEL + '''" aria-label="Call {{phone}}">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"></path></svg>
      </a>
      <details class="mobnav">
        <summary aria-label="Menu">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg>
          <span>Menu</span>
        </summary>
        <nav class="mobnav-panel" aria-label="Site">
          ''' + mob + '''
          <a href="Contact.dc.html" class="mobnav-cta">Book your service</a>
        </nav>
      </details>
    </div>
  </header>
'''


STATUSBAR = '''
  <!-- Status strip -->
  <div class="statusbar" style="background: {{dark}}; color: #A7B4C0; font-size: 13.5px; font-weight: 500; border-bottom: 1px solid rgba(255,255,255,.08)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 10px 40px; display: flex; flex-wrap: wrap; gap: 16px; justify-content: space-between">
      <div style="display: flex; align-items: center; gap: 8px">
        <span style="width: 7px; height: 7px; border-radius: 50%; background: {{primaryOnDark}}; display: inline-block" aria-hidden="true"></span>
        <strong style="color: #FFFFFF">Family owned in Brooklyn for nearly 30 years</strong>
        <span class="tail">— and answering the phone 24 hours a day</span>
      </div>
      <div style="display: flex; flex-wrap: wrap; gap: 20px"><a href="mailto:[EMAIL]" style="text-decoration: none">[EMAIL ADDRESS]</a>
        <a href="''' + TEL + '''" style="text-decoration: none; color: var(--ink); font-weight: 600">{{phone}}</a>
      </div>
    </div>
  </div>
'''


def crumb(label):
    return '''
  <nav aria-label="Breadcrumb" style="border-bottom: 1px solid var(--line); background: var(--surface-2)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 14px 40px; font-size: 14.5px; font-weight: 600; color: var(--ink-soft); display: flex; flex-wrap: wrap; gap: 10px; align-items: center">
      <a href="NYHVACServices.dc.html" style="text-decoration: none">Home</a>
      <span aria-hidden="true">/</span>
      <span style="color: var(--ink)">''' + label + '''</span>
    </div>
  </nav>
'''


def hero(eyebrow, lines, lede, facts, cta_label='Book this service'):
    spans = []
    for text, col in lines:
        c = ('; color: ' + col) if col else ''
        spans.append('          <span style="display: block' + c + '">' + text + '</span>')
    factrows = []
    for t, d in facts:
        factrows.append('''        <div style="display: flex; gap: 13px; align-items: start; padding: 18px 20px; border-bottom: 1px solid rgba(255,255,255,.12)">
          <svg viewBox="0 0 24 24" fill="none" stroke="{{primaryOnDark}}" stroke-width="1.9" stroke-linecap="round" aria-hidden="true" style="flex: none; width: 19px; height: 19px; margin-top: 3px"><path d="M4.5 12.5 9.5 17.5 19.5 7"></path></svg>
          <span style="font-size: 16px; color: #CBD4DD"><strong style="color: #FFFFFF; display: block; font-size: 17px">''' + t + '''</strong>''' + d + '''</span>
        </div>''')
    return '''
  <!-- Hero -->
  <section id="top" style="background: {{dark}}; color: #FFFFFF">
    <div style="max-width: 1280px; margin: 0 auto; padding: 72px 40px 84px; display: flex; flex-wrap: wrap; gap: 64px; align-items: start">
      <div style="flex: 999 1 540px; min-width: 0">
        <p class="heroeyebrow" style="margin: 0 0 22px; font-size: 14px; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: #A7B4C0">''' + eyebrow + '''</p>
        <h1 style="margin: 0; font-weight: 800; font-size: 104px; line-height: .86; letter-spacing: -.005em; text-transform: uppercase">
''' + '\n'.join(spans) + '''
        </h1>
        <div class="herorule" style="display: flex; width: 200px; height: 5px; margin-top: 30px" aria-hidden="true">
          <span style="flex: 1; background: {{secondary}}"></span>
          <span style="flex: 1; background: {{primary}}"></span>
        </div>
        <p class="herolede" style="margin: 26px 0 0; font-size: 20px; line-height: 1.55; color: #CBD4DD; max-width: 52ch">''' + lede + '''</p>
        <div class="herocta" style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 34px">
          <a href="''' + TEL + '''" class="call-breathe" style="--ring: {{ringColor}}; display: inline-flex; align-items: center; gap: 10px; padding: 19px 28px; border-radius: 4px; background: {{primaryDeep}}; color: #FFFFFF; font-weight: 700; font-size: 17px; text-decoration: none">
            <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="width: 19px; height: 19px"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"></path></svg>
            Call {{phone}}
          </a>
          <a href="Contact.dc.html" style="display: inline-block; padding: 19px 28px; border: 1px solid rgba(255,255,255,.4); border-radius: 4px; color: #FFFFFF; font-weight: 700; font-size: 17px; text-decoration: none">''' + cta_label + '''</a>
        </div>
      </div>
      <div style="flex: 1 1 360px; min-width: 0; border: 1px solid rgba(255,255,255,.14); border-radius: 6px; overflow: hidden; background: {{panelDark}}">
        <h2 style="margin: 0; padding: 20px 22px; font-size: 15px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: #FFFFFF; border-bottom: 1px solid rgba(255,255,255,.12)">What you get, either way</h2>
''' + '\n'.join(factrows) + '''
        <div style="padding: 20px 22px">
          <a href="Contact.dc.html" style="display: block; text-align: center; padding: 15px 20px; border-radius: 4px; background: {{primaryDeep}}; color: #FFFFFF; font-weight: 700; font-size: 16px; text-decoration: none">Get a free estimate</a>
        </div>
      </div>
    </div>
  </section>
'''


def cards(eyebrow, h2, intro, items, accent='{{primary}}'):
    out = []
    for t, b, link in items:
        out.append('''        <div style="border: 1px solid var(--line); border-top: 4px solid ''' + accent + '''; border-radius: 6px; padding: 36px; display: flex; flex-direction: column">
          <h3 style="margin: 0; font-size: 30px; font-weight: 700; line-height: 1.02; text-transform: uppercase">''' + t + '''</h3>
          <p style="margin: 10px 0 0; color: var(--ink-soft); font-size: 16.5px">''' + b + '''</p>
          <a href="Contact.dc.html" style="display: inline-block; margin-top: auto; padding-top: 18px; font-weight: 700; font-size: 15.5px; color: {{primaryOnLight}}">''' + link + '''</a>
        </div>''')
    return '''
  <section id="services" style="border-bottom: 1px solid var(--line)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 88px 40px">
      <div style="max-width: 64ch">
        <p style="margin: 0 0 14px; font-size: 14px; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: {{primaryOnLight}}">''' + eyebrow + '''</p>
        <h2 style="margin: 0; font-size: 68px; font-weight: 800; line-height: .92; text-transform: uppercase; text-wrap: balance">''' + h2 + '''</h2>
        <p style="margin: 20px 0 0; font-size: 19px; color: var(--ink-soft); line-height: 1.55">''' + intro + '''</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; margin-top: 52px">
''' + '\n'.join(out) + '''
      </div>
    </div>
  </section>
'''


def signs(h2, intro, items):
    rows = []
    for i, (t, b) in enumerate(items):
        rows.append('''        <div style="border-top: 2px solid {{secondary}}; padding-top: 20px">
          <b style="display: block; font-family: 'Barlow Condensed', 'Roboto Condensed', 'Arial Narrow', sans-serif; font-size: 44px; font-weight: 800; line-height: 1; color: {{secondaryOnLight}}">0''' + str(i + 1) + '''</b>
          <h3 style="margin: 12px 0 0; font-size: 26px; font-weight: 700; text-transform: uppercase">''' + t + '''</h3>
          <p style="margin: 6px 0 0; color: var(--ink-soft); font-size: 16px">''' + b + '''</p>
        </div>''')
    return '''
  <section style="background: var(--surface-2); border-bottom: 1px solid var(--line)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 88px 40px">
      <div style="max-width: 62ch">
        <h2 style="margin: 0; font-size: 60px; font-weight: 800; line-height: .94; text-transform: uppercase; text-wrap: balance">''' + h2 + '''</h2>
        <p style="margin: 18px 0 0; font-size: 18px; color: var(--ink-soft)">''' + intro + '''</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 32px; margin-top: 46px">
''' + '\n'.join(rows) + '''
      </div>
    </div>
  </section>
'''


PROMISE = '''
  <section class="pledge" style="border-bottom: 1px solid var(--line)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 80px 40px; display: flex; flex-wrap: wrap; gap: 48px; align-items: center">
      <div style="flex: 999 1 560px; min-width: 0">
        <p style="margin: 0 0 16px; font-size: 14px; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: {{primaryOnLight}}">Our promise</p>
        <p style="margin: 0; font-family: 'Barlow Condensed', 'Roboto Condensed', 'Arial Narrow', sans-serif; font-size: 42px; font-weight: 700; line-height: 1.08; text-wrap: balance; color: var(--ink)">“We will never recommend a product or service that we would not recommend for our own families.”</p>
        <p style="margin: 20px 0 0; font-size: 17px; color: var(--ink-soft); max-width: 62ch">Which is why you will hear “this has a few years left in it” as often as you hear “this needs replacing” — and why, if something is not right afterwards, we will not rest until we have made it right.</p>
      </div>
      <div style="flex: 1 1 300px; min-width: 0">
        <a href="About.dc.html" style="display: inline-block; padding: 16px 24px; border: 1.5px solid var(--ink); border-radius: 4px; color: var(--ink); font-weight: 700; font-size: 16px; text-decoration: none">Meet the family behind it</a>
      </div>
    </div>
  </section>
'''


def related(items):
    out = []
    for href, t, b in items:
        out.append('''        <a href="''' + href + '''" style="display: flex; flex-direction: column; border: 1px solid var(--line); border-radius: 6px; padding: 30px; text-decoration: none">
          <h3 style="margin: 0; font-size: 28px; font-weight: 700; line-height: 1.04; text-transform: uppercase">''' + t + '''</h3>
          <p style="margin: 8px 0 0; color: var(--ink-soft); font-size: 16px">''' + b + '''</p>
          <span aria-hidden="true" style="margin-top: 16px; font-weight: 700; color: {{primaryOnLight}}">→</span>
        </a>''')
    return '''
  <section style="border-bottom: 1px solid var(--line)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 80px 40px">
      <h2 style="margin: 0 0 36px; font-size: 44px; font-weight: 800; line-height: 1; text-transform: uppercase">While we're here</h2>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">
''' + '\n'.join(out) + '''
      </div>
    </div>
  </section>
'''


def closing(h2, sub):
    return '''
  <section style="background: var(--surface-2); color: var(--ink)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 92px 40px; text-align: center; display: flex; flex-direction: column; align-items: center">
      <span class="lg-swap" style="display: block">
        <img class="lg-light closelogo" src="''' + LOGO_L + '''" alt="NY HVAC Services" style="height: 56px; width: auto; display: block">
        <img class="lg-dark closelogo" src="''' + LOGO_D + '''" alt="NY HVAC Services" style="height: 56px; width: auto">
      </span>
      <h2 style="margin: 30px 0 0; font-size: 78px; font-weight: 800; line-height: .9; text-transform: uppercase; text-wrap: balance">''' + h2 + '''</h2>
      <p style="margin: 20px auto 0; font-size: 19px; color: var(--ink-soft); max-width: 52ch">''' + sub + '''</p>
      <div style="display: flex; flex-wrap: wrap; gap: 12px; justify-content: center; margin-top: 32px">
        <a href="''' + TEL + '''" class="call-breathe" style="--ring: {{ringColor}}; display: inline-block; padding: 19px 30px; border-radius: 4px; background: {{primaryDeep}}; color: #FFFFFF; font-weight: 700; font-size: 17px; text-decoration: none">Call {{phone}}</a>
        <a href="Contact.dc.html" style="display: inline-block; padding: 19px 30px; border: 1.5px solid var(--ink); border-radius: 4px; color: var(--ink); font-weight: 700; font-size: 17px; text-decoration: none">Get a free estimate</a>
      </div>
    </div>
  </section>
'''


FOOTER = '''
  <!-- Footer -->
  <footer style="background: var(--surface); color: var(--ink-soft); border-top: 1px solid var(--line)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 64px 40px 40px">
      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 40px">
        <div>
          <span class="lg-swap" style="display: block">
            <img class="lg-light footlogo" src="''' + LOGO_L + '''" alt="NY HVAC Services" style="height: 44px; width: auto; display: block">
            <img class="lg-dark footlogo" src="''' + LOGO_D + '''" alt="NY HVAC Services" style="height: 44px; width: auto">
          </span>
          <p style="margin: 18px 0 0; font-size: 15px">Heating, cooling and plumbing for homes, buildings and businesses in Brooklyn, Queens and Manhattan. Family owned and operated for nearly thirty years.</p>
        </div>
        <div>
          <h4 style="margin: 0; color: var(--ink); font-size: 14px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase">Services</h4>
          <ul style="list-style: none; margin: 16px 0 0; padding: 0; display: flex; flex-direction: column; gap: 10px; font-size: 15px">
            <li><a href="Heating.dc.html" style="text-decoration: none">Heating</a></li>
            <li><a href="AirConditioning.dc.html" style="text-decoration: none">Air conditioning</a></li>
            <li><a href="Plumbing.dc.html" style="text-decoration: none">Plumbing</a></li>
            <li><a href="Commercial.dc.html" style="text-decoration: none">Commercial</a></li>
            <li><a href="Maintenance.dc.html" style="text-decoration: none">Maintenance program</a></li>
          </ul>
        </div>
        <div>
          <h4 style="margin: 0; color: var(--ink); font-size: 14px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase">Company</h4>
          <ul style="list-style: none; margin: 16px 0 0; padding: 0; display: flex; flex-direction: column; gap: 10px; font-size: 15px">
            <li><a href="About.dc.html" style="text-decoration: none">About us</a></li>
            <li><a href="Financing.dc.html" style="text-decoration: none">Financing</a></li>
            <li><a href="Coupons.dc.html" style="text-decoration: none">Coupons</a></li>
            <li><a href="Contact.dc.html" style="text-decoration: none">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4 style="margin: 0; color: var(--ink); font-size: 14px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase">Contact</h4>
          <ul style="list-style: none; margin: 16px 0 0; padding: 0; display: flex; flex-direction: column; gap: 10px; font-size: 15px">
            <li><a href="''' + TEL + '''" style="text-decoration: none; color: var(--ink); font-weight: 600">{{phone}}</a></li>
            <li><a href="mailto:[EMAIL]" style="text-decoration: none">[EMAIL ADDRESS]</a></li>
            <li>109 S 5th St, 1st Floor<br>Brooklyn, NY 11249</li>
            <li style="color: {{primaryOnLight}}">Emergency service — 24 hours</li>
          </ul>
        </div>
      </div>
      <div style="margin-top: 44px; padding-top: 24px; border-top: 1px solid var(--line); display: flex; flex-wrap: wrap; gap: 16px; justify-content: space-between; font-size: 13.5px">
        <span>© 2026 NY HVAC Services Inc · Brooklyn, NY</span>
        <span>Privacy policy · Terms · Accessibility</span>
      </div>
    </div>
  </footer>
'''

STICKY = '''
  <!-- Sticky call bar -->
  <div class="stickybar" style="position: sticky; bottom: 0; z-index: 50; background: {{panelDark}}; color: #FFFFFF; border-top: 1px solid rgba(255,255,255,.08); box-shadow: 0 -12px 30px -12px rgba(0,0,0,.45); padding: 14px 40px; display: flex; flex-wrap: wrap; gap: 26px; align-items: center; justify-content: center">
    <p style="margin: 0; font-size: 16px; color: #CBD4DD"><strong style="color: #FFFFFF">No heat, no cooling or a leak right now?</strong> A real person answers, 24 hours a day.</p>
    <div style="display: flex; flex-wrap: wrap; gap: 10px">
      <a href="''' + TEL + '''" class="call-breathe" style="--ring: {{ringColor}}; display: inline-flex; align-items: center; gap: 9px; padding: 15px 24px; border-radius: 4px; background: {{primaryDeep}}; color: #FFFFFF; font-weight: 700; font-size: 16px; text-decoration: none">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="width: 17px; height: 17px"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"></path></svg>
        Call {{phone}}
      </a>
      <a href="Contact.dc.html" style="display: inline-block; padding: 15px 24px; border: 1px solid rgba(255,255,255,.4); border-radius: 4px; color: #FFFFFF; font-weight: 700; font-size: 16px; text-decoration: none">Free estimate</a>
    </div>
  </div>
'''

SCRIPT_HEAD = '''
<script type="text/x-dc" data-dc-script data-props='{
  "phone": {"editor": "text", "default": "718-551-2029", "section": "Client"},
  "primary": {"editor": "color", "default": "#ED1C24", "section": "Brand"},
  "secondary": {"editor": "color", "default": "#346699", "section": "Brand"},
  "dark": {"editor": "color", "default": "#0D1B2A", "section": "Brand"},
  "$preview": {"width": 1440, "height": __H__}
}'>
class Component extends DCLogic {
  shift(hex, amount) {
    var m = /^#?([0-9a-f]{6})$/i.exec(String(hex || '').trim());
    if (!m) return hex;
    var n = parseInt(m[1], 16);
    var parts = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map(function (c) {
      var v = amount >= 0 ? c + (255 - c) * amount : c * (1 + amount);
      return Math.max(0, Math.min(255, Math.round(v)));
    });
    return '#' + parts.map(function (c) { return ('0' + c.toString(16)).slice(-2); }).join('');
  }
  rgba(hex, alpha) {
    var m = /^#?([0-9a-f]{6})$/i.exec(String(hex || '').trim());
    if (!m) return 'rgba(0,0,0,' + alpha + ')';
    var n = parseInt(m[1], 16);
    return 'rgba(' + [(n >> 16) & 255, (n >> 8) & 255, n & 255].join(',') + ',' + alpha + ')';
  }
__EXTRA__
  renderVals() {
    var primary = this.props.primary ?? '#ED1C24';
    var secondary = this.props.secondary ?? '#346699';
    var dark = this.props.dark ?? '#0D1B2A';
    return {
      phone: this.props.phone ?? '718-551-2029',
      dark: dark,
      panelDark: this.shift(dark, 0.07),
      footerDark: this.shift(dark, -0.35),
      primary: primary,
      secondary: secondary,
      primaryDeep: this.shift(primary, -0.14),
      primaryOnLight: this.shift(primary, -0.3),
      primaryOnDark: this.shift(primary, 0.42),
      secondaryOnLight: this.shift(secondary, -0.28),
      secondaryOnDark: this.shift(secondary, 0.45),
      ringColor: this.rgba(primary, 0.3)__EXTRAVALS__
    };
  }
}
</script>
'''


def build(slug, title, body, height, extra='', extravals=''):
    script = SCRIPT_HEAD.replace('__H__', str(height)).replace('__EXTRA__', extra).replace('__EXTRAVALS__', extravals)
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>'
            + title + ' — NY HVAC Services</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>'
            + HELMET + '</helmet>\n\n<div class="pg" style="width: 100%; background: var(--page); color: var(--ink); font-size: 17px; line-height: 1.6">\n'
            + body + '\n</div>\n</x-dc>\n' + script + '</body>\n</html>\n')
    open(ROOT + slug + '.dc.html', 'w', encoding='utf-8').write(html)
    return len(html)


# ---------------------------------------------------------------- HEATING
h = 4950
body = (STATUSBAR + masthead('Heating.dc.html', 'NYHVACServices.dc.html') + crumb('Heating')
    + hero('Heating · Brooklyn, Queens &amp; Manhattan',
           [('Heat back on.', None), ('Tonight.', '{{primaryOnDark}}')],
           'A dead boiler in January is not a scheduling problem, it is a safety one. Our line is answered around the clock, and a trained technician finds the actual fault rather than guessing at a part.',
           [('24-hour emergency service', 'Furnace and boiler failures answered any hour, any day.'),
            ('Every brand, not just ours', 'We service all major makes of heater — not only the lines we sell.'),
            ('Nearly 30 years of Brooklyn winters', 'The same family business since the start.'),
            ('Financing on larger jobs', 'No-interest and low-monthly options on replacements.')],
           'Book a heating visit')
    + cards('Heating services', 'Everything that makes a building warm.',
            'Repair, replacement, installation and inspection — for furnaces, boilers and heaters in apartments, brownstones, walk-ups and commercial buildings.',
            [('Furnace repair', 'No heat, uneven heat, short cycling, pilot and ignition faults, noisy blowers and thermostats that have stopped talking to the unit.', 'Book a furnace repair'),
             ('Emergency furnace service', 'The call that gets answered at 3am. Nights, weekends and holidays included — because that is when heating fails.', 'Get someone out tonight'),
             ('Boiler services', 'Repair, replacement and annual service on residential and commercial boilers, including the older systems common in pre-war Brooklyn buildings.', 'Book a boiler visit'),
             ('Heater repair', 'Wall heaters, unit heaters and space heating of every major brand, diagnosed properly and repaired to last the season.', 'Book a heater repair'),
             ('Heating installation', 'Designed and engineered for the actual space, then installed — we size the system to the building rather than selling you the biggest one.', 'Plan an installation'),
             ('Pre-winter inspection', 'Booked in the quiet weeks so faults are found in daylight, not on the first freezing night with the whole city calling at once.', 'Book an inspection')])
    + signs('Call us before it becomes an emergency.',
            'Heating rarely fails without warning. These are the four that most often arrive a week before a no-heat call.',
            [('It is cold in one room', 'Uneven heat usually means circulation, not capacity — and it is cheaper to fix than to live with.'),
             ('It cycles on and off', 'Short cycling wears a system out fast and almost always points at a fault worth finding now.'),
             ('A new noise', 'Banging, whistling and rattling each mean something specific. None of them mean "ignore it".'),
             ('The bill jumped', 'A system working harder for the same warmth is telling you something before it stops entirely.')])
    + PROMISE
    + related([('AirConditioning.dc.html', 'Air conditioning', 'The other half of the year, handled by the same crew.'),
               ('Maintenance.dc.html', 'Maintenance program', 'Scheduled seasonal service so small faults get caught early.'),
               ('Financing.dc.html', 'Financing', 'No-interest and low-monthly options on a new system.')])
    + closing('No heat? Call now.', 'A real person answers, 24 hours a day, and a trained technician is dispatched from Brooklyn.')
    + FOOTER + STICKY)
print('Heating', build('Heating', 'Heating', body, h))

# ------------------------------------------------------- AIR CONDITIONING
h = 4950
body = (STATUSBAR + masthead('AirConditioning.dc.html', 'NYHVACServices.dc.html') + crumb('Air conditioning')
    + hero('Air conditioning · Brooklyn, Queens &amp; Manhattan',
           [('Cold air.', None), ('Fast.', '{{secondaryOnDark}}')],
           'When the AC quits in a July heat wave, every company in the city is booked. We answer around the clock and we work on every major brand — so the answer is never "we do not touch that one".',
           [('24-hour emergency service', 'Cooling failures answered through the heat wave, any hour.'),
            ('Every brand serviced', 'Central, ductless, window and through-the-wall, whoever made it.'),
            ('Repair or replace, told straight', 'We will say when a unit has years left rather than sell you a new one.'),
            ('Financing on replacements', 'No-interest and low-monthly options, decided online in minutes.')],
           'Book an AC visit')
    + cards('Cooling services', 'Cold, quiet, and running all summer.',
            'Repair, installation, replacement and seasonal maintenance for every kind of air conditioning a New York building throws at us.',
            [('AC repair', 'Not cooling, leaking water, tripping breakers, icing up or running constantly without getting anywhere. Diagnosed on the spot.', 'Book an AC repair'),
             ('Emergency AC service', 'Around-the-clock dispatch during heat waves, when a failed system in an apartment with an elderly resident is an emergency.', 'Get someone out now'),
             ('Air conditioning installation', 'Central, ductless mini-split and through-the-wall systems, sized and engineered for the space before anything is ordered.', 'Plan an installation'),
             ('Full AC replacement', 'When repair stops being the better buy, we say so — and show you the running-cost difference rather than just the price.', 'Price a replacement'),
             ('Maintenance &amp; tune-ups', 'Coils, filters, drains, refrigerant levels and electrical connections checked so the system is not discovering problems in August.', 'Book a tune-up'),
             ('Spring pre-season clean', 'Booked before the first hot day, when we can still get to you the same week rather than the following one.', 'Book a spring clean')],
            '{{secondary}}')
    + signs('Four things worth a call before June.',
            'Cooling problems are cheapest in April. These are the signs that the system will not make it through a heat wave.',
            [('It runs but barely cools', 'Usually refrigerant or airflow. Both get worse, and one of them is a leak.'),
             ('Water where it should not be', 'A blocked condensate drain floods ceilings. It is a small job until it is not.'),
             ('It smells when it starts', 'Microbial growth on the coil, which is an air-quality problem as much as a comfort one.'),
             ('It is over ten years old', 'Not a reason to replace it — but a reason to have it looked at before the season.')])
    + PROMISE
    + related([('Heating.dc.html', 'Heating', 'Furnaces, boilers and heaters, by the same crew.'),
               ('Maintenance.dc.html', 'Maintenance program', 'Seasonal service on the cooling and the heating.'),
               ('Coupons.dc.html', 'Coupons', 'Current offers on service calls and installations.')])
    + closing('Not cooling? Call now.', 'A person answers 24 hours a day, and we work on every major brand of air conditioner.')
    + FOOTER + STICKY)
print('AirConditioning', build('AirConditioning', 'Air conditioning', body, h))

# --------------------------------------------------------------- PLUMBING
h = 4950
body = (STATUSBAR + masthead('Plumbing.dc.html', 'NYHVACServices.dc.html') + crumb('Plumbing')
    + hero('Plumbing · Brooklyn, Queens &amp; Manhattan',
           [('Water stops.', None), ('We start.', '{{secondaryOnDark}}')],
           'Most HVAC companies hand you a plumber’s card. We do both — so the no-heat call that turns out to be a burst pipe is handled on the same visit, by people you have already let into your home.',
           [('24-hour emergency plumbing', 'Burst pipes and major leaks answered at any hour.'),
            ('HVAC and plumbing in one crew', 'One company, one number, one visit when a job is both.'),
            ('Residential and commercial', 'Apartments, brownstones, restaurants and retail alike.'),
            ('Nearly 30 years in these buildings', 'We know what is behind a century-old Brooklyn wall.')],
           'Book a plumbing visit')
    + cards('Plumbing services', 'From a dripping faucet to the main line.',
            'Emergency work, planned repairs and the drain and sewer jobs that need proper equipment rather than a snake and some optimism.',
            [('Emergency plumbing', 'Burst pipes, major leaks and no water — answered and dispatched any hour of any day, including weekends and holidays.', 'Get someone out now'),
             ('Water heater services', 'Repair, replacement and installation of tank and tankless water heaters, residential and commercial.', 'Price a water heater'),
             ('Drain cleaning', 'Slow sinks, backed-up tubs and blocked mains cleared properly — and we tell you why it blocked, not just that it did.', 'Book a drain clearing'),
             ('Sewer line services', 'Inspection, repair and replacement, including the awkward runs under buildings that were plumbed before anyone drew a diagram.', 'Ask about a sewer line'),
             ('Hydro jetting', 'High-pressure jetting for grease, scale and root intrusion that snaking will not shift. The real fix for restaurant kitchen lines.', 'Book hydro jetting'),
             ('Repairs &amp; fixtures', 'Pipe repairs, leaks, toilets, faucets and shut-off valves — including the small jobs other companies will not come out for.', 'Book a repair')],
            '{{secondary}}')
    + signs('What to do while you wait for us.',
            'If water is actively coming in, these four steps limit the damage before the technician arrives. Call first — whoever answers will talk you through it.',
            [('Find the shut-off', 'Main valve for the whole property, or the local valve under the fixture. Turn it clockwise.'),
             ('Kill the power nearby', 'If water is near outlets or a panel, switch that circuit off at the breaker.'),
             ('Open the taps', 'Draining the pipes after shut-off takes pressure off the leak and reduces what escapes.'),
             ('Photograph it', 'Before you mop. Insurers ask, and it costs you nothing to have taken the picture.')])
    + PROMISE
    + related([('Heating.dc.html', 'Heating', 'Boilers and furnaces, by the same crew.'),
               ('Commercial.dc.html', 'Commercial', 'Kitchen lines, grease and commercial water heaters.'),
               ('Contact.dc.html', 'Contact', 'Phone, address and a booking form.')])
    + closing('Leak now? Call, do not type.', 'Whoever answers can tell you what to shut off while the technician is already on the way.')
    + FOOTER + STICKY)
print('Plumbing', build('Plumbing', 'Plumbing', body, h))

# ------------------------------------------------------------- COMMERCIAL
h = 4700
body = (STATUSBAR + masthead('Commercial.dc.html', 'NYHVACServices.dc.html') + crumb('Commercial')
    + hero('Commercial HVAC &amp; plumbing · Three boroughs',
           [('A closed day', None), ('costs more.', '{{primaryOnDark}}')],
           'Restaurants, retail, offices and buildings across Brooklyn, Queens and Manhattan. We schedule around your opening hours wherever we possibly can, and we answer at the hours when a failure actually happens.',
           [('After-hours and overnight slots', 'Work scheduled so you do not lose a trading day.'),
            ('HVAC and plumbing together', 'One contractor for the rooftop unit and the kitchen line.'),
            ('Service agreements', 'Planned maintenance for multi-site and multi-unit clients.'),
            ('24-hour emergency response', 'Because a walk-in freezer does not fail at 10am.')],
           'Talk about a site')
    + cards('Commercial services', 'The systems your business runs on.',
            'Planned and emergency work for commercial heating, cooling and plumbing — quoted properly, scheduled around you, and warrantied.',
            [('Commercial HVAC repair', 'Rooftop units, split systems and packaged units repaired fast, with after-hours slots so the floor stays open.', 'Book a commercial repair'),
             ('Replacement &amp; installation', 'Planned replacement quoted before the season turns, so capital spend happens on your calendar rather than in a crisis.', 'Plan a replacement'),
             ('Commercial plumbing', 'Leak and pipe repair with minimal shut-off time, plus commercial water heaters repaired and replaced.', 'Book commercial plumbing'),
             ('Kitchen line hydro jetting', 'Grease-heavy restaurant lines cleared under high pressure — the difference between a scheduled visit and a closed kitchen.', 'Book hydro jetting'),
             ('Sewer line work', 'Inspection, repair and replacement for commercial properties, coordinated with building management.', 'Ask about a sewer line'),
             ('Service agreements', 'Scheduled maintenance across one site or many, with priority response and a single point of contact.', 'Ask about an agreement')])
    + signs('Who we look after.',
            'Four kinds of commercial client, each with a different reason that downtime is expensive.',
            [('Restaurants &amp; bars', 'Grease lines, walk-ins and kitchen ventilation. Serviced before service, not during it.'),
             ('Retail &amp; storefronts', 'A shop that is too hot empties out. Rooftop and split systems kept running through the season.'),
             ('Offices', 'Comfort complaints, zoning and systems that were specified for a different floor plan than the one you have.'),
             ('Buildings &amp; management', 'Multi-unit work coordinated with supers and management, scheduled across a whole property.')])
    + related([('Plumbing.dc.html', 'Plumbing', 'The residential side of the same plumbing crew.'),
               ('Maintenance.dc.html', 'Maintenance program', 'Planned service, so failures stop being surprises.'),
               ('Contact.dc.html', 'Contact', 'Talk to us about a site or a portfolio.')])
    + closing('Let us quote the site.', 'Tell us what you run and where, and we will come and look before we put a number on it.')
    + FOOTER + STICKY)
print('Commercial', build('Commercial', 'Commercial', body, h))

# ------------------------------------------------------------------ ABOUT
h = 4600
body = (STATUSBAR + masthead('About.dc.html', 'NYHVACServices.dc.html') + crumb('About us')
    + hero('About NY HVAC Services',
           [('Nearly', None), ('thirty years.', '{{primaryOnDark}}')],
           'A local, family owned and operated business serving Brooklyn since before most of the companies you will find online existed. Same family, same neighbourhood, same phone number.',
           [('Family owned and operated', 'Not a franchise, not a call centre, not a rotating crew.'),
            ('Local experts for nearly three decades', 'We know these buildings because we have been inside them.'),
            ('Constantly trained technicians', 'Formally trained, and retrained on new equipment and technology.'),
            ('Licensed to install the top brands', 'And licensed, insured and accountable to you.')],
           'Get in touch')
    + PROMISE
    + signs('What thirty years actually buys you.',
            'Longevity is only worth something if it changes the work. Here is where it does.',
            [('We have seen your building', 'Pre-war walk-ups, brownstones and post-war co-ops each fail in their own way. That is pattern recognition, not luck.'),
             ('We will be here for the warranty', 'A guarantee is only as good as the company behind it in five years time.'),
             ('No incentive to oversell', 'We are not hitting a franchise quota. Repeat custom over three decades is the whole business model.'),
             ('Trained on what is current', 'Experience plus constant retraining on new equipment — not one without the other.')])
    + cards('How we work', 'Fast, friendly, honest — in that order.',
            'Three commitments that have not changed since the business started, and that the reviews tend to pick up on.',
            [('A person, every time', 'The phone is answered around the clock by someone who can dispatch a technician, not simply take a message and pass it on.', 'Call us now'),
             ('Told straight', 'What failed, what it costs to fix, and whether repairing or replacing is genuinely the better buy. Then you decide, not us.', 'Ask us anything'),
             ('We do not rest until it is right', 'If a problem comes back after we leave, so do we. Your comfort and safety is the priority that outranks the schedule.', 'Book a visit')])
    + related([('Heating.dc.html', 'Heating', 'Furnaces, boilers and heaters.'),
               ('AirConditioning.dc.html', 'Air conditioning', 'Repair, installation and replacement.'),
               ('Plumbing.dc.html', 'Plumbing', 'Emergency work, drains and sewer lines.')])
    + closing('Thirty years. One number.', 'Brooklyn, Queens and Manhattan — answered by a person, any hour of any day.')
    + FOOTER + STICKY)
print('About', build('About', 'About us', body, h))

# -------------------------------------------------------------- FINANCING
h = 4150
body = (STATUSBAR + masthead('Financing.dc.html', 'NYHVACServices.dc.html') + crumb('Financing')
    + hero('Financing · Approved online in minutes',
           [('Pay monthly.', None), ('Not all at once.', '{{secondaryOnDark}}')],
           'A boiler does not choose a convenient month to fail. Financing means the right repair or replacement happens now and is paid for over time — rather than the cheapest patch happening today and the real bill arriving next winter.',
           [('No interest or low monthly options', 'Plans built around what the job actually costs.'),
            ('Fast online credit decision', 'Minutes, not a week of waiting on paperwork.'),
            ('Easy online account access', 'View the balance and pay online if you want to.'),
            ('Available on repairs and replacements', 'Not only on the biggest installations.')],
           'Ask about financing')
    + cards('How it works', 'Three steps, and no pressure at any of them.',
            'Financing is offered after the diagnosis, alongside the price — never used to steer you toward a bigger job than you need.',
            [('1. We quote the work', 'A technician diagnoses the fault and prices the options. You see the repair cost and the replacement cost side by side.', 'Book a diagnosis'),
             ('2. Apply online', 'A fast online credit decision comes back in minutes, so you can make the call while the technician is still there.', 'Call to start'),
             ('3. Work goes ahead', 'Approved, scheduled and done — paid monthly from there, with online account access and online payment if you want it.', 'Talk it through')])
    + signs('When financing is the right call.',
            'It is not always. These are the four situations where spreading the cost genuinely saves money rather than just moving it.',
            [('The repair keeps recurring', 'Three service calls in two winters usually costs more than the replacement would have.'),
             ('The system is badly oversized', 'Paying monthly for the right-sized unit beats paying monthly in running costs forever.'),
             ('It failed at the wrong moment', 'Emergencies do not wait for payday. Financing stops that becoming a worse decision.'),
             ('You want the better equipment', 'The gap between adequate and genuinely efficient is often smaller per month than it looks.')])
    + related([('Coupons.dc.html', 'Coupons', 'Current offers, which stack with financing.'),
               ('Maintenance.dc.html', 'Maintenance program', 'The cheapest way to avoid needing either.'),
               ('Contact.dc.html', 'Contact', 'Ask us what a job would cost.')])
    + closing('Ask about financing.', 'Call and we will talk through the options before anything is committed to. [ADD LENDER NAME AND TERMS]')
    + FOOTER + STICKY)
print('Financing', build('Financing', 'Financing', body, h))

# ---------------------------------------------------------------- COUPONS
h = 3800
body = (STATUSBAR + masthead('Coupons.dc.html', 'NYHVACServices.dc.html') + crumb('Coupons')
    + hero('Coupons &amp; current offers',
           [('Same work.', None), ('Less money.', '{{primaryOnDark}}')],
           'Seasonal offers on service calls, tune-ups and installations, plus manufacturer promotions when they are running. Mention the offer when you call and we will apply it — no printing, no codes, no small print designed to trip you up.',
           [('Mention it on the phone', 'No printing and no codes to type in.'),
            ('Stacks with financing', 'An offer and a monthly plan are not either/or.'),
            ('Manufacturer promotions too', 'Including current brand promotions when they run.'),
            ('No bait pricing', 'The discount comes off the honest price, not an inflated one.')],
           'Claim an offer')
    + cards('This month', 'Current offers.',
            '[REPLACE THESE THREE CARDS WITH YOUR LIVE COUPONS. Keep the shape: what it is worth, what it applies to, and when it expires.]',
            [('[$XX off a service call]', '[What it applies to, any minimum spend, and the expiry date. One sentence is plenty — the offer should be legible in three seconds.]', 'Claim this offer'),
             ('[$XXX off a new system]', '[Which installations qualify, whether it combines with financing, and the expiry date.]', 'Claim this offer'),
             ('[Seasonal tune-up price]', '[What the tune-up includes and which months it is available. Pair this one with the maintenance program.]', 'Claim this offer')])
    + signs('How to use them.',
            'Four things worth knowing before you call, so nothing gets lost between the offer and the invoice.',
            [('Say it when you book', 'Mention the offer on the call rather than at the end of the job, and it is on the paperwork from the start.'),
             ('Check the dates', 'Seasonal offers run to a deadline. If it is close, book the visit rather than the work.'),
             ('Ask what else applies', 'Manufacturer promotions change through the year and are not always listed here yet.'),
             ('Combine with financing', 'An offer reduces the amount financed, which reduces the monthly figure too.')])
    + related([('Financing.dc.html', 'Financing', 'Spread what is left over monthly payments.'),
               ('Maintenance.dc.html', 'Maintenance program', 'Members get scheduled seasonal service.'),
               ('Contact.dc.html', 'Contact', 'Call and mention the offer.')])
    + closing('Call and mention the offer.', 'We will apply it when the job is booked, not argue about it when the invoice arrives.')
    + FOOTER + STICKY)
print('Coupons', build('Coupons', 'Coupons', body, h))

# ------------------------------------------------------------ MAINTENANCE
h = 4150
body = (STATUSBAR + masthead('Maintenance.dc.html', 'NYHVACServices.dc.html') + crumb('Maintenance program')
    + hero('Maintenance program · Members',
           [('Find it in', None), ('daylight.', '{{secondaryOnDark}}')],
           'Almost every emergency call we take was a small fault six months earlier. The maintenance program books the heating and the cooling in during the quiet weeks, so problems get found on a Tuesday morning instead of the first freezing night of the year.',
           [('Scheduled seasonal visits', 'Heating before winter, cooling before summer.'),
            ('Small faults caught early', 'Before they become a 3am call and a bigger bill.'),
            ('We do the remembering', 'You are booked in rather than hoping to get round to it.'),
            ('[MEMBER BENEFITS]', '[Priority response, discounts and any waived fees — add yours.]')],
           'Join the program')
    + cards('What is included', 'Two visits a year, and the year in between.',
            '[CONFIRM AND EDIT THIS LIST AGAINST YOUR ACTUAL PROGRAM — including the price and whether priority response and parts discounts are part of it.]',
            [('Heating visit', 'Before the first freeze: controls and safeties checked, burner and heat exchanger inspected, filters changed, and the system run under load rather than just switched on.', 'Join the program'),
             ('Cooling visit', 'Before the first hot day: coils and condensate drains cleared, refrigerant levels and electrical connections checked, airflow verified.', 'Join the program'),
             ('[Member benefits]', '[Priority response during peak weeks, a discount on repairs, waived diagnostic fee — list what members actually get and what it costs per year.]', 'Ask what is included')],
            '{{secondary}}')
    + signs('Why maintenance pays for itself.',
            'Four reasons that have nothing to do with sales copy and everything to do with how equipment actually fails.',
            [('Peak weeks are booked solid', 'The first cold night is when the whole city calls. Members are already in the calendar.'),
             ('Small faults are cheap faults', 'A capacitor found in October is a part. Found in January it is an emergency call-out.'),
             ('Efficiency drifts quietly', 'Dirty coils and low refrigerant raise running costs long before anyone notices the comfort.'),
             ('Warranties expect it', 'Most manufacturer warranties assume annual service. Skipping it can cost you the cover.')])
    + related([('Heating.dc.html', 'Heating', 'What the winter visit covers.'),
               ('AirConditioning.dc.html', 'Air conditioning', 'What the summer visit covers.'),
               ('Coupons.dc.html', 'Coupons', 'Seasonal tune-up offers.')])
    + closing('Get on the schedule.', 'Call and we will set the two visits for the year, so neither season catches you out.')
    + FOOTER + STICKY)
print('Maintenance', build('Maintenance', 'Maintenance program', body, h))

# ---------------------------------------------------------------- CONTACT
CONTACT_EXTRA = '''
  issueOptions(primary, secondary) {
    var self = this;
    var picked = (this.state && this.state.issue) || 'heat';
    var looks = {
      heat: { fg: this.shift(primary, -0.34), bg: this.shift(primary, 0.9), ring: primary },
      cool: { fg: this.shift(secondary, -0.3), bg: this.shift(secondary, 0.88), ring: secondary },
      plumb: { fg: 'var(--ink)', bg: 'var(--tint-neutral)', ring: 'var(--ink)' },
      install: { fg: 'var(--ink)', bg: 'var(--tint-neutral)', ring: 'var(--ink)' }
    };
    var opts = [
      { id: 'heat', label: 'No heat', icon: 'M12 2.7c.6 4 3 5.6 4.4 7.6a6.9 6.9 0 1 1-11.5 4.6c0-3 1.7-4.8 2.8-6.3.3 1.9 1.1 2.8 2.1 3.2-.6-3.6.3-7.1 2.2-9.1z' },
      { id: 'cool', label: 'Not cooling', icon: 'M12 2.6v18.8M3.9 7.3l16.2 9.4M3.9 16.7l16.2-9.4' },
      { id: 'plumb', label: 'Leak or blockage', icon: 'M12 2.8s5.6 5.7 5.6 9.4a5.6 5.6 0 1 1-11.2 0C6.4 8.5 12 2.8 12 2.8z' },
      { id: 'install', label: 'Install or replace', icon: 'M4.5 7h15a1.5 1.5 0 0 1 1.5 1.5v7a1.5 1.5 0 0 1-1.5 1.5h-15A1.5 1.5 0 0 1 3 15.5v-7A1.5 1.5 0 0 1 4.5 7zM6 11h12M6 14h12' }
    ];
    return opts.map(function (o) {
      var on = o.id === picked;
      var l = looks[o.id];
      return {
        label: o.label, icon: o.icon,
        pressed: on ? 'true' : 'false',
        fg: on ? l.fg : 'var(--ink-soft)',
        bg: on ? l.bg : 'var(--surface)',
        ring: on ? 'inset 0 0 0 2px ' + l.ring : 'none',
        pick: function () { self.setState({ issue: o.id }); }
      };
    });
  }
  submitLabel() {
    var picked = (this.state && this.state.issue) || 'heat';
    return {
      heat: 'Get my free heating estimate',
      cool: 'Get my free AC estimate',
      plumb: 'Get my free plumbing estimate',
      install: 'Book an install consultation'
    }[picked];
  }
'''
CONTACT_VALS = ''',
      issues: this.issueOptions(primary, secondary),
      submitLabel: this.submitLabel()'''

h = 3700
contact_body = (STATUSBAR + masthead('Contact.dc.html', 'NYHVACServices.dc.html') + crumb('Contact')
+ '''
  <section id="top" style="background: {{dark}}; color: #FFFFFF">
    <div style="max-width: 1280px; margin: 0 auto; padding: 72px 40px 84px; display: flex; flex-wrap: wrap; gap: 64px; align-items: start">
      <div style="flex: 999 1 520px; min-width: 0">
        <p class="heroeyebrow" style="margin: 0 0 22px; font-size: 14px; font-weight: 700; letter-spacing: .2em; text-transform: uppercase; color: #A7B4C0">Contact · Brooklyn, Queens &amp; Manhattan</p>
        <h1 style="margin: 0; font-weight: 800; font-size: 104px; line-height: .86; letter-spacing: -.005em; text-transform: uppercase">
          <span style="display: block">Call us.</span>
          <span style="display: block; color: {{primaryOnDark}}">Any hour.</span>
        </h1>
        <div class="herorule" style="display: flex; width: 200px; height: 5px; margin-top: 30px" aria-hidden="true">
          <span style="flex: 1; background: {{secondary}}"></span>
          <span style="flex: 1; background: {{primary}}"></span>
        </div>
        <p class="herolede" style="margin: 26px 0 0; font-size: 20px; line-height: 1.55; color: #CBD4DD; max-width: 52ch">If something has failed right now, call rather than filling in the form — whoever answers can tell you what to shut off while a technician is on the way.</p>

        <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1px; margin-top: 40px; background: rgba(255,255,255,.14); border: 1px solid rgba(255,255,255,.14); border-radius: 6px; overflow: hidden">
          <div style="background: {{dark}}; padding: 26px 24px">
            <h2 style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: {{primaryOnDark}}">Phone — 24 hours</h2>
            <a href="''' + TEL + '''" style="display: inline-block; margin-top: 10px; font-family: 'Barlow Condensed', 'Roboto Condensed', 'Arial Narrow', sans-serif; font-size: 40px; font-weight: 800; line-height: 1; color: #FFFFFF; text-decoration: none">{{phone}}</a>
            <p style="margin: 10px 0 0; font-size: 15px; color: #A7B4C0">Answered by a person, including nights, weekends and holidays.</p>
          </div>
          <div style="background: {{dark}}; padding: 26px 24px">
            <h2 style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: {{primaryOnDark}}">Email</h2>
            <a href="mailto:[EMAIL]" style="display: inline-block; margin-top: 10px; font-size: 19px; font-weight: 600; color: #FFFFFF; text-decoration: none">[EMAIL ADDRESS]</a>
            <p style="margin: 10px 0 0; font-size: 15px; color: #A7B4C0">For quotes, invoices and anything that is not urgent.</p>
          </div>
          <div style="background: {{dark}}; padding: 26px 24px">
            <h2 style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: {{primaryOnDark}}">Address</h2>
            <p style="margin: 10px 0 0; font-size: 18px; font-weight: 600; color: #FFFFFF">109 S 5th St, 1st Floor<br>Brooklyn, NY 11249</p>
            <p style="margin: 10px 0 0; font-size: 15px; color: #A7B4C0">Williamsburg. Visits by appointment.</p>
          </div>
          <div style="background: {{dark}}; padding: 26px 24px">
            <h2 style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: {{primaryOnDark}}">Hours</h2>
            <p style="margin: 10px 0 0; font-size: 18px; font-weight: 600; color: #FFFFFF">Emergency — 24 hours</p>
            <p style="margin: 10px 0 0; font-size: 15px; color: #A7B4C0">Office hours [ADD OFFICE HOURS]</p>
          </div>
        </div>
      </div>

      <!-- Booking panel -->
      <div id="quote" style="flex: 1 1 400px; min-width: 0; border-radius: 6px; overflow: hidden; box-shadow: 0 40px 90px -40px rgba(0,0,0,.85)">
        <div style="background: {{panelDark}}; padding: 28px 30px">
          <h2 style="margin: 0; color: #FFFFFF; font-size: 26px; font-weight: 700; line-height: 1.05; text-transform: uppercase">Tell us what's going on.</h2>
          <p style="margin: 8px 0 0; color: #A7B4C0; font-size: 15px; line-height: 1.5">Thirty seconds here. We call you back to confirm a time — free estimate, no obligation.</p>
        </div>
        <div style="background: var(--surface); padding: 26px 28px 30px; display: flex; flex-direction: column; gap: 12px">
          <div role="group" aria-label="What's going on?" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 5px; overflow: hidden">
            <sc-for list="{{issues}}" as="opt" hint-placeholder-count="4">
              <button type="button" onClick="{{opt.pick}}" aria-pressed="{{opt.pressed}}" style="min-height: 52px; padding: 15px 16px; display: flex; align-items: center; gap: 10px; border: 0; margin: 0; text-align: left; font-family: inherit; font-weight: 600; font-size: 15.5px; cursor: pointer; transition: background .18s ease, color .18s ease, box-shadow .18s ease; color: {{opt.fg}}; background: {{opt.bg}}; box-shadow: {{opt.ring}}">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none; width: 18px; height: 18px"><path d="{{opt.icon}}"></path></svg>
                <span>{{opt.label}}</span>
              </button>
            </sc-for>
          </div>
          <label for="k-name" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Your name</label>
          <input id="k-name" type="text" placeholder="Your name" style="width: 100%; box-sizing: border-box; padding: 16px 15px; border: 1px solid var(--line); border-radius: 5px; background: var(--surface-2); font-family: inherit; font-size: 16px; font-weight: 500; color: var(--ink)">
          <label for="k-phone" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Phone number</label>
          <input id="k-phone" type="tel" placeholder="Phone number" style="width: 100%; box-sizing: border-box; padding: 16px 15px; border: 1px solid var(--line); border-radius: 5px; background: var(--surface-2); font-family: inherit; font-size: 16px; font-weight: 500; color: var(--ink)">
          <label for="k-zip" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">ZIP code</label>
          <input id="k-zip" type="text" placeholder="ZIP code" style="width: 100%; box-sizing: border-box; padding: 16px 15px; border: 1px solid var(--line); border-radius: 5px; background: var(--surface-2); font-family: inherit; font-size: 16px; font-weight: 500; color: var(--ink)">
          <label for="k-note" style="position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0)">Anything else we should know</label>
          <textarea id="k-note" rows="3" placeholder="Anything else we should know" style="width: 100%; box-sizing: border-box; padding: 16px 15px; border: 1px solid var(--line); border-radius: 5px; background: var(--surface-2); font-family: inherit; font-size: 16px; font-weight: 500; color: var(--ink); resize: vertical"></textarea>
          <button type="button" style="width: 100%; padding: 19px 24px; border: 0; border-radius: 4px; background: var(--ink); color: var(--page); font-family: inherit; font-weight: 700; font-size: 17px; cursor: pointer">{{submitLabel}}</button>
          <p style="margin: 4px 0 0; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 13.5px; color: var(--ink-soft)">
            <svg viewBox="0 0 24 24" fill="none" stroke="{{secondaryOnLight}}" stroke-width="2.6" stroke-linecap="round" aria-hidden="true" style="width: 14px; height: 14px"><path d="M4.5 12.5 9.5 17.5 19.5 7"></path></svg>
            Free estimate. No obligation. Your details stay with us.
          </p>
        </div>
      </div>
    </div>
  </section>

  <section style="border-bottom: 1px solid var(--line)">
    <div style="max-width: 1280px; margin: 0 auto; padding: 80px 40px">
      <h2 style="margin: 0 0 14px; font-size: 60px; font-weight: 800; line-height: .94; text-transform: uppercase">Where we work.</h2>
      <p style="margin: 0 0 36px; font-size: 18px; color: var(--ink-soft); max-width: 62ch">Brooklyn, Queens and Manhattan — those three boroughs and nothing else, which is exactly why we know the buildings. Not sure if we reach your block? Call and ask.</p>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px">
        <div style="border: 1px solid var(--line); border-top: 4px solid {{primary}}; border-radius: 6px; padding: 32px"><h3 style="margin: 0; font-size: 32px; font-weight: 800; text-transform: uppercase">Brooklyn</h3><p style="margin: 8px 0 0; color: var(--ink-soft); font-size: 16px">Home ground. Based in Williamsburg, working across the borough.</p></div>
        <div style="border: 1px solid var(--line); border-top: 4px solid {{secondary}}; border-radius: 6px; padding: 32px"><h3 style="margin: 0; font-size: 32px; font-weight: 800; text-transform: uppercase">Queens</h3><p style="margin: 8px 0 0; color: var(--ink-soft); font-size: 16px">Residential and commercial, with the same response times.</p></div>
        <div style="border: 1px solid var(--line); border-top: 4px solid {{primary}}; border-radius: 6px; padding: 32px"><h3 style="margin: 0; font-size: 32px; font-weight: 800; text-transform: uppercase">Manhattan</h3><p style="margin: 8px 0 0; color: var(--ink-soft); font-size: 16px">Co-ops, condos and storefronts, coordinated with supers and management.</p></div>
      </div>
      <div style="margin-top: 24px; aspect-ratio: 16 / 6; background: var(--surface-2); border: 1px solid var(--line); border-radius: 6px; display: grid; place-items: center; text-align: center; padding: 24px; color: var(--ink-soft); font-size: 15px; font-weight: 600">[MAP — embed a map of the three boroughs, or a pin on 109 S 5th St]</div>
    </div>
  </section>
'''
+ signs('What happens after you call.',
        'No four-hour window that turns into eight, and no surprise invoice at the end of it.',
        [('We take the details', 'The unit, the fault, the building and how urgent it is. Emergencies are dispatched straight away.'),
         ('We agree a window', 'A time that works for you, including after-hours slots for commercial clients.'),
         ('We diagnose and quote', 'The fault is found and priced before any work starts. You approve it, or you do not.'),
         ('We finish and tidy', 'Tested in front of you, the space left clean, and we come back if anything is not right.')])
+ closing('Call 718-551-2029.', 'A real person answers, 24 hours a day, every day of the year.')
+ FOOTER + STICKY)
print('Contact', build('Contact', 'Contact', contact_body, h, CONTACT_EXTRA, CONTACT_VALS))


# ------------------------------------------- rewire home + phone nav links
OLD_NAV_L = '''        <a href="#services" style="text-decoration: none">Heating &amp; cooling</a>
        <a href="#plumbing" style="text-decoration: none">Plumbing</a>
        <a href="#commercial" style="text-decoration: none">Commercial</a>'''
NEW_NAV_L = '''        <a href="Heating.dc.html" style="text-decoration: none">Heating</a>
        <a href="AirConditioning.dc.html" style="text-decoration: none">Air conditioning</a>
        <a href="Plumbing.dc.html" style="text-decoration: none">Plumbing</a>'''

OLD_NAV_R = '''          <a href="#savings" style="text-decoration: none">Savings</a>
          <a href="#reviews" style="text-decoration: none">Reviews</a>
          <a href="#faq" style="text-decoration: none">FAQ</a>'''
NEW_NAV_R = '''          <a href="Commercial.dc.html" style="text-decoration: none">Commercial</a>
          <a href="Financing.dc.html" style="text-decoration: none">Financing</a>
          <a href="About.dc.html" style="text-decoration: none">About</a>'''

OLD_MOB = '''          <a href="#services">Heating &amp; cooling</a>
          <a href="#plumbing">Plumbing</a>
          <a href="#emergency">24-hour emergency</a>
          <a href="#commercial">Commercial</a>
          <a href="#savings">Savings &amp; financing</a>
          <a href="#reviews">Reviews</a>
          <a href="#faq">FAQ</a>
          <a href="#quote" class="mobnav-cta">Book your service</a>'''
NEW_MOB = '''          <a href="Heating.dc.html">Heating</a>
          <a href="AirConditioning.dc.html">Air conditioning</a>
          <a href="Plumbing.dc.html">Plumbing</a>
          <a href="Commercial.dc.html">Commercial</a>
          <a href="About.dc.html">About</a>
          <a href="Financing.dc.html">Financing</a>
          <a href="Coupons.dc.html">Coupons</a>
          <a href="Maintenance.dc.html">Maintenance program</a>
          <a href="Contact.dc.html" class="mobnav-cta">Contact &amp; booking</a>'''

# in-page section links on the home page that now have a real page behind them
HOME_SWAPS = [
    ('<a href="#quote" style="display: inline-block; padding: 14px 20px; border: 1.5px solid var(--ink); border-radius: 4px; color: var(--ink); font-weight: 700; font-size: 15.5px; text-decoration: none">Book your service</a>',
     '<a href="Contact.dc.html" style="display: inline-block; padding: 14px 20px; border: 1.5px solid var(--ink); border-radius: 4px; color: var(--ink); font-weight: 700; font-size: 15.5px; text-decoration: none">Book your service</a>'),
    ('<li><a href="#services" style="text-decoration: none">Furnace &amp; heater repair</a></li>',
     '<li><a href="Heating.dc.html" style="text-decoration: none">Furnace &amp; heater repair</a></li>'),
    ('<li><a href="#services" style="text-decoration: none">Boiler services</a></li>',
     '<li><a href="Heating.dc.html" style="text-decoration: none">Boiler services</a></li>'),
    ('<li><a href="#services" style="text-decoration: none">AC repair &amp; installation</a></li>',
     '<li><a href="AirConditioning.dc.html" style="text-decoration: none">AC repair &amp; installation</a></li>'),
    ('<li><a href="#plumbing" style="text-decoration: none">Emergency plumbing</a></li>',
     '<li><a href="Plumbing.dc.html" style="text-decoration: none">Emergency plumbing</a></li>'),
    ('<li><a href="#plumbing" style="text-decoration: none">Water heaters</a></li>',
     '<li><a href="Plumbing.dc.html" style="text-decoration: none">Water heaters</a></li>'),
    ('<li><a href="#plumbing" style="text-decoration: none">Drain cleaning &amp; hydro jetting</a></li>',
     '<li><a href="Plumbing.dc.html" style="text-decoration: none">Drain cleaning &amp; hydro jetting</a></li>'),
    ('<li><a href="#plumbing" style="text-decoration: none">Sewer line services</a></li>',
     '<li><a href="Plumbing.dc.html" style="text-decoration: none">Sewer line services</a></li>'),
    ('<li><a href="#commercial" style="text-decoration: none">Commercial HVAC &amp; plumbing</a></li>',
     '<li><a href="Commercial.dc.html" style="text-decoration: none">Commercial HVAC &amp; plumbing</a></li>'),
    ('<a href="About.dc.html" style="display: inline-block; margin-top: 26px;',
     '<a href="About.dc.html" style="display: inline-block; margin-top: 26px;'),
]

for fn in ('NYHVACServices.dc.html', 'NYHVACServicesPhone.dc.html'):
    p = ROOT + fn
    s = open(p, encoding='utf-8').read()
    before = s
    for a, b in ((OLD_NAV_L, NEW_NAV_L), (OLD_NAV_R, NEW_NAV_R), (OLD_MOB, NEW_MOB)):
        if a not in s:
            raise SystemExit('nav block not found in ' + fn)
        s = s.replace(a, b)
    hits = 0
    for a, b in HOME_SWAPS:
        if a in s:
            s = s.replace(a, b)
            hits += 1
    open(p, 'w', encoding='utf-8').write(s)
    print(fn, 'nav rewired, footer/CTA swaps:', hits, 'changed:', s != before)


# --------------------------------------------------------------- canvas.json
cv = json.load(open(ROOT + 'canvas.json', encoding='utf-8'))
ROW_A = [('Heating', 4950), ('AirConditioning', 4950), ('Plumbing', 4950), ('Commercial', 4700)]
ROW_B = [('About', 4600), ('Financing', 4150), ('Coupons', 3800), ('Maintenance', 4150), ('Contact', 3700)]
TITLES = dict(PAGES)

ya = 30310
yb = ya + max(x[1] for x in ROW_A) + 120
for row, y in ((ROW_A, ya), (ROW_B, yb)):
    for i, (slug, hh) in enumerate(row):
        cv['boards'][slug + '.dc.html'] = {
            'expand': 'fill', 'h': hh, 'is_interactive': True,
            'title': 'NY HVAC — ' + TITLES[slug], 'w': 1440, 'x': i * 1520, 'y': y,
        }
        if slug + '.dc.html' not in cv['order']:
            cv['order'].append(slug + '.dc.html')

cv['notes']['nyhvacsvc'] = {'kind': 'title1', 'maxW': 6000, 'text': 'NY HVAC Services — service pages',
                            'w': 240, 'x': 0, 'y': ya - 300}
cv['notes']['nyhvacco'] = {'kind': 'title1', 'maxW': 7520, 'text': 'NY HVAC Services — company, offers & contact',
                           'w': 240, 'x': 0, 'y': yb - 300}

json.dump(cv, open(ROOT + 'canvas.json', 'w', encoding='utf-8'), indent=2, sort_keys=True, ensure_ascii=False)
print('canvas boards:', len(cv['boards']), 'order:', len(cv['order']))
