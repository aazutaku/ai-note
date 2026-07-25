# 概要
このSkillは、開発者の作業環境に突如“OS公式の架空休日”を通知することで、作業の合間に遊び心とリフレッシュを提供します。現実の業務やファイルには一切影響しない安全設計です。

# 公式ドキュメント抜粋
通知表示にはPythonのnotify2ライブラリ（[公式PyPI](https://pypi.org/project/notify2/)）を利用しています。Linux系デスクトップ環境で標準的に動作します。

# 利用例
- 明示的に `python os_fake_holiday_announcer.py notify` で即時通知
- `python os_fake_holiday_announcer.py log` で過去の通知履歴を確認
- 1時間ごとに最大1回の自動通知（暗黙トリガー）

# 注意点
- 通知内容は完全に架空で、業務やシステムには何も影響を与えません。
- 履歴は ~/.os_fake_holiday_announcer_log.json に保存されます。
- Windows/Macではnotify2が動作しない場合があります。

# 設計方針
過剰な通知による作業妨害を避けるため、頻度制限と履歴管理を重視しています。メッセージはランダム生成で毎回異なるユーモアを提供します。