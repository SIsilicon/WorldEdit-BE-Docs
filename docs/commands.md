# Commands

Commands are the main way to use the many features of WorldEdit. Type `;help` to get a list of available commands. If you don't find a command here that's in the original, look in the  [differences](differences.md) page to see if it's planned.

[TOC]

## Reading this documentation

Commands may come with arguments. When you see an argument surrounded in `[square brackets]`, then that argument is optional. If it's surrounded in `<angled brackets>`, then you need to define it when using the command. If you find arguments that look like `[-this]`, they are flags. Flags change how commands are executed. Each letter after the "-" is its own flag. You can define them apart (`-a -b`) or together (`-ab`). Some flags even require an argument defined after them. Finally, `|` means you have a choice among the list it makes and must choose one.

## Permissions

Each command has their own permission requirements to be useable by a player. To give yourself or anyone else permission for various commands, just type `/tag "@s, or a player name" add "permission"`. For example, `/tag @s add worldedit.region.set` would give yourself permission to use the `;set` command. You can give yourself permission for multiple comands at once. Using `worldedit.clipboard` for instance would give you permission to use every clipboard command. If you add `-` to the begin of a permission, you can also blacklist commands that use those permissions. So `-worldedit.clipboard` would _prevent_ you from using clipboard commands.

!!! note

    No command will work unless you _at least_ have explicit permission to use any worldedit command. `/tag @s add worldedit` would give you permission for all of them.

## The commands
<!--COMMANDAREA-->
!!! note ""
	
	**;help (or ;?)**

	|||
	|:--|:--|
	|**Description**|Get a list of commands available and a quick description for each of them|
	|**Permission**|`worldedit.help`|
	|**Usage**|`;help (<command>|[page])`|

!!! note ""
	
	**;kit**

	|||
	|:--|:--|
	|**Description**|Give yourself a set of items to do common worldedit functions|
	|**Permission**|`worldedit.kit`|
	|**Usage**|`;kit`|

!!! note ""
	
	**;worldedit (or ;we)**

	|||
	|:--|:--|
	|**Description**|WorldEdit commands|
	|**Permission**||
	|**Usage**|`;worldedit <version>`|

!!! note ""
	
	**;worldedit version**

	|||
	|:--|:--|
	|**Description**|Get WorldEdit version|
	|**Permission**||
	|**Usage**|`;worldedit version`|

!!! note ""
	
	**;pos1 (or ;1)**

	|||
	|:--|:--|
	|**Description**|Set the first position of your selection to the specified or current position|
	|**Permission**|`worldedit.selection.pos`|
	|**Usage**|`;pos1 [coordinates]`|

!!! note ""
	
	**;pos2 (or ;2)**

	|||
	|:--|:--|
	|**Description**|Set the second position of your selection to the specified or current position|
	|**Permission**|`worldedit.selection.pos`|
	|**Usage**|`;pos2 [coordinates]`|

!!! note ""
	
	**;drawsel**

	|||
	|:--|:--|
	|**Description**|Toggle your selection's visibility|
	|**Permission**|`worldedit.drawsel`|
	|**Usage**|`;drawsel`|

!!! note ""
	
	**;sel (or ;deselect, ;desel)**

	|||
	|:--|:--|
	|**Description**|Change selection mode (currently can only clear selection)|
	|**Permission**||
	|**Usage**|`;sel`|

!!! note ""
	
	**;wand**

	|||
	|:--|:--|
	|**Description**|Give yourself a selection wand|
	|**Permission**|`worldedit.wand`|
	|**Usage**|`;wand`|

!!! note ""
	
	**;cut**

	|||
	|:--|:--|
	|**Description**|Remove your current selection and place it in the clipboard|
	|**Permission**|`worldedit.clipboard.cut`|
	|**Usage**|`;cut [-ae] [fill] [-m <mask>]`|

!!! note ""
	
	**;copy**

	|||
	|:--|:--|
	|**Description**|Copy the current selection to the clipboard|
	|**Permission**|`worldedit.clipboard.copy`|
	|**Usage**|`;copy [-aem <mask>]`|

!!! note ""
	
	**;paste**

	|||
	|:--|:--|
	|**Description**|Paste your clipboard into the world|
	|**Permission**|`worldedit.clipboard.paste`|
	|**Usage**|`;paste [-osn]`|

!!! note ""
	
	**;clearclipboard**

	|||
	|:--|:--|
	|**Description**|Clear your clipboard|
	|**Permission**|`worldedit.clipboard.clear`|
	|**Usage**|`;clearclipboard`|

