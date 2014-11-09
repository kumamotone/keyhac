from keyhac import *
from pyauto import *

def configure(keymap):
    if 1:
        keymap_global = keymap.defineWindowKeymap()

        # vi風にカーソル移動
        keymap_global[ "C-B" ] = "Left"
        keymap_global[ "C-N" ] = "Down"
        keymap_global[ "C-P" ] = "Up"
        keymap_global[ "C-F" ] = "Right"

        keymap_global[ "C-H" ] = "BackSpace"
        keymap_global[ "C-D" ] = "Delete"
        
        keymap_global[ "C-A" ] = "Home"
        keymap_global[ "C-E" ] = "End"

		keymap_global[ "C-M" ] = "Enter"

        keymap_global[ "C-K" ] = "End" "Delete"

        # Ctrl
        keymap_global[ "C-Commma" ] = "C-Left"
        keymap_global[ "C-Period" ] = "C-Right"


