# R-System2
数値を生成し、受け取り先で加工してまたデータを出す。

# Demo
https://youtu.be/qLfY98hApzo

# Features
- 数値の生成
- 生成された数値の倍化

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
3. 停止する際は「Ctrl+C」を用いる。

# Requirement
- Raspberry Pi 3 モデルB
- Ubuntu18.04.3(ARM64)
- ROS Melodic
