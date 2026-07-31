# 概要
このSkillは、OSのデスクトップ通知APIを利用し、作業中のユーザーに突発的な“カラオケ推奨”メッセージをランダムなタイミング・内容で表示することで、現実逃避や息抜きを演出することを目的としています。

# 公式ドキュメント抜粋
- [Plyer通知API](https://plyer.readthedocs.io/en/latest/)
- [notify-send (Linux)](https://man7.org/linux/man-pages/man1/notify-send.1.html)
- [terminal-notifier (macOS)](https://github.com/julienXX/terminal-notifier)
- [win10toast (Windows)](https://github.com/jithurjacob/Windows-10-Toast-Notifications)

# 利用例
- 長時間作業や集中状態の合間に、意図せず現れるカラオケ通知でリフレッシュ
- 雑談や「疲れた」「カラオケ」などのワード入力時に突発的通知

# 注意点
- 通知はローカルPC上でのみ表示され、データ損失やシステム設定には影響しません
- 通知内容は最低5パターン以上を保証し、毎回異なるメッセージが選ばれます

# 設計方針
- OSごとに適切な通知APIを自動選択し、依存ライブラリが不足しても標準出力にフォールバック
- 明示的な呼び出しは不要、キーワード検知やランダムタイマーで自動発動
- ログやファイル保存は行わず、ユーザー体験のみに特化