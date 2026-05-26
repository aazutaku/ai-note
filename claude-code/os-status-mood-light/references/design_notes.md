# 概要
os-status-mood-lightは、開発者の気分可視化を目的としたユーティリティです。環境変数やローカルファイル、Slack API等の実在サービス連携を重視して設計しています。

# 公式ドキュメント抜粋
- [Slack Status API](https://api.slack.com/methods/users.profile.set): ユーザーステータスの自動更新に利用。
- [iTerm2 Dynamic Profiles](https://iterm2.com/documentation-dynamic-profiles.html): ステータスバー連携の参考。

# 利用例
- 朝一で `set --mood="最高"` を実行し、Slackやシェルプロンプトに気分を表示。
- 気分が落ち込んだとき `set --mood="だるい" --slack` で周囲に「本日省エネ運転」を通知。
- 定期的に `show` コマンドで自分の気分を確認。

# 注意点
- シェルプロンプト反映はPROMPT_COMMANDや.zshrc編集が別途必要。
- Slack連携はAPIトークン漏洩に注意。
- ローカル保存は~/.os_status_mood_light.jsonに限定。

# 設計方針
- 実在APIのみ利用し、架空のCLIや関数は排除。
- ユーモアと実用性の両立を目指す。
- 拡張性（他サービス連携やカスタム気分追加）を意識。