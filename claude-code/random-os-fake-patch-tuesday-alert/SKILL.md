---
name: random-os-fake-patch-tuesday-alert
description: このSkillは、コマンド実行や作業の合間に“パッチ”や“アップデート”といったキーワードが現れた際、または明示的に /random-os-fake-patch-tuesday-alert を呼び出した際に発動します。完全ランダムな内容の“謎OSパッチノート風通知”を生成し、デスクトップ通知またはターミナル演出で表示します。
---

# 機能概要
random-os-fake-patch-tuesday-alertは、あなたの作業中に突然“謎のOS公式・緊急パッチチューズデー通知”を炸裂させるSkillです。内容は完全ランダム生成で、現実には絶対存在しない珍妙なパッチノート風（例：Ctrlキーの押下速度が基準値未満のため緊急アップデート、新機能: Altキー長押しでOSが詩を朗読等）。真面目な作業やコマンド実行の合間に、集中力を一瞬でハッキングする演出を提供します。

# 使い方
- 明示的な呼び出し: `/random-os-fake-patch-tuesday-alert` または `/skill random-os-fake-patch-tuesday-alert`
- 暗黙発動: 「パッチ」「アップデート」「OS」「チューズデー」などのキーワードや、コマンド履歴・作業ログ内の類似語を検知した際に自動発動します。
- デスクトップ通知/ターミナル演出は環境に応じて自動選択されます。

# 出力例
```
[Patch Tuesday Alert]
OSバージョン: 13.4.7-fake
- 新機能: Shiftキー5連打で画面が180度回転します。
- 修正: CapsLockが押された際、全ウィンドウが詩的に閉じる問題を解決。
- 既知の問題: マウスホイール逆回転時に天気予報が流れる場合があります。
```

# 注意点
- 本Skillは完全に架空の通知を生成します。実際のOSアップデートやセキュリティ情報とは一切関係ありません。
- ローカルに通知履歴は保存されません。
- 一部環境ではデスクトップ通知が表示されない場合があります（その場合はターミナル演出のみ）。
- 通知内容は毎回ランダム生成されます。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- 公式API: [plyer.notification](https://plyer.readthedocs.io/en/latest/)
- Python標準: random, argparse, sys