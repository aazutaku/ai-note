---
name: random-os-fake-bluescreen-notifier
description: 作業中のリフレッシュや緊張緩和が必要な場面で、/skills menuやrandom-os-fake-bluescreen-notifierへの明示的な呼び出し、または「ブルースクリーン」「エラー」「息抜き」などのキーワードを検知した際に発動します。
---

# 機能概要
このSkillは、開発現場やオフィスで突然“OSブルースクリーン風”のジョーク通知をデスクトップに表示します。通知内容は毎回ランダムで、例えば「STOP CODE: コーヒーブレイク不足」や「原因: キーボードに猫が乗りました」など、実害のないユーモラスなメッセージです。これにより、作業中の緊張感を和らげたり、チーム内のコミュニケーションを活性化することができます。誤認防止のため、実際のBSoDとは明確に異なるデザインや文言を用いています。

# 使い方
- 明示呼び出し例: `/skills menu` から「random-os-fake-bluescreen-notifier」を選択、または `$random-os-fake-bluescreen-notifier` を直接メンション。
- 暗黙発動キーワード例: 「ブルースクリーン」「エラー通知」「息抜き」「ジョーク」「集中力低下」などの会話内出現時。

# 出力例
```
[FAKE OS BLUESCREEN]
エラー: コーヒーブレイク不足
STOP CODE: 眠気の暴走
原因: キーボードに猫が乗りました
ヒント: 立ち上がってストレッチしましょう
---
これはジョーク通知です。作業を続けても問題ありません。
```

# 注意点
- 本Skillは実際のシステムエラーやブルースクリーンを発生させるものではありません。
- 通知は一時的な表示のみで、ローカルファイルやシステム設定には一切影響を与えません。
- 出力はユーザーのデスクトップ通知機能に依存します。
- ジョーク内容は毎回ランダム生成されますが、不快な表現や誤認を避ける工夫が施されています。

# 参考資料
- [参考: references/design_notes.md](references/design_notes.md)
- [Python公式: plyer通知API](https://github.com/kivy/plyer)
- [Microsoft BSoDデザインガイド](https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes)
