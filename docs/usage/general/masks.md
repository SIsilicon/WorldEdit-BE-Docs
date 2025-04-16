# Masks

Masks, alongside patterns, are commonly used in WorldEdit commands. Unlike patterns, masks determine which blocks will be affected by commands, brushes, and so on.

Aside from commands that take a mask as a parameter, like `/wedit:replace [mask] <pattern>`, you can also apply masks to individual brushes by using the `/wedit:mask` command, or you can apply a mask to all your WorldEdit actions globally with `/wedit:gmask`. The global mask can also be set from the kit using the [Mask Picker](../kit.md#mask_picker).

!!! Note

    Masks applied through different means will stack with each other. If you set your global mask with `/wedit:gmask dirt`, and then set a brush mask with `/wedit:mask stone`, that brush will not be able to modify any blocks at all! This is because the combined mask will only match blocks which are both stone and dirt!

!!! Tip

    You can clear your global mask by using `/wedit:gmask` again without arguments.

[TOC]

## Combining Masks

You can combine masks in two way: intersection, where all masks must pass to be matched successfully; or union, where it only takes one passing mask for a successful match.

!!! Example

    `/wedit:replace stone,dirt bedrock`

    This replace blocks that are stone OR dirt with bedrock.

    `/wedit:replace "dirt <air" grass`

    This replace blocks that are dirt AND under air with grass.

Notice how since a space is used to denote an intersection, the whole mask needs to be surrounded in double quotes.

## Availiable Masks

### Block Mask

Like [single block patterns](patterns.md#single-block-pattern), masks also take blocks as part of their definition, and use the same syntax as well. Unlike patterns though, Defining the block without its states doesn't just match blocks with the default states, but also any block no matter what state they're in.

!!! Example

    `/wedit:replace wool dirt`

    Replaces wool of any colour with dirt.

    `/wedit:replace log2[new_log_type=dark_oak,pillar_axis=0],cobblestone air`

    Replaces dark oak logs facing up, and cobblestone with air.

### Mask Negation

Using the `!` symbol allows you to match blocks that do NOT match any other masks that follow it.

!!! Example

    `/wedit:replace !gravel,dirt,sand grass`

    This replaces any block that isn't gravel, dirt or sand with grass.

### Existing Block Mask

`#existing` will match any actual block. In Minecraft: Bedrock Edition, this is basically just another version of `!air`.

### Offset Mask

You can test if a block is being overlayed (`>`) or underlayed (`<`) by the current block being matched.

!!! Example

    `/wedit:replace "air >stone" grass`

    This replaces any air that's overlaying(above) stone with grass.

### Random Noise Mask

The noise mask will randomly test a block as a match. You'd type `%percent` where `percent` is a number between 0 and 100. The higher the percent, the more likely the mask matches. This mask is most useful when used by itself, or in an intersection with another mask.

### Block State Mask

This mask will match blocks that match it's defined states, no matter what type of block it is. It comes in two modes: _lenient_ where the mask can match blocks even when it doesn't have its defined states (`^[state=value,...]`), or _strict_ where the block MUST have all the defined states (`^=[state=value,...]`).

!!! Example

    `/wedit:replace ^=[pillar_axis=0] stone`

    This sets any pillar-like blocks that face up to stone.

### Surface Mask

This mask matches any block that's directly adjacent to air blocks, i.e. exposed to air. You type either `#exposed` or `#surface`.

### Shadow Mask

This mask matches blocks that can't be seen from where you are. It's best used in combination with `#surface`. For example, `/wedit:replace "#shadow #surface" stone` on some grass under trees while you're above them will turn them into stone. Inverting it like `!#shadow` will only match with blocks that can be seen from where you are.
