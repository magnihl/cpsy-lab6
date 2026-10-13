# /// script
# dependencies = ["matplotlib"]
# ///
"""Draw Figure 6-1, the emergency stop circuit, for the Lab 6 notebook.

Run on the laptop:  uv run fig61.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

INK, MUTED = "#0b0b0b", "#52514e"
LW = 1.3

fig, ax = plt.subplots(figsize=(4.7, 3.3), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 72)
ax.axis("off")


def wire(pts):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=INK, linewidth=LW, solid_capstyle="round")


def resistor(x0, y0, x1, y1, label, sub=None):
    """Zigzag between two points, horizontal or vertical."""
    n, amp = 6, 3.0
    if y0 == y1:
        seg = (x1 - x0) / n
        pts = [(x0, y0)]
        for i in range(n):
            pts.append((x0 + seg * (i + 0.5), y0 + (amp if i % 2 == 0 else -amp)))
        pts.append((x1, y1))
        ax.text((x0 + x1) / 2, y0 + 7, label, ha="center", va="bottom",
                fontsize=8, color=INK)
        if sub:
            ax.text((x0 + x1) / 2, y0 - 8, sub, ha="center", va="top",
                    fontsize=7, color=MUTED)
    else:
        seg = (y1 - y0) / n
        pts = [(x0, y0)]
        for i in range(n):
            pts.append((x0 + (amp if i % 2 == 0 else -amp), y0 + seg * (i + 0.5)))
        pts.append((x1, y1))
        ax.text(x0 + 6, (y0 + y1) / 2, label, ha="left", va="center",
                fontsize=8, color=INK)
        if sub:
            ax.text(x0 + 6, (y0 + y1) / 2 - 6, sub, ha="left", va="center",
                    fontsize=7, color=MUTED)
    wire(pts)


def node(x, y):
    ax.plot([x], [y], marker="o", markersize=4, color=INK)


# the Pi, as a dashed boundary
ax.add_patch(Rectangle((3, 8), 34, 58, fill=False, linestyle=(0, (4, 3)),
                       edgecolor=MUTED, linewidth=0.9))
ax.text(5, 68, "Raspberry Pi Zero", fontsize=8, color=MUTED, va="bottom")

# internal 3V3 and pull up down to the GPIO4 node
ax.text(14, 62, "3V3", fontsize=8, color=INK, ha="center")
wire([(14, 60), (14, 56)])
resistor(14, 56, 14, 44, "internal", "pull up")
wire([(14, 44), (14, 38), (37, 38)])
node(14, 38)
ax.text(17, 35, "GPIO4", fontsize=8, color=INK, ha="left", va="top")

# pin 7 out to the series resistor, the switch, and back to the rail
ax.text(39, 40, "pin 7", fontsize=8, color=INK, ha="left", va="bottom")
wire([(37, 38), (52, 38)])
resistor(52, 38, 68, 38, "1k")
wire([(68, 38), (76, 38)])

# switch, drawn open
node(76, 38)
wire([(76, 38), (87, 47)])
node(89, 38)
wire([(89, 38), (95, 38), (95, 18)])
ax.text(82, 51, "stop switch", fontsize=8, color=INK, ha="center")

# the breadboard blue rail back to pin 9
wire([(95, 18), (37, 18)])
ax.text(66, 15, "breadboard blue rail", fontsize=7.5, color=MUTED,
        ha="center", va="top")
ax.text(39, 20, "pin 9", fontsize=8, color=INK, ha="left", va="bottom")

# ground symbol inside the Pi
wire([(37, 18), (20, 18), (20, 14)])
for i, w in enumerate((7, 4.5, 2)):
    y = 14 - i * 2.2
    ax.plot([20 - w, 20 + w], [y, y], color=INK, linewidth=LW)
ax.text(20, 4, "GND", fontsize=8, color=INK, ha="center", va="top")

fig.tight_layout(pad=0.2)
fig.savefig("fig6-1.png")
print("wrote fig6-1.png")
