# Collage.py

Collage.py was created when I needed to quickly produce compilations of cropped game screenshots. When executed, Collage.py will quickly produce a tiled collage of all images within the `images/` folder. Images will be scaled to the average (mean) height of all images in the folder, so it is best that the screenshots are of roughly equal height.

#### Usage

 1. Place images in `images/` folder
 2. Run `Collage.py`

```
usage: Collage.py [-h] [--border-width BORDER_WIDTH]
                  [--collage-width COLLAGE_WIDTH]

optional arguments:
  -h, --help            show this help message and exit
  --border-width BORDER_WIDTH
                        The width (in pixels) of the border between images and
                        around the collage.
  --collage-width COLLAGE_WIDTH
                        The maximum width (in pixels) of the collage.
```

#### Dependencies
Python 2.7  
[Python Imaging Library](http://www.pythonware.com/library/pil/handbook/index.htm)

This project was created for personal use in quickly producing a collage of game screenshots, but I guess it has lots of other uses.

#### License

The MIT License (MIT)

Copyright (c) 2013 jsrn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.