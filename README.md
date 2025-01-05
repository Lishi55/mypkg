# 現在時刻送信
![test](https://github.com/Lishi55/Ros2_demo/actions/workflows/test.yml/badge.svg)

## 概要
- 日本(東京)の現在時刻(時分秒)を出力送信

## 使用例

- 現在を19時43分の時　実行<br>
- 送信側
```bash
$ ros2 run mypkg talker
```
- 受信側
```bash
$ ros2 topic echo /nowtime
data: 194349
---
data: 194350
---
data: 194351
---
data: 194352
---
data: 194353
---
```

- 実行例の画像
![image](https://github.com/user-attachments/assets/af5bd492-e137-48e0-ba7a-fb67c9f25f62)


## 必要なソフトウェア
- Python
  - テスト環境　Ubuntu 22.04 LTS
  - テスト済みバージョン: 3.10
  - テストで利用したコンテナhttps://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます.
- © 2024 Satoshi Nemoto
