# Kit

As WorldEdit for Bedrock is made for different devices, the kit was created to make it easier to use on any control; whether it's a keyboard, touchscreen or controller. It gives access to items that act as shortcuts to many common WorldEdit functions; such as undoing, redoing, copying and pasting.

## Main items

Upon typing the command `/wedit:kit`, you are given the following items:

-   <a name="selection_wand"></a>**Selection Wand ![](../img/icons/wood_axe.png):** Make selections to do stuff with. You can remove your selection by dropping the wand. See [Selection](regions/selection.md).
-   <a name="region_tools"></a>**Region Tools:** These tools are all used with your selection to do various things with it. They are a single item and you can switch between them by sneaking and using said item. By default it is "Fill Selection".
    -   **Fill Selection ![](../img/icons/selection_fill.png)**: Fill your selection with blocks determined by the pattern picker.
    -   **Outline Selection ![](../img/icons/selection_outline.png)**: Outline your selection with blocks determined by the pattern picker.
    -   **Wall Selection ![](../img/icons/selection_wall.png)**: Wall off your selection with blocks determined by the pattern picker.
    -   **Hollow Selection ![](../img/icons/selection_hollow.png)**: Hollow out anything solid in your selection.
    -   **Move Selection ![](../img/icons/selection_move.png)**: Move your selection over a specified distance
    -   **Stack Selection ![](../img/icons/selection_stack.png)**: Stack your selection a specified number of times.
-   <a name="pattern_picker"></a>**Pattern Picker ![](../img/icons/eyedropper.png):** Select blocks to use in a pattern. Sneaking will add blocks to the pattern. The pattern is used by various tools in the kit such as "Fill Selection".
-   <a name="copy"></a>**Copy ![](../img/icons/copy.png):** Copy whatever is in your selection to the clipboard.
-   <a name="cut"></a>**Cut ![](../img/icons/cut.png):** Cut whatever is in your selection to the clipboard. The selection is then replaced with air.
-   <a name="paste"></a>**Paste ![](../img/icons/paste.png):** Paste whatever is in your clipboard to the world. The location of the paste is relative to the selection when you last copied/cut. Also, if you sneak while using the tool, you're given the option to rotate and/or flip the clipboard before pasting it. See [Clipboard](clipboard.md).
-   <a name="undo"></a>**Undo ![](../img/icons/undo.png):** Undo your previous action that affected the world. See [History](general/history.md).
-   <a name="redo"></a>**Redo ![](../img/icons/redo.png):** Redo your previous action that affected the world. See [History](general/history.md).
-   <a name="config"></a>**WorldEdit Settings ![](../img/icons/config.png):** Enter a menu to change and setup some things about WorldEdit and the kit items.
-   <a name="mask_picker"></a>**Mask Picker ![](../img/icons/maskdropper.png):** Select blocks to use in the global mask. Like the Pattern Picker, sneaking will add blocks to the mask. This affects "Fill Selection", and the brushes. To clear it, use the command `/wedit:gmask`.
-   <a name="shape_tools"></a>**Shape Tools:** These tools let you make a variety of shapes made of any block. Like the region tools, they are a single item, and you switch between them by sneaking and using said item. By default it is "Draw Line".
    -   **Draw Line ![](../img/icons/draw_line.png):** Draw a line from your first position to your second.
    -   **Draw Sphere ![](../img/icons/draw_sphere.png):** Draw a sphere from your first position with a radius determined by the distance from the second position.
    -   **Draw Cylinder ![](../img/icons/draw_cylinder.png):** Draw a cylinder from your first position with a radius and height determined by the distance from the second position.
    -   **Draw Pyramid ![](../img/icons/draw_pyramid.png):** Draw a pyramid from your first position with a size determined by the distance from the second position.
-   <a name="spawn_glass"></a>**Spawn Glass ![](../img/icons/spawn_glass.png):** Make a glass block where you stand. Useful for when you need to make a midair selection mark.

## Settings Menu

Upon using the "WorldEdit Settings" item, a menu will popup giving you access to some aspects of WorldEdit. There are a few sections to choose from.

### General ![](../img/icons/config.png)

This section allows you to change some things that affect WorldEdit overall. You have some settings to use here.

-   **Include Entities**: Whether to include entities in your clipboard when copying or cutting. This only affects the kit items. See [Clipboard](clipboard.md) for how to include entities via commands.
-   **Include Air**: Whether to include air in your clipboard. Like the previous setting, this only affects the kit items.
-   **Performance Mode**: Whether to run WorldEdit in performance mode. In this mode, the clipboard is saved in a simpler format; allowing you to copy, cut and paste more quickly. However, this limits your clipboard's capabilities. For example, you can only rotate along the Y axis, and air is always included. This can also be toggled by entering `/wedit:worldedit perf`.
-   **Selection Mode**: What selection mode to use. See [Selection](./regions/selection.md).

### Tools ![](../img/icons/tool_config.png) and Brushes ![](../img/icons/brush_config.png)

These other two sections allow you to manage tools or brushes respectively. There will be a button for each active tool you have, and if it has properties you can edit, tapping them will open up another menu to let you change how that tool works.

You also have the option to create a new tool. When tapped, you will be prompted to hold an item you want to bind a tool to. Once you've done that, you can then set it up as you wish.

Finally, there's a button that allows you to select what tools to delete.

### Gradients

A gradient is a set of blocks that patterns use to determine a transition from one block to another and so forth. You can manage, create and delete gradients from the config menu, but to use these gradients, see [Patterns](./general/patterns.md#gradient-patterns).
