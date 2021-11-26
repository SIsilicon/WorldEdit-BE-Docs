# Navigation

You may often find yourself in need of getting to places in order to do your work better. The following commands deal with that issue.

[TOC]

## The Navigation Wand

WorldEdit gives you access to a Navigation Wand, a tool that is bound to the compass.

At any time, you can interact with the compass to jump to the top of any block you are looking at (as with the `;jumpto` command, described below). You can also use the compass while sneaking to pass through walls (as with the `;thru` command, described below).

## Freeing yourself
```
;unstuck
;!
```

This will get you out of a block if you somehow got inside it. It moves you to the top-most free position, choosing to do nothing if you were not stuck to begin with. The short alias `;!` can often be useful if you aren’t in creative mode and find yourself suffocating after pasting or generating something on top of yourself.

## Jumping to the block in sight
```
;jumpto
```

This command sends you to the top of the block that you are looking at. If that block is a vertical wall, you will be placed on top of the cliff at the very edge.

## Passing through walls
```
;thru
```

This command sends you through a wall in the direction you are looking. Just look into a wall and use the command. Make sure that you do not look downwards into a wall because it will attempt to go through the ground. This command limits the thickness of the wall to a reasonable amount.

## Ascending up an arbitrary distance
```
;up <distance>
```

This will move you up a certain number of blocks. You cannot pass through walls with this command and a glass block will be placed at your feet to support you. The glass block has to be removed manually after you are done.