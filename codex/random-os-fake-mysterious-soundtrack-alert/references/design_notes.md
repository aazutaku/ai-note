# 概要
このSkillは、作業中の気分転換や会話のネタとして“謎のOS公式BGM推奨通知”を演出するために設計されています。実際の音楽再生は行わず、独自生成のBGMタイトルを通知・ターミナル出力します。

# 公式ドキュメント抜粋
- OS通知API: macOS (osascript), Linux (notify-send), Windows (ctypes.windll.user32.MessageBoxW)
- Python subprocess: https://docs.python.org/ja/3/library/subprocess.html

# 利用例
- `/skills random-os-fake-mysterious-soundtrack-alert` で即時発動
- コマンド実行の合間や「BGM」「作業用」等の発話時に自動発動

# 注意点
- 音は一切鳴りません。通知・演出のみです。
- 履歴はセッション内のみ保持、永続保存はしません。
- 本Skillはジョーク用途であり、業務通知や実際のBGM推奨とは無関係です。

# 設計方針
- OS種別ごとに最適な通知手段を自動選択
- BGMタイトルはプレフィックス・サフィックスをランダム合成
- テスト・デモ用途としても活用可能