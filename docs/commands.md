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
<!--TODO: Fix expand command documentation-->
<!--COMMANDAREA-->
!!! note ""
	
	**;help (or ;?)**

	|**Description**|Get a list of commands available and a quick description for each of them|
	|:--|:--|
	|**Permission**|`worldedit.help`|
	|**Usage**|`;help ([page]|<command>)`|

!!! note ""
	
	**;worldedit (or ;we)**

	|**Description**|WorldEdit commands|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;worldedit <version|perf>`|

!!! note ""
	
	**;worldedit version**

	|**Description**|Get WorldEdit version|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;worldedit version`|

!!! note ""
	
	**;worldedit perf**

	|**Description**|Toggle performance mode for the current session.|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;worldedit perf`|

!!! note ""
	
	**;limit**

	|**Description**|Set the number of blocks you can change per action|
	|:--|:--|
	|**Permission**|`worldedit.limit`|
	|**Usage**|`;limit [limit]`|

!!! note ""
	
	**;kit**

	|**Description**|Give yourself a set of items to do common worldedit functions|
	|:--|:--|
	|**Permission**|`worldedit.kit`|
	|**Usage**|`;kit`|

!!! note ""
	
	**;toggleplace**

	|**Description**|Toggles the placement position used in various WorldEdit operations.|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;toggleplace`|

!!! note ""
	
	**;blockid (or ;id)**

	|**Description**|Prints the id and states of the block you're looking at.|
	|:--|:--|
	|**Permission**|`worldedit.blockid`|
	|**Usage**|`;blockid [-d]`|

!!! note ""
	
	**;cancel**

	|**Description**|Cancels one of, or all your active jobs.|
	|:--|:--|
	|**Permission**|`worldedit.cancel`|
	|**Usage**|`;cancel [job]`|

!!! note ""
	
	**;pos1 (or ;1)**

	|**Description**|Set the first position of your selection to the specified or current position|
	|:--|:--|
	|**Permission**|`worldedit.selection.pos`|
	|**Usage**|`;pos1 [coordinates]`|

!!! note ""
	
	**;pos2 (or ;2)**

	|**Description**|Set the second position of your selection to the specified or current position|
	|:--|:--|
	|**Permission**|`worldedit.selection.pos`|
	|**Usage**|`;pos2 [coordinates]`|

!!! note ""
	
	**;hpos1**

	|**Description**|Set the first position of your selection to the position of the block you're facing|
	|:--|:--|
	|**Permission**|`worldedit.selection.hpos`|
	|**Usage**|`;hpos1`|

!!! note ""
	
	**;hpos2**

	|**Description**|Set the second position of your selection to the position of the block you're facing|
	|:--|:--|
	|**Permission**|`worldedit.selection.hpos`|
	|**Usage**|`;hpos2`|

!!! note ""
	
	**;chunk**

	|**Description**|Select your current, or specified chunk.|
	|:--|:--|
	|**Permission**|`worldedit.selection.chunk`|
	|**Usage**|`;chunk [-cs] ([coordinates]|<coordinates>)`|

!!! note ""
	
	**;drawsel**

	|**Description**|Toggle your selection's visibility|
	|:--|:--|
	|**Permission**|`worldedit.drawsel`|
	|**Usage**|`;drawsel`|

!!! note ""
	
	**;sel (or ;deselect, ;desel)**

	|**Description**|Change selection mode|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;sel <cuboid|extend|sphere|cyl>`|

!!! note ""
	
	**;sel cuboid**

	|**Description**|Select two corners of a cuboid|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;sel [-d] cuboid`|

!!! note ""
	
	**;sel extend**

	|**Description**|Fast cuboid selection mode|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;sel [-d] extend`|

!!! note ""
	
	**;sel sphere**

	|**Description**|Select a sphere|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;sel [-d] sphere`|

!!! note ""
	
	**;sel cyl**

	|**Description**|Select a cylinder|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;sel [-d] cyl`|

!!! note ""
	
	**;wand**

	|**Description**|Give yourself a selection wand|
	|:--|:--|
	|**Permission**|`worldedit.wand`|
	|**Usage**|`;wand`|

!!! note ""
	
	**;contract**

	|**Description**|Contract the selection area|
	|:--|:--|
	|**Permission**|`worldedit.selection.contract`|
	|**Usage**|`;contract (<amount> [direction]|<amount> <reverseAmount> [direction])`|

!!! note ""
	
	**;expand**

	|**Description**|Expand the selection area|
	|:--|:--|
	|**Permission**|`worldedit.selection.expand`|
	|**Usage**|`;expand <vert>`|

!!! note ""
	
	**;expand vert**

	|**Description**|Vertically expand your selection to world height limits|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;expand vert [height]`|

