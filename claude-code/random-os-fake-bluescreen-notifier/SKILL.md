---
name: random-os-fake-bluescreen-notifier
description: このSkillは「ブルースクリーン」「エラー通知」「集中力低下」「作業中の息抜き」などのキーワードや、/random-os-fake-bluescreen-notifier コマンドで発動します。開発現場にユーモラスな通知を届けたい時に最適です。
---

# 機能概要
`random-os-fake-bluescreen-notifier`は、作業中のデスクトップに“謎のOSブルースクリーン風”のネタ通知をランダムに表示するSkillです。通知内容は毎回異なり、「STOP CODE: 眠気の暴走」「エラー: コーヒーブレイク不足」など、実害のないユーモア溢れるメッセージが特徴です。開発現場やチーム作業の緊張感を和らげ、ちょっとした息抜きや話題作りに役立ちます。本物のBSoDとは明確に異なるデザイン・文言で、誤認や混乱を防ぎます。

# 使い方
- 明示的な呼び出し: `/random-os-fake-bluescreen-notifier` コマンドを実行
- 暗黙発動: 「ブルースクリーン」「エラー通知」「集中力低下」「眠気」などのキーワードが会話やコード中に現れた際に自動発動

# 出力例
```
[FAKE-OS-BLUESCREEN]
STOP CODE: 眠気の暴走
エラー: コーヒーブレイク不足
原因: キーボードに猫が乗りました
ヒント: 立ち上がってストレッチしましょう
---
これは本物のエラーではありません。安心して作業を続けてください。
```

# 注意点
- 本Skillは通知表示のみで、システムやファイルには一切変更を加えません。
- 本物のOSエラー画面と誤認されないよう、明確に「FAKE」や注意書きを付与しています。
- ローカル保存やログ出力は行いません。
- 実際の障害やエラー対応には使用しないでください。

# 参考資料
- references/design_notes.md
- https://docs.python.org/ja/3/library/tkinter.html
- https://www.microsoft.com/en-us/windows/
