# Utilities

The utility commands are meant for the common stuff that usually take several commands, or one larger command to be done. They're all executed from the player's position.

[TOC]

## Editing nearby blocks

Sometimes you want to set or replace blocks in an area, but don’t need a precise selection - you just want to use an area around you.

Removing blocks above and below:

```
/removeabove <size> [height]
/removebelow <size> [depth]
```
These two commands let you easily remove blocks above or below you. An example usage is to remove those tower blocks people create in order to get to a high point. The size parameter indicates the size of the cuboid to remove. The cuboid’s width and length will be (size - 1) * 2 + 1. The center of the cuboid is the block above the one that you are standing on. If you don’t specify a height or depth, the commands will extend to the extents of the world.

Removing nearby blocks:

```
;removenear <mask> <size>
```
This command removes nearby blocks of a certain type. The size parameter indicates the size of the cuboid to remove. The cuboid’s width and length will be (size - 1) * 2 + 1. The center of the cuboid is the block above the one that you are standing on.

Replacing nearby blocks:

```
;replacenear <size> <mask> <pattern>
```
If you need to quickly replace nearby blocks, this command is a nice shortcut. The size parameter indicates the size of the cuboid to replace. The cuboid’s width and length will be (size - 1) * 2 + 1. The center of the cuboid is the block above the one that you are standing on.

## Filling pits

```
;fill <pattern> <radius> [depth] [direction]
```
The fill command will start at the your position and work outward and downward, filling air with the given pattern. Note that it only works straight downward from the starting layer, so while it will fill a pond, it will not fill a cave (that goes “outward” as it goes down).

If you want to, you can also fill areas in other directions apart from down.

## Recursive Fill

```
;fillr <pattern> <radius> [depth] [direction]
```
Unlike the fill command, the recursive fill command will work outwards as it moves down, meaning it can fill caves and other holes that expand into the walls.

Like the fill command, you can specify any direction you want to fill in.

## Draining pools

```
;drain [-w] <radius>
```
The drain command can empty a pool of water or lava. It only removes connected blocks from the starting position, so it will not drain non-connected pools even if they are in the radius.

Adding the -w flag will also un-waterlog blocks, leaving them dry.

## Fixing pools

```
;fixwater <radius>
;fixlava <radius>
```
These functions deal with a very common problem of some blocks in a pool of water or lava being flowing blocks! These will turn any connected flowing water/lava blocks into source blocks.

## Let it snow!

```
;snow [-s] <size> [height]
```

This command will turn the immediate area into a winter wonderland! It will turn water into ice and snow will build up where there's sky access. Use the `-s` flag to let snow build up on top of each other with each use.

## Thawing the snow

```
;thaw <size> [height]
```

Too much snow? Fine, use this command to get rid of it and also thaw the ice as well.

## Put out fires

```
;ex <radius>
```

This command will get rid of any fire in the area. It won't get rid of the lava that started it, but hey, you get what you get. Speaking of which you should probably grab a bucket. ;)

## Removing mobs

```
;butcher [-pngabtfrw] [radius]
```
This command is basically a neat shortcut for `/kill @e`. By default it will kill everything around you (except players), but using each flag allows you to narrow it down to different kinds of mobs.

| Flag | Description |
| ------- | ----------- |
| `-p` | Kills pets (tamed animals) |
| `-n` | Kills npc, including villagers and wandering traders |
| `-g` | Kills golems |
| `-a` | Kills all land animals |
| `-b` | Kills ambient mobs |
| `-t` | Kills any entity with a name tag |
| `-f` | Kills all friendly mobs (under the hood, it's just a combination of `-pngabt`) |
| `-r` | Kills all armor stands |
| `-w` | Kills all water mobs |