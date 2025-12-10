print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard.extensions.append(MediaKeys())

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

keyboard.row_pins = (board.GP29, board.GP6, board.GP7)
keyboard.col_pins = (board.GP3, board.GP4, board.GP2, board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP27, board.GP26, board.GP28)
    )

keyboard.keymap = [
    [KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_4,
     KC.KP_5, KC.KP_6, KC.KP_7, KC.KP_8,
     KC.KP_9, KC.KP_0, KC.KP_ENTER, KC.PLUS,]
]

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)
]

if __name__ == '__main__':
    keyboard.go()