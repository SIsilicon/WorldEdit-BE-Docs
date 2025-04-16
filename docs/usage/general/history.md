# History

Almost every operation in WorldEdit is recorded in your [session's](sessions.md) history; more specifically, any action that adds, changes or deletes blocks in your world.
This includes brush uses, filling areas with blocks, and pasting structures all around the place.

## Undo and Redo

It's important to know how to undo any actions you've made, intentional or not. You can easily do this with `/wedit:undo`, and there's also `/wedit:redo` to go forward in history as well. These two commands are also available trigerrable from the [Kit](../kit.md#undo).

!!! warning

    Side effects of block changes, such as water flowing, fire spreading and explosions are not recorded and cannot be undone.

You can also undo and redo multiple actions at once by specifying how many time to do so. For example `/wedit:undo 5` undoes 5 actions.

!!! note

    Sessions can only hold up to 25 of your last actions by default. This can be changed in the addon's config file (see [Configuration](../../configuration.md)).

Finally, you can clear your entire history with `/wedit:clearhistory`.