!!! note ""
	
	**;shift**

	|**Description**|Shift the selection area|
	|:--|:--|
	|**Permission**|`worldedit.selection.shift`|
	|**Usage**|`;shift <amount> [direction]`|

!!! note ""
	
	**;outset**

	|**Description**|Outset the selection area|
	|:--|:--|
	|**Permission**|`worldedit.selection.outset`|
	|**Usage**|`;outset [-hv] <amount>`|

!!! note ""
	
	**;inset**

	|**Description**|Inset the selection area|
	|:--|:--|
	|**Permission**|`worldedit.selection.inset`|
	|**Usage**|`;inset [-hv] <amount>`|

!!! note ""
	
	**;trim**

	|**Description**|Minimize the selection to encompass matching blocks|
	|:--|:--|
	|**Permission**|`worldedit.selection.trim`|
	|**Usage**|`;trim [mask]`|

!!! note ""
	
	**;count**

	|**Description**|Count the number of blocks that match a mask|
	|:--|:--|
	|**Permission**|`worldedit.analysis.count`|
	|**Usage**|`;count <mask>`|

!!! note ""
	
	**;distr**

	|**Description**|Analyse the amount of different blocks in the selection|
	|:--|:--|
	|**Permission**|`worldedit.analysis.distr`|
	|**Usage**|`;distr [-cd]`|

!!! note ""
	
	**;cut**

	|**Description**|Remove your current selection and place it in the clipboard|
	|:--|:--|
	|**Permission**|`worldedit.clipboard.cut`|
	|**Usage**|`;cut [-ae] [fill] [-m <mask>]`|

!!! note ""
	
	**;copy**

	|**Description**|Copy the current selection to the clipboard|
	|:--|:--|
	|**Permission**|`worldedit.clipboard.copy`|
	|**Usage**|`;copy [-aem <mask>]`|

!!! note ""
	
	**;paste**

	|**Description**|Paste your clipboard into the world|
	|:--|:--|
	|**Permission**|`worldedit.clipboard.paste`|
	|**Usage**|`;paste [-osnm <mask>]`|

!!! note ""
	
	**;clearclipboard**

	|**Description**|Clear your clipboard|
	|:--|:--|
	|**Permission**|`worldedit.clipboard.clear`|
	|**Usage**|`;clearclipboard`|

!!! note ""
	
	**;hsphere**

	|**Description**|Generate a hollow sphere|
	|:--|:--|
	|**Permission**|`worldedit.generation.sphere`|
	|**Usage**|`;hsphere [-rd <dome>] <pattern> <radii>`|

!!! note ""
	
	**;sphere**

	|**Description**|Generate a sphere|
	|:--|:--|
	|**Permission**|`worldedit.generation.sphere`|
	|**Usage**|`;sphere [-hrd <dome>] <pattern> <radii>`|

!!! note ""
	
	**;cyl**

	|**Description**|Generate a cylinder|
	|:--|:--|
	|**Permission**|`worldedit.generation.cylinder`|
	|**Usage**|`;cyl [-hrd <direction>] <pattern> <radii> [height]`|

!!! note ""
	
	**;hcyl**

	|**Description**|Generate a hollow cylinder|
	|:--|:--|
	|**Permission**|`worldedit.generation.cylinder`|
	|**Usage**|`;hcyl [-rd <direction>] <pattern> <radii> [height]`|

!!! note ""
	
	**;pyramid**

	|**Description**|Generate a pyramid|
	|:--|:--|
	|**Permission**|`worldedit.generation.pyramid`|
	|**Usage**|`;pyramid [-h] <pattern> <size>`|

!!! note ""
	
	**;hpyramid**

	|**Description**|Generate a hollow pyramid|
	|:--|:--|
	|**Permission**|`worldedit.generation.pyramid`|
	|**Usage**|`;hpyramid <pattern> <size>`|

