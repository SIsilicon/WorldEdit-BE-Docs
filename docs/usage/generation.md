# Generation

WorldEdit comes with a few commands help you make shapes without the use of a region selection. Instead, it takes the block that you are standing in as the center of these shapes.

[TOC]

## Spheres

```txt
;sphere [-hr] <pattern> <radius> [radiusY] [radiusZ]
;hsphere [-r] <pattern> <radius> [radiusY] [radiusZ]
```

This generates a sphere or spheroid of any dimensions. You can also define 2, or 3 numbers to define the radius in different axes. `-h` makes it hollow, and `-r` raises the sphere's bottom to the origin.

## Cylinders

```txt
;cyl [-hr] <pattern> <radius> ([radiusY]) [height]
;hcyl [-r] <pattern> <radius> ([radiusY]) [height]
```

This generates a cylinder of any dimensions. You can also define 2 numbers to define the radius in different axes. Again, `-h` makes it hollow, and `-r` raises the its bottom to the origin.

## Pyramids

```txt
;pyramid [-h] <pattern> <size>
;hpyramid <pattern> <size>
```

This generates a pyramid. Unlike the previous two shapes, the center is at the base of the pyramid.

## Custom Shapes

Apart from these builtin shapes, there's also the ability to make your own with the `;gen` command!

```txt
;gen [-h] <pattern> <expression>
```

Unlike the others, you need to first make a selection to define where the shape will be made. Then, you need to define an expression that will determine where blocks will be generated. If it returns true or a number besides 0, then a block is generated. You can use the three variables `x`, `y` and `z` to reference the location, which is normalized within the selection ([-1, -1, -1] - [1, 1, 1]). You also have a bunch of math functions at your disposal. Experiment!

!!! Examples

    `;gen -h stone "y < x^2-z^2"`- Generates a stone saddle

    `;gen stone "(0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2"` - Generates a stone torus

    `;gen glass "y < cos(sqrt(x^2+z^2)^2 * 10) * 0.2"` - Generates a radial cosine wave

    `;gen -h wool "y^2/9+x^2/6*(1/(1-0.4*y))+z^2/6*(1/(1-0.4*y))<0.08"` - Generates a hollow wooly egg
