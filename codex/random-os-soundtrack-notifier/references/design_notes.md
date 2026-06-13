# 概要
random-os-soundtrack-notifier は、作業開始時や明示コマンドで、完全に無関係なBGMタイトルをOS通知で1回だけ表示するSkillです。実用性よりも“無駄な演出”を重視し、開発現場に遊び心を提供します。

# 公式ドキュメント抜粋
- macOS通知: AppleScript (osascript) を subprocess で呼び出し
- Linux通知: notify-send コマンド
- Windows通知: win10toast ライブラリ (pip install win10toast)

# 利用例
- ターミナル起動時に自動で「あなたの今日の作業BGM: 朝礼のチャイム」などが通知される
- /skills menu で明示的に呼び出し、毎回異なるBGMタイトルを楽しむ

# 注意点
- 実際のBGM再生や外部API呼び出しは行いません
- 通知は1回のみ。連続起動時や明示コマンド時も、同一セッション中は再通知されません (resetで解除可)
- OS通知が未対応の環境では標準出力のみ

# 設計方針
- Skill本体はPythonで実装し、クロスプラットフォーム対応
- サブコマンドで通知・リスト表示・リセット・概要表示を提供
- BGMタイトルは拡張/差し替えが容易なリスト構造