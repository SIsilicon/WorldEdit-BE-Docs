# Patterns

Many comnands in WorldEdit take a pattern as one of their arguments. A pattern determines what blocks, and what _kind_ of blocks are placed in the world.

[TOC]

## Available Patterns

### Single Block Pattern

This is the most basic common type of pattern. Using this kind simply places the block as it is defined. Unlike the java mod, you can't use number block IDs to specify blocks. You instead define blocks by their string IDs, and optional block states. The syntax is as follows: `namespace:block[state1=value,state2=value,...]`. When a state isn't specified, it's left as its default value.
The namespace can be assumed to be `minecraft` for vanilla blocks. However, it's required for blocks coming from other addons.

!!! Example

    `;set stone`
    
    This sets the selected region to normal stone.
    
    `;set red_wool`
    
    This sets the region to red wool.
    
    `;set stone_slab[stone_slab_type=brick,top_slot_bit=true]`
    
    This sets the region to upper half brick slabs.

!!! Tip

    Using the `;blockid` command while facing a block tells you how that block should be written in WorldEdit patterns!

!!! Note

    You can also define certain block variations by adding a data value to the block ID. `wool:1` is orange wool for instance. This can't be defined alongside block states. You can do `;blockid -d` To get the id along with the data value of the block you look at.

### Random Pattern

It's possible to make a pattern that creates a mixture of other patterns. The simplest way is to just to make a comma separated list (`pattern1,pattern2,etc...`). This would make an even distribution of the list's elements. To make one pattern more common than an other, you can add percentages to each element (`percent%pattern,...`). A larger number means larger chance of being placed in an operation. The numbers don't have to add up to 100.

!!! Example

    `;set dirt,grass`
    
    This sets the region to half dirt, half grass.
    
    `;set 20%*wool,80%stone`
    
    This sets the region to 20% random wool, and 80% stone.

Notice in the last example, how block patterns aren't the only patterns you can use. There's more!

### Random State Pattern

Random state patterns create blocks with different random states. You make one by prefixing '\*' infront of a block ID. For example, `*log` would make logs of most types and in all directions. Most types because some logs use their own ID.

### Type/State Applying Pattern

Prefixing '^' to a block ID or block states allows you to change that aspect of blocks, and nothing more. Useful for when you want to change the type of a block without changing the orientation for instance.

!!! Example

    `;replace birch_stairs ^acacia_stairs`
    
    This turns birch stairs into acacia ones while keeping their orientation.
    
    `;replace wheat ^[growth=7]`
    
    This makes all wheat crops fully grown.

### Clipboard Pattern

Some patterns you want can get too complex to type. With `#clipboard` though, you can use what you've copied as your pattern. You can also offset the pattern by defining an offset like this. `#clipboard@[x,y,z]`

### Hand Pattern

Want to quickly use a block without having to type it in? Use `#hand` to use the block in your main hand as your pattern. So if you were to hold sponge for instance, your pattern will contain sponge.

## Gradients

Gradients are a complex pattern type. To create a gradient, type the command `;gradient` followed by the name of the gradient, then patterns of your choice each separated with a space. For example, `;gradient nature stone dirt grass` will make a gradient called "nature" that transitions from stone to dirt then grass.

!!! Tips

    You can specify the gradient based on a selection by running `;gradient -s "name"`. The command will read the selection along its longest side like a gradient map.

    You can also change how much the patterns fade into each other with the `-f` flag. For example `;gradient -f 0 test stone dirt` makes a gradient pattern called "test" of stone and dirt with a hard transition between the two.

Once you have defined a gradient you can then use it in a pattern like so: `$gradient_name`. By default the gradient goes upward, but you can specify the direction by adding a dot followed by the direction. For example, `$gradient_name.north`. Only absolute directions are supported, so `left`, `right`, `forward` nor `back` can't be used.
