# Tools

Tools are special items that let you do things faster than with commands. For example, the selection wand is a shortcut for using `;pos1` and `;pos2`.

!!! Note
    
    Both the selection and navigation wand are tools.

## Stacker wand

The stacker wand is the only other tool that is currently implemented, but it is very useful. It acts like the `;stack` comnand, but on individual blocks. Useful for when you want to extend things like walls and roofs quickly. To get one, just type `;tool stacker amount` where `amount` is the amount of times a block will get stacked. To prevent the stack from going through other blocks though, type `;tool stacker amount mask` where `mask` determines what kind of blocks the stack will go through.

!!! Example
    
    `;tool stacker 10 air` would give you a stacker wand that will copy blocks up to 10 times, or until it meets a block that's not air.
    If you were building underwater, You'd replace the mask with `water`.
