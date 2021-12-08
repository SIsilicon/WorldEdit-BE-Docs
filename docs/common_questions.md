# Frequently Asked Questions

[TOC]

## Does it work on consoles?

The GameTest Framework, an API this addon relies on, does not on work on Playstation nor the Nintendo Switch as of writing. Theoratically, it should work on XBox, but it hasn't been tested. If you want to use it on consoles, you can host a server/world somewhere else and join that world.

## Why isn't the addon working for me?

There are three possible reasons why your addon may not be working.

1. You didn't enable both "Holiday Creator Features" and "Enable Gametest Framework".
2. You didn't apply both the behaviour pack and resource pack to your world.
3. The addon may be broken for you. There isn't a known reason why, but until that's resolved, you can try two things.

    * Restart Minecraft
    * Reinstall Minecraft 
  
    You may report the bug [here](https://github.com/SIsilicon/WorldEdit-BE/issues).

## Can I use WorldEdit with other addons?

It should be compatible with any other addon you have in your world.

## How do I make coloured blocks, different type of wood, etc...?

How Minecraft works is that some blocks are just variations of a base block. Red wool for example is just a variation of the default white wool, and granite is just a variation of stone. To define these variations, you can use either data values (`wool:1` = orange wool), or block states (`stone_slab['stone_slab_type':'brick']` = brick slabs). For more information on blocks in commands, go to [this docs page](usage/general/patterns.md).
 
## How do I uninstall the addon from the world?

Because the addon uses scripts, Minecraft does not allow you to deactivate the behaviour pack. You'll have to uninstall manually by deleting the behaviour pack from the world's behaviour pack folder.

## Why does the message "History was already being recorded" show?

Something went wrong while the addon was being used. Restarting the world, Restarting Minecraft or Reinstalling the game might fix this, but if not, please report the issue [here](https://github.com/SIsilicon/WorldEdit-BE/issues).

## May I (use this on my server / showcase this)?

You are allowed to do so. Mind you that the addon is Work in Progress, so keep regular backups of your world.

## Are you affiliated with the original mod creators?

Nope! I developed this addon on my own.

## My question hasn't been answered here; Where else can I ask?

I have a [Discord](https://discord.gg/M5uAkr9WU2) server for this addon. You can go there, hangout, and ask away.
