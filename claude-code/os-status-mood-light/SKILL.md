---
name: os-status-mood-light
description: 環境変数MOODやOSステータスバー、シェルプロンプトの状態変化を検知し、ユーザーの気分をリアルタイムで可視化したい場合に発動。気分変更やSlack連携、日替わりネタ表示などのキーワードが含まれるときに推奨。
---

# 機能概要
`os-status-mood-light`は、開発者の「気分」を環境変数MOODやシェルプロンプト、OSステータスバー、Slackステータス等に自動反映し、周囲や自分自身に可視化するスキルです。作業者のメンタル状態をリアルタイムで表現し、ちょっとしたユーモアや日替わりネタ、ツッコミ文も交えながら、作業現場の空気を和らげます。気分は環境変数やCLIから変更でき、即座に反映されます。

# 使い方
- 明示呼び出し: `/os-status-mood-light set --mood="最高"`
- 暗黙発動: `MOOD=だるい` をexportした際や、「気分」「ステータス」「Slack連携」などのワードを含む会話・コマンド実行時
- ステータス表示: `/os-status-mood-light show`
- Slack連携: `--slack` オプション

# 出力例
```
$ export MOOD=最高
$ python os_status_mood_light.py show
[絶好調] 今日もバリバリいきましょう！
（本日のネタ: 6月の開発者は梅雨に負けない）
$ export MOOD=だるい
$ python os_status_mood_light.py show
[本日省エネ運転] 無理せずいきましょう。
（ツッコミ: そろそろコーヒータイム？）
```

# 注意点
- 気分データはローカル保存され、個人PC/セッションごとに管理されます。
- Slack連携には環境変数SLACK_TOKENが必要です。
- OSステータスバー反映はmacOS/iTerm2やtmux等のAPIに依存します。
- シェルプロンプト連携はbash/zsh等でPROMPT_COMMANDを編集してください。

# 参考資料
- [iTerm2 Dynamic Profiles](https://iterm2.com/documentation-dynamic-profiles.html)
- [Slack Status API](https://api.slack.com/methods/users.profile.set)
- references/design_notes.md も参照してください。