# Content still needed

Every item below appears in the pages as a bracketed placeholder. Fill them in
`canvas/`, then re-run `python3 tools/build_site.py`.

Find them all with:

```bash
grep -rno '\[[A-Z][^]]*\]' canvas/
```

## Blocking — these appear on every page

| Placeholder | Where | Notes |
| --- | --- | --- |
| `[EMAIL ADDRESS]` / `[EMAIL]` | Status strip + footer, all 11 pages | No email is published on the current site. Needed, or remove the slot entirely. |
| `[OFFICE HOURS]` | Footer, Contact | The 24-hour emergency line is covered; this is the office's own hours. |
| `[LICENSE NO.]` | Footer | NY contractor licence number. |
| `[SOCIAL LINKS]` | Footer | Or delete the line if there are no accounts to link. |

## High value — these are conversion copy

| Placeholder | Where | Notes |
| --- | --- | --- |
| `[X.X]` + `[Average rating]` + `[Google]` | Home, About, reviews block | Star rating and review count. Strong proof; worth getting right. |
| `[YEAR]` | Home hero trust row | Founding year. The copy says "nearly thirty years" — a real year is better. |
| `[BRAND]` ×8 | Home + Financing brand row | Five brand names. **Lennox is confirmed** (their site runs a Lennox promotion); four more needed. |
| `[COUPON — e.g. $XX off your first service call]` | Exit pop-up, home | One headline offer. |
| `[LIST THIS MONTH'S OFFERS]` | Home savings block | |

## Coupons page

The live coupons page would not load, so all three offer cards are shaped but
empty. Each needs: what it is worth, what it applies to, and the expiry date.

- `[$XX off a service call]`
- `[$XXX off a new system]`
- `[Seasonal tune-up price]`

## Maintenance program page

Same situation — the program page would not load.

- `[MEMBERSHIP PRICE AND WHAT'S INCLUDED]`
- `[MEMBER BENEFITS]` — priority response, repair discount, waived diagnostic fee?
- `[CONFIRM AND EDIT THIS LIST AGAINST YOUR ACTUAL PROGRAM]` — the two-visit
  breakdown is written from standard practice and needs checking against what
  is actually delivered.

## Financing page

- `[ADD LENDER NAME AND TERMS]` — the three claims on the page (no-interest and
  low-monthly options, fast online credit decision, online account access) are
  taken from the company's own financing page and are safe. The lender and the
  actual terms are not published anywhere and need supplying.

## Images

| Placeholder | Where |
| --- | --- |
| `[PHOTO — one of your technicians on a real Brooklyn job, portrait orientation]` | Home, About |
| `[MAP — embed a map of the three boroughs, or a pin on 109 S 5th St]` | Contact |

Real job photography matters more than usual here, because the whole positioning
is "family owned, local, thirty years". Stock photography actively undercuts it.

---

## Known inconsistency

The homepage footer has four columns — logo, Services, Contact, Hours — while
the nine inner pages have logo, Services, **Company**, Contact. The homepage is
missing the Company column (About / Financing / Coupons / Contact links). Worth
reconciling before launch; the inner-page version is the better of the two.

## Not a placeholder, but worth a decision

- **The exit-intent pop-up** exists on the canvas and is dropped from the static
  build (it needs the canvas runtime). Decide whether production wants it.
- **The tri-state claim.** The company's own About page says "Providing
  Excellent Service Near the Tri-State Area", but this site says Brooklyn,
  Queens and Manhattan only, on instruction. If the wider area is real, the site
  is underselling; if not, their live site needs correcting.
