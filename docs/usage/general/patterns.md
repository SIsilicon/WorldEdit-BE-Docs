# Patterns

Many comnands in WorldEdit take a pattern as one of their arguments. A pattern determines what blocks, and what _kind_ of blocks are placed in the world. They currently more limited than the original mod's, but that will change in the future.

## Available Patterns

The only kind of pattern available for now is the Block Pattern. Using this kind of pattern simply places the block as it is defined. Unlike the java mod, you can't use number block IDs to specify blocks. You instead define blocks by their string IDs, and optional block states. The syntax is as follows: `namespace:block['state1':value,'state2':value,...]`. When a state isn't specified, it's left as its default value.
The namespace can be assumed to be `minecraft` for vanilla blocks. However, it's required for blocks coming from other addons.

!!! Example

    `;set stone`
    
    This sets the selected region to normal stone.
    
    `;set wool['color':'red']`
    
    This sets the region to red wool.
    
    `;set dirt,stone_slab['stone_slab_type':'brick','top_slot_bit':true]`
    
    This sets the region to half dirt, and upper half brick slabs

As you saw in the example, you can combine multiple patterns together with commas (,) inbetween them. **No spaces!** Also, every state name is surrounded in single quotes ('), and so are the state values __if they are not true, false, or a number__.

Since percentages have not been implemented yet, if you want more of one block than another, just define it multiple times.

!!! Tip

    You can also define certain block variations by adding a data value to the block ID. `wool:1` is orange wool for instance. This can't be defined alongside block states.

!!! Tip

    Using the [Pattern Picker](../kit.md#pattern_picker) displays the block's ID and block states, so you can do this to find the ID and states of different blocks!
