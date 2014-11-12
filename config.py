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

    keymap_global = keymap.defineWindowKeymap(check_func=is_target) 

    # 無変換キーをShift，変換キーをモディファイアUser0に割り当てる
    # ポン押しで無変換キーと変換キーとしても使える(ワンショットモディファイア）
	
    # 無変換キーをShiftに割り当てると何が嬉しいかというと，
    # 範囲指定をするCtrl+Shift+→ or ← or Home or End
    # なんかが劇的にやりやすくなる
	
    # また，単順にすべてキャピタルの文字列を打つ場合に関しても，
    # 小指でShiftキーを押さえるより親指で無変換キーを押さえるほうが相当打ちやすい
    # 親指にShiftキーを割り当てるという考えにはSandSがあるが，それの亜種と考えてもらってもいい
	
    # 変換キーは直感的にはAltキーとかに割り当てたいのだが，AltキーはWindowsではポン押し（ワンショット）すると，
    # メニューにフォーカスが移ってしまうので，本来使用したいIME ON の機能が正しく使えなくなってしまうためこうしている
	
    # 極稀に「本来のCtrl+Lが使えなくて困る！」というときがあるので，C-?で潰してしまったショートカットキーは，
    # C-U0-?で使用できるようにしている
    keymap.replaceKey(29, "LShift")
    keymap_global["O-LShift"] = "(29)"
    keymap.defineModifier(28, "User0")
    keymap_global["O-(28)"] = "(28)"

    # 【矢印キー】
    # Vimっぽい感じ
    # 他のキーバインドは割とEmacs風なので中途半端な感じはある
    keymap_global[ "C-H" ] = "Left"
    keymap_global[ "C-J" ] = "Down"
    keymap_global[ "C-K" ] = "Up"
    keymap_global[ "C-L" ] = "Right"

    # 範囲指定する場合
    keymap_global[ "C-S-H" ] = "S-Left"
    keymap_global[ "C-S-J" ] = "S-Down"
    keymap_global[ "C-S-K" ] = "S-Up"
    keymap_global[ "C-S-L" ] = "S-Right"

    # 本来のキーマップ
    keymap_global[ "C-U0-S-H" ] = "C-H"
    keymap_global[ "C-U0-S-J" ] = "C-J"
    keymap_global[ "C-U0-S-K" ] = "C-K"
    keymap_global[ "C-U0-S-L" ] = "C-L"

    # 【Home, End, Delete, Backの設定】
    # C-Q以外はEmacsっぽい感じ
    # 本当はHomeをC-Aに割り当てたいけれど，WindowsはC-Aで全選択なのでそのまま使いたい
    # C-EがEndなのでキーボードの位置的にC-QがHomeだと直感的なのでは，
    # ということでHomeにはC-Qを割り当てることに
    keymap_global[ "C-Q" ] = "Home"
    keymap_global[ "C-E" ] = "End"
    keymap_global[ "C-D" ] = "Delete"
    keymap_global[ "C-B" ] = "Back"

    # 範囲指定する場合
    keymap_global[ "C-S-Q" ] = "S-Home"
    keymap_global[ "C-S-E" ] = "S-End"
    keymap_global[ "C-S-D" ] = "S-Delete"
    keymap_global[ "C-S-B" ] = "S-Back"

    # 本来のキーマップ
    keymap_global[ "C-U0-S-Q" ] = "C-Q"
    keymap_global[ "C-U0-S-E" ] = "C-E"
    keymap_global[ "C-U0-S-D" ] = "C-D"
    keymap_global[ "C-U0-S-B" ] = "C-B"
    
    # 【PageUp, PageDown】
    # 割と行き場がなくなってしまいこうなってしまった感がある
    # Vimだと半ページ移動がC-UとC-Dなのでそれにしたいのだが，
    # C-DはDeleteの意味で使っているので使えない
    # Emacs的にはC-VとA-VだけどAltは使いたくない
    # 第一C-Vは貼り付けだって小学生の頃から記憶してしまっているのでC-Vには割り当てたくない
    # というわけで暫定的にC-UとC-Nで
    # キーボードの位置的に割と直感的なような気もする
    # もう慣れちゃったのであんまり変える気無いですがU0-JとU0-Kあたりに割り当てるのもいいかもですね
    keymap_global[ "C-U" ] = "PageUp"
    keymap_global[ "C-N" ] = "PageDown"
    keymap_global[ "C-U0-S-U" ] = "C-U"
    keymap_global[ "C-U0-S-N" ] = "C-N"

    # 【Enterキー】
    # Enterキーは思いの外遠いのでC-Mに割り当てるとほんとうに便利
    # そもそもC-Mは改行ですよという設定のアプリケーションもそこそこあるらしい
    keymap_global[ "C-M" ] = "Enter"
    keymap_global[ "C-U0-S-M" ] = "C-M"

    # 【Escキー】
    # 最初は自分のvimの設定とと同じように imap jk <Esc> (素早くjkと入力するとEscキーになる)
    # を割り当てたいと思ったのだが，なかなか設定がややこしそうなので断念
    # しかしC-S-Fもかなり押しやすく便利
    keymap_global["C-S-F"] = "Esc"
    
    # 【Alt-F4(ウィンドウを閉じる)】
    # C-Wが多くのアプリケーションで「閉じる」「タブを閉じる」に割り当てられているので，
    # C-S-WがAlt+F4なのは割と直感的かなと思い割り当て
    keymap_global["C-S-W"] = "A-F4"
    
    # 【単語移動】
    # Vimを使うまで単語移動という概念自体ほとんど未知のものだったので，
    # あまり使いこなせてないが，使えるとかなり強力だと思う
    # C-, C-. C-< C-> に割り当てるの直感的だと思うしかなり良いと思うのだけど
    # あんまりこうしてる人見てない
    keymap_global[ "C-Comma" ] = "C-Left"
    keymap_global[ "C-Period" ] = "C-Right"
    keymap_global[ "C-S-Comma" ] = "C-S-Left"
    keymap_global[ "C-S-Period" ] = "C-S-Right"

    # モディファイアキーUser0の割り当て
    # 基本方針は【U0+？ｄ Vimの操作モードと同じ動きをすること】
    # ただ，あんまりVimのキーバインド覚えてないので憶えたやつから
    # 憶えたやつだけ割り当てていく
    # 本当は右手親指とかいう最高な位置にあるので
    # 積極的に色々割り当てていくべきなのだろうが模索中
    
    # 【キー移動】
    keymap_global["U0-H"] = "Left"
    keymap_global["U0-J"] = "Down"
    keymap_global["U0-K"] = "Up"
    keymap_global["U0-L"] = "Right"

    # 範囲指定する場合
    keymap_global[ "U0-S-H" ] = "S-Left"
    keymap_global[ "U0-S-J" ] = "S-Down"
    keymap_global[ "U0-S-K" ] = "S-Up"
    keymap_global[ "U0-S-L" ] = "S-Right"

    # 【単語移動】
    keymap_global["U0-W"] = "C-Right"
    keymap_global["U0-B"] = "C-Left"

    # 【アンドゥ】
    # 何気にC-Zって押しにくいのよね
    keymap_global["U0-U"] = "C-Z"
    
    # 【ペースト】
    # もっと便利に使えそうだからもっと慎重に割り当てるべきかもだけど一応暫定的に
    # C-Vは文脈によっては結構押しづらいし
    keymap_global["U0-P"] = "C-V"

    # 【Vimのdd dwが使いたくてマップ　割と強力】
    keymap_global["U0-D"] = keymap.defineMultiStrokeKeymap("U0-D")
    keymap_global["U0-D"]["U0-D"]  = "Home", "S-End", "C-X"
    keymap_global["U0-D"]["U0-W"]  = "C-S-Right", "C-X"
    keymap_global["U0-D"]["U0-B"]  = "C-S-Left", "C-X"
    
    # 【Vimの検索】
    keymap_global["U0-Slash"] = "C-F"
    keymap_global["U0-N"] = "F3"
    keymap_global["U0-S-N"] = "S-F3"
    
    # 【Win + 矢印キー】
    # そうだ，WindowsキーはC-U0にしよう　というアイデア
    # 使わんやつは別にいいやというスタンス
    keymap_global["C-U0-H" ] = "Win-Left"
    keymap_global["C-U0-J" ] = "Win-Down"
    keymap_global["C-U0-K" ] = "Win-Up"
    keymap_global["C-U0-L" ] = "Win-Right"

    keymap_global["C-U0-E"] = "Win-E"
    keymap_global["C-U0-D"] = "Win-D"
    keymap_global["C-U0-L"] = "Win-L"
    keymap_global["C-U0-R"] = "Win-R"
	
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