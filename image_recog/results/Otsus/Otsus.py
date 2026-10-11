from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\Bipro\OneDrive\Documents\Study\image_recog\image\images.jpg").convert("L")
px = np.array(img)
h, w = px.shape

pix_list = []
for i in range(h):
    for j in range(w):
        pix_list.append(px[i][j])

best_score = None
best_threshold = 0

for a in range(0, 256):
    dark = []
    bright = []
    for k in range(len(pix_list)):
        if pix_list[k] <= a:
            dark.append(pix_list[k])
        else:
            bright.append(pix_list[k])

    if len(dark) == 0 or len(bright) == 0:
        continue

    avg_dark = sum(dark) / len(dark)
    avg_bright = sum(bright) / len(bright)

    var_dark = sum((v - avg_dark)**2 for v in dark) / len(dark)
    var_bright = sum((v - avg_bright)**2 for v in bright) / len(bright)

    total = len(dark) + len(bright)
    w_dark = len(dark) / total
    w_bright = len(bright) / total

    score = w_dark * var_dark + w_bright * var_bright

    if best_score is None or score < best_score:
        best_score = score
        best_threshold = a

canvas = np.where(px <= best_threshold, 0, 255).astype(np.uint8)
Image.fromarray(canvas).save("otsu_result.png")
print("threshold:", best_threshold)