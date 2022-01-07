# Kit

As WorldEdit for Bedrock is made for different devices, the kit was created to make it easier to use on any control; whether it's a keyboard, touchscreen or controller. It gives access to items that act as shortcuts to many common WorldEdit functions; such as undoing, redoing, copying and pasting.

## Main items

Upon typing the command `;kit`, you are given the following items:

* **Selection Wand (<img src="../img/icons/wood_axe.png" class="wedit-icn" id="selection_wand"/>):** Make selections to do stuff with. See [Quick Start](/quick_start).
* **Selection Fill (<img src="../img/icons/selection_fill.png" class="wedit-icn" id="selection_fill"/>):** Fill your selection with blocks determined by the pattern picker.
* **Pattern Picker (<img src="../img/icons/eyedropper.png" class="wedit-icn" id="pattern_picker"/>):** Select blocks to use in a pattern. Sneaking will add blocks to the pattern. The pattern is used by Selection Fill.
* **Copy (<img src="../img/icons/copy.png" class="wedit-icn" id="copy"/>):** Copy whatever is in your selection to the clipboard.
* **Cut (<img src="../img/icons/cut.png" class="wedit-icn" id="cut"/>):** Cut whatever is in your selection to the clipboard. The selection is then replaced with air.
* **Paste (<img src="../img/icons/paste.png" class="wedit-icn"  id="paste"/>):** Paste whatever is in your clipboard to the world. The location of the paste is relative to the selection when you last copied/cut. See [Clipboard](/usage/clipboard).
* **Undo (<img src="../img/icons/undo.png" class="wedit-icn" id="undo"/>):** Undo your previous action that affected the world. See [History](/usage/general/history).
* **Redo (<img src="../img/icons/redo.png" class="wedit-icn" id="redo"/>):** Redo your previous action that affected the world. See [History](/usage/general/history).
* **Spawn Glass (<img src="../img/icons/spawn_glass.png" class="wedit-icn" id="spawn_glass"/>):** Make a glass block where you stand. Useful for when you need to make a midair selection mark.
* **Flip (<img src="../img/icons/flip.png" class="wedit-icn" id="flip"/>):** Flip your selection left to right relative to your orientation. Sneaking will make it flip about its center.
* **Rotate (<img src="../img/icons/rotate_cw.png" class="wedit-icn" id="rotate"/> and <img src="../img/icons/rotate_ccw.png" class="wedit-icn"/>):** Rotate your selection relative to your orientation. Sneaking will make it rotate about its center.
* **Mask Picker (<img src="../img/icons/maskdropper.png" class="wedit-icn" id="mask_picker"/>):** Select blocks to use in the global mask. Like the Pattern Picker, sneaking will add blocks to the mask. This affects "Selection Fill", and the brushes. To clear it, use the command `;gmask`.
* <a name="config"></a>**WorldEdit Settings ![](/img/icons/config.png):** Enter a hotbar menu to change and setup some things about WorldEdit and the kit.

## Settings Menu

Using "WorldEdit Settings" creates a menu in your hotbar. Not to worry!  Any items in your hotbar before, will come back once you exit. Currently there are three buttons.

* **Include Air (<img src="../img/icons/include_air.png" class="wedit-icn"/>):** Choose whether to copy air into the clipboard. If not, empty spaces are not made when pasting.
* **Include Entities (<img src="../img/icons/include_entities.png" class="wedit-icn"/>):** Choose whether to copy entities into the clipboard. When cutting, entities in the selection are deleted.
* **Brush Settings (<img src="../img/icons/brush_config.png" class="wedit-icn"/>):** Setup brushes with this item. Before using this, be sure to place blocks that you will use in a brush's pattern and mask.