!!! note ""
	
	**;torus**

	|**Description**|Generate a torus.|
	|:--|:--|
	|**Permission**|`worldedit.generation.torus`|
	|**Usage**|`;torus [-hd <direction>] <pattern> <outerRadius> <innerRadius>`|

!!! note ""
	
	**;htorus**

	|**Description**|Generate a hollow torus.|
	|:--|:--|
	|**Permission**|`worldedit.generation.torus`|
	|**Usage**|`;htorus [-d <direction>] <pattern> <outerRadius> <innerRadius>`|

!!! note ""
	
	**;gen (or ;g)**

	|**Description**|Generate any kind of shape in your selection|
	|:--|:--|
	|**Permission**|`worldedit.generation.shape`|
	|**Usage**|`;gen [-h] <pattern> <expr>`|

!!! note ""
	
	**;gradient**

	|**Description**|Manage your gradients.|
	|:--|:--|
	|**Permission**|`worldedit.generation.gradient`|
	|**Usage**|`;gradient <create|delete|list>`|

!!! note ""
	
	**;gradient create**

	|**Description**|Create a gradient to use in patterns.|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;gradient create [-sf <fade>] <id> [patterns...]`|

!!! note ""
	
	**;gradient delete**

	|**Description**|Delete a gradient.|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;gradient delete <id>`|

