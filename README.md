# R-System2
講義の課題2として提出したコードです。

# Demo

# Features

# Usage
1. 以下のコードによりノードを立ち上げる。コマンドはそれぞれ別ウィンドウで行うこと。
    ```
    $ rosrun kadai_pkg count.py
    ```
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
