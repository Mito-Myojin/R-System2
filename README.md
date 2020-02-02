# R-System2
数値を生成し、受け取り先で加工してまたデータを出す。<br>
また、受け取ったデータに合わせてLEDを点灯させる。

# Demo
数値の生成と加工・出力 : https://youtu.be/qLfY98hApzo<br>
3の倍数でLチカ : 

# Features
- 数値の生成
- 生成された数値の倍化
- count.py で3が生成された場合にLEDを点灯

# Usage
1. 以下のコードによりノードを立ち上げる。<br> 
    count.py では時間経過とともにインクリメントされた数値を作り出す。
    ```
    $ rosrun kadai_pkg count.py
    ```
2. count.py 実行後、以下のコードが利用可能となる。各コマンドはそれぞれ別ウィンドウで行うこと。<br>
    twice.py では count.py で作り出された数値を2倍にしている。
    ```
    $ rosrun kadai_pkg twice.py
    ```
    LED.py では count.py で作り出された数値が3の倍数である時にLEDを転倒させる.
    ```
    $ rosrun kadai_pkg LED.py
    ```
3. 各ノードが生成している数値の確認。コマンドはそれぞれ別ウィンドウで行うこと。<br>
    twice.py で生成された数値の確認用。
    ```
    $ rostopic echo /count_up
    ```
    twice.py で生成された数値の確認用。
    ```
    $ rostopic echo /twice
    ```
3. 停止する際は「Ctrl+C」を用いる。

# Requirement
- Raspberry Pi 3 モデルB
- Ubuntu18.04.3(ARM64)
- ROS Melodic
- WiringPi

# Extra
WiringPiの用意
    ```
    $ git clone https://github.com/hardkernel/wiringPi
    $ cd wiringPi
    $ ./build
    $ gpio -v  // インストール確認用
    ```