!!! note ""
	
	**;gradient list**

	|**Description**|List created gradients.|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;gradient list`|

!!! note ""
	
	**;gmask**

	|**Description**|Set the global mask|
	|:--|:--|
	|**Permission**|`worldedit.global-mask`|
	|**Usage**|`;gmask [mask]`|

!!! note ""
	
	**;set**

	|**Description**|Fill the selection with a block pattern|
	|:--|:--|
	|**Permission**|`worldedit.region.set`|
	|**Usage**|`;set <pattern>`|

!!! note ""
	
	**;replace**

	|**Description**|Replace certain blocks in the selection with other blocks|
	|:--|:--|
	|**Permission**|`worldedit.region.replace`|
	|**Usage**|`;replace <mask> <pattern>`|

!!! note ""
	
	**;move**

	|**Description**|Move the selection in a certain direction|
	|:--|:--|
	|**Permission**|`worldedit.region.move`|
	|**Usage**|`;move [-aes] [amount] [offset] [replace] [-m <mask>]`|

!!! note ""
	
	**;stack**

	|**Description**|Repeat the contents of the current selection|
	|:--|:--|
	|**Permission**|`worldedit.region.stack`|
	|**Usage**|`;stack [-aers] [count] [offset] [-m <mask>]`|

!!! note ""
	
	**;revolve**

	|**Description**|Make copies of the selection revolving around the player|
	|:--|:--|
	|**Permission**|`worldedit.region.revolve`|
	|**Usage**|`;revolve [-as] <count> [start] [end] [heightDiff] [-d <direction>] [-m <mask>]`|

!!! note ""
	
	**;rotate**

	|**Description**|Rotate the selection|
	|:--|:--|
	|**Permission**|`worldedit.region.rotate`|
	|**Usage**|`;rotate [-ows] <rotate> [rotateX] [rotateZ]`|

!!! note ""
	
	**;flip**

	|**Description**|Flip the selection|
	|:--|:--|
	|**Permission**|`worldedit.region.flip`|
	|**Usage**|`;flip [-ows] [direction]`|

!!! note ""
	
	**;walls**

	|**Description**|Generate a wall from your selection|
	|:--|:--|
	|**Permission**|`worldedit.region.walls`|
	|**Usage**|`;walls <pattern>`|

!!! note ""
	
	**;smooth**

	|**Description**|Smooth the surface within the selection|
	|:--|:--|
	|**Permission**|`worldedit.region.smooth`|
	|**Usage**|`;smooth [iterations] [mask]`|

!!! note ""
	
	**;faces**

	|**Description**|Generate an outline from your selection|
	|:--|:--|
	|**Permission**|`worldedit.region.faces`|
	|**Usage**|`;faces <pattern>`|

!!! note ""
	
	**;hollow**

	|**Description**|Hollow out the objects contained in your selection|
	|:--|:--|
	|**Permission**|`worldedit.region.hollow`|
	|**Usage**|`;hollow [thickness] [pattern]`|

!!! note ""
	
	**;line**

	|**Description**|Create a line between your first and second selection points|
	|:--|:--|
	|**Permission**|`worldedit.region.line`|
	|**Usage**|`;line <pattern>`|

!!! note ""
	
	**;center (or ;middle)**

	|**Description**|Set the center block(s).|
	|:--|:--|
	|**Permission**|`worldedit.region.center`|
	|**Usage**|`;center <pattern>`|

!!! note ""
	
	**;fill**

	|**Description**|Fill an area with certain blocks|
	|:--|:--|
	|**Permission**|`worldedit.utility.fill`|
	|**Usage**|`;fill <pattern> <radius> [depth] [direction]`|

!!! note ""
	
	**;fillr**

	|**Description**|Recursively fill an area with certain blocks|
	|:--|:--|
	|**Permission**|`worldedit.utility.fillr`|
	|**Usage**|`;fillr <pattern> <radius> [depth] [direction]`|

!!! note ""
	
	**;removeabove**

	|**Description**|Remove blocks above you|
	|:--|:--|
	|**Permission**|`worldedit.utility.removeabove`|
	|**Usage**|`;removeabove <size> [height]`|

!!! note ""
	
	**;removebelow**

	|**Description**|Remove blocks below you|
	|:--|:--|
	|**Permission**|`worldedit.utility.removebelow`|
	|**Usage**|`;removebelow <size> [depth]`|

!!! note ""
	
	**;removenear**

	|**Description**|Remove nearby blocks|
	|:--|:--|
	|**Permission**|`worldedit.utility.removenear`|
	|**Usage**|`;removenear <mask> <size>`|

!!! note ""
	
	**;replacenear**

	|**Description**|Replace nearby blocks with other blocks|
	|:--|:--|
	|**Permission**|`worldedit.utility.replacenear`|
	|**Usage**|`;replacenear <size> <mask> <pattern>`|

!!! note ""
	
	**;drain**

	|**Description**|Drain nearby fluids|
	|:--|:--|
	|**Permission**|`worldedit.utility.drain`|
	|**Usage**|`;drain [-w] <radius>`|

!!! note ""
	
	**;fixwater**

	|**Description**|Make nearby flowing water blocks source blocks|
	|:--|:--|
	|**Permission**|`worldedit.utility.fixwater`|
	|**Usage**|`;fixwater <radius>`|

!!! note ""
	
	**;fixlava**

	|**Description**|Make nearby flowing lava blocks source blocks|
	|:--|:--|
	|**Permission**|`worldedit.utility.fixlava`|
	|**Usage**|`;fixlava <radius>`|

!!! note ""
	
	**;snow**

	|**Description**|Simulate snow in the area|
	|:--|:--|
	|**Permission**|`worldedit.utility.snow`|
	|**Usage**|`;snow [-s] <size> [height]`|

!!! note ""
	
	**;thaw**

	|**Description**|Melt snow and ice exposed to the sky|
	|:--|:--|
	|**Permission**|`worldedit.utility.thaw`|
	|**Usage**|`;thaw <size> [height]`|

!!! note ""
	
	**;green**

	|**Description**|Turn nearby dirt into grass|
	|:--|:--|
	|**Permission**|`worldedit.utility.green`|
	|**Usage**|`;green [-f] <radius>`|

!!! note ""
	
	**;extinguish (or ;ext, ;ex)**

	|**Description**|Extinguish nearby fires|
	|:--|:--|
	|**Permission**|`worldedit.utility.extinguish`|
	|**Usage**|`;extinguish <radius>`|

!!! note ""
	
	**;butcher**

	|**Description**|Kill nearby entities.|
	|:--|:--|
	|**Permission**|`worldedit.utility.butcher`|
	|**Usage**|`;butcher [-pngabtrwf] [radius]`|

!!! note ""
	
	**;calculate (or ;calc, ;eval, ;evaluate, ;solve)**

	|**Description**|Evaluate a mathematical expression.|
	|:--|:--|
	|**Permission**|`worldedit.utility.calc`|
	|**Usage**|`;calculate <expr>`|

!!! note ""
	
	**;navwand**

	|**Description**|Give yourself a navigation wand|
	|:--|:--|
	|**Permission**|`worldedit.setwand`|
	|**Usage**|`;navwand`|

!!! note ""
	
	**;up**

	|**Description**|Move up a certain number of blocks|
	|:--|:--|
	|**Permission**|`worldedit.navigation.up`|
	|**Usage**|`;up <height>`|

!!! note ""
	
	**;unstuck (or ;!)**

	|**Description**|Move out of blocks|
	|:--|:--|
	|**Permission**|`worldedit.navigation.unstuck`|
	|**Usage**|`;unstuck`|

!!! note ""
	
	**;jumpto (or ;j)**

	|**Description**|Teleport you to the top of the block you're looking at|
	|:--|:--|
	|**Permission**|`worldedit.navigation.jumpto.command`|
	|**Usage**|`;jumpto`|

!!! note ""
	
	**;thru**

	|**Description**|Teleport through any wall you look at|
	|:--|:--|
	|**Permission**|`worldedit.navigation.thru.command`|
	|**Usage**|`;thru`|

!!! note ""
	
	**;ascend**

	|**Description**|Go up a floor|
	|:--|:--|
	|**Permission**|`worldedit.navigation.ascend`|
	|**Usage**|`;ascend [levels]`|

!!! note ""
	
	**;descend**

	|**Description**|Go down a floor|
	|:--|:--|
	|**Permission**|`worldedit.navigation.descend`|
	|**Usage**|`;descend [levels]`|

!!! note ""
	
	**;ceil**

	|**Description**|Go to the ceiling.|
	|:--|:--|
	|**Permission**|`worldedit.navigation.ceiling`|
	|**Usage**|`;ceil [clearance]`|

!!! note ""
	
	**;tool**

	|**Description**|Get all sorts of tools|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;tool <none|stacker|selwand|navwand|farwand|cmd|repl|cycler>`|

