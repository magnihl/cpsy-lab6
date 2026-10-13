# /// script
# dependencies = ["matplotlib"]
# ///
"""Put Figure 6-1 on an A4 sheet at its true size, with the caption.

Print at 100 percent, not "fit to page", then cut and paste into the
notebook on page 2.

Run on the laptop:  uv run printsheet.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

A4 = (8.27, 11.69)
FIG_W, FIG_H = 4.7, 3.3
INK, MUTED = "#0b0b0b", "#52514e"

CAPTION = (
    "Figure 6-1. Emergency stop circuit as built, 6 Oct 2026. GPIO4's\n"
    "internal pull up holds the line high; closing the switch pulls it to\n"
    "ground through the breadboard rail. The 1k limits current if the pin\n"
    "is ever misconfigured as an output, it does not debounce. Debouncing\n"
    "is in software at 50 ms, gpiozero Button bounce_time. The stop drops\n"
    "the DRV8833 SLP pin on GPIO25 rather than commanding the motors, so\n"
    "it still works if the control loop is wedged."
)

fig = plt.figure(figsize=A4, dpi=300)
left = (A4[0] - FIG_W) / 2 / A4[0]
width = FIG_W / A4[0]
height = FIG_H / A4[1]
bottom = 1 - (0.06 + height)

ax = fig.add_axes([left, bottom, width, height])
ax.imshow(mpimg.imread("fig6-1.png"))
ax.axis("off")
fig.text(left, bottom - 0.015, CAPTION, fontsize=7.5, color=INK,
         va="top", ha="left", linespacing=1.5)
fig.text(left, 0.975, "CPSY Lab 6 figure, cut along the edges",
         fontsize=7, color=MUTED, va="top")
fig.savefig("lab6-print-sheet.pdf")
print("wrote lab6-print-sheet.pdf")
