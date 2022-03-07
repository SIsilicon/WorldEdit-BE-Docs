# Brushes

Brush tools are a more specific set of tools. They're meant to sculpt, shape and paint the world. You can bind a brush to almost any vanilla item, as long as you are holding it. For example, `;brush sphere log 5` Binds a sphere brush to the item you're holding.

You can unbind a brush from an item with `;brush none`.

[TOC]

## Brush Listing

### Sphere Brush

```
;brush sphere [-h] <pattern> <radius>
```
The sphere brush creates a sphere of blocks wherever it hits. It's a brush you'll likely use most often. `-h` makes the shape hollow.

### Cylinder Brush

```
;brush cylinder [-h] <pattern> <radius> [height]
```
The cylinder brush creates a cylinder of blocks wherever it hits. Again, `-h` makes it hollow.

### Smooth Brush

```
;brush smooth [radius] [iterations] [mask]
```
The smooth brush smoothes down terrain on use. `iterations` will specify how much the terrain will get smooth.

## Brush Settings

A few things about a brush can be adjusted to better fit your situation.

### Size

```
;brush size <size>
```
This changes the size of the area the brush affects.

### Range

```
;brush range <range>
```
This changes the how far the brush can reach. If hits the limit, then it will apply mid-air.

### Material

```
;brush material <pattern>
```
This changes what blocks the brush can make. This will only work on brushes that create blocks.

### Mask

```
;brush mask [mask]
```
This changes what blocks the brush can affect. This mask is also used in combination with the global mask.

### Trace Mask

```
;brush tracemask [mask]
```
This changes the blocks what this brush can trace through before hitting something that matches this mask. Useful if you want to build through certain blocks.

## Configuring the Brush without Commands

You can also set up brushes within the Kit's [Config Menu](kit.md/#config). using the item will show another button that will let you create and edit each brush item as instructed by WorldEdit.
