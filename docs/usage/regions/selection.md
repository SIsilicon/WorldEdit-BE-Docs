# Selection

A selection in WorldEdit is a region of interest that you do all sorts of stuff with, from copying blocks to stacking them in a given direction. Being able to manipulate your selection's shape and size is a useful skill to have, and this section will show you all you need to know.

[TOC]

## Seeing your selection

By default, WorldEdit displays your selection with particles. This can help visualize where you're performing operations. If you ever want to turn it off for any reason, toggle its visibility with the command `/wedit:drawsel`. Running the command again makes your selection visible again.

## Selecting cuboids

As of the time of writing, WorldEdit currently only supports the cuboid selection shapes, but it's the only shape you'd need for most cases, and is the most basic. By default, a selection is defined by marking two opposite corners of the cuboid. There are several ways to mark these points.

### Using the selection wand.

The selection wand (a wooden axe by default) is a tool used for making selections; received with the command `/wedit:wand`. To make selections with it, you break a block to mark the first corner, and use the wand on a block to mark the second corner. To clear your selection, just drop the wand.

### Selecting at your current location

`/wedit:pos1` and `/wedit:pos2` are the command equivalent of using the selection wand. Using them marks the location you're currently standing in as the first or second position respectively. Useful for when you're midair for example.

### Selecting what you're looking at

`/wedit:hpos1` and `/wedit:hpos2` do exactly what the previous two commands do, but instead of marking your current location, it marks the block you're looking at. They also have a tool equivalent, the far wand, which you can bind to any item with `/wedit:tool farwand`.

### Selection information

The `/wedit:size` command, while it's used for changing the brush size, can also tell you information about your selection. Just use the command without any arguments. Adding the `-c` flag will give you information about the clipboard instead.

## Adjusting the selection

### Expanding the selection

```txt
;expand <amount> [direction]
;expand <amount> <reverseAmount> [direction]
;expand vert
```

This command allows you to easily enlarge a region in a couple of different ways:

-   By specifying a direction
-   By looking in the direction
-   To the world height limits (using vert)

To specify a direction, use
"N", "S", "W", "E", "U" (for up), or "D" (for down) for the direction. If you want to use the direction you're facing, either use "me" for the direction, or don’t enter a direction at all.

You can also specify relative directions like "F" (forward, same as "me"), "B" (back), "L" (left), or "R" (right), which will be relative to the direction you are facing.

You can also specify two numbers and the region will be expanded in two opposite directions simultaneously.

!!! Examples

    `/wedit:expand 10 up`. The selection will grow larger at the top.

    `/wedit:expand 10 10 left`. The selection will grow larger to your left and right.

    `/wedit:expand vert`. The selection will grow to the dimension's height limits (in the overworld, Y 319 to Y -64).

### Contracting the selection

```txt
;contract <amount> [direction]
;contract <amount> <reverseAmount> [direction]
```

This command is like `/wedit:expand`, but instead shrinks the selection in the specified direction.

!!! Example

    `/wedit:contract 5 down`. The selection would shrink from top going down.

### Inset and Outset

If you want to expand or contract in all directions at once (or just horizontal or vertical directions), you can use the `/wedit:outset` and `/wedit:inset` commands. For example, `/wedit:outset -v 5` will expand your selection vertically (both up and down) 5 blocks each, while `/wedit:inset -h 5` will contract your selection horizontally (north, west, south, and east) 5 blocks each. Leaving out the v or h will work in all 6 directions.

## Counting blocks

Sometimes when doing builds in creative, you'd like to know the amount of blocks used so it can be replicated in survival. The commands `/wedit:count` and `/wedit:distr` can help you with that.

-   `/wedit:count <mask>` counts the number of blocks in your selection that match the specified mask.

-   `/wedit:distr [-cd]` counts _every_ block in your selection. If you want it to be more specific, include the `-d` flag to count blocks of different states (eg: different coloured wool blocks).

## Selection Modes

Using the `/wedit:sel <mode>` command allows you to change between different shapes.

-   `/wedit:sel cuboid`

    The standard cuboid selection mode, described above.

-   `/wedit:sel extend`

    This mode works like cuboid mode, but with each second position, the selection expands.
    Selecting the first position works like normal, but any second position after that will extend the cuboid selection to include the new position.

-   `/wedit:sel sphere`

    This mode creates a sperical selection.
    The first position defines where the sphere is at, and the second position defines the radius.

-   `/wedit:sel cyl`

    This mode creates a cylindrical selection
    The first position marks the start of the cylinder, and every second position after that will expand the cylinder in both radius and height.
