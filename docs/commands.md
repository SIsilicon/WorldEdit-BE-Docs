# Commands

Commands are the main way to use the many features of WorldEdit. Type `/help` to get a list of available commands. If you don't find a command here that's in the original, look in the [differences](differences.md) page to see if it's planned.

[TOC]

## Reading this documentation

Commands may come with arguments. When you see an argument surrounded in `[square brackets]`, then that argument is optional. If it's surrounded in `<angled brackets>`, then you need to define it when using the command.

## Permissions

Each command has their own permission requirements to be useable by a player. To give yourself or anyone else permission for various commands, just type `/tag "@s, or a player name" add "permission"`. For example, `/tag @s add worldedit.region.set` would give yourself permission to use the `/wedit:set` command. You can give yourself permission for multiple comands at once. Using `worldedit.clipboard` for instance would give you permission to use every clipboard command. If you add `-` to the begin of a permission, you can also blacklist commands that use those permissions. So `-worldedit.clipboard` would _prevent_ you from using clipboard commands.

!!! note

    No command will work unless you _at least_ have explicit permission to use any worldedit command. `/tag @s add worldedit` would give you permission for all of them.

## The commands

<!--TODO: Fix expand command documentation-->
<!--COMMANDAREA-->

!!! note ""
**/wedit:worldedit (or /wedit:we)**

    |**Description**|WorldEdit commands|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:worldedit <version|perf>`|

!!! note ""
**/wedit:worldedit version**

    |**Description**|Get WorldEdit version|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:worldedit version`|

!!! note ""
**/wedit:worldedit perf**

    |**Description**|Toggle performance mode for the current session.|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:worldedit perf`|

!!! note ""
**/wedit:limit**

    |**Description**|Set the number of blocks you can change per action|
    |:--|:--|
    |**Permission**|`worldedit.limit`|
    |**Usage**|`/wedit:limit [limit]`|

!!! note ""
**/wedit:kit**

    |**Description**|Give yourself a set of items to do common worldedit functions|
    |:--|:--|
    |**Permission**|`worldedit.kit`|
    |**Usage**|`/wedit:kit`|

!!! note ""
**/wedit:toggleplace**

    |**Description**|Toggles the placement position used in various WorldEdit operations.|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:toggleplace`|

!!! note ""
**/wedit:blockid (or /wedit:id)**

    |**Description**|Prints the id and states of the block you're looking at.|
    |:--|:--|
    |**Permission**|`worldedit.blockid`|
    |**Usage**|`/wedit:blockid [type]`|

!!! note ""
**/wedit:cancel**

    |**Description**|Cancels one of, or all your active jobs.|
    |:--|:--|
    |**Permission**|`worldedit.cancel`|
    |**Usage**|`/wedit:cancel [job]`|

!!! note ""
**/wedit:pos1 (or /wedit:1)**

    |**Description**|Set the first position of your selection to the specified or current position|
    |:--|:--|
    |**Permission**|`worldedit.selection.pos`|
    |**Usage**|`/wedit:pos1 [coordinates]`|

!!! note ""
**/wedit:pos2 (or /wedit:2)**

    |**Description**|Set the second position of your selection to the specified or current position|
    |:--|:--|
    |**Permission**|`worldedit.selection.pos`|
    |**Usage**|`/wedit:pos2 [coordinates]`|

!!! note ""
**/wedit:hpos1**

    |**Description**|Set the first position of your selection to the position of the block you're facing|
    |:--|:--|
    |**Permission**|`worldedit.selection.hpos`|
    |**Usage**|`/wedit:hpos1`|

!!! note ""
**/wedit:hpos2**

    |**Description**|Set the second position of your selection to the position of the block you're facing|
    |:--|:--|
    |**Permission**|`worldedit.selection.hpos`|
    |**Usage**|`/wedit:hpos2`|

!!! note ""
**/wedit:chunk**

    |**Description**|Select your current, or specified chunk.|
    |:--|:--|
    |**Permission**|`worldedit.selection.chunk`|
    |**Usage**|`/wedit:chunk ([coordinates] [expandSelection]|<coordinates> [expandSelection])`|

