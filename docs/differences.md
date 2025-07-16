# Differences

As this addon is still under development, there are a bunch of features that it doesn't have that the original mod does; some features can't be implemented at all due to Minecraft's limitations.

## Commands

The following commands are planned to be implemented.

-   //sel
    -   poly
    -   ellipsoid
    -   convex
-   //curve
-   //overlay
-   //naturalize
-   //deform
-   /tool()
    -   deltree
    -   lrbuild
    -   floodfill
    -   info
-   /brush
    -   butcher
    -   gravity
    -   extinguish
    -   raise
    -   lower
    -   set
    -   deform
    -   snow
-   /listchunks
-   /delchunks
-   /remove

Commands that alter biome data, use images, or do any form of arbitrary file operation will be much harder to implement due to API limitations, so they will take longer to become a feature of the addon.

## Brushes and Tools

Items are not the only things you can bind to in the addon. Unlike the Java mod, you can also bind to blocks as well! Remember that once you bind a tool to a block, you can no longer place down that block until you unbind the tool/brush with either `;tool none` or `;brush none`.
Also, VoxelSniper's brush set has been implemented in the form of `;brush erode` and `;brush overlay`.

## Selections

Some of the more advanced selection modes have not been implemented yet. The ones you find in the planned command list will be implemented in the future.

One thing this has over the Java mod, is the ability to see selections, and not be limited to a specific version of Minecraft, or structure blocks. This can be toggled with `;drawsel`.

## Kit

Unlike the original mod, which was made for a game intended for keyboard only, this addon is made for all kinds of devices. The purpose of the kit, which you can get with `;kit`, is to be able to use WorldEdit's more common features more easily. See [Kit](usage/kit.md) for more info.

## Exporting Structures and Setting Biomes

Exporting structures to other worlds, and setting biome data cannot be done within Minecraft. An external app is required to make this happen. See [WorldEdit App](usage/worldedit_app.md) for details.
