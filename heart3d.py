import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ============================================================
# 3D RED & WHITE HEART
# ============================================================

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

fig.patch.set_facecolor("black")
ax.set_facecolor("black")


# ============================================================
# HEART EQUATION
# ============================================================

u = np.linspace(0, 2 * np.pi, 180)
v = np.linspace(0, np.pi, 90)

U, V = np.meshgrid(u, v)

# Heart surface
r = 1.0

x = r * 16 * np.sin(U) ** 3
y = r * (
    13 * np.cos(U)
    - 5 * np.cos(2 * U)
    - 2 * np.cos(3 * U)
    - np.cos(4 * U)
)

# Make it 3D
z = 2.0 * np.sin(V)

# Spread the heart surface
X = x * (0.18 + 0.82 * np.sin(V))
Y = y * (0.18 + 0.82 * np.sin(V))
Z = z + 0.15 * np.cos(U)


# ============================================================
# OUTER HEART
# ============================================================

def draw_heart(frame):

    ax.clear()

    # --------------------------------------------------------
    # Camera
    # --------------------------------------------------------

    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_zlim(-2.5, 2.5)

    ax.set_box_aspect([1, 1, 0.8])

    ax.set_axis_off()

    # ========================================================
    # MAIN RED HEART
    # ========================================================

    ax.plot_surface(
        X,
        Y,
        Z,
        color="#e60000",
        alpha=0.95,
        linewidth=0,
        antialiased=True,
        shade=True
    )

    # ========================================================
    # WHITE DECORATIVE HEART OUTLINE
    # ========================================================

    outline_u = np.linspace(
        0,
        2 * np.pi,
        500
    )

    hx = (
        16 * np.sin(outline_u) ** 3
    )

    hy = (
        13 * np.cos(outline_u)
        - 5 * np.cos(2 * outline_u)
        - 2 * np.cos(3 * outline_u)
        - np.cos(4 * outline_u)
    )

    hx *= 0.18
    hy *= 0.18

    hz = np.ones_like(hx) * 2.05

    ax.plot3D(
        hx,
        hy,
        hz,
        color="white",
        linewidth=3
    )

    # ========================================================
    # WHITE GLOW DOTS
    # ========================================================

    dots = 35

    for i in range(dots):

        angle = (
            2 * np.pi * i / dots
        )

        radius = 2.8

        dx = radius * np.sin(angle)
        dy = radius * np.cos(angle)
        dz = 0.2

        ax.scatter(
            dx,
            dy,
            dz,
            color="white",
            s=15,
            alpha=0.8
        )

    # ========================================================
    # WHITE HEART HIGHLIGHT
    # ========================================================

    highlight_u = np.linspace(
        0.7,
        2.2,
        80
    )

    highlight_x = (
        16 * np.sin(highlight_u) ** 3
    )

    highlight_y = (
        13 * np.cos(highlight_u)
        - 5 * np.cos(2 * highlight_u)
        - 2 * np.cos(3 * highlight_u)
        - np.cos(4 * highlight_u)
    )

    highlight_x *= 0.18
    highlight_y *= 0.18

    highlight_z = np.ones_like(
        highlight_x
    ) * 2.08

    ax.plot3D(
        highlight_x,
        highlight_y,
        highlight_z,
        color="white",
        linewidth=4,
        alpha=0.9
    )

    # ========================================================
    # ROTATION
    # ========================================================

    ax.view_init(
        elev=20,
        azim=frame
    )


# ============================================================
# ANIMATION
# ============================================================

animation = FuncAnimation(
    fig,
    draw_heart,
    frames=360,
    interval=40,
    repeat=True
)

plt.show()