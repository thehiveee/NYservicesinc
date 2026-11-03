from PIL import Image, ImageFilter
import numpy as np
from collections import deque

SRC = '/mnt/user-data/attachments/e8a34c17-06b4-5615-96e9-ae989328367f/b76af360-image.png'
OUT = '/tmp/claude-0/-home-claude/e8a34c17-06b4-5615-96e9-ae989328367f/scratchpad/logo/'

im = Image.open(SRC).convert('RGBA')
a = np.array(im).astype(np.int16)
h, w = a.shape[:2]
rgb = a[:, :, :3]

# --- 1. background removal: flood fill near-white from the border ---
near_white = (rgb[:, :, 0] > 228) & (rgb[:, :, 1] > 228) & (rgb[:, :, 2] > 228)
bg = np.zeros((h, w), bool)
q = deque()
for x in range(w):
    for y in (0, h - 1):
        if near_white[y, x] and not bg[y, x]:
            bg[y, x] = True; q.append((y, x))
for y in range(h):
    for x in (0, w - 1):
        if near_white[y, x] and not bg[y, x]:
            bg[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w and near_white[ny, nx] and not bg[ny, nx]:
            bg[ny, nx] = True; q.append((ny, nx))

alpha = np.full((h, w), 255, np.int16)
alpha[bg] = 0
# soften the 1px fringe: partially transparent where a kept pixel touches background
lum = rgb.mean(axis=2)
fringe = (~bg) & (lum > 232)
nb = np.zeros((h, w), bool)
nb[1:,:] |= bg[:-1,:]; nb[:-1,:] |= bg[1:,:]; nb[:,1:] |= bg[:,:-1]; nb[:,:-1] |= bg[:,1:]
alpha[fringe & nb] = 90

# --- 2. crop to content ---
ys, xs = np.where(alpha > 0)
y0, y1, x0, x1 = ys.min(), ys.max()+1, xs.min(), xs.max()+1
pad = 6
y0, x0 = max(0, y0-pad), max(0, x0-pad)
y1, x1 = min(h, y1+pad), min(w, x1+pad)

base = np.dstack([rgb, alpha]).astype(np.uint8)[y0:y1, x0:x1]
bh, bw = base.shape[:2]
print('cropped to', bw, 'x', bh)

def upscale(arr, factor=4):
    img = Image.fromarray(arr, 'RGBA')
    big = img.resize((arr.shape[1]*factor, arr.shape[0]*factor), Image.LANCZOS)
    return big.filter(ImageFilter.UnsharpMask(radius=2.2, percent=85, threshold=2))

# --- 3. light-mode logo (original colours) ---
light = upscale(base)
light.save(OUT+'nyhvac-logo.png', optimize=True)
print('light', light.size)

# --- 4. dark-mode logo: black ink -> near-white, white outline -> near-black, blue lifted ---
d = base.copy().astype(np.int16)
r, g, b, al = d[:,:,0], d[:,:,1], d[:,:,2], d[:,:,3]
l = (r + g + b) / 3.0
sat = d[:,:,:3].max(axis=2) - d[:,:,:3].min(axis=2)
neutral = sat < 42
ink    = neutral & (l < 95)   & (al > 0)   # black letterforms
paper  = neutral & (l > 205)  & (al > 0)   # white outlines / keylines
mid    = neutral & (l >= 95) & (l <= 205) & (al > 0)
blue   = (b > r + 28) & (b > 70)

for ch, v in ((0, 244), (1, 246), (2, 249)):
    d[:,:,ch][ink] = v
for ch, v in ((0, 16), (1, 20), (2, 26)):
    d[:,:,ch][paper] = v
# antialiased mid-greys: invert around the midpoint so edges stay smooth
inv = (255 - l).clip(0, 255)
for ch in range(3):
    d[:,:,ch][mid] = inv[mid]
# lift the blue so it holds up on a dark ground
d[:,:,0][blue] = (r[blue] * 1.00 + 46).clip(0, 255)
d[:,:,1][blue] = (g[blue] * 1.00 + 40).clip(0, 255)
d[:,:,2][blue] = (b[blue] * 1.00 + 30).clip(0, 255)

dark = upscale(d.astype(np.uint8))
dark.save(OUT+'nyhvac-logo-dark.png', optimize=True)
print('dark', dark.size)