!!! note ""
	
	**;tool none**

	|**Description**|Unbind held tool|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;tool none`|

!!! note ""
	
	**;tool stacker**

	|**Description**|Block stacker tool|
	|:--|:--|
	|**Permission**|`worldedit.tool.stack`|
	|**Usage**|`;tool stacker [range] [mask]`|

!!! note ""
	
	**;tool selwand**

	|**Description**|Selection tool|
	|:--|:--|
	|**Permission**|`worldedit.setwand`|
	|**Usage**|`;tool selwand`|

!!! note ""
	
	**;tool navwand**

	|**Description**|Navigation tool|
	|:--|:--|
	|**Permission**|`worldedit.setwand`|
	|**Usage**|`;tool navwand`|

!!! note ""
	
	**;tool farwand**

	|**Description**|Selection tool, but can reach farther|
	|:--|:--|
	|**Permission**|`worldedit.farwand`|
	|**Usage**|`;tool farwand`|

!!! note ""
	
	**;tool cmd**

	|**Description**|Command exeution tool; both vanilla and worldedit|
	|:--|:--|
	|**Permission**|`worldedit.tool.cmd`|
	|**Usage**|`;tool cmd <command...>`|

!!! note ""
	
	**;tool repl**

	|**Description**|Block replacer tool|
	|:--|:--|
	|**Permission**|`worldedit.repl`|
	|**Usage**|`;tool repl <pattern>`|

!!! note ""
	
	**;tool cycler**

	|**Description**|Block cycler tool|
	|:--|:--|
	|**Permission**|`worldedit.cycler`|
	|**Usage**|`;tool cycler`|

!!! note ""
	
	**;superpickaxe (or ;sp)**

	|**Description**|Toggle the super pickaxe|
	|:--|:--|
	|**Permission**|`worldedit.superpickaxe`|
	|**Usage**|`;superpickaxe <single|area|recursive>`|

!!! note ""
	
	**;superpickaxe single**

	|**Description**|Make the super pickaxe break a single block|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;superpickaxe single`|

!!! note ""
	
	**;superpickaxe area**

	|**Description**|Make the super pickaxe break blocks in a cubic range|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;superpickaxe area <range>`|

!!! note ""
	
	**;superpickaxe recursive**

	|**Description**|Make the super pickaxe break blocks starting from the initial one|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;superpickaxe recursive <range>`|

!!! note ""
	
	**;brush (or ;br)**

	|**Description**|Set the type of a brush being held|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;brush <none|sphere|cyl|smooth|struct|erode|overlay>`|

!!! note ""
	
	**;brush none**

	|**Description**|Unbind a bound brush from your current item|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;brush none`|

