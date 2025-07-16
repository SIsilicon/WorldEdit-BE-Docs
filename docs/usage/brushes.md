# Brushes

Brush tools are a more specific set of tools. They're meant to sculpt, shape and paint the world. You can bind a brush to almost any vanilla item, as long as you are holding it. For example, `;brush sphere log 5` Binds a sphere brush to the item you're holding.

You can unbind a brush from an item with `;brush none`.

[TOC]

## Brush Listing

### Sphere Brush

```txt
;brush sphere [-h] <pattern> <radius>
```

The sphere brush creates a sphere of blocks wherever it hits. It's a brush you'll likely use most often. `-h` makes the shape hollow.

### Cylinder Brush

```txt
;brush cyl [-h] <pattern> <radius> [height]
```

The cylinder brush creates a cylinder of blocks wherever it hits. Again, `-h` makes it hollow.

### Smooth Brush

```txt
;brush smooth [radius] [iterations] [mask]
```

The smooth brush smoothes down terrain on use. `iterations` will specify how much the terrain will get smoothed. `mask` determines what is part of the terrain to be smoothed. This mask acts different from `;gmask` which determines what blocks are affected all together.

### Erosion Brush

```txt
;brush erode [radius]
;brush erode lift [radius]
;brush erode fill [radius]
;brush erode melt [radius]
;brush erode smooth [radius]
```

Use the erosion brush to shape terrain with great control. It comes in various modes.

-   The default mode pushes terrain in.
-   `lift` mode pushes terrain out.
-   `fill` mode filles in areas of the terrain.
-   `melt` mode does the opposite of `fill`.
-   `smooth` mode smoothes the terrain.

### Overlay brush

```
;brush overlay <pattern> [radius] [depth] [mask]
```

The overlay brush replaces blocks exposed to the sky with a pattern of choice, like dirt or grass. For example, `;br overlay dirt 3 2` creates a brush of radius 3 that will overlay dirt 2 blocks deep in an affected surface. The mask parameter lets you choose what blocks count as a surface.

### Structure/Clipboard brush

```
;brush struct clipboard
;brush struct <structure(s)...>
```

The structure brush will paste a structure down wherever the brush is used. Do this to sprinkle features on landscapes for example. You can either use your clipboard, which offers the mask for flexibility, or exported structures which you can define multiple of to be picked randomly every brush use.

## Brush Settings

A few things about a brush can be adjusted to better fit your situation.

### Size

```txt
;size <size>
```

This changes the size of the area the brush affects.

### Range

```txt
;range <range>
```

This changes the how far the brush can reach. If hits the limit, then it will apply mid-air.

### Material

```txt
;material <pattern>
```

This changes what blocks the brush can make. This will only work on brushes that create blocks.

### Mask

```txt
;mask [mask]
```

This changes what blocks the brush can affect. This mask is also used in combination with the global mask.

### Trace Mask

```txt
;tracemask [mask]
```

This changes the blocks what this brush can trace through before hitting something that matches this mask. Useful if you want to build through certain blocks.

## Configuring the Brush without Commands

You can also set up brushes within the Kit's [Config Menu](kit.md/#config). using the item will show another button that will let you create and edit each brush item as instructed by WorldEdit.
