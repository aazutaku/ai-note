# 概要
このSkillは、OSやターミナル上で突然フェイクなカフェイン過剰摂取警告を表示し、作業空間にユーモアとカオスをもたらすことを目的としています。クロスプラットフォーム対応のため、Pythonの標準機能と外部通知API（plyer, osascript, notify-send, win10toast）を組み合わせています。

# 公式ドキュメント抜粋
- plyer: https://github.com/kivy/plyer
- notify-send: https://specifications.freedesktop.org/notification-spec/latest/

# 利用例
- `/random-os-fake-caffeine-overdose-alert` 明示呼び出しで即座に警告
- 長時間の作業や「徹夜」などのキーワードを含む会話時に自動発動

# 注意点
- 通知内容は完全なフィクションであり、健康や実際のカフェイン摂取量とは無関係です。
- システム設定や通知権限によりOS通知が表示されない場合はターミナル表示に自動フォールバックします。

# 設計方針
- どのOSでも害のない演出のみを採用
- 通知履歴はメモリ上のみ保持し、ローカル保存は行いません
- 理不尽なタイミングでの発動を重視し、intervalはランダム化
