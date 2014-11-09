from keyhac import *
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

    if 1:
        keymap_global = keymap.defineWindowKeymap(check_func=is_target) 

        # vimっぽいカーソル移動
        keymap_global[ "C-H" ] = "Left"
        keymap_global[ "C-J" ] = "Down"
        keymap_global[ "C-K" ] = "Up"
        keymap_global[ "C-L" ] = "Right"

        # ここからはEmacsっぽいキーバインド        
        # 本当はHomeをC-Aに割り当てたいけれど，WindowsはC-Aで全選択なので
        # あんまコンフリクトしなさそうなC-Qに割り当てることにした

        keymap_global[ "C-Q" ] = "Home"
        keymap_global[ "C-E" ] = "End"
        keymap_global[ "C-D" ] = "Delete"
        keymap_global[ "C-B" ] = "Back"


        # 上述のShift押したとき版はいちいち定義しないといけないらしい
        keymap_global[ "C-S-H" ] = "S-Left"
        keymap_global[ "C-S-J" ] = "S-Down"
        keymap_global[ "C-S-K" ] = "S-Up"
        keymap_global[ "C-S-L" ] = "S-Right"
        keymap_global[ "C-S-Q" ] = "S-Home"
        keymap_global[ "C-S-E" ] = "S-End"
        keymap_global[ "C-S-D" ] = "S-Delete"
        keymap_global[ "C-S-B" ] = "S-Back"

        # Windowsキー＋矢印キーの挙動
        # 本当はCtrl付けたくないのだけど，Win+L押すと誤動作（ロックがかかる）問題を回避できず断念
        keymap_global[ "C-Win-H" ] = "Win-Left"
        keymap_global[ "C-Win-L" ] = "Win-Right"
        keymap_global[ "C-Win-K" ] = "Win-Up"
        keymap_global[ "C-Win-J" ] = "Win-Down"

        # Vim風スクロール
        # 本当はPageDownはC-DなのだけどDeleteとかぶるためDeleteを優先
        keymap_global[ "C-U" ] = "PageUp"
        keymap_global[ "C-N" ] = "PageDown"

        # EnterをC-Mに割り当てるとほんとうに便利
        # 調べてみたらそもそもそういう設定になってるレガシーなアプリもチラホラあるらしい
        keymap_global[ "C-M" ] = "Enter"

        # Escキーが遠すぎるので一応割り当て
        # 本当はVimと同じように imap jk <Esc> したい
        keymap_global[" C-I"] = "Esc"
        keymap_global[" C-Semicolon"] = "A-F4"

        # 単語移動はC+,とC+.に割り当て　なぜかC+<とC+>が設定できない
        # 単語移動便利なのはわかるけどあんまり使えてない
        keymap_global[ "C-Comma" ] = "C-Left"
        keymap_global[ "C-Period" ] = "C-Right"
        keymap_global[ "C-S-Comma" ] = "C-S-Left"
        keymap_global[ "C-S-Period" ] = "C-S-Right"

	# ExplorerでCtrl+Mでフォルダを開こうとするとCtrlキーが押されてるからって
        # 新しいウィンドウで開こうとして最悪なのでそれを半ば無理やり回避するコード
        # http://anago.2ch.net/test/read.cgi/software/1239109333#569
        keymap_notepad = keymap.defineWindowKeymap(exe_name=u"explorer.exe")

        def input_enter():
                del keymap_notepad["U-LCtrl"]
                keymap.wnd = 0
                keymap.command_InputKey("U-LCtrl", "Enter")()

        def set_trap():
                keymap_notepad["U-LCtrl"] = input_enter
                keymap.wnd = 0

        keymap_notepad["C-M"] = set_trap