!!! note ""
**/wedit:drawsel**

    |**Description**|Toggle your selection's visibility|
    |:--|:--|
    |**Permission**|`worldedit.drawsel`|
    |**Usage**|`/wedit:drawsel`|

!!! note ""
**/wedit:sel (or /wedit:deselect, /wedit:desel)**

    |**Description**|Change selection mode|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:sel [mode] [makeDefault]`|

!!! note ""
**/wedit:wand**

    |**Description**|Give yourself a selection wand|
    |:--|:--|
    |**Permission**|`worldedit.wand`|
    |**Usage**|`/wedit:wand`|

!!! note ""
**/wedit:contract**

    |**Description**|Contract the selection area|
    |:--|:--|
    |**Permission**|`worldedit.selection.contract`|
    |**Usage**|`/wedit:contract (<amount> [direction]|<amount> <reverseAmount> [direction])`|

!!! note ""
**/wedit:expand**

    |**Description**|Expand the selection area|
    |:--|:--|
    |**Permission**|`worldedit.selection.expand`|
    |**Usage**|`/wedit:expand <vert>`|

!!! note ""
**/wedit:expand vert**

    |**Description**|Vertically expand your selection to world height limits|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:expand vert [height]`|

!!! note ""
**/wedit:shift**

    |**Description**|Shift the selection area|
    |:--|:--|
    |**Permission**|`worldedit.selection.shift`|
    |**Usage**|`/wedit:shift <amount> [direction]`|

!!! note ""
**/wedit:outset**

    |**Description**|Outset the selection area|
    |:--|:--|
    |**Permission**|`worldedit.selection.outset`|
    |**Usage**|`/wedit:outset <amount> [horizontal] [vertical]`|

!!! note ""
**/wedit:inset**

    |**Description**|Inset the selection area|
    |:--|:--|
    |**Permission**|`worldedit.selection.inset`|
    |**Usage**|`/wedit:inset <amount> [horizontal] [vertical]`|

!!! note ""
**/wedit:trim**

    |**Description**|Minimize the selection to encompass matching blocks|
    |:--|:--|
    |**Permission**|`worldedit.selection.trim`|
    |**Usage**|`/wedit:trim [mask]`|

!!! note ""
**/wedit:count**

    |**Description**|Count the number of blocks that match a mask|
    |:--|:--|
    |**Permission**|`worldedit.analysis.count`|
    |**Usage**|`/wedit:count <mask>`|

!!! note ""
**/wedit:distr**

    |**Description**|Analyse the amount of different blocks in the selection|
    |:--|:--|
    |**Permission**|`worldedit.analysis.distr`|
    |**Usage**|`/wedit:distr [checkClipboard] [strict]`|

!!! note ""
**/wedit:cut**

    |**Description**|Remove your current selection and place it in the clipboard|
    |:--|:--|
    |**Permission**|`worldedit.clipboard.cut`|
    |**Usage**|`/wedit:cut [includeAir] [includeEntities] [mask] [fill]`|

!!! note ""
**/wedit:copy**

    |**Description**|Copy the current selection to the clipboard|
    |:--|:--|
    |**Permission**|`worldedit.clipboard.copy`|
    |**Usage**|`/wedit:copy [includeAir] [includeEntities] [mask]`|

!!! note ""
**/wedit:paste**

    |**Description**|Paste your clipboard into the world|
    |:--|:--|
    |**Permission**|`worldedit.clipboard.paste`|
    |**Usage**|`/wedit:paste [mask] [originalLocation] [pasteContent]`|

!!! note ""
**/wedit:clearclipboard**

    |**Description**|Clear your clipboard|
    |:--|:--|
    |**Permission**|`worldedit.clipboard.clear`|
    |**Usage**|`/wedit:clearclipboard`|

!!! note ""
**/wedit:hsphere**

    |**Description**|Generate a hollow sphere|
    |:--|:--|
    |**Permission**|`worldedit.generation.hsphere`|
    |**Usage**|`/wedit:hsphere <pattern> (<radii> [hollow] [raised] [dome]|<radiiXZ> <radiiY> [hollow] [raised] [dome]|<radiiX> <radiiY> <radiiZ> [hollow] [raised] [dome])`|

