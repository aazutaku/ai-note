# 概要
このSkillは、開発現場の空気を一瞬でカオスに染めるための“無意味なデスクトップ通知”を安全に発生させることを目的としています。実用性はゼロですが、息抜きやチームビルディング、アイスブレイク用途で活躍します。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html
- plyer通知API: https://plyer.readthedocs.io/en/latest/
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications

# 利用例
- `/desktop-chaos-alert` で即座に謎の通知を発動
- ミーティング中のアイスブレイクや、開発現場の息抜きタイムに
- 「カオスな通知を出して」などの自然言語でのトリガーにも対応

# 注意点
- 通知はOS標準APIを利用し、ファイルやシステムには一切影響しません
- 通知許可が必要な場合があります
- 不要時はスクリプト停止やSkill無効化で簡単にオフ可能

# 設計方針
- OSごとに最適な通知APIを自動選択
- メッセージは完全に無害で、実害ゼロ
- スクリプト単体で完結し、依存性は最小限