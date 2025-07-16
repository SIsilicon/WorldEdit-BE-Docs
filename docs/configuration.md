# Configuration

Some parts of WorldEdit can be changed by editing a configuration file that's bundled with the addon. The location of this file depends on the platform the addon is running on, but the path relative to the `com.mojang` folder is `minecraftWorlds/(world folder)/behavior_packs/WorldEditB/scripts/config.js`.

!!! Warning

    Any changes to this file will not stay when you update the addon. You must copy this file and put it back after updating to keep your settings.

**Windows**

```txt
%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\(path to config)
```

**Android**

```txt
/storage/emulated/0/Android/data/com.mojang.minecraftpe/files/games/com.mojang/(path to config)
```

It's recommended that you use [CX File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer) to access this path. You must also have Minecraft's storage mode set to External.

**iOS**

```txt
Minecraft/games/com.mojang/(path to config)
```

**Dedicated Servers**

For servers, there's a dedicated file that holds configuration data called `variables.json` located in `config/default` or `config/<module_uuid>`

## Settings

| Setting              | Default               | Description                                                                                                                                                                  |
| -------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| debug                | false                 | Enables debugging messages in the content logs                                                                                                                               |
| maxHistorySize       | 25                    | How many operations can be recorded in a session's history                                                                                                                   |
| performanceMode      | false                 | Whether the addon should use simpler methods to run operations faster. This comes with the drawback of more limited capabilities.                                            |
| ticksToDeleteSession | 12000 (10 mins)       | How long until a previously active user's session gets deleted.                                                                                                              |
| printToActionBar     | true                  | Whether using items prints their messages to the action bar or chat.                                                                                                         |
| commandPrefix        | ;                     | What character(s) to use to define the beginning of custom commands. Forward slash (/) can't be used.                                                                        |
| wandItem             | minecraft:wooden_axe  | The default item the selection wand is bound to from `;wand`.                                                                                                                |
| navWandItem          | minecraft:ender_pearl | The default item the navigation wand is bound to from `;navwand`.                                                                                                            |
| traceDistance        | 256                   | How far the navigation wand, along with other tool, will trace for a block of interest.                                                                                      |
| maxBrushRadius       | 12                    | The maximum radius a brush is allowed to be.                                                                                                                                 |
| drawOutlines         | true                  | Whether the player's selections are visible by default. Apart from true or false, it also supports "local" which makes selections only visible to the players who made them. |
| defaultChangeLimit   | -1                    | The default amount of blocks that can be "potentially" affected within a single operation                                                                                    |
| maxChangeLimit       | -1                    | The absolute change limit that can be set from the `;limit` command; bypassed with `worldedit.limit.unlimited` permission                                                    |
| asyncTimeBudget      | 150                   | How long an async operation will run until giving Minecraft a chance to run; the higher the value, the faster the operation, but the slower Minecraft takes to run           |
| superPickaxeDrop     | true                  | Whether blocks broken by the super pickaxe in "single" mode drop.                                                                                                            |
| superPickaxeManyDrop | false                 | Whether blocks broken by the super pickaxe in "area" or "recursive" mode drop.                                                                                               |
