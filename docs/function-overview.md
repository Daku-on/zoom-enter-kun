# 関数一覧と動作概要

このドキュメントではリポジトリ内で利用されている主な Python 関数・メソッドの目的と挙動をまとめます。

## zoom-enter-kun.py

### `zoom_enter_kun` クラス
- `__init__` – 各種属性（待機秒数・入室時刻・URL など）を初期化します【F:zoom-enter-kun.py†L17-L25】。
- `assign_meeting_key(choice)` – CSV から選択したキーに対応する URL を取得し `self.meeting_url` に保存します【F:zoom-enter-kun.py†L27-L29】。
- `ask_meeting(arg1)` – Tkinter でコンボボックスを表示し、ユーザーに会議名を選ばせます。選択後 `assign_meeting_key` を呼び出します【F:zoom-enter-kun.py†L31-L48】。
- `ask_schedule()` – ダイアログで入室時刻を文字列入力させ、`datetime` に変換します。失敗時は再入力を促します【F:zoom-enter-kun.py†L50-L70】。
- `enter_zoom()` – Chrome ブラウザで `self.meeting_url` を開きます【F:zoom-enter-kun.py†L72-L74】。
- `done_message(arg1)` – 予約完了時刻をメッセージとして表示し、一定時間後にウィンドウを閉じます【F:zoom-enter-kun.py†L76-L107】。
- `current_dir()` – 実行ファイルの場所を基準に `url.csv` のパスを返します【F:zoom-enter-kun.py†L110-L118】。
- `make_delay(what_time)` – 入室予定時刻までの残り時間からランダムな待機時間を計算します【F:zoom-enter-kun.py†L124-L136】。
- `timer()` – 計算した待機秒数後に `enter_zoom` を実行するタイマーを開始します【F:zoom-enter-kun.py†L138-L139】。

スクリプト末尾ではこれらを利用し、CSV 読み込みから入室予約までの一連の処理を実行しています【F:zoom-enter-kun.py†L141-L153】。

## sample.py

### `zoom_enter_kun` クラス
- `current_dir()` から `timer()` までのメソッドは上記 `zoom-enter-kun.py` とほぼ同様の動作を行います【F:sample.py†L24-L78】。
- `get_time(arg1)` – ユーザー入力を一時的に保持する簡易メソッドです【F:sample.py†L42-L44】。
- `get_scheduled_time()` – 入室時刻の文字列から `datetime` への変換を行い、失敗時は再入力ダイアログを開きます【F:sample.py†L46-L61】。

### `Application` クラス
- コンストラクタで Tkinter ウィンドウを設定し、会議選択・時刻設定ボタンを配置します【F:sample.py†L80-L103】。
- `create_ask_meeting_dialog()` – 会議名選択用のダイアログを表示します【F:sample.py†L105-L124】。
- `create_ask_time_dialog()` – 入室時刻入力用のダイアログを表示します【F:sample.py†L126-L145】。

`__main__` ではウィンドウを起動後、待機時間を計算しタイマーを開始します【F:sample.py†L148-L157】。

## GUIwindow_byChatGPT.py

- `ZoomEnterKun.assign_meeting_key()` – 指定した行の URL を返します【F:GUIwindow_byChatGPT.py†L11-L12】。
- `Application.create_widgets()` – ドロップダウンと入力欄を含む簡易 GUI を生成します【F:GUIwindow_byChatGPT.py†L24-L40】。
- `Application.enter_zoom()` – 入力時刻を検証し、ブラウザで Zoom URL を開きます【F:GUIwindow_byChatGPT.py†L42-L61】。

## codes_from_ChatGPT.py

開発過程のメモ的スクリプトで、`zoom_enter_kun` クラスや `Application` クラスの初期版が含まれます。実装内容は `zoom-enter-kun.py` とほぼ同様ですが、ファイル末尾が途中で終了しておりサンプルコードとして残されています【F:codes_from_ChatGPT.py†L1-L70】。

---
以上がリポジトリに含まれる主要な関数とその挙動の概要です。