!!! note ""
**/wedit:sphere**

    |**Description**|Generate a sphere|
    |:--|:--|
    |**Permission**|`worldedit.generation.sphere`|
    |**Usage**|`/wedit:sphere <pattern> (<radii> [hollow] [raised] [dome]|<radiiXZ> <radiiY> [hollow] [raised] [dome]|<radiiX> <radiiY> <radiiZ> [hollow] [raised] [dome])`|

!!! note ""
**/wedit:cyl**

    |**Description**|Generate a cylinder|
    |:--|:--|
    |**Permission**|`worldedit.generation.cylinder`|
    |**Usage**|`/wedit:cyl <pattern> (<radii> [height] [hollow] [raised] [direction]|<radiiX> <radiiZ> [height] [hollow] [raised] [direction])`|

!!! note ""
**/wedit:hcyl**

    |**Description**|Generate a hollow cylinder|
    |:--|:--|
    |**Permission**|`worldedit.generation.hcylinder`|
    |**Usage**|`/wedit:hcyl <pattern> (<radii> [height] [raised] [direction]|<radiiX> <radiiZ> [height] [raised] [direction])`|

!!! note ""
**/wedit:pyramid**

    |**Description**|Generate a pyramid|
    |:--|:--|
    |**Permission**|`worldedit.generation.pyramid`|
    |**Usage**|`/wedit:pyramid <pattern> <size> [hollow]`|

!!! note ""
**/wedit:hpyramid**

    |**Description**|Generate a hollow pyramid|
    |:--|:--|
    |**Permission**|`worldedit.generation.pyramid`|
    |**Usage**|`/wedit:hpyramid <pattern> <size>`|

!!! note ""
**/wedit:torus**

    |**Description**|Generate a torus.|
    |:--|:--|
    |**Permission**|`worldedit.generation.torus`|
    |**Usage**|`/wedit:torus <pattern> <outerRadius> <innerRadius> [hollow] [direction]`|

!!! note ""
**/wedit:htorus**

    |**Description**|Generate a hollow torus.|
    |:--|:--|
    |**Permission**|`worldedit.generation.torus`|
    |**Usage**|`/wedit:htorus <pattern> <outerRadius> <innerRadius> [direction]`|

!!! note ""
**/wedit:gen (or /wedit:g)**

    |**Description**|Generate any kind of shape in your selection|
    |:--|:--|
    |**Permission**|`worldedit.generation.shape`|
    |**Usage**|`/wedit:gen <pattern> <expression> [hollow]`|

!!! note ""
**/wedit:gradient**

    |**Description**|Manage your gradients.|
    |:--|:--|
    |**Permission**|`worldedit.generation.gradient`|
    |**Usage**|`/wedit:gradient <create|delete|list>`|

!!! note ""
**/wedit:gradient create**

    |**Description**|Create a gradient to use in patterns.|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:gradient create <selection>`|

!!! note ""
**/wedit:gradient delete**

    |**Description**|Delete a gradient.|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:gradient delete <id>`|