!!! note ""
	
	**;brush sphere**

	|**Description**|Create a sphere brush|
	|:--|:--|
	|**Permission**|`worldedit.brush.sphere`|
	|**Usage**|`;brush sphere [-h] <pattern> [radius]`|

!!! note ""
	
	**;brush cyl**

	|**Description**|Create a cylinder brush|
	|:--|:--|
	|**Permission**|`worldedit.brush.cylinder`|
	|**Usage**|`;brush cyl [-h] <pattern> [radius] [height]`|

!!! note ""
	
	**;brush smooth**

	|**Description**|Create a terrain smoothing brush|
	|:--|:--|
	|**Permission**|`worldedit.brush.smooth`|
	|**Usage**|`;brush smooth [radius] [iterations] [mask]`|

!!! note ""
	
	**;brush struct**

	|**Description**|Creates a brush that places structures|
	|:--|:--|
	|**Permission**|`worldedit.brush.struct`|
	|**Usage**|`;brush struct <clipboard>`|

!!! note ""
	
	**;brush erode**

	|**Description**|Creates a terrain shaping brush|
	|:--|:--|
	|**Permission**|`worldedit.brush.erode`|
	|**Usage**|`;brush erode <lift|fill|melt|smooth>`|

!!! note ""
	
	**;brush overlay**

	|**Description**|Creates a terrain overlaying brush|
	|:--|:--|
	|**Permission**|`worldedit.brush.overlay`|
	|**Usage**|`;brush overlay <pattern> [radius] [depth] [mask]`|

!!! note ""
	
	**;mask**

	|**Description**|Set what kind of blocks a brush can affect, if any|
	|:--|:--|
	|**Permission**|`worldedit.brush.options.mask`|
	|**Usage**|`;mask [mask]`|

!!! note ""
	
	**;tracemask**

	|**Description**|Set what kind of blocks a brush can be used on|
	|:--|:--|
	|**Permission**|`worldedit.brush.options.tracemask`|
	|**Usage**|`;tracemask [mask]`|

!!! note ""
	
	**;size**

	|**Description**|Set the size of a brush or get information about the selection|
	|:--|:--|
	|**Permission**||
	|**Usage**|`;size (<size>|[-c])`|

!!! note ""
	
	**;range**

	|**Description**|Set how far a brush can be used from|
	|:--|:--|
	|**Permission**|`worldedit.brush.options.range`|
	|**Usage**|`;range [range]`|

!!! note ""
	
	**;material**

	|**Description**|Set what kind of blocks a brush should make|
	|:--|:--|
	|**Permission**|`worldedit.brush.options.material`|
	|**Usage**|`;material <pattern>`|

!!! note ""
	
	**;undo**

	|**Description**|Undo a certain amount of actions|
	|:--|:--|
	|**Permission**|`worldedit.history.undo`|
	|**Usage**|`;undo [times]`|

!!! note ""
	
	**;redo**

	|**Description**|Redo a certain amount of actions|
	|:--|:--|
	|**Permission**|`worldedit.history.redo`|
	|**Usage**|`;redo [times]`|

!!! note ""
	
	**;clearhistory**

	|**Description**|Clear your editing history|
	|:--|:--|
	|**Permission**|`worldedit.history.clear`|
	|**Usage**|`;clearhistory`|

!!! note ""
	
	**;export**

	|**Description**|Exports the selection for later use.|
	|:--|:--|
	|**Permission**|`worldedit.structure.export`|
	|**Usage**|`;export [-ea] <name>`|

!!! note ""
	
	**;import**

	|**Description**|Imports a structure to the clipboard.|
	|:--|:--|
	|**Permission**|`worldedit.structure.import`|
	|**Usage**|`;import <name>`|

!!! note ""
	
	**;biomeinfo**

	|**Description**|Retrieve the kinds of biomes in your selection|
	|:--|:--|
	|**Permission**|`worldedit.biome.info`|
	|**Usage**|`;biomeinfo [-pt]`|

!!! note ""
	
	**;setbiome**

	|**Description**|Change the biomes in your selection|
	|:--|:--|
	|**Permission**|`worldedit.biome.set`|
	|**Usage**|`;setbiome <biome> [-p]`|

