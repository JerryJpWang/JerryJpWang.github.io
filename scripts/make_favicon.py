from PIL import Image

# Symmetric pixel-art cat head, authored as a half-grid (columns 0..HALF-1)
# and mirrored around the seam so column HALF-1 sits next to column HALF.
HALF = 12
H = 24
W = HALF * 2

TRANS = (0, 0, 0, 0)
OUTLINE = (35, 28, 24, 255)
FUR = (247, 165, 79, 255)
INNER_EAR = (255, 202, 168, 255)
EYE = (58, 150, 90, 255)
NOSE = (216, 108, 120, 255)

# Each row: (left_bound, right_cap) -> filled columns are [left_bound, right_cap].
# right_cap < HALF-1 for the ear rows keeps a gap between the two ears at the
# top; once right_cap reaches HALF-1 the ear merges into the head silhouette.
rows_spec = {
    0: (8, 9),
    1: (7, 9),
    2: (6, 9),
    3: (5, 9),
    4: (4, 9),
    5: (4, 11),
    6: (3, 11),
    7: (2, 11),
    8: (1, 11),
    9: (0, 11),
    10: (0, 11),
    11: (0, 11),
    12: (0, 11),
    13: (0, 11),
    14: (0, 11),
    15: (0, 11),
    16: (1, 11),
    17: (2, 11),
    18: (3, 11),
    19: (5, 11),
    20: (7, 11),
    21: (9, 11),
    22: (10, 11),
}

grid = [['.' for _ in range(HALF)] for _ in range(H)]

for row, (b, cap) in rows_spec.items():
    for c in range(b, cap + 1):
        grid[row][c] = 'F'
    grid[row][b] = 'O'  # left outline
    if row <= 4:
        grid[row][cap] = 'O'  # ear's own right outline while still separate

# inner ear highlight near the tips
grid[1][9] = 'I'
grid[2][8] = 'I'
grid[2][9] = 'I'
grid[3][8] = 'I'

# eyes
for r in (10, 11):
    for c in (3, 4):
        grid[r][c] = 'E'

# nose (1px per half -> 2px wide once mirrored)
grid[14][11] = 'N'
grid[15][11] = 'N'

COLORS = {
    '.': TRANS, 'O': OUTLINE, 'F': FUR,
    'I': INNER_EAR, 'E': EYE, 'N': NOSE,
}

for row in grid:
    mirrored = row + row[::-1]
    print(''.join(mirrored))

img = Image.new("RGBA", (W, H), TRANS)
px = img.load()
for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        color = COLORS[ch]
        px[x, y] = color
        px[W - 1 - x, y] = color

img.save("static/fav.png")
img.resize((256, 256), Image.NEAREST).save("static/fav_preview.png")

sizes = [16, 24, 32, 48]
imgs = [img.resize((s, s), Image.NEAREST) for s in sizes]
imgs[0].save("static/favicon.ico", format="ICO", sizes=[(s, s) for s in sizes])

print("done")
