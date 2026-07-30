---
name: random-os-fake-license-violation-alert
description: 作業中やコマンド実行時に、ランダムなタイミング・内容で“謎のOSライセンス違反”警告をデスクトップ通知として表示。通知・警告・ライセンス違反・ジョーク・演出等のキーワードを含む会話や明示呼び出しで発動。
---

# 機能概要
このSkillは、ユーザーの作業中に突如として「謎のOSライセンス違反警告」をデスクトップ通知で表示します。警告内容は毎回ランダムで生成され、「椅子の座りすぎライセンス違反」「コーヒーブレイク無許可利用」など、現実には存在しない意味不明な違反ばかり。真面目な作業空間にユーモアを加え、緊張感を和らげる演出や、ジョークとしての利用に最適です。

# 使い方
- 明示呼び出し例:
  - `/skills random-os-fake-license-violation-alert`
  - `$random-os-fake-license-violation-alert`
- 暗黙発動キーワード例:
  - 「通知」「警告」「ライセンス違反」「ジョーク」「演出」などの単語を含む会話やコマンド実行時に自動発動します。

# 出力例
```
[通知] OSライセンス違反警告
違反内容: あなたのキーボード配列が未承認です。
対策: 管理者に連絡してください。違反コード: KBD-314

[通知] OSライセンス違反警告
違反内容: コーヒーブレイク無許可利用を検出。
対策: 直ちに作業に戻ってください。違反コード: CFE-007

[通知] OSライセンス違反警告
違反内容: 椅子の座りすぎライセンス違反。
対策: 立ち上がってストレッチしてください。違反コード: CHR-999
```

# 注意点
- 本Skillはジョーク目的であり、実際のOSやライセンス違反とは一切関係ありません。
- 通知内容は毎回ランダム生成されますが、実際のシステム警告と混同しないよう演出されています。
- ローカル環境でのみ動作し、通知履歴や個人情報は保存されません。
- Linux/macOSでは`notify-send`や`osascript`を利用、Windowsは`win10toast`等公式APIを使用します。

# 参考資料
- references/design_notes.md を参照
- 公式API: [Python plyer.notification](https://plyer.readthedocs.io/en/latest/), [notify-send](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html), [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications)
