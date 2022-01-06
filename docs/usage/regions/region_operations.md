# Region Operations

Besides clipboard operations, there are other thing you can do with your selection.

[TOC]

## Setting Blocks

The set command is a simple command (`;set <pattern: Pattern>`) that sets all the blocks in your selection to a specified pattern.

!!! Examples

    `;set stone`
    
    Sets the region to stone.
    
    `;set air,air,wool['color':'orange']`
    
    Sets the region to 2/3 air, and 1/3 orange wool.

## Replacing Blocks

You can use the replace command (`;replace <mask: Mask> <pattern: Pattern>`) when you only want to set _specific_ blocks in your selection.

!!! Examples

    `;replace air water`
    
    Replaces air with water.
    
    `;replace grass,dirt log`
    
    Replaces grass and dirt with oak logs.

## Stacking

The stack command repeats your selection, in a certain direction (`;stack <times: int> [direction: Direction]`). Useful for when you want to build something with a repeating pattern; like bridges, hallways, and rows of pillars.

`Direction` by default is the one you are currently facing. There are other directions you can choose too.

**forward, back, left and right** are all directions relative to where you're facing;  **up, down, north, south, east and west** are all directions relative to the world.

!!! Tip

    You can also reference these directions by their initial. Eg: 'north' can simply be typed as 'n'.

## Moving

Suppose you think a build would look better if it were nudged a little to the right. Rather than cutting and pasting the build, you also have the option of using the move command to adjust the its position (`;move <amount: int> [direction: Direction]`).

## Rotating

The rotate command allows you to rotate your builds in increments of 90°  around you (`;rotate [-cos] <rotate: int>`). The `-c` flag makes this command affect the clipboard, `-o` makes it rotate around its center, and `-s` changes your selection to fit the rotated build.

## Flipping

The flip command flips your builds in a direction of your choice around you `;flip [-cos] [direction: Direction]`). The flags here do the same things as the ones for `;rotate`.