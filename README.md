# York University HP Plotter Art 1970
*Arthur Ryman, last updated 2025-11-29*

This repo contains art I created in 1970 at York University using an HP plotter located in
the Math Department.

Most plots were created by connecting successive points that on a
[Lissajou curve](https://en.wikipedia.org/wiki/Lissajous_curve) that are separated
by some large, fixed parameter delta value. 
Using a very small delta would produce a smooth curve. 
Using a large delta produces "string" art. 
The intersection points of the strings produce interesting secondary curves.

I scanned the original paper plots using an Epson FastFoto FF-680W scanner.
The scanner software produces both a verbatim copy, e.g. FastFoto_0025.jpg,
and an enhanced version, e.g. FastFoto_0025_a.jpg.

The HP plotter was connected to an HP programmable calculator, but not to
any network or computer.
The programs were stored on small magnetic cards.
Due to the limited memory of the programmable calculator, 
my only option was to create plots
from simple mathematical procedures, hence the use of Lissajou curves.

Each Lissajou plot is described three parameters, namely the horizontal and vertical
frequencies and the time value step size.

In addition to the x-y Lissajou figures, 
a few plots were expressed in polar coordinates where the radius was a function of the 
angle. These made rosette patterns.

I plan to recreate the math in Python programs. 
I will then be able to reverse engineer the scanned images and 
add the plot type and parameter values to the titles.

Watch this space.
