# Configuration

Some parts of WorldEdit can be changed by editing a configuration file that's bundled with the addon. The location of this file depends on the platform the addon is running on, but the path relative to the `com.mojang` folder is `minecraftWorlds/(world folder)/behavior_packs/WorldEditB/scripts/config.js`.

!!! Warning

    Any changes to this file will not stay when you update the addon. You must copy this file and put it back after updating to keep your settings.

**Windows**

``` txt
%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\(path to config)
```

**Android**

``` txt
/storage/emulated/0/Android/data/com.mojang.minecraftpe/files/games/com.mojang/(path to config)
```
It's recommended that you use [CX File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer) to access this path. You must also have Minecraft's storage mode set to External.

**iOS**

``` txt
Minecraft/games/com.mojang/(path to config)
```

## Settings

| Setting | Default | Description |
| ------- | ------- | ----------- |
| DEBUG | false | Enables debugging messages in the content logs |
| MAX_HISTORY_SIZE | 20 | How many operations can be recorded in a session's history |
| HISTORY_MODE | 2 (accurate) | How to handle general undo and redo |
| BRUSH_HISTORY_MODE | 1 (fast) | How to handle brush undo and redo |
| TICKS_TO_DELETE_SESSION | 12000 (10 mins) | How long until a previously active user's session gets deleted. |
| PRINT_TO_ACTION_BAR | true | Whether using items prints their messages to the action bar or chat. |
| COMMAND_PREFIX | ; | The character that every WorldEdit comman shoukd start with. |
| WAND_ITEM | minecraft:wooden_axe | The default item the selection wand is bound to from `;wand`. |
| NAV_WAND_ITEM | minecraft:ender_pearl | The default item the navigation wand is bound to from `;navwand`. |
| NAV_WAND_DISTANCE | 128 | How far the navigation wand, along with other tool, will trace for a block of interest. |
| MAX_BRUSH_RADIUS | 6 | The maximum radius a brush is allowed to be. |
| DRAW_SELECTION | true | Whether the player's selection is visible by default |
| DEFAULT_CHANGE_LIMIT | -1 | The default amount of blocks that can be "potentially" affected within a single operation |
| MAX_CHANGE_LIMIT | -1 | The absolute change limit that can be set from the `;limit` command; bypassed with `worldedit.limit.unlimited` permission |
| ASYNC_TIME_BUDGET | 1000 | How long an async operation will run until giving Minecraft a chance to run; the higher the value, the faster the operation, but the slower Minecraft takes to run |
| FAST_MODE | false | Whether the addon should use simpler methods to run operations faster; this comes with the drawback of more limited capabilities |