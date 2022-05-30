# Selection

A selection in WorldEdit is a region of interest that you do all sorts of stuff with, from copying blocks to stacking them in a given direction. Being able to manipulate your selection's shape and size is a useful skill to have, and this section will show you all you need to know.

[TOC]

## Seeing your selection

By default, WorldEdit displays your selection with particles. This can help visualize where you're performing operations. If you ever want to turn it off for any reason, toggle its visibility with the command `;drawsel`. Running the command again makes your selection visible again.

## Selecting cuboids

As of the time of writing, WorldEdit currently only supports the cuboid selection shapes, but it's the only shape you'd need for most cases, and is the most basic. By default, a selection is defined by marking two opposite corners of the cuboid. There are several ways to mark these points.

### Using the selection wand.

The selection wand (a wooden axe by default) is a tool used for making selections; received with the command `;wand`. To make selections with it, you tap on a block to mark it as one of the corners of the cuboid. Doing it while sneaking marks the first corner, and without sneaking marks the second corner.

### Selecting at your current location

`;pos1` and `;pos2` are the command equivalent of using the selection wand. Using them marks the location you're currently standing in as the first or second position respectively. Useful for when you're midair for example.

### Selecting what you're looking at

`;hpos1` and `;hpos2` do exactly what the previous two commands do, but instead of marking your current location, it marks the block you're looking at. They also have a tool equivalent, the far wand, which you can bind to any item with `;tool farwand`.

## Adjusting the selection

### Expanding the selection

``` txt
;expand <amount> [direction]
;expand <amount> <reverseAmount> [direction]
;expand vert
```
This command allows you to easily enlarge a region in a couple of different ways:

- By specifying a direction
- By looking in the direction
- To the world height limits (using vert)

To specify a direction, use 
"N", "S", "W", "E", "U" (for up), or "D" (for down) for the direction. If you want to use the direction you're facing, either use "me" for the direction, or don’t enter a direction at all.

You can also specify relative directions like "F" (forward, same as "me"), "B" (back), "L" (left), or "R" (right), which will be relative to the direction you are facing.

You can also specify two numbers and the region will be expanded in two opposite directions simultaneously.

!!! Examples

    `;expand 10 up`. The selection will grow larger at the top.

    `;expand 10 10 left`. The selection will grow larger to your left and right.

    `;expand vert`. The selection will grow to the dimension's height limits (in the overworld, Y 319 to Y -64).

### Contracting the selection

``` txt
;contract <amount> [direction]
;contract <amount> <reverseAmount> [direction]
```
This command is like `;expand`, but instead shrinks the selection in the specified direction.

!!! Example

    `;contract 5 down`. The selection would shrink from top going down.

### Inset and Outset

If you want to expand or contract in all directions at once (or just horizontal or vertical directions), you can use the `;outset` and `;inset` commands. For example, `;outset -v 5` will expand your selection vertically (both up and down) 5 blocks each, while `;inset -h 5` will contract your selection horizontally (north, west, south, and east) 5 blocks each. Leaving out the v or h will work in all 6 directions.

## Counting blocks

Sometimes when doing builds in creative, you'd like to know the amount of blocks used so it can be replicated in survival. The commands `;count` and `;distr` can help you with that.

- `;count <mask>` counts the number of blocks in your selection that match the specified mask. 

- `;distr [-cd]` counts _every_ block in your selection. If you want it to be more specific, include the `-d` flag to count blocks of different states (eg: different colored wool blocks).

## Selection Modes

Using the `;sel <mode>` command allows you to change between different shapes.

- `;sel cuboid`

    The standard cuboid selection mode, described above.

- `;sel extend`

    This mode works like cuboid mode, but with each second position, the selection expands.
    Selecting the first position works like normal, but any second position after that will extend the cuboid selection to include the new position.

- `;sel sphere`

    This mode creates a sperical selection.
    The first position defines where the sphere is at, and the second position defines the radius.