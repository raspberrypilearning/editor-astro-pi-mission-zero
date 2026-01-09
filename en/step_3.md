<h2 class="c-project-heading--task">Draw a picture</h2>
--- task ---
Edit your `image` to create your own picture
--- /task ---

<h2 class="c-project-heading--explainer">PROBABLY UNNECCESARY TITLE</h2>

By adding more colours, and changing the `image` list, you can create your very own picture on the LED matrix.

The following is an example of a fish

![fish](images/fish.png)

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
z = (153, 50, 204) # DarkOrchid
q = (255, 255, 0) # Yellow
d = (51, 153, 255) # blue
c = (0, 0, 0) # Black

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