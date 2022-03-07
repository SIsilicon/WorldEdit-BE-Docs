# Tools

Tools are special items that let you do things faster than with commands. For example, the selection wand is a shortcut for using `;pos1` and `;pos2`.

!!! Note
    
    Both the selection and navigation wand are tools, and can be binded to other items with `;tool selwand` and `;tool navwand` respectively.

## Binding and unbinding

The act of associating a tool with an item is called "binding". This allows you to use tools by using the bound item.
Most vanilla items can be bound to a tool. Just hold the item while using the `;tool` command. You can also unbind tools by using `;tool none`.

## Stacker wand

The stacker wand is a simple yet powerful tool. It acts like the `;stack` comnand, but on individual blocks. Useful for when you want to extend things like walls and roofs quickly. To get one, just type `;tool stacker amount` where `amount` is the amount of times a block will get stacked. To prevent the stack from going through other blocks though, type `;tool stacker amount mask` where `mask` determines what kind of blocks the stack 
can go through.

!!! Example
    
    `;tool stacker 10 air` would give you a stacker wand that will copy blocks up to 10 times, or until it meets a block that's not air.
    If you were building underwater, You'd replace the mask with `water`.
