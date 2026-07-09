# 概要
このSkillは、エンジニアが重大コマンドを実行する直前に、意図的に緊張感と演出を加えることで、操作ミスの防止や作業体験の向上を狙っています。音と通知の両方を活用し、日常的な作業をイベント化する設計です。

# 公式ドキュメント抜粋
- [playsound](https://github.com/TaylorSMarks/playsound): クロスプラットフォームな音声再生
- [notify2](https://pypi.org/project/notify2/): Linux通知
- [Windows Toast Notification](https://docs.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/send-local-toast)

# 利用例
- `python drumroll_alert.py git push`
- `python drumroll_alert.py --dry-run rm -rf /tmp/test`
- 重大コマンド検知時に自動発動（エディタやターミナル統合）

# 注意点
- 音声ファイルはプロジェクト内の`sounds/`ディレクトリに配置してください。
- 通知APIはOSごとに異なるため、必要なパッケージ（playsound, win10toast等）は事前インストールが必要です。
- サーバー用途や無音環境では、環境変数で演出を無効化できます。

# 設計方針
- ユーザーの作業フローを妨げないよう、演出は短時間・非同期で完結。
- コマンド検知はシンプルなstartswith判定で誤検知を防止。
- 明示/暗黙両方のトリガーをサポートし、拡張性を重視。