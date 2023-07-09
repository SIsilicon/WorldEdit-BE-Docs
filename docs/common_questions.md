# Frequently Asked Questions

[TOC]

## How do I use this addon?

The documentation is full of neat information! As a beginner, it's best to start in the [Quick Start page](quick_start.md).

## Does it work on consoles?

In theory the addon should work on consoles, but it hasn't been tested on those. Realms can be used to transfer a world with the addon installed.

## Why isn't the addon working for me?

There are four possible reasons why your addon may not be working.

1. You didn't enable the "Beta API" experimental feature.
2. You didn't apply both the behaviour pack and resource pack to your world.
3. You are not playing on the right version of Minecraft. As of writing, the addon supports 1.20.10.
4. The addon may be broken for you. There isn't a known reason why, but you can try three things.

    * Restart Minecraft
    * Redownload the addon
    * Reinstall Minecraft

    You may report the bug [here](https://github.com/SIsilicon/WorldEdit-BE/issues).

## Can I use WorldEdit with other addons?

It should be compatible with any other addon you have in your world, but said compatibility is not guaranteed. For instance, if another addon is using custom server forms, manipulates your hotbar, or uses the acion bar for certain effects, it might clash with this addon.

## How do I make coloured blocks, different types of wood, etc...?

How Minecraft works is that some blocks are just variations of a base block. Granite for instance is just a variation of stone. To define these variations, you can use either data values (deprecated in vanilla Minecraft), or block states (`stone_slab[stone_slab_type=brick]` = brick slabs). For more information on blocks in commands, go to [this docs page](usage/general/patterns.md).
 
## How do I remove selection particles?

That depends on the outcome you want.
- Use `;drawsel` to toggle the visiblity of the selection. The selection is still there, so you can still use your usual selection based commands.
- Use `;desel` to clear your selection (not the blocks inside. Use `;cut` for that). As soon as you start making your selection it will once again be highlighted with particles, unless you used `;drawsel` to disable it.

## How do I uninstall the addon from the world?

[See this section in the intallation page.](installation.md#uninstalling-from-a-world)

## Why does the message "Cannot modify unloaded chunks" show?

This usually is because the operation you're attempting, may also affect parts of your world that aren't "loaded"; loaded in the sense that things actually update in those chunks (grass growing, TNT exploding, redstone updating, etc...). If you can, perform your operation in smaller pieces. If not, make more chunks loaded by either increasing your Simulation Distance, or adding ticking areas where necessary.

## May I (use this on my server / showcase this)?

You are allowed to do so. Mind you that the addon is work in progress, so keep regular backups of your world.

## Are you affiliated with the original mod creators?

Nope! I (SIsilicon) developed this addon on my own with help from various contributors.

## My question hasn't been answered here. Where else can I ask?

There is a [Discord](https://discord.gg/M5uAkr9WU2) server for this addon. You can go there, hangout, and ask away.