!!! note ""
**/wedit:gradient list**

    |**Description**|List created gradients.|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:gradient list`|

!!! note ""
**/wedit:gmask**

    |**Description**|Set the global mask|
    |:--|:--|
    |**Permission**|`worldedit.global-mask`|
    |**Usage**|`/wedit:gmask [mask]`|

!!! note ""
**/wedit:set**

    |**Description**|Fill the selection with a block pattern|
    |:--|:--|
    |**Permission**|`worldedit.region.set`|
    |**Usage**|`/wedit:set <pattern>`|

!!! note ""
**/wedit:replace**

    |**Description**|Replace certain blocks in the selection with other blocks|
    |:--|:--|
    |**Permission**|`worldedit.region.replace`|
    |**Usage**|`/wedit:replace <mask> <pattern>`|

!!! note ""
**/wedit:move**

    |**Description**|Move the selection in a certain direction|
    |:--|:--|
    |**Permission**|`worldedit.region.move`|
    |**Usage**|`/wedit:move [amount] [offset] [replace] [includeAir] [includeEntities] [mask]`|

!!! note ""
**/wedit:stack**

    |**Description**|Repeat the contents of the current selection|
    |:--|:--|
    |**Permission**|`worldedit.region.stack`|
    |**Usage**|`/wedit:stack [count] [offset] [offsetMode] [includeAir] [includeEntities] [mask]`|

!!! note ""
**/wedit:revolve**

    |**Description**|Make copies of the selection revolving around the player|
    |:--|:--|
    |**Permission**|`worldedit.region.revolve`|
    |**Usage**|`/wedit:revolve <count> [start] [end] [heightDiff] [includeAir] [includeEntities] [direction] [mask]`|

!!! note ""
**/wedit:rotate**

    |**Description**|Rotate the selection|
    |:--|:--|
    |**Permission**|`worldedit.region.rotate`|
    |**Usage**|`/wedit:rotate <rotate> [rotateX] [rotateZ] [aroundOrigin] [affectWorld]`|

!!! note ""
**/wedit:flip**

    |**Description**|Flip the selection|
    |:--|:--|
    |**Permission**|`worldedit.region.flip`|
    |**Usage**|`/wedit:flip [direction] [aroundOrigin] [affectWorld]`|

!!! note ""
**/wedit:scale**

    |**Description**|commands.wedit:scale.description|
    |:--|:--|
    |**Permission**|`worldedit.region.scale`|
    |**Usage**|`/wedit:scale (<scale> [aroundOrigin] [affectWorld]|<scaleXZ> <scaleY> [aroundOrigin] [affectWorld]|<scaleX> <scaleY> <scaleZ> [aroundOrigin] [affectWorld])`|

!!! note ""
**/wedit:walls**

    |**Description**|Generate a wall from your selection|
    |:--|:--|
    |**Permission**|`worldedit.region.walls`|
    |**Usage**|`/wedit:walls <pattern>`|

!!! note ""
**/wedit:smooth**

    |**Description**|Smooth the surface within the selection|
    |:--|:--|
    |**Permission**|`worldedit.region.smooth`|
    |**Usage**|`/wedit:smooth [iterations] [mask]`|

!!! note ""
**/wedit:faces**

    |**Description**|Generate an outline from your selection|
    |:--|:--|
    |**Permission**|`worldedit.region.faces`|
    |**Usage**|`/wedit:faces <pattern>`|

!!! note ""
**/wedit:hollow**

    |**Description**|Hollow out the objects contained in your selection|
    |:--|:--|
    |**Permission**|`worldedit.region.hollow`|
    |**Usage**|`/wedit:hollow [thickness] [pattern]`|

!!! note ""
**/wedit:line**

    |**Description**|Create a line between your first and second selection points|
    |:--|:--|
    |**Permission**|`worldedit.region.line`|
    |**Usage**|`/wedit:line <pattern> [thickness]`|

!!! note ""
**/wedit:center (or /wedit:middle)**

    |**Description**|Set the center block(s).|
    |:--|:--|
    |**Permission**|`worldedit.region.center`|
    |**Usage**|`/wedit:center <pattern>`|

!!! note ""
**/wedit:fill**

    |**Description**|Fill an area with certain blocks|
    |:--|:--|
    |**Permission**|`worldedit.utility.fill`|
    |**Usage**|`/wedit:fill <pattern> <radius> [depth] [direction]`|

!!! note ""
**/wedit:fillr**

    |**Description**|Recursively fill an area with certain blocks|
    |:--|:--|
    |**Permission**|`worldedit.utility.fillr`|
    |**Usage**|`/wedit:fillr <pattern> <radius> [depth] [direction]`|

!!! note ""
**/wedit:removeabove**

    |**Description**|Remove blocks above you|
    |:--|:--|
    |**Permission**|`worldedit.utility.removeabove`|
    |**Usage**|`/wedit:removeabove <size> [height]`|

!!! note ""
**/wedit:removebelow**

    |**Description**|Remove blocks below you|
    |:--|:--|
    |**Permission**|`worldedit.utility.removebelow`|
    |**Usage**|`/wedit:removebelow <size> [depth]`|

!!! note ""
**/wedit:removenear**

    |**Description**|Remove nearby blocks|
    |:--|:--|
    |**Permission**|`worldedit.utility.removenear`|
    |**Usage**|`/wedit:removenear <mask> <size>`|

!!! note ""
**/wedit:replacenear**

    |**Description**|Replace nearby blocks with other blocks|
    |:--|:--|
    |**Permission**|`worldedit.utility.replacenear`|
    |**Usage**|`/wedit:replacenear <size> <mask> <pattern>`|

!!! note ""
**/wedit:drain**

    |**Description**|Drain nearby fluids|
    |:--|:--|
    |**Permission**|`worldedit.utility.drain`|
    |**Usage**|`/wedit:drain <radius>`|

!!! note ""
**/wedit:fixwater**

    |**Description**|Make nearby flowing water blocks source blocks|
    |:--|:--|
    |**Permission**|`worldedit.utility.fixwater`|
    |**Usage**|`/wedit:fixwater <radius>`|

!!! note ""
**/wedit:fixlava**

    |**Description**|Make nearby flowing lava blocks source blocks|
    |:--|:--|
    |**Permission**|`worldedit.utility.fixlava`|
    |**Usage**|`/wedit:fixlava <radius>`|

!!! note ""
**/wedit:snow**

    |**Description**|Simulate snow in the area|
    |:--|:--|
    |**Permission**|`worldedit.utility.snow`|
    |**Usage**|`/wedit:snow <size> [height] [accumulateSnow]`|

!!! note ""
**/wedit:thaw**

    |**Description**|Melt snow and ice exposed to the sky|
    |:--|:--|
    |**Permission**|`worldedit.utility.thaw`|
    |**Usage**|`/wedit:thaw <size> [height]`|

!!! note ""
**/wedit:green**

    |**Description**|Turn nearby dirt into grass|
    |:--|:--|
    |**Permission**|`worldedit.utility.green`|
    |**Usage**|`/wedit:green <radius> [strictDirt]`|

!!! note ""
**/wedit:extinguish (or /wedit:ext, /wedit:ex)**

    |**Description**|Extinguish nearby fires|
    |:--|:--|
    |**Permission**|`worldedit.utility.extinguish`|
    |**Usage**|`/wedit:extinguish <radius>`|

!!! note ""
**/wedit:calculate (or /wedit:calc, /wedit:eval, /wedit:evaluate, /wedit:solve)**

    |**Description**|Evaluate a mathematical expression.|
    |:--|:--|
    |**Permission**|`worldedit.utility.calc`|
    |**Usage**|`/wedit:calculate <expr>`|

!!! note ""
**/wedit:navwand**

    |**Description**|Give yourself a navigation wand|
    |:--|:--|
    |**Permission**|`worldedit.setwand`|
    |**Usage**|`/wedit:navwand`|

!!! note ""
**/wedit:up**

    |**Description**|Move up a certain number of blocks|
    |:--|:--|
    |**Permission**|`worldedit.navigation.up`|
    |**Usage**|`/wedit:up <height>`|

!!! note ""
**/wedit:unstuck**

    |**Description**|Move out of blocks|
    |:--|:--|
    |**Permission**|`worldedit.navigation.unstuck`|
    |**Usage**|`/wedit:unstuck`|

!!! note ""
**/wedit:jumpto (or /wedit:j)**

    |**Description**|Teleport you to the top of the block you're looking at|
    |:--|:--|
    |**Permission**|`worldedit.navigation.jumpto.command`|
    |**Usage**|`/wedit:jumpto`|

!!! note ""
**/wedit:thru**

    |**Description**|Teleport through any wall you look at|
    |:--|:--|
    |**Permission**|`worldedit.navigation.thru.command`|
    |**Usage**|`/wedit:thru`|

!!! note ""
**/wedit:ascend**

    |**Description**|Go up a floor|
    |:--|:--|
    |**Permission**|`worldedit.navigation.ascend`|
    |**Usage**|`/wedit:ascend [levels]`|

!!! note ""
**/wedit:descend**

    |**Description**|Go down a floor|
    |:--|:--|
    |**Permission**|`worldedit.navigation.descend`|
    |**Usage**|`/wedit:descend [levels]`|

!!! note ""
**/wedit:ceil**

    |**Description**|Go to the ceiling.|
    |:--|:--|
    |**Permission**|`worldedit.navigation.ceiling`|
    |**Usage**|`/wedit:ceil [clearance]`|

!!! note ""
**/wedit:tool**

    |**Description**|Get all sorts of tools|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:tool <none|stacker|extruder|selwand|navwand|farwand|cmd|fill|repl|cycler>`|

