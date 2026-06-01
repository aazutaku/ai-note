---
name: boss-key-fake-excel
description: 作業中に“あっヤバい！”という瞬間や監督者の気配を感じた際、即座に本Skillを発動し、ターミナルやエディタ画面をExcel風フェイク画面に切り替えて視線を欺きます。boss、監査、急な来客などのキーワードで発動。
---

# 機能概要
boss-key-fake-excelは、開発者や作業者が“見られたくない”作業中に、瞬時に本物そっくりのExcel風フェイク画面を表示してカモフラージュできるSkillです。ターミナルやエディタの画面を、業務用Excelのウィンドウ画像に切り替え、監督者や同僚の目をごまかします。遊び心と秘密主義を両立し、真面目なフリをしたい場面や、開発者同士のジョークにも最適です。

# 使い方
明示的な呼び出しは `/boss-key-fake-excel` コマンドで実行します。暗黙的には「ボスが来た」「監査」「やばい」「切り替え」「フェイクExcel」などのキーワードで発動します。発動時、現在の作業画面を隠し、OSのウィンドウ上にExcel風のダミー画面を表示します。終了はウィンドウ右上の「×」ボタン、またはCtrl+Q等のショートカットで元の作業に戻ります。

# 出力例
```
$ python boss_key_fake_excel.py
[INFO] Fake Excel window launched. Press Ctrl+Q or close window to return.
[DEBUG] Screenshot of current desktop saved to: /tmp/bosskey_backup_20240610_101500.png
[INFO] Excel-style window closed. Restoring previous state.
```

# 注意点
本SkillはローカルのPython環境とGUIライブラリ（tkinter, PIL等）が必要です。実際のExcelデータやファイル操作は行いません。フェイク画面は画像生成であり、編集や保存は不可。ウィンドウマネージャやOSによっては動作に制限がある場合があります。セキュリティ上の重要データは保護されません。

# 参考資料
参考設計や実装例は `references/design_notes.md` を参照。公式Pythonドキュメント（tkinter, PIL）も活用しています。
- https://docs.python.org/ja/3/library/tkinter.html
- https://pillow.readthedocs.io/en/stable/