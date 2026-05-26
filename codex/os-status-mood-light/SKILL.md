---
name: os-status-mood-light
description: Codexがユーザーの作業中の気分や状態を可視化したい、または環境変数MOODの変化を検知してシェルやSlack等に通知・反映したい場合に発動します。キーワード例: 気分, MOOD, ステータスバー, シェルプロンプト, Slack連携。
---

# 機能概要
このSkillは、作業中の開発者の「気分」を環境変数MOODで管理し、リアルタイムでターミナルのシェルプロンプトやOSのステータスバー、Slackステータス等に自動反映する自己主張型可視化ツールです。MOODの値に応じて、定型フレーズや日替わりネタ、ツッコミ文が表示され、開発者のメンタル状態を周囲に伝えます。気分の見える化により、チーム内のコミュニケーションやセルフケアを促進します。

# 使い方
- 明示呼び出し例: `/skills os-status-mood-light set --mood='最高'`
- 環境変数MOODを更新: `export MOOD='だるい'`
- 暗黙発動キーワード: 「気分」「メンタル」「ステータスバー」「Slack連携」などを含む発話やスクリプト実行時
- Slack連携時は `--slack-webhook-url` オプションを指定

# 出力例
```
$ export MOOD='最高'
$ python mood_light.py show
[os-status-mood-light] 気分: 最高
絶好調！今日もバリバリ行きましょう。

$ export MOOD='だるい'
$ python mood_light.py show
[os-status-mood-light] 気分: だるい
本日省エネ運転。無理せずいきましょう。

$ python mood_light.py set --mood='ねむい'
[os-status-mood-light] 気分: ねむい
睡眠は大事。仮眠推奨。
```

# 注意点
- MOOD環境変数が未設定の場合は「普通」として扱います。
- シェルプロンプト反映には一部設定が必要です（詳細は参考資料参照）。
- Slack通知にはWebhook URLが必要です。
- ローカル環境のみ対応。クラウドやリモート端末では動作保証外です。

# 参考資料
- [os-status-mood-light 参考設計ノート](references/design_notes.md)
- [Slack API 公式ドキュメント](https://api.slack.com/messaging/webhooks)
- [Bashプロンプトカスタマイズ](https://wiki.archlinux.jp/index.php/Bash/プロンプトのカスタマイズ)