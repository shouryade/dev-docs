There was no output of my laptop when I connected with an HDMI cable. The solution was to use a new display mode with params that were supported by the HDMI cable.

```bash
 xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
```

By running this command, you are defining a new display mode with the specified resolution, refresh rate, and timings. After defining this mode, you can use it with the `xrandr` command to change your display to this resolution and refresh rate if your hardware supports it.

## Explanation

This command is using the `xrandr` tool, which is a command-line interface to the X Resize, Rotate, and Reflect Extension (RandR) used in X Window System. The purpose of this specific command is to create a new display mode with a resolution of 1920x1080 pixels and a refresh rate of 60 Hz.

1. `--newmode "1920x1080_60.00"`: This part of the command defines a new display mode with a label "1920x1080_60.00". The format is `"widthxheight_refreshrate"`. In this case, the width is 1920 pixels, the height is 1080 pixels, and the refresh rate is 60 Hz.

2. `173.00`: This number represents the dot clock, which is the speed at which the pixels are transmitted for display. It is typically measured in MHz.

3. `1920 2048 2248 2576`: These numbers represent the horizontal timings of the display mode in pixels. Specifically, they denote the active width, the front porch, the sync width, and the back porch, respectively.

4. `1080 1083 1088 1120`: These numbers represent the vertical timings of the display mode in pixels. Similar to the horizontal timings, they denote the active height, the front porch, the sync width, and the back porch, respectively.

5. `-hsync +vsync`: These parameters specify the sync polarity. `-hsync` indicates negative horizontal sync, and `+vsync` indicates positive vertical sync. These settings are important for ensuring the proper synchronization between the graphics card and the monitor.
