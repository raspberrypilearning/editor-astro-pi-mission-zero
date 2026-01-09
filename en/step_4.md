<h2 class="c-project-heading--task">Sense a colour</h2>
--- task ---
The Astro Pi has a colour sensor, to detect colours
--- /task ---

<h2 class="c-project-heading--explainer">Use the colour sensor to change your image</h2>

Choose a new letter to store what the colour sensor is "seeing". Then add this colour into your picture somewhere.

It could be:
- The eye colour of a face
- The background colour
- The colour of a flower's petals
- Whatever you like

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13
line_highlights: 
---
# Add colour variables and image
z = (153, 50, 204) # Tail and fins
q = (255, 255, 0) # Body
d = (51, 153, 255) # Water
c = (0, 0, 0) # Eye

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
d, d, d, z, d, d, d, d]
--- /code ---
</div>

Before you click **Run**, change the colour on the colour sensor.
![colour sensor](images/colour_sensor.png)

<div class="c-project-output">
<pre>WHAT THEY SHOULD SEE IF OUTPUT IS TEXT - OTHERWISE USE IMAGE</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

BULLET POINT TIPS HERE (OPTIONAL)

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

BULLET POINT DEBUG POINTS HERE (OPTIONAL)

</div>