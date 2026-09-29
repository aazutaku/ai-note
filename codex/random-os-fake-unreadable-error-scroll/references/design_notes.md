# 概要
本Skillは、開発現場やチーム内での緊張を和らげるために、意味不明なエラー通知を巻物風に演出することを目的としています。実際のエラー検知や修復機能は持たず、純粋なジョーク・演出用途です。

# 公式ドキュメント抜粋
- Python curses: https://docs.python.org/ja/3/library/curses.html
- colorama: https://pypi.org/project/colorama/

# 利用例
- チームの定例会議中や、長時間作業の合間に自動発動させて笑いを誘う
- 明示的に `/skills menu` から呼び出して、場の空気を和ませる

# 注意点
- 本Skillは外部に情報を送信しません。出力はローカル端末のみです。
- 頻繁な自動発動は作業の妨げになる場合があるため、interval引数で調整可能です。

# 設計方針
- cursesによる巻物風UIと、テキストのみのfallbackを両立
- 意味不明な行の多様性を確保し、毎回異なる演出を実現
- CLIサブコマンド(run/plain/auto)で柔軟な運用が可能