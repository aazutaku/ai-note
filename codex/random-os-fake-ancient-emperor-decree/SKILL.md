---
name: random-os-fake-ancient-emperor-decree
description: 作業中やコマンド実行の合間に、Codexが“OS公式・古代皇帝の勅令通知”をランダムな文面で表示したい場合に発動。通知・演出・OS連携、明示呼び出しや任意のタイミングで利用可能。
---

# 機能概要
このSkillは、日常の作業やコマンド実行の最中に、なぜか“OS公式・古代皇帝の勅令”をデスクトップやターミナルへ突然通知します。通知内容は毎回ランダムで、「皇帝より勅令：本日よりCapsLockの使用を禁ず」「御前会議：スペースキーの叛逆を鎮圧せよ」など、理不尽かつ威厳ある一文が炸裂。真面目な作業風景にカオスな演出を加え、思わず手が止まる体験を提供します。冗談や息抜き、チームのアイスブレイクに最適です。

# 使い方
- 明示呼び出し例：`/skills random-os-fake-ancient-emperor-decree` もしくは `@codex random-os-fake-ancient-emperor-decree`
- 暗黙発動キーワード例：`通知`, `皇帝`, `勅令`, `OS演出`, `理不尽な命令` などが会話やコマンドに含まれる場合
- CLIからは `python decree_notifier.py notify` で即時発動

# 出力例
```
皇帝より勅令：本日よりCapsLockの使用を禁ず。
御前会議：スペースキーの叛逆を鎮圧せよ。
帝国情報局：ファイル名に空白を用いる者は全員尋問せよ。
皇帝の意志：本日以降、Tabキーは三度押すべし。
勅令：スクリーンショットは一日一回に制限する。
```

# 注意点
- 本Skillは通知のみを行い、実際のシステムや作業への影響は一切ありません。
- ローカル保存や履歴機能はありません。
- 通知内容は完全なフィクションであり、実際のOSや権限とは無関係です。
- 一部環境では通知表示のため追加パッケージ（例: `notify-send`や`osascript`）が必要な場合があります。

# 参考資料
- [Python公式 subprocess モジュール](https://docs.python.org/ja/3/library/subprocess.html)
- references/design_notes.md に設計方針や利用例を記載