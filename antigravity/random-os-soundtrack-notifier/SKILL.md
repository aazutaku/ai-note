---
name: random-os-soundtrack-notifier
description: ターミナルやエディタの起動時、または作業開始を示すキーワード（例: start, open, launch, begin, edit, code）が検出された際に自動発動し、OSの通知で“今日の作業BGM”を毎回ランダムに提案します。通知は1セッションにつき1回のみ表示されます。
---

# 機能概要
random-os-soundtrack-notifierは、開発者がターミナルやエディタを起動した瞬間に、完全ランダムな“今日の作業BGM”タイトルをOSの通知で提案するスキルです。選曲は「なつかしのファミコン効果音」や「宇宙戦艦発進テーマ」など、作業に全く関係ないジャンルばかり。真面目な開発環境に“無駄な演出”を加え、ちょっとした笑いや集中力の混乱を体験できます。

# 使い方
このSkillは明示的な呼び出しは不要です。ターミナルやエディタの起動、または`start`, `open`, `launch`, `begin`, `edit`, `code`などのキーワードが検出された時点で自動的に発動します。通知は1セッションにつき1回のみ表示されます。

# 出力例
（ターミナル起動時の通知例）

```
[通知] 今日の作業BGM: なつかしのファミコン効果音
[通知] 今日の作業BGM: 宇宙戦艦発進テーマ
[通知] 今日の作業BGM: 朝礼のチャイム
[通知] 今日の作業BGM: 盆踊りの太鼓
[通知] 今日の作業BGM: 駅の発車ベル
```

# 注意点
- 通知は1セッションにつき1回のみ表示されます。
- BGMは実際に再生されません。タイトルのみの通知です。
- 外部APIやファイル保存は行いません。完全にローカルで完結します。
- 通知機能はOS標準API（Windows: win10toast, macOS: osascript, Linux: notify-send）を利用します。

# 参考資料
詳細な設計方針や利用例は`references/design_notes.md`を参照してください。OSごとの通知APIの詳細は[Windows公式ドキュメント](https://docs.microsoft.com/ja-jp/windows/uwp/design/shell/tiles-and-notifications/)、[AppleScript通知](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)、[notify-send manページ](https://man7.org/linux/man-pages/man1/notify-send.1.html)を参照。