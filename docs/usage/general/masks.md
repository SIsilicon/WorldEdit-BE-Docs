# Masks

Masks, alongside patterns, are commonly used in WorldEdit commands. Unlike patterns, masks determine which blocks will be affected by commands, brushes, and so on.

Aside from commands that take a mask as a parameter, like `;replace [mask] <pattern>`, you can also apply masks to individual brushes by using the `;mask` command, or you can apply a mask to all your WorldEdit actions globally with `;gmask`. The global mask can also be set from the kit using the [Mask Picker](../kit.md#mask_picker).

!!! Note

    Masks applied through different means will stack with each other. If you set your global mask with `;gmask dirt`, and then set a brush mask with `;mask [tier] stone`, that brush will not be able to modify any blocks at all! This is because the combined mask will only match blocks which are both stone and dirt!

!!! Tip

    You can clear your global mask by using `;gmask` again without arguments.

## Availiable Masks

Like [patterns](patterns.md), masks also take blocks as part of their definition, and use the same syntax as well. Unlike patterns though, Defining the block without its states doesn't just match blocks with the default states, but also any block no matter what state they're in.

!!! Example

    `;replace wool dirt`
    
    Replaces wool of any colour with dirt.
    
    `;replace log2['new_log_type':'dark_oak','pillar_axis':0],cobblestone air`
    
    Replaces dark oak logs facing up, and cobblestone with air.
