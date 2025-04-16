# Tools

Tools are special items that let you do things faster than with commands alone. For example, the selection wand is a shortcut for using `/wedit:pos1` and `/wedit:pos2`.

!!! Note

    Both the selection and navigation wand are tools, and can be bound to other items with `/wedit:tool selwand` and `/wedit:tool navwand` respectively. See their respective pages for more details ([Selection](regions/selection.md), [Navigation](navigation.md)).

!!! Warning

    When using mobile controls, you may break blocks when using tools that require you to tap and hold the screen to use them. To prevent this from happening, bind tools to items that don't normally break things when you tap and hold; such as swords, snowballs, fishing rods, etc.

## Binding and unbinding

The act of associating a tool with an item is called "binding". This allows you to use tools by using the bound item.
Any item, even blocks, can be bound to a tool. Just hold the item while using the `/wedit:tool` command. You can also unbind tools by using `/wedit:tool none` while holding it.

## Stacker wand

The stacker wand is a simple yet powerful tool. It acts like the `/wedit:stack` comnand, but on individual blocks. Useful for when you want to extend things like walls and roofs quickly. To get one, just type `/wedit:tool stacker amount` where `amount` is the amount of times a block will get stacked. To prevent the stack from going through other blocks, type `/wedit:tool stacker amount mask` where `mask` determines what kind of blocks the stack can go through.

!!! Example

    `/wedit:tool stacker 10 air` would create a stacker wand that will copy blocks up to 10 times, or until it meets a block that's not air.
    If you were building underwater, you'd replace the mask with `water`.

## Far wand

The far wand is a long range version of the Selection wand. You mark selection points with it like usual, but you can do it from a distance. Created by typing `/wedit:tool farwand`.

## Command Wand

The command wand allows you to run both vanilla Minecraft and WorldEdit commands on tool use. Very useful if you have a command you want to run quickly and repeatedly. Note that you need OP permissions to use vanilla commands, and normal WorldEdit permissions still apply.

!!! Examples

    `/wedit:tool cmd /tp 23 40 50` would let you teleport to specific coordinates.
    `/wedit:tool cmd ;replacenear 5 grass stone` would replace nearby grass with stone.
    Notice how the commands start with their respective prefix.

## Block Replacer

The block replacer simply replaces any block you interact with with a pattern of choice (eg: `/wedit:tool repl stone`).

## Block Cycler

This tool, made with the command `/wedit:tool cycler`, lets you change the state of an interacted block. Using it while sneaking lets you choose which state to cycle through.

## Super Pickaxe

The super pickaxe is different from other tools. It's more like a mode that you toggle on and off. While enabled, it will increase the amount of blocks any pickaxe can break at a time. This is activated using the `/wedit:superpickaxe`/`/wedit:sp` command along with a specified mode. Specifying no mode deactivates the super pickaxe. There are three modes in total.

### Single Mode

Pickaxes in this mode operate mostly like they always do, apart from their dropping behaviour. Activated with `/wedit:sp single`.

### Area Mode

Pickaxes will break blocks within a cubic area around the initial block broken. Only the block that are the same as the initial one broken are affected. Activated with `/wedit:sp area <range>`.

### Recursive Mode

Pickaxes will break blocks starting from the initial broken block. It will stop once it can no longer find adjacent blocks to break of the same type. Activated with `/wedit:sp recursive <range>`.
