# 概要
このSkillは、コマンド失敗時にOS通知領域へ“全力の言い訳”を表示し、失敗体験を前向きに変えることを目的としています。Pythonのsubprocessとplyerライブラリを組み合わせ、クロスプラットフォームで動作します。

# 公式ドキュメント抜粋
- subprocess: https://docs.python.org/ja/3/library/subprocess.html
- plyer (OS通知): https://plyer.readthedocs.io/en/latest/

# 利用例
- `python command_failure_excuse_notifier.py run ls /notfound`
- `python command_failure_excuse_notifier.py list`
- `python command_failure_excuse_notifier.py summary`

# 注意点
- plyerが未インストールの場合、通知は標準エラー出力にフォールバックします。
- サーバやCUI専用環境では通知が表示されない場合があります。
- 通知履歴はプロセスごとに保持され、永続保存はされません。

# 設計方針
- 言い訳メッセージは毎回ランダム生成。
- 本来のエラー出力は失われず、標準出力/標準エラーにそのまま出力。
- 複数サブコマンド(run/list/summary)で柔軟な利用を実現。