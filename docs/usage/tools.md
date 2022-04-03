# Tools

Tools are special items that let you do things faster than with commands alone. For example, the selection wand is a shortcut for using `;pos1` and `;pos2`.

!!! Note
    
    Both the selection and navigation wand are tools, and can be bound to other items with `;tool selwand` and `;tool navwand` respectively. See their respective pages for more details ([Selection](regions/selection.md), [Navigation](navigation.md)).

!!! Warning

    When using mobile controls, you may break blocks when using tools that require you to tap and hold the screen to use them. To prevent this from happening, bind tools to items that don't normally break things when you tap and hold; such as swords, snowballs, fishing rods, etc.

## Binding and unbinding

The act of associating a tool with an item is called "binding". This allows you to use tools by using the bound item.
Any item, even blocks, can be bound to a tool. Just hold the item while using the `;tool` command. You can also unbind tools by using `;tool none` while holding it.

## Stacker wand

The stacker wand is a simple yet powerful tool. It acts like the `;stack` comnand, but on individual blocks. Useful for when you want to extend things like walls and roofs quickly. To get one, just type `;tool stacker amount` where `amount` is the amount of times a block will get stacked. To prevent the stack from going through other blocks, type `;tool stacker amount mask` where `mask` determines what kind of blocks the stack can go through.

!!! Example
    
    `;tool stacker 10 air` would create a stacker wand that will copy blocks up to 10 times, or until it meets a block that's not air.
    If you were building underwater, you'd replace the mask with `water`.

## Far wand

The far wand is a long range version of the Selection wand. You mark selection points with it like usual, but you can do it from a distance. Created by typing `;tool farwand`.
