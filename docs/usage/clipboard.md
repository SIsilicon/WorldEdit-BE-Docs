# Clipboard

WorldEdit has a handy clipboard function that allows you to copy an area, and paste it anywhere else. Clipboard contents are currently only cuboids and copying uses the region you have selected. These operations can also done using the [Kit](kit.md).

[TOC]

Note that like history, your current clipboard is stored in your session and thus will be kept for 10 minutes by default after logging off (deleted immediately in singleplayer).

Also like history, your current clipboard can be cleared with the `/wedit:clearclipboard` command.

## Copy and cut

The `/wedit:copy` command copies your current selection to your session’s clipboard, keeping track of where you are relative to the copy. The second part of that sentence is very important; if you want to later paste, for example, a bridge so that it is under where you are standing, you must stand in a location above the bridge when you make the copy. This method allows you to easily align your later paste because you can plan ahead a bit. It requires some spatial abilities to master the copying process, but you will find it particularly helpful once you get the hang of it.

`/wedit:cut` works just like `/wedit:copy` except that it also deletes the selected area afterwards. By default, it leaves air, but you can also specify a different block to leave behind.

!!! Note

    This remembers your current position relative to the copy. This is a very important concept to grasp otherwise you will not be able to control where you paste your copy!

Both commands have three additional flags:

-   `-a` can be used to remove air from your selection, so that it doesn't replace anything when pasting.
-   `-e` can be specified to also copy/cut entities from the selection.
-   `-m <mask>` can be used to specify a mask of blocks to copy/cut. Any blocks that do not match will be replaced with air in your clipboard.

## Pasting

Once you have something in your clipboard, you can paste it to the world. If you want the copy to paste at the same point that it was copied at, type `/wedit:paste -o`, otherwise the paste will be placed relative to you. Remember that if you are pasting relatively, it will be relative to where you were when you made the initial copy. For example, if you were on top of your castle when you copied it, pasting it would result in the castle being pasted under you.

<!-- ..;..;_images;copypasta.png
A primer on how relative positions work for clipboards -->

Like cut and copy, paste has some additional flags:

-   `-s` will set your selection to the area you are pasting into.
-   `-n` will set your selection like `-s` does, but will not actually paste anything. This can be useful to check where your clipboard will end up before actually pasting.
-   `-o` will paste the clipboard back to its original origin, as explained above. This will disregard the entire “relative positions”.
