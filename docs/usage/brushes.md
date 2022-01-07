# Brushes

Brush tools are a more specific set of tools. They're meant to sculpt, shape and paint the world. You can bind a brush to six different shovels; each one referenced by tier. For example, `;brush 2 sphere log 5` Binds a brush to the stone shovel, as stone is the second tier.

|![Shovel Tier](/img/shovel_tiers.png)|
|:---:|
|The shovel tiers, left to right.|

You can unbind a brush from a shovel with `;brush <tier> none`.

[TOC]

## Brush Listing

### Sphere Brush

```
;brush <tier> sphere [-h] <pattern> <radius>
```
The sphere brush creates a sphere of blocks wherever it hits. It's a brush you'll likely use most often. `-h` makes the shape hollow.

### Cylinder Brush

```
;brush <tier> cylinder [-h] <pattern> <radius> [height]
```
The cylinder brush creates a cylinder of blocks wherever it hits. Again, `-h` makes it hollow.

## Brush Settings

A few things about a brush can be adjusted to better fit your situation.

### Size

```
;brush <tier> size <size>
```
This changes the size of the area the brush affects.

### Range

```
;brush <tier> range <range>
```
This changes the how far the brush can reach. If hits the limit, then it will apply mid-air.

### Mask

```
;brush <tier> mask [mask]
```
This changes what blocks the brush can affect. This mask is also used in combination with the global mask.

### Trace Mask

```
;brush <tier> tracemask [mask]
```
This changes the blocks what this brush can trace through before hitting something that matches this mask. Useful if you want to build through certain blocks.

## Configuring the Brush without Commands

You can also set up brushes within the Kit's [Config Menu](../kit/#config). using the item will show another button that will let you edit each brush tier as instructed by WorldEdit.
