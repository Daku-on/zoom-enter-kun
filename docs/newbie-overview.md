# 新規コントリビューター向け概要

このプロジェクトでは、指定した時刻の数分前にZoomのミーティングURLを自動で開く小さなスクリプト群を提供しています。`tkinter`を用いたGUI実験やCSV操作の例も含まれています。ここでは、リポジトリの構成と学習の手順を簡単に紹介します。

## リポジトリ構成

- `zoom-enter-kun.py` – 予定時刻に合わせてZoomを起動するメインスクリプト
- `sample.py` と `codes_from_ChatGPT.py` – 開発過程のプロトタイプコード
- `GUIwindow_byChatGPT.py` – ミーティング選択用の簡易GUI例
- `sample_url.csv` – ミーティング名とURLを記載したサンプルCSV
- `comment_from_ChatGPT.txt` – これまでのチャットログ
- `README.md` – プロジェクトの概要と利用方法

## 重要なポイント

1. ミーティング情報は以下のようなCSV形式で管理します。

   ```csv
   name,url
   定例の会議,https://example.com/meeting
   ```
   `sample_url.csv` を自分の環境に合わせて編集してください。
2. CSV読み込みには `pandas` ライブラリを利用しています。
3. スケジュール管理には `tkinter` を使用しており、`zoom-enter-kun.py` 内の `zoom_enter_kun` クラスが主な処理を担当します。

## はじめに

1. 依存ライブラリをインストールします。
   ```bash
   pip install pandas
   ```
2. 先ほどの形式で `url.csv` を用意し、スクリプトと同じディレクトリに置きます。
3. メインスクリプトを実行します。
   ```bash
   python3 zoom-enter-kun.py
   ```

### 学習のステップ

1. `zoom-enter-kun.py` を読み、クラス構成やスケジューリングの仕組みを把握します。
2. `tkinter` に不慣れな場合は `GUIwindow_byChatGPT.py` の簡易GUI例から試してみてください。
3. 開発経緯を知りたい場合は `comment_from_ChatGPT.txt` を参照してください。
4. `sample_url.csv` を編集して実際に動かし、動作を確認してみましょう。

貢献はいつでも歓迎しています。改善点や新機能の提案があれば、ぜひプルリクエストを送ってください。
