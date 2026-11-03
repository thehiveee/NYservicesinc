# Brand

Everything here is derived from the logo artwork — no colour or typeface was
invented.

## Colour

Three source colours, sampled directly from the logo:

| Name | Hex | Where it came from |
| --- | --- | --- |
| Red | `#ED1C24` | The logo's lower bar (`#FE0000` in the artwork, tempered slightly for screen) |
| Blue | `#346699` | The logo's upper bar and diamond |
| Navy | `#0D1B2A` | Echoes the logo's black letterforms; used as the dark ground |

Every other colour is computed from those by lightening or darkening, so the
palette stays in step if a source colour changes:

| Token | Derivation | Use |
| --- | --- | --- |
| `primaryDeep` | red −14% | CTA fills. White text on it clears 4.5:1 — raw `#ED1C24` does not |
| `primaryOnLight` | red −30% | Red text and icons on light backgrounds (≈7.7:1 on white) |
| `primaryOnDark` | red +42% | Red text on the navy ground |
| `secondaryOnLight` | blue −28% | Blue text on light backgrounds (≈9.5:1 on white) |
| `secondaryOnDark` | blue +45% | Blue text on the navy ground |
| `panelDark` | navy +7% | Booking panel, sticky bar — one step up from the hero |
| `ringColor` | red at 30% alpha | The pulsing ring on the call button |

### Accessibility

Raw logo red on white is about 3.9:1, which fails body-text contrast. That is
why text uses `primaryOnLight` and buttons use `primaryDeep`. If the red is ever
changed, re-check both. Red and blue are also separated in lightness, not hue
alone, so the palette survives colour-blindness.

## Logo

| File | Use |
| --- | --- |
| `assets/nyhvac-logo.png` | Light backgrounds — the primary mark |
| `assets/nyhvac-logo-dark.png` | Dark backgrounds and dark mode |
| `assets/logo-original.png` | The supplied original, white background, unmodified |

Both working files are transparent, 3768 × 664, ~150 KB. They were produced
from the original by `tools/make_logo.py`: the white background is flood-filled
from the border (so the white keylines *inside* the letterforms survive),
cropped tight, upscaled 4× with Lanczos plus an unsharp pass, then quantised.

The dark variant is not a different logo — it is the same mark with the ink
inverted: black letterforms become near-white, the white keyline becomes
near-black, and the blue is lifted so it holds against a dark ground.

**Rules**

- One mark per surface. The page picks light or dark by background, never both.
- No box, plate or panel behind the logo. If it will not read, the background is
  wrong, not the logo.
- Do not set a fixed height *and* a max-width on it without `height: auto`, or
  it squashes horizontally on narrow screens.

## Type

Google Fonts, two families:

- **Barlow Condensed** (600/700/800) — all headings, stat figures, the wordmark
  lockup. Set uppercase, tight leading (0.84–0.94), weight 800 at display sizes.
- **Barlow** (400/500/600/700) — body, navigation, buttons, labels.

Fallback stack is Roboto Condensed → Arial Narrow → Liberation Sans Narrow for
the condensed face, and system sans for the body.

## Voice

Taken from the company's own line — *fast, friendly, honest* — and from what
their About page already says.

- Plain and specific. "A person answers, 24 hours a day", not "exceptional
  customer service".
- Claims must be theirs. Everything on the site traces to something the company
  has said about itself.
- Honest where it costs something. "This has a few years left in it" is a
  selling point; so is naming the three boroughs rather than implying wider
  coverage.
- No invented statistics, no stock testimonials. The three reviews are real and
  quoted word for word.
