import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

# Function to draw the split W
def draw_split_w(ax):
    vertices = [
        (0.2, 0.8), (0.3, 0.5), (0.4, 0.2),  # Left leg
        (0.5, 0.8), (0.6, 0.5), (0.7, 0.2),  # Right leg
        (0.8, 0.8)
    ]
    codes = [
        Path.MOVETO, Path.LINETO, Path.LINETO,
        Path.MOVETO, Path.LINETO, Path.LINETO,
        Path.MOVETO
    ]
    path = Path(vertices, codes)
    patch = PathPatch(path, facecolor='none', edgecolor='purple', linewidth=15, capstyle='round', joinstyle='round')
    ax.add_patch(patch)

# Function to draw the interwoven W
def draw_interwoven_w(ax):
    vertices = [
        (0.2, 0.8), (0.25, 0.5), (0.3, 0.8),  # Left leg
        (0.35, 0.6), (0.4, 0.2),  # Left leg cross
        (0.5, 0.8), (0.55, 0.5), (0.6, 0.8),  # Right leg
        (0.65, 0.6), (0.7, 0.2),  # Right leg cross
        (0.8, 0.8)
    ]
    codes = [
        Path.MOVETO, Path.LINETO, Path.LINETO,
        Path.MOVETO, Path.LINETO,
        Path.MOVETO, Path.LINETO, Path.LINETO,
        Path.MOVETO, Path.LINETO,
        Path.MOVETO
    ]
    path = Path(vertices, codes)
    patch = PathPatch(path, facecolor='none', edgecolor='purple', linewidth=15, capstyle='round', joinstyle='round')
    ax.add_patch(patch)

# Create figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Draw the split W
draw_split_w(axes[0])
axes[0].set_xlim(0, 1)
axes[0].set_ylim(0, 1)
axes[0].axis('off')
axes[0].set_title('Split W')

# Draw the interwoven W
draw_interwoven_w(axes[1])
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1)
axes[1].axis('off')
axes[1].set_title('Interwoven W')

# Display the plot
plt.savefig('logo-w .png')
