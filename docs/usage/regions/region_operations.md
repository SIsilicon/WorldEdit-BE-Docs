# Region Operations

Besides clipboard operations, there are other thing you can do with your selection.

[TOC]

## Setting Blocks

The set command is a simple command (`/wedit:set <pattern: Pattern>`) that sets all the blocks in your selection to a specified pattern.

!!! Examples

    `/wedit:set stone`

    Sets the region to stone.

    `/wedit:set 75%air,25%wool[color=orange]`

    Sets the region to 3/4 air, and 1/4 orange wool.

## Replacing Blocks

You can use the replace command (`/wedit:replace <mask: Mask> <pattern: Pattern>`) when you only want to set _specific_ blocks in your selection.

!!! Examples

    `/wedit:replace air water`

    Replaces air with water.

    `/wedit:replace grass,dirt log`

    Replaces grass and dirt with oak logs.

## Stacking

The stack command repeats your selection, in a certain direction (`/wedit:stack <times: int> [direction: Direction]`). Useful for when you want to build something with a repeating pattern; like bridges, hallways, and rows of pillars.

`Direction` by default is the one you are currently facing. There are other directions you can choose too.

**forward, back, left and right** are all directions relative to where you're facing; **up, down, north, south, east and west** are all directions relative to the world.

!!! Tip

    You can also reference these directions by their initial. Eg: 'north' can simply be typed as 'n'.

## Moving

Suppose you think a build would look better if it were nudged a little to the right. Rather than cutting and pasting the build, you also have the option of using the move command to adjust the its position (`/wedit:move <amount: int> [direction: Direction]`).

## Rotating

The rotate command allows you to rotate your builds around you (`/wedit:rotate [-ows] <rotate: int>`). By default, it affects the clipboard, but adding the `-w` flag will make it affect your selection instead. `-o` makes it rotate around its center, and `-s` changes your selection to fit the rotated build (only works with the `-w` flag).

## Flipping

The flip command flips your builds in a direction of your choice around you (`/wedit:flip [-ows] [direction: Direction]`). The flags here do the same things as the ones for `/wedit:rotate`.

## Lines, Walls, and Faces

The `/wedit:line`, `/wedit:walls` and `/wedit:faces` commands are all simple commands that only need a pattern to work, but are also affected by the global mask. They all do what they say. `/wedit:line` makes a line from the first to the second position, `/wedit:walls` makes walls around the selection, and `/wedit:faces` surrounds the selection with an outline (like `/wedit:walls`, but with a floor and ceiling).

## Hollowing

With the `/wedit:hollow` command you can hollow out what you have selected. You can specify the thickness of the wall that would be left from the operation, and even what blocks to replace the hollowed out area with. This is air by default.

## Reading and Changing Biomes

Two commands are available to read and set biomes respectively. `/wedit:biomeinfo` and `/wedit:setbiome`. With `/wedit:biomeinfo` you can get a list of biomes that the selection is covering. You can also do `/wedit:biomeinfo -p` to get the biome at your current position.

As for setting biomes, that's done with `/wedit:setbiome <biome>` and you can change how parts of the world look and operate with it. Whether it be the colour of the grass, or whether rain or snow (or nothing) falls. Note that due to limitations, these changes **won't apply on their own**. To do that, you need to exit the world, and process it with the [WorldEdit app](../worldedit_app.md).
