import numpy as np
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Define colors
sky_color = "#87CEEB"  # Light blue for the sky
sun_color = "#FFD700"   # Yellow for the sun
mountain_color = "#008000"  # Green for the mountains
earth_color = "#228B22"  # Green for the earth surface
sea_color = "#6495ED"    # Blue for the sea surface

# Set the background color to sky_color
fig.patch.set_facecolor(sky_color)
ax.set_facecolor(sky_color)

# Create the sea surface
sea = plt.Rectangle((0, 0), 4, 0.7, linewidth=0, edgecolor="none", facecolor=sea_color)
ax.add_artist(sea)

# Create the earth surface
earth = plt.Rectangle((0, 0.7), 4, 0.3, linewidth=0, edgecolor="none", facecolor=earth_color)
ax.add_artist(earth)

# Create the sun as a larger yellow circle
sun_radius = 0.3  # Adjust the size as needed
sun_center = (0.8, 3.3)  # Adjust the position as needed
sun = plt.Circle(sun_center, sun_radius, color=sun_color)
ax.add_artist(sun)

# Create three mountains
mountain_heights = [1.2, 1.8, 1.5]  # Adjust the heights as needed
mountain_positions = [(0, 1.0), (3, 1.0), (1.5, 1.0)]  # Adjust the positions as needed

for height, position in zip(mountain_heights, mountain_positions):
    mountain_points = np.array([[position[0], position[1]], [position[0] + 1.5, position[1]], [position[0] + 0.75, position[1] + height], [position[0], position[1]]])
    ax.fill(mountain_points[:, 0], mountain_points[:, 1], mountain_color)

# Set axis limits and aspect ratio
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_aspect('equal')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

# Display the improved sunrise scene with the sea surface
plt.show()
