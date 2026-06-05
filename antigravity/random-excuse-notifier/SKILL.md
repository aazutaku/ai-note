---
name: random-excuse-notifier
description: ターミナル操作やコマンド実行時など、ユーザーが作業するたびに“言い訳”をOS通知領域へランダム表示するSkill。triggerType: always、semantic-match-onlyで発動。
---

# 機能概要
random-excuse-notifierは、ターミナルでコマンドを実行するたびに、全く根拠のない“言い訳”をOSの通知領域にランダムで表示するスキルです。例えば「Wi-Fiが不安定で…」「今日は運が悪い日です」など、思わず笑ってしまうようなメッセージが作業中にそっと現れます。真面目な通知を期待している場面ほど、意表を突く演出となり、業務効率には一切寄与しませんが、作業の合間にユーモアを提供します。

# 使い方
このSkillは明示的な呼び出しは不要です。triggerType: always および semantic-match-only の条件下で、ターミナル操作（ls, git, python, make など）やコマンド実行時に自動で発動します。明示的な呼び出しは想定していません。

## 発動例
- コマンド: `ls`
- コマンド: `git status`
- コマンド: `python script.py`

# 出力例
```terminal
$ git pull
[通知] 今日の運勢が悪いのでエラーが出ました。
$ make build
[通知] ネットワークが遅いので少々お待ちください。
$ python main.py
[通知] マウスが反応しなくて遅れました。
$ ls
[通知] 水星逆行中につきご容赦ください。
$ echo hello
[通知] 今日はPCの機嫌が悪いです。
```

# 注意点
- 本SkillはOSの通知API（Linux: notify-send, macOS: osascript, Windows: toast通知）を利用します。環境によっては追加パッケージが必要です。
- 言い訳メッセージは100種以上を内包し、都度ランダム選択されますが、短期間で同じものが出る場合もあります。
- 通知内容はローカルに保存されません。
- 実務用途には全く役立ちません。

# 参考資料
- references/design_notes.md
- https://specifications.freedesktop.org/notification-spec/latest/
- https://docs.python.org/3/library/subprocess.html