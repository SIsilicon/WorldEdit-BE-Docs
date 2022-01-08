# Kit

As WorldEdit for Bedrock is made for different devices, the kit was created to make it easier to use on any control; whether it's a keyboard, touchscreen or controller. It gives access to items that act as shortcuts to many common WorldEdit functions; such as undoing, redoing, copying and pasting.

## Main items

Upon typing the command `;kit`, you are given the following items:

* <a name="selection_wand"></a>**Selection Wand ![](../img/icons/wood_axe.png):** Make selections to do stuff with. See [Quick Start](../../quick_start.md).
* <a name="selection_fill"></a>**Selection Fill ![](../img/icons/selection_fill.png):** Fill your selection with blocks determined by the pattern picker.
* <a name="pattern_picker"></a>**Pattern Picker ![](../img/icons/eyedropper.png):** Select blocks to use in a pattern. Sneaking will add blocks to the pattern. The pattern is used by Selection Fill.
* <a name="copy"></a>**Copy ![](../img/icons/copy.png):** Copy whatever is in your selection to the clipboard.
* <a name="cut"></a>**Cut ![](../img/icons/cut.png):** Cut whatever is in your selection to the clipboard. The selection is then replaced with air.
* <a name="paste"></a>**Paste ![](../img/icons/paste.png):** Paste whatever is in your clipboard to the world. The location of the paste is relative to the selection when you last copied/cut. See [Clipboard](clipboard.md).
* <a name="undo"></a>**Undo ![](../img/icons/undo.png):** Undo your previous action that affected the world. See [History](../general/history.md).
* <a name="redo"></a>**Redo ![](../img/icons/redo.png):** Redo your previous action that affected the world. See [History](../general/history.md).
* <a name="spawn_glass"></a>**Spawn Glass ![](../img/icons/spawn_glass.png):** Make a glass block where you stand. Useful for when you need to make a midair selection mark.
* <a name="flip"></a>**Flip ![](../img/icons/flip.png):** Flip your selection left to right relative to your orientation. Sneaking will make it flip about its center.
* <a name="rotate"></a>**Rotate ![](../img/icons/rotate_cw.png) ![](../img/icons/rotate_ccw.png):** Rotate your selection relative to your orientation. Sneaking will make it rotate about its center.
* <a name="mask_picker"></a>**Mask Picker ![](../img/icons/maskdropper.png):** Select blocks to use in the global mask. Like the Pattern Picker, sneaking will add blocks to the mask. This affects "Selection Fill", and the brushes. To clear it, use the command `;gmask`.
* <a name="config"></a>**WorldEdit Settings ![](../img/icons/config.png):** Enter a hotbar menu to change and setup some things about WorldEdit and the kit.

## Settings Menu

Using "WorldEdit Settings" creates a menu in your hotbar. Not to worry!  Any items in your hotbar before, will come back once you exit. Currently there are three buttons.

* **Include Air ![](../img/icons/include_air.png):** Choose whether to copy air into the clipboard. If not, empty spaces are not made when pasting.
* **Include Entities ![](../img/icons/include_entities.png):** Choose whether to copy entities into the clipboard. When cutting, entities in the selection are deleted.
* **Brush Settings ![](../img/icons/brush_config.png):** Setup brushes with this item. Before using this, be sure to place blocks that you will use in a brush's pattern and mask.