!!! note ""
**/wedit:tool none**

    |**Description**|Unbind held tool|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:tool none`|

!!! note ""
**/wedit:tool stacker**

    |**Description**|Block stacker tool|
    |:--|:--|
    |**Permission**|`worldedit.tool.stack`|
    |**Usage**|`/wedit:tool stacker [range] [mask]`|

!!! note ""
**/wedit:tool extruder**

    |**Description**|commands.wedit:tool.description.extruder|
    |:--|:--|
    |**Permission**|`worldedit.tool.extruder`|
    |**Usage**|`/wedit:tool extruder [range] [digging]`|

!!! note ""
**/wedit:tool selwand**

    |**Description**|Selection tool|
    |:--|:--|
    |**Permission**|`worldedit.setwand`|
    |**Usage**|`/wedit:tool selwand`|

!!! note ""
**/wedit:tool navwand**

    |**Description**|Navigation tool|
    |:--|:--|
    |**Permission**|`worldedit.setwand`|
    |**Usage**|`/wedit:tool navwand`|

!!! note ""
**/wedit:tool farwand**

    |**Description**|Selection tool, but can reach farther|
    |:--|:--|
    |**Permission**|`worldedit.farwand`|
    |**Usage**|`/wedit:tool farwand`|

!!! note ""
**/wedit:tool cmd**

    |**Description**|Command exeution tool; both vanilla and worldedit|
    |:--|:--|
    |**Permission**|`worldedit.tool.cmd`|
    |**Usage**|`/wedit:tool cmd <command...>`|

!!! note ""
**/wedit:tool fill**

    |**Description**|commands.wedit:tool.description.fill|
    |:--|:--|
    |**Permission**|`worldedit.utility.fill`|
    |**Usage**|`/wedit:tool fill <pattern> <radius> [depth] [direction]`|

!!! note ""
**/wedit:tool repl**

    |**Description**|Block replacer tool|
    |:--|:--|
    |**Permission**|`worldedit.repl`|
    |**Usage**|`/wedit:tool repl <pattern>`|

!!! note ""
**/wedit:tool cycler**

    |**Description**|Block cycler tool|
    |:--|:--|
    |**Permission**|`worldedit.cycler`|
    |**Usage**|`/wedit:tool cycler`|

!!! note ""
**/wedit:superpickaxe (or /wedit:sp)**

    |**Description**|Toggle the super pickaxe|
    |:--|:--|
    |**Permission**|`worldedit.superpickaxe`|
    |**Usage**|`/wedit:superpickaxe <single|area|recursive>`|

!!! note ""
**/wedit:superpickaxe single**

    |**Description**|Make the super pickaxe break a single block|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:superpickaxe single`|

