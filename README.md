# NY HVAC Services — website

Marketing site for **NY HVAC Services Inc**, a family owned heating, cooling and
plumbing company operating in Brooklyn, Queens and Manhattan.

- **Phone:** 718-551-2029 (answered 24 hours)
- **Address:** 109 S 5th St, 1st Floor, Brooklyn, NY 11249
- **Service area:** Brooklyn, Queens and Manhattan — these three boroughs only

---

## Layout

```
canvas/     Design-canvas artboards (.dc.html) — THE SOURCE OF TRUTH
assets/     Logo files (transparent PNG, light and dark variants)
site/       Generated static site — do not hand-edit, it is overwritten
tools/      Build scripts
```

### `canvas/` — source of truth

Eleven `.dc.html` artboards plus `canvas.json`. These are Design Component
files: self-contained HTML that runs inside Claude's Design canvas, where the
pages were laid out and where edits should continue to be made.

| Artboard | Page |
| --- | --- |
| `NYHVACServices.dc.html` | Home |
| `NYHVACServicesPhone.dc.html` | Home, framed at 390px for review |
| `Heating.dc.html` | Heating |
| `AirConditioning.dc.html` | Air conditioning |
| `Plumbing.dc.html` | Plumbing |
| `Commercial.dc.html` | Commercial |
| `About.dc.html` | About us |
| `Financing.dc.html` | Financing |
| `Coupons.dc.html` | Coupons |
| `Maintenance.dc.html` | Maintenance program |
| `Contact.dc.html` | Contact |

Every page is responsive; the phone artboard is the same file at a narrower
frame, not a separate mobile build.

### `site/` — the deployable site

Plain HTML with no build step, no framework and no JavaScript. Ten pages,
~40 KB each. Serve the repo root and open `site/index.html`, or point a host
at `site/` and move `assets/` alongside it.

```bash
python3 tools/build_site.py      # regenerate site/ from canvas/
python3 -m http.server 8000      # then open http://localhost:8000/site/
```

### `tools/`

| Script | What it does |
| --- | --- |
| `build_site.py` | Converts `canvas/*.dc.html` into `site/*.html` |
| `gen_pages.py` | Generates the nine inner artboards from shared chrome + per-page content |
| `make_logo.py` | Rebuilds the logo PNGs from `assets/logo-original.png` |

`gen_pages.py` is how the inner pages were produced: the header, footer, sticky
bar and stylesheet live in one place, so a change to the chrome propagates to
every page. Edit the chrome there rather than in eleven files.

---

## What the build does

`canvas/` files carry `{{token}}` holes and Design-runtime tags. `build_site.py`:

- resolves the brand tokens to literal colours
- lifts `<helmet>` into `<head>` and unwraps `<x-dc>`
- drops the runtime script and `support.js`
- rewrites `/_blob/<id>` asset URLs to `../assets/*.png`
- rewrites `Page.dc.html` links to `page.html`
- replaces the templated issue picker with CSS-only radio buttons
- **drops the exit-intent pop-up**, which needs the canvas runtime's state

The pop-up is the one feature present on the canvas and absent from the static
build. If it is wanted in production, it needs ~20 lines of vanilla JS or
whatever the host platform provides.

The build fails loudly rather than shipping broken output: an unresolved token
or a leftover runtime tag raises and stops.

---

## Brand

See [`BRAND.md`](BRAND.md). In short:

| Token | Value | Use |
| --- | --- | --- |
| Red | `#ED1C24` | From the logo. Accents, rules, CTA fills (deepened) |
| Blue | `#346699` | From the logo. Secondary accent, cooling |
| Navy | `#0D1B2A` | Dark sections, hero, headings |

All three are sampled from the logo artwork. Colours derive from these by a
lighten/darken function, so changing one of the three recolours the whole site
consistently — in `build_site.py` for the static build, or in each artboard's
Tweaks panel on the canvas.

---

## Before this goes live

See [`CONTENT-TODO.md`](CONTENT-TODO.md) for the full list. The site is
structurally complete but carries bracketed placeholders — `[EMAIL ADDRESS]`,
`[OFFICE HOURS]`, `[LICENSE NO.]` and others — wherever a real detail was not
available. Search for `[` in `canvas/` to find every one.

Nothing in the copy claims anything the company has not claimed itself. The
30-years, family-owned, all-brands-serviced, 24-hour and financing points all
come from their own site; the three customer reviews are quoted verbatim.
