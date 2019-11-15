# SnakeGameByPython
Pythonのレトロゲームエンジン、pyxelを利用したスネークゲームです。

#### 開発の環境
Pythonのバージョン: Python3.7.1
pyxelのバージョン: 1.1系

#### 起動方法
1.pyxelなどの必要なパッケージを事前にインストール
2.ディレクトリSnakeGameByPythonに移動する
3.コマンド`Python3 App.py`を実行する

`App.py`が全てのコントローラとなるファイルです。

#### パッケージ内容
`screen`:　
　スタート画面やゲームオーバー画面の表示を実現するクラスがまとめられています。外部からは`ScreenCreator`クラスを利用して`Screen`インスタンスを生成し、そこから描画を行います。

`game_contents`:　
　蛇、フィールド、エサなど、ゲームを実現するクラス群がまとめられています。
　メインとなるクラスは`GameController`で、ここから各オブジェクトに命令を送ってゲームの動作を実現します。

`test_module`:　
　一部のクラスのメソッド動作をテストするためのスクリプトがまとめられています。そのため、ゲームの動作実現にはなんら関係がありません。

#### Tester.pyについて
　パッケージ`test_module`のテストを全て実行するためのスクリプトです。したがって、ゲームの動作実現にはなんら関係がありません。

# ライセンス
### pyxelのライセンス
MIT License

Copyright (c) 2018 Takashi Kitao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