!!! note ""
**/wedit:superpickaxe area**

    |**Description**|Make the super pickaxe break blocks in a cubic range|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:superpickaxe area <range>`|

!!! note ""
**/wedit:superpickaxe recursive**

    |**Description**|Make the super pickaxe break blocks starting from the initial one|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:superpickaxe recursive <range>`|

!!! note ""
**/wedit:brush (or /wedit:br)**

    |**Description**|Set the type of a brush being held|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:brush <none|sphere|cyl|smooth|struct|erode|overlay|blob>`|

!!! note ""
**/wedit:brush none**

    |**Description**|Unbind a bound brush from your current item|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:brush none`|

!!! note ""
**/wedit:brush sphere**

    |**Description**|Create a sphere brush|
    |:--|:--|
    |**Permission**|`worldedit.brush.sphere`|
    |**Usage**|`/wedit:brush sphere <pattern> [radius] [hollow]`|

!!! note ""
**/wedit:brush cyl**

    |**Description**|Create a cylinder brush|
    |:--|:--|
    |**Permission**|`worldedit.brush.cylinder`|
    |**Usage**|`/wedit:brush cyl <pattern> [radius] [height] [hollow]`|

!!! note ""
**/wedit:brush smooth**

    |**Description**|Create a terrain smoothing brush|
    |:--|:--|
    |**Permission**|`worldedit.brush.smooth`|
    |**Usage**|`/wedit:brush smooth [radius] [iterations] [mask]`|

