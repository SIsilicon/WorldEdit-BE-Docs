# Configuration

Some parts of WorldEdit can be changed by editing a configuration file that's bundled with the addon. The location of this file depends on the platform the addon is running on, but the path relative to the `com.mojang` folder is `behavior_packs/WorldEdit[/scripts/config.js`.

!!! Warning

    Any changes to this file will not stay when you update the addon. You must copy this file and put it back after updating to keep your settings.

**Windows**

```
%localappdata%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\(path to config)
```

**Android**

```
/storage/emulated/0/Android/data/com.mojang.minecraftpe/files/games/com.mojang/(path to config)
```
It's recommended that you use CX File Explorer to access this path.

**iOS**

```
Minecraft/games/com.mojang/(path to config)
```

## Settings

|Setting            |Default        |Description |
|-------------------|---------------|------------|
| DEBUG | false | Enables debugging messages |
| MAX_HISTORY_SIZE | 20 | How many operations can be recorded in a session's history |
| HISTORY_MODE | 2 (accurate) | How to handle general undo and redo |
| BRUSH_HISTORY_MODE | 1 (fast) | How to handle brush undo and redo |
| TICKS_TO_DELETE_SESSION | 12000 (10 mins) | How long until a previously active builder's session gets deleted. |
| PLAYER_HEIGHT | 1.61 | The eye level of the player; used in raytracing |