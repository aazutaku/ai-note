# 概要
このSkillは、架空のサイバーパンクOS通知を現実のデスクトップ通知APIで実現します。演出や雰囲気作り、配信・イベント用途を主眼としています。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- notify-send (Linux): https://specifications.freedesktop.org/notification-spec/
- terminal-notifier (macOS): https://github.com/julienXX/terminal-notifier

# 利用例
- 作業中に非日常感を演出
- 配信やイベントのBGM的な演出
- チームの気分転換やアイスブレイク

# 注意点
- 通知内容はすべてフィクションです。実用的な警告や障害通知は含みません。
- OS標準の通知APIが有効である必要があります。
- plyer, notify-send, terminal-notifier等、一部外部ツールが必要な場合があります。

# 設計方針
- クロスプラットフォーム対応
- 実在APIのみ利用し、架空コマンドや独自通知エンジンは使わない
- 迷惑にならない頻度・ランダム性を重視
- メッセージ内容は随時拡張可能