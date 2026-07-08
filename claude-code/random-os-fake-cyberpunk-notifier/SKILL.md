---
name: random-os-fake-cyberpunk-notifier
description: このSkillは「サイバーパンク」「SF通知」「未来的演出」などのキーワードや、/random-os-fake-cyberpunk-notifier コマンドが入力された際に発動します。作業中の合間や気分転換、雰囲気づくりの演出用途に最適です。
---

# 機能概要
random-os-fake-cyberpunk-notifierは、現実には存在しないサイバーパンク風の未来OS通知をデスクトップに表示するSkillです。ニューロン接続エラーや義手アップデートなど、SF世界の住人になった気分を味わえます。実用性はありませんが、作業の合間や気分転換、配信・イベントの演出などで「非日常感」を演出したい時に最適です。

# 使い方
明示的には `/random-os-fake-cyberpunk-notifier` コマンドで即時発動できます。また、「サイバーパンク」「SF通知」「未来的演出」などのキーワードを含む会話やコード内で暗黙的にトリガーされます。通知頻度やタイミングは自動調整され、迷惑にならない範囲でランダムに出現します。

# 出力例
```
[NeuroOS] ニューロン接続不良を検出: シナプス・インターフェース再起動推奨
[ChromeSys] クローム義手ファームウェアのアップデートが利用可能です
[SynthWave] シンセ脳波異常: 脳内信号の再調整を推奨
[GhostShell] ゴースト・プロトコルがアクティブ化されました
[GridNet] ネットワーク・ジャック警告: 外部アクセス試行を検出
```

# 注意点
本Skillは実用的な通知や警告は一切行いません。通知内容はすべてフィクションです。ローカル環境の通知API（Windows: Toast, macOS: terminal-notifier, Linux: notify-send）を利用するため、OS標準通知が有効である必要があります。通知履歴は保存されません。

# 参考資料
本SkillはPythonの標準通知APIおよび外部ツール（plyer, notify-send, terminal-notifier等）を利用しています。詳細は`references/design_notes.md`および公式ドキュメント（https://plyer.readthedocs.io/）を参照してください。