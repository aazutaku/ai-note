# 概要
このSkillは、開発現場や作業中のデスクトップに意味不明な陰謀論アラートをランダムに通知することで、場の雰囲気を和ませたり、気分転換を促すことを目的としています。

# 公式ドキュメント抜粋
- Python win10toast: https://pypi.org/project/win10toast/
- notify-send (Linux): https://man7.org/linux/man-pages/man1/notify-send.1.html
- osascript (macOS): https://ss64.com/osx/osascript.html

# 利用例
- コーディング中に一息つきたい時
- チームのSlackやDiscordで話題作りに
- デスクトップ通知で笑いを誘いたい時

# 注意点
- 通知内容は完全なフィクションであり、実際の事実や現実の陰謀論とは一切関係ありません。
- 通知頻度はスクリプト側で制御可能ですが、過剰な連続発動には注意してください。
- ログファイルはスクリプトディレクトリに保存されます。

# 設計方針
- OSごとに適切な通知APIを自動判別し利用
- ログ機能とサマリー機能で発生履歴の可視化
- CLIサブコマンドで柔軟な操作性を確保
