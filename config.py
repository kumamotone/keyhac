﻿from keyhac import *
from pyauto import *

def configure(keymap):
    # キーバインドに"したくない"アプリケーションソフトを指定する（False を返す）
    def is_target(window):
        if window.getProcessName() in ("cmd.exe",            # cmd
                                       "mintty.exe",         # mintty
                                       "gvim.exe",           # GVim
                                       # "eclipse.exe",        # Eclipse
                                       "VirtualBox.exe",     # VirtualBox
                                       "putty.exe",          # PuTTY
                                       "ttermpro.exe",       # TeraTerm
                                       "vncviewer.exe"):     # UltraVNC
            return False
        return True

    keymap_global = keymap.defineWindowKeymap(check_func=is_target) 

    # 【基本方針】
    # UNIXライクな感じで端末とそれ以外との違和感を減らす
    
    # 【補足事項】
    # CapsLockキーは，そこそこ良い所にあるキーなのでモディファイアとして使用したい
    # しかしながらCapsLockはKeyhacだけだとうまくモディファイできないので一旦レジストリで右Ctrlになっていることを想定しています
    # 本来のショートカットであるC-?を潰すとたまに面倒くさいことになるので，
    # それらはLC-RC-?で呼び出せるようにしておきます

    keymap.replaceKey(29, "LShift")
    keymap_global["O-LShift"] = "(29)"
    keymap.replaceKey("(28)", "RShift")
    keymap_global["O-RShift"] = "(28)"

    # 【矢印キー】
    # Vimっぽい感じ
    # 他のキーバインドは割とEmacs風なので中途半端な感じはある
    keymap_global[ "LC-B" ] = "Left"
    keymap_global[ "LC-N" ] = "Down"
    keymap_global[ "LC-P" ] = "Up"
    keymap_global[ "LC-F" ] = "Right"

    # 範囲指定する場合
    keymap_global[ "LC-S-B" ] = "S-Left"
    keymap_global[ "LC-S-N" ] = "S-Down"
    keymap_global[ "LC-S-P" ] = "S-Up"
    keymap_global[ "LC-S-F" ] = "S-Right"

    # 本来のキーマップ
    keymap_global[ "LC-RC-S-B" ] = "C-B"
    keymap_global[ "LC-RC-S-N" ] = "C-N"
    keymap_global[ "LC-RC-S-P" ] = "C-P"
    keymap_global[ "LC-RC-S-F" ] = "C-F"

    keymap_global["LC-Slash"] = "C-F"

    # 【Home, End, Delete, Backの設定】
    # C-Q以外はEmacsっぽい感じ
    # 本当はHomeをC-Aに割り当てたいけれど，WindowsはC-Aで全選択なのでそのまま使いたい
    # C-EがEndなのでキーボードの位置的にC-QがHomeだと直感的なのでは，
    # ということでHomeにはC-Qを割り当てることに
    keymap_global[ "LC-A" ] = "Home"
    keymap_global[ "LC-E" ] = "End"
    keymap_global[ "LC-D" ] = "Delete"
    keymap_global[ "LC-H" ] = "Back"

    # 範囲指定する場合
    keymap_global[ "LC-S-A" ] = "S-Home"
    keymap_global[ "LC-S-E" ] = "S-End"
    keymap_global[ "LC-S-D" ] = "S-Delete"
    keymap_global[ "LC-S-H" ] = "S-Back"

    # 本来のキーマップ
    keymap_global[ "LC-Q" ] = "C-A"
    keymap_global[ "LC-RC-S-E" ] = "C-E"
    keymap_global[ "LC-RC-S-D" ] = "C-D"
    keymap_global[ "LC-RC-S-H" ] = "C-H"
    
    # 【PageUp, PageDown】
    # 割と行き場がなくなってしまいこうなってしまった感がある
    # Vimだと半ページ移動がC-UとC-Dなのでそれにしたいのだが，
    # C-DはDeleteの意味で使っているので使えない
    # Emacs的にはC-VとA-VだけどAltは使いたくない
    # 第一C-Vは貼り付けだって小学生の頃から記憶してしまっているのでC-Vには割り当てたくない
    # というわけで暫定的にC-UとC-Nで
    # キーボードの位置的に割と直感的なような気もする
    keymap_global[ "LC-U" ] = "PageUp"
    keymap_global[ "LC-Y" ] = "PageDown"
    keymap_global[ "LC-RC-S-U" ] = "C-U"
    keymap_global[ "LC-RC-S-Y" ] = "C-Y"

    keymap_global["LC-S-Y"] = "C-Y"

    # 【Enterキー】
    # Enterキーは思いの外遠いのでC-Mに割り当てるとほんとうに便利
    # そもそもC-Mは改行ですよという設定のアプリケーションもそこそこあるらしい
    keymap_global[ "LC-M" ] = "Enter"
    keymap_global[ "LC-RC-S-M" ] = "C-M"
    
    # 【Escキー】
    # 最初は自分のvimの設定とと同じように imap jk <Esc> (素早くjkと入力するとEscキーになる)
    # を割り当てたいと思ったのだが，なかなか設定がややこしそうなので断念
    # しかしC-S-Fもかなり押しやすく便利
    keymap_global["LC-J"] = "Esc"

    keymap_global["LC-K"] = "S-End", "C-X"
    keymap_global["LC-L"] = "Home", "S-End", "C-X", "Back"

    # 【Alt-F4(ウィンドウを閉じる)】
    # C-Wが多くのアプリケーションで「閉じる」「タブを閉じる」に割り当てられているので，
    # C-S-WがAlt+F4なのは割と直感的かなと思い割り当て
    keymap_global["LC-S-W"] = "A-F4"
    
    # 【単語移動】
    # Vimを使うまで単語移動という概念自体ほとんど未知のものだったので，
    # あまり使いこなせてないが，使えるとかなり強力だと思う
    # C-, C-. C-< C-> に割り当てるの直感的だと思うしかなり良いと思うのだけど
    # あんまりこうしてる人見てない
    keymap_global[ "LC-Comma" ] = "C-Left"
    keymap_global[ "LC-Period" ] = "C-Right"
    keymap_global[ "LC-S-Comma" ] = "C-S-Left"
    keymap_global[ "LC-S-Period" ] = "C-S-Right"

    # 【HomeとEnd】
    # 特等席なので本当はもっと別なキーに割り当てるべきなのだけどどうにもC-Q,C-Eに慣れないので
    keymap_global["RC-H"] = "Home"
    keymap_global["RC-L"] = "End"
    keymap_global[ "RC-S-H" ] = "S-Home"
    keymap_global[ "RC-S-L" ] = "S-End"

    # Escキーはやっぱいるだろということで
    keymap_global["RC-J"] = "Esc"
    # EmacsのC-K
    keymap_global["RC-K"] = "S-End", "C-X"

    # なんか他に便利なの割り当てたい
    keymap_global[ "RC-S-J" ] = "C-S-Tab"
    keymap_global[ "RC-S-K" ] = "C-Tab"

    # 【単語移動】
    keymap_global["RC-W"] = "C-Right"
    keymap_global["RC-B"] = "C-Left"
    
    # 【ペースト】
    # もっと便利に使えそうだからもっと慎重に割り当てるべきかもだけど一応暫定的に
    # keymap_global["RC-S-P"] = "Up", "End", "Enter", "C-V"

    # 【Vimのdd dwが使いたくてマップ　これは割と強力だと思う】
    keymap_global["RC-D"] = keymap.defineMultiStrokeKeymap("RC-D")
    keymap_global["RC-D"]["RC-D"]  = "Home", "S-End", "C-X", "Back"
    keymap_global["RC-D"]["RC-W"]  = "C-S-Right", "C-X"
    keymap_global["RC-D"]["RC-B"]  = "C-S-Left", "C-X"
    
    # 【Vimの検索】
    keymap_global["RC-Slash"] = "C-F"
    keymap_global["RC-N"] = "F3"
    keymap_global["RC-S-N"] = "S-F3"
    
    # 【Win + 矢印キー】
    # Winキーは基本LC-RCで呼び出す
    keymap_global["LC-RC-H" ] = "Win-Left"
    keymap_global["LC-RC-J" ] = "Win-Down"
    keymap_global["LC-RC-K" ] = "Win-Up"
    keymap_global["LC-RC-L" ] = "Win-Right"

    keymap_global["LC-RC-E"] = "Win-E"
    keymap_global["LC-RC-D"] = "Win-D"
    keymap_global["LC-RC-R"] = "Win-R"
	
	# ExplorerでCtrl+Mでフォルダを開こうとするとCtrlキーが押されてるからって
    # 新しいウィンドウで開こうとして最悪なのでそれを半ば無理やり回避するコード
    # http://anago.2ch.net/test/read.cgi/software/1239109333#569
    keymap_explorer = keymap.defineWindowKeymap(exe_name=u"explorer.exe")

    def input_enter():
            del keymap_explorer["U-LCtrl"]
            keymap.wnd = 0
            keymap.command_InputKey("U-LCtrl", "Enter")()

    def set_trap():
            keymap_explorer["U-LCtrl"] = input_enter
            keymap.wnd = 0

    keymap_explorer["C-M"] = set_trap