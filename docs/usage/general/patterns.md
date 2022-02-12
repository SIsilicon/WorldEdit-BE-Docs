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
    
    `;set wool[color=red]`
    
    This sets the region to red wool.
    
    `;set stone_slab[stone_slab_type=brick,top_slot_bit=true]`
    
    This sets the region to upper half brick slabs.

!!! Tip

    Using the [Pattern Picker](/usage/kit#pattern_picker) displays the block's ID and block states, so you can do this to find the ID and states of different blocks!

!!! Note

    You can also define certain block variations by adding a data value to the block ID. `wool:1` is orange wool for instance. This can't be defined alongside block states. You can find these data values in places like the Minecraft Wiki.

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
