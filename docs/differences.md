# Differences

As this addon is still under development, there are a bunch of features that it doesn't have that the original mod does; some features can't be implemented at all due to Minecraft's limitations.

## Commands

The following commands are planned to be implemented.

- /toggleplace
- /ascend
- /descend
- /ceil
- //hpos1
- //hpos2
- //sel
    - extend
    - poly
    - ellipsoid
    - sphere
    - cyl
    - convex
- //chunk
- //contract
- //shift
- //offset
- //outset
- //inset
- //size
- //count
- //distr
- //expand [vert]
- //curve
- //overlay
- //center
- //naturalize
- //deform
- //hollow
- //generate
- /tool()
    - repl
    - farwand
    - deltree
    - lrbuild
    - floodfill
    - cycler
    - info
- /, (Super Pickaxe)
- /superpickaxe
    - single
    - area
    - recursive
- /brush 
    - butcher
    - clipboard
    - gravity
    - extinguish
    - raise
    - lower
    - set
    - deform
    - snow
- /listchunks
- /delchunks
- //fill
- //fillr
- //drain
- //fixlava
- //fixwater
- //removeabove
- //removebelow
- //removenear
- //replacenear
- //snow
- //thaw
- //green
- /extinguish
- /butcher
- /remove
- //calculate

Commands that alter biome data, use images, or do any form of arbitrary file operation will be harder, if not impossible to implement due to API limitations.
The schematics commands will be implemented, but will use structure files instead, and limited to the world they're made in.

## Brushes and Tools

Brushes and tools currently only are limited to preset items. Soon though, any item can be binded to, so stay tuned for that!

## Selections

The only selection shape available is a cuboid. The other selection modes that you find in the planned command list will be implemented in the future.

One thing we got over the Java mod, is we have the ability to see our selections, and not limited to a specific version of Minecraft, or structure blocks. This can be toggled with `;drawsel`.

## Kit

Unlike the original mod, which was made for game intended for keyboard only, this addon is made for all kinds of devices. The purpose of the kit, which can be received with `;kit`, is to be able to use WorldEdit's more common features more easily. See [Kit](usage/kit.md) for more info.