!!! note ""
	
	**;hsphere**

	|||
	|:--|:--|
	|**Description**|Generate a hollow sphere|
	|**Permission**|`worldedit.generation.sphere`|
	|**Usage**|`;hsphere [-r] <pattern> <radii>`|

!!! note ""
	
	**;sphere**

	|||
	|:--|:--|
	|**Description**|Generate a sphere|
	|**Permission**|`worldedit.generation.sphere`|
	|**Usage**|`;sphere [-hr] <pattern> <radii>`|

!!! note ""
	
	**;cyl**

	|||
	|:--|:--|
	|**Description**|Generate a cylinder|
	|**Permission**|`worldedit.generation.cylinder`|
	|**Usage**|`;cyl [-hr] <pattern> <radii> [height]`|

!!! note ""
	
	**;hcyl**

	|||
	|:--|:--|
	|**Description**|Generate a hollow cylinder|
	|**Permission**|`worldedit.generation.cylinder`|
	|**Usage**|`;hcyl [-r] <pattern> <radii> [height]`|

!!! note ""
	
	**;pyramid**

	|||
	|:--|:--|
	|**Description**|Generate a pyramid|
	|**Permission**|`worldedit.generation.pyramid`|
	|**Usage**|`;pyramid [-h] <pattern> <size>`|

!!! note ""
	
	**;hpyramid**

	|||
	|:--|:--|
	|**Description**|Generate a hollow pyramid|
	|**Permission**|`worldedit.generation.pyramid`|
	|**Usage**|`;hpyramid <pattern> <size>`|

!!! note ""
	
	**;gmask**

	|||
	|:--|:--|
	|**Description**|Set the global mask|
	|**Permission**|`worldedit.global-mask`|
	|**Usage**|`;gmask [mask]`|

!!! note ""
	
	**;set**

	|||
	|:--|:--|
	|**Description**|Fill the selection with a block pattern|
	|**Permission**|`worldedit.region.set`|
	|**Usage**|`;set <pattern>`|

!!! note ""
	
	**;replace**

	|||
	|:--|:--|
	|**Description**|Replace certain blocks in the selection with other blocks|
	|**Permission**|`worldedit.region.replace`|
	|**Usage**|`;replace <mask> <pattern>`|

!!! note ""
	
	**;move**

	|||
	|:--|:--|
	|**Description**|Move the selection in a certain direction|
	|**Permission**|`worldedit.region.move`|
	|**Usage**|`;move [amount] [offset]`|

!!! note ""
	
	**;stack**

	|||
	|:--|:--|
	|**Description**|Repeat the contents of the current selection|
	|**Permission**|`worldedit.region.stack`|
	|**Usage**|`;stack [count] [offset]`|

!!! note ""
	
	**;rotate**

	|||
	|:--|:--|
	|**Description**|Rotate the selection|
	|**Permission**|`worldedit.region.rotate`|
	|**Usage**|`;rotate [-ocs] <rotate>`|

!!! note ""
	
	**;flip**

	|||
	|:--|:--|
	|**Description**|Flip the selection|
	|**Permission**|`worldedit.region.flip`|
	|**Usage**|`;flip [-ocs] [direction]`|

!!! note ""
	
	**;walls**

	|||
	|:--|:--|
	|**Description**|Generate a wall from your selection|
	|**Permission**|`worldedit.region.walls`|
	|**Usage**|`;walls <pattern>`|

!!! note ""
	
	**;smooth**

	|||
	|:--|:--|
	|**Description**|Smooth the surface within the selection|
	|**Permission**|`worldedit.region.smooth`|
	|**Usage**|`;smooth [iterations] [mask]`|

!!! note ""
	
	**;faces**

	|||
	|:--|:--|
	|**Description**|Generate an outline from your selection|
	|**Permission**|`worldedit.region.faces`|
	|**Usage**|`;faces <pattern>`|

!!! note ""
	
	**;line**

	|||
	|:--|:--|
	|**Description**|Create a line between your first and second selection points|
	|**Permission**|`worldedit.region.line`|
	|**Usage**|`;line <pattern>`|

!!! note ""
	
	**;navwand**

	|||
	|:--|:--|
	|**Description**|Give yourself a navigation wand|
	|**Permission**|`worldedit.setwand`|
	|**Usage**|`;navwand`|

