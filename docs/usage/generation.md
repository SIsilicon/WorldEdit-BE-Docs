# Generation

WorldEdit comes with a few commands help you make shapes without the use of a region selection. Instead, it takes the block that you are standing in as the center of these shapes.

[TOC]

## Spheres

``` txt
;sphere [-hr] <pattern> <radius> [radiusY] [radiusZ]
;hsphere [-r] <pattern> <radius> [radiusY] [radiusZ]
```
This generates a sphere or spheroid of any dimensions. You can also define 2, or 3 numbers to define the radius in different axes. `-h` makes it hollow, and `-r` raises the sphere's bottom to the origin.

## Cylinders

``` txt
;cyl [-hr] <pattern> <radius> ([radiusY]) [height]
;hcyl [-r] <pattern> <radius> ([radiusY]) [height]
```
This generates a cylinder of any dimensions. You can also define 2 numbers to define the radius in different axes. Again, `-h` makes it hollow, and `-r` raises the its bottom to the origin.

## Pyramids

``` txt
;pyramid [-h] <pattern> <size>
;hpyramid <pattern> <size>
```
This generates a pyramid. Unlike the previous two shapes, the center is at the base of the pyramid.

