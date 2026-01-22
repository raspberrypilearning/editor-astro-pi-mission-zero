<h2 class="c-project-heading--task">Keep the colour changing</h2>
--- task ---
The colour can be updated as the sensor changes.
--- /task ---

<h2 class="c-project-heading--explainer">Use a loop with a pause</h2>

Add a `for` loop to your code, so that the colour sensor is checked every second, and your image is updated.

This program will run for 28 seconds.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 19, 36
---
# Add colour variables and image
z = (153, 50, 204) # Tail and fins
q = (255, 255, 0) # Body
d = (51, 153, 255) # Water
c = (0, 0, 0) # Eye

for i in range(28):
    rgb = sense.color # get the colour from the sensor
    c = (rgb.red, rgb.green, rgb.blue) # colour the fish eye

    image = [
        d, d, z, d, d, d, d, d,
        d, d, d, z, z, d, d, d,
        z, d, q, q, q, q, d, d,
        z, z, q, q, q, c, q, d,
        z, z, z, q, q, q, q, d,
        z, z, q, q, q, q, q, d,
        z, d, q, z, z, q, d, d,
        d, d, d, z, d, d, d, d
        ]

    # Display the image
    sense.set_pixels(image)
    sleep(1)
--- /code ---
</div>

<div class="c-project-output">
![animation of astro pi showing colour picker being changed and fish colours changing as a result](images/colour-change.gif)
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure you have **four** spaces of indentation on all lines below the `for` loop.

Don't forget to add the `sleep(1)` on the last line, to give you time to change the colours.

</div>