!!! note ""
	
	**;up**

	|||
	|:--|:--|
	|**Description**|Move up a certain number of blocks|
	|**Permission**|`worldedit.navigation.up`|
	|**Usage**|`;up <height>`|

!!! note ""
	
	**;unstuck (or ;!)**

	|||
	|:--|:--|
	|**Description**|Move out of blocks|
	|**Permission**|`worldedit.navigation.unstuck`|
	|**Usage**|`;unstuck`|

!!! note ""
	
	**;jumpto (or ;j)**

	|||
	|:--|:--|
	|**Description**|Teleport you to the top of the block you're looking at|
	|**Permission**|`worldedit.navigation.jumpto.command`|
	|**Usage**|`;jumpto`|

!!! note ""
	
	**;thru**

	|||
	|:--|:--|
	|**Description**|Teleport through any wall you look at|
	|**Permission**|`worldedit.navigation.thru.command`|
	|**Usage**|`;thru`|

!!! note ""
	
	**;tool**

	|||
	|:--|:--|
	|**Description**|Get all sorts of tools (currently only the stacker)|
	|**Permission**||
	|**Usage**|`;tool <stacker>`|

!!! note ""
	
	**;tool stacker**

	|||
	|:--|:--|
	|**Description**|Block stacker tool|
	|**Permission**|`worldedit.tool.stack`|
	|**Usage**|`;tool stacker [range] [mask]`|

!!! note ""
	
	**;brush (or ;br)**

	|||
	|:--|:--|
	|**Description**|Set the type of a brush being held|
	|**Permission**||
	|**Usage**|`;brush <none|sphere|cyl|smooth>`|

!!! note ""
	
	**;brush none**

	|||
	|:--|:--|
	|**Description**|Unbind a bound brush from your current item|
	|**Permission**||
	|**Usage**|`;brush none`|

!!! note ""
	
	**;brush sphere**

	|||
	|:--|:--|
	|**Description**|Create a sphere brush|
	|**Permission**|`worldedit.brush.sphere`|
	|**Usage**|`;brush sphere [-h] <pattern> [radius]`|

!!! note ""
	
	**;brush cyl**

	|||
	|:--|:--|
	|**Description**|Create a cylinder brush|
	|**Permission**|`worldedit.brush.cylinder`|
	|**Usage**|`;brush cyl [-h] <pattern> [radius] [height]`|

!!! note ""
	
	**;brush smooth**

	|||
	|:--|:--|
	|**Description**|Create a terrain smoothing brush|
	|**Permission**|`worldedit.brush.smooth`|
	|**Usage**|`;brush smooth [radius] [iterations] [mask]`|

!!! note ""
	
	**;mask**

	|||
	|:--|:--|
	|**Description**|Set what kind of blocks a brush can affect, if any|
	|**Permission**|`worldedit.brush.options.mask`|
	|**Usage**|`;mask [mask]`|

!!! note ""
	
	**;tracemask**

	|||
	|:--|:--|
	|**Description**|Set what kind of blocks a brush can be used on|
	|**Permission**|`worldedit.brush.options.tracemask`|
	|**Usage**|`;tracemask [mask]`|

!!! note ""
	
	**;size**

	|||
	|:--|:--|
	|**Description**|Set the size of a brush|
	|**Permission**|`worldedit.brush.options.size`|
	|**Usage**|`;size <size>`|

!!! note ""
	
	**;range**

	|||
	|:--|:--|
	|**Description**|Set how far a brush can be used from|
	|**Permission**|`worldedit.brush.options.range`|
	|**Usage**|`;range [range]`|

!!! note ""
	
	**;material**

	|||
	|:--|:--|
	|**Description**|Set what kind of blocks a brush should make|
	|**Permission**|`worldedit.brush.options.material`|
	|**Usage**|`;material <pattern>`|

!!! note ""
	
	**;undo**

	|||
	|:--|:--|
	|**Description**|Undo a certain amount of actions|
	|**Permission**|`worldedit.history.undo`|
	|**Usage**|`;undo [times]`|

!!! note ""
	
	**;redo**

	|||
	|:--|:--|
	|**Description**|Redo a certain amount of actions|
	|**Permission**|`worldedit.history.redo`|
	|**Usage**|`;redo [times]`|

!!! note ""
	
	**;clearhistory**

	|||
	|:--|:--|
	|**Description**|Clear your editing history|
	|**Permission**|`worldedit.history.clear`|
	|**Usage**|`;clearhistory`|

