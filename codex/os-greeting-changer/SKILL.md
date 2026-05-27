---
name: os-greeting-changer
description: ターミナルやコンソール起動時、または /skills menu などの明示呼び出し時に発動。現実には存在しないOSや珍しい起動演出をランダムに表示し、実作業やファイルには一切影響しない安全なSkillです。
---

# 機能概要
os-greeting-changerは、ターミナルやコンソールを開くたびに現実には存在しない“偽OS起動メッセージ”をランダム表示するSkillです。Windows 99やMacintosh SE/30の時空を超えた復活、Linuxがコーヒーブレイク中など、実際には絶対に見られない珍OSや謎の起動演出で、毎日の作業開始にちょっとした異世界感を注入します。実用性はありませんが、開発の合間にクスッと笑える理不尽な遊び心を提供します。

# 使い方
- 明示呼び出し: `/skills menu` でSkill一覧から選択、または `$os-greeting-changer` で直接呼び出し
- 暗黙発動: ターミナル/コンソール起動時やセッション開始時に自動で発動（triggerType: always）

# 出力例
```
[Windows 99 Professional Edition 起動中...]
[Macintosh SE/30が時空を超えて復活しました]
[Linux 12.04: コーヒータイム中、しばらくお待ち下さい]
[BeOS Hyper Edition: メモリ空間を再構築しています]
[NEC PC-9801 Universe 起動... 未来OSモード]
[Amiga Galaxy OS: フロッピーを宇宙からダウンロード中]
[Atari ST++: MIDIシーケンサーを自己進化中]
[Sun Solaris 11.99: 太陽フレア検出...再起動します]
```

# 注意点
- 本Skillは出力のみで、ファイルやシステムには一切影響を与えません
- ローカル保存や履歴機能はありません
- ジョークメッセージのみで実用性はありません
- 既存のOS環境や設定を変更することはありません

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- 公式ドキュメント: https://ai-note.tech/docs/skills/os-greeting-changer