!!! note ""
**/wedit:brush struct**

    |**Description**|Creates a brush that places structures|
    |:--|:--|
    |**Permission**|`worldedit.brush.struct`|
    |**Usage**|`/wedit:brush struct <clipboard>`|

!!! note ""
**/wedit:brush erode**

    |**Description**|Creates a terrain shaping brush|
    |:--|:--|
    |**Permission**|`worldedit.brush.erode`|
    |**Usage**|`/wedit:brush erode <lift|fill|melt|smooth>`|

!!! note ""
**/wedit:brush overlay**

    |**Description**|Creates a terrain overlaying brush|
    |:--|:--|
    |**Permission**|`worldedit.brush.overlay`|
    |**Usage**|`/wedit:brush overlay <pattern> [radius] [depth] [mask]`|

!!! note ""
**/wedit:brush blob**

    |**Description**|commands.wedit:brush.description.blob|
    |:--|:--|
    |**Permission**|`worldedit.brush.blob`|
    |**Usage**|`/wedit:brush blob <pattern> [radius] [growPercent] [smoothness]`|

!!! note ""
**/wedit:mask**

    |**Description**|Set what kind of blocks a brush can affect, if any|
    |:--|:--|
    |**Permission**|`worldedit.brush.options.mask`|
    |**Usage**|`/wedit:mask [mask]`|

!!! note ""
**/wedit:tracemask**

    |**Description**|Set what kind of blocks a brush can be used on|
    |:--|:--|
    |**Permission**|`worldedit.brush.options.tracemask`|
    |**Usage**|`/wedit:tracemask [mask]`|

!!! note ""
**/wedit:size**

    |**Description**|Set the size of a brush or get information about the selection|
    |:--|:--|
    |**Permission**||
    |**Usage**|`/wedit:size (<size>|[countClipboard])`|

!!! note ""
**/wedit:range**

    |**Description**|Set how far a brush can be used from|
    |:--|:--|
    |**Permission**|`worldedit.brush.options.range`|
    |**Usage**|`/wedit:range [range]`|

!!! note ""
**/wedit:material**

    |**Description**|Set what kind of blocks a brush should make|
    |:--|:--|
    |**Permission**|`worldedit.brush.options.material`|
    |**Usage**|`/wedit:material <pattern>`|

!!! note ""
**/wedit:undo**

    |**Description**|Undo a certain amount of actions|
    |:--|:--|
    |**Permission**|`worldedit.history.undo`|
    |**Usage**|`/wedit:undo [times]`|

!!! note ""
**/wedit:redo**

    |**Description**|Redo a certain amount of actions|
    |:--|:--|
    |**Permission**|`worldedit.history.redo`|
    |**Usage**|`/wedit:redo [times]`|

!!! note ""
**/wedit:clearhistory**

    |**Description**|Clear your editing history|
    |:--|:--|
    |**Permission**|`worldedit.history.clear`|
    |**Usage**|`/wedit:clearhistory`|

!!! note ""
**/wedit:export**

    |**Description**|Exports the selection for later use.|
    |:--|:--|
    |**Permission**|`worldedit.structure.export`|
    |**Usage**|`/wedit:export <name> [includeAir] [includeEntities]`|

!!! note ""
**/wedit:import**

    |**Description**|Imports a structure to the clipboard.|
    |:--|:--|
    |**Permission**|`worldedit.structure.import`|
    |**Usage**|`/wedit:import <name>`|

!!! note ""
**/wedit:biomeinfo**

    |**Description**|Retrieve the kinds of biomes in your selection|
    |:--|:--|
    |**Permission**|`worldedit.biome.info`|
    |**Usage**|`/wedit:biomeinfo [detectAt]`|

!!! note ""
**/wedit:setbiome**

    |**Description**|Change the biomes in your selection|
    |:--|:--|
    |**Permission**|`worldedit.biome.set`|
    |**Usage**|`/wedit:setbiome <biome> [changeAtPosition]`|
