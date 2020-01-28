# R-System2
講義の課題2として提出したコードです。
1ずつ増加する数値をコマンドライン上に

# Demo

# Features

# Usage
1. 以下のコードによりノードを立ち上げる。コマンドはそれぞれ別ウィンドウで行うこと。<br> 
    count.py では時間経過とともにインクリメントされた数値を作り出す。
    ```
    $ rosrun kadai_pkg count.py
    ```
    twice.py では count.py で作り出された数値を2倍にしている。
    ```
    $ rosrun kadai_pkg twice.py
    ```
2. 各ノードからデータを取得する。コマンドはそれぞれ別ウィンドウで行うこと。
    ```
    $ rostopic echo /count_up
    ```
    ```
    $ rostopic echo /twice
    ```

# Requirement
- Raspberry Pi 3 モデルB
- Ubuntu18.04.3(ARM64)
- ROS Melodic
