---
name: random-os-annoying-tooltips
description: 作業中や集中時、または/skillsコマンド実行時などに“OS風うざいツールチップ”をデスクトップ通知で発動します。通知・演出・OS連携カテゴリで、random, annoying, tooltip, notification, OS, desktop などのキーワードに反応します。
---

# 機能概要
このSkillは、ユーザーの作業中やコマンド実行時に、あえて“OS風のうざいツールチップ”をデスクトップ通知として表示します。内容は「CapsLockが押されているかもしれません」「アップデートのタイミングです」「あなたの入力速度、気づいてますか？」など、誰得な小言や謎の提案ばかり。懐かしの“助けにならないヘルプ”体験を現代に再現し、職場や作業環境に小さな笑いとイライラを提供します。

# 使い方
- 明示呼び出し: `/skills random-os-annoying-tooltips` または `@codex random-os-annoying-tooltips`
- 暗黙発動: 「random」「tooltip」「notification」「OS」「desktop」「annoying」などのキーワードを含む会話やコマンド、または一定時間作業が続いた際に自動発動

# 出力例
```
[通知] CapsLockが押されているかもしれません。
[通知] 今アップデートしませんか？（推奨: 今すぐ再起動）
[通知] あなたの入力速度、気づいてますか？
[通知] ファイルを保存していないようです。
[通知] ネットワークが不安定かもしれません。
[通知] システムの空き容量が残りわずかです。
```

# 注意点
- 通知は主要OS（Windows, macOS, Linux）で動作する標準APIのみ利用し、環境依存を極力排除しています
- 通知頻度は1分以上の間隔を設け、過剰な連発は防止
- ローカルにデータは保存しません
- 一部環境で通知が表示されない場合があります

# 参考資料
- [plyer通知API公式ドキュメント](https://plyer.readthedocs.io/en/latest/#plyer.notification.notification)
- references/design_notes.md も参照