# 概要
terminal-boss-bgm-suggester は、最初のターミナルコマンド実行時に本日のBGMを完全ランダムで提案することで、日々の作業を少しだけ楽しくするユーティリティです。音楽再生は行わず、テキスト通知のみで環境を壊さない設計としています。

# 公式ドキュメント抜粋
- Python 標準ライブラリのみで実装
- ~/.terminal_boss_bgm_state.json にて1日1回の発動制御
- BGMリストはスクリプト内で管理

# 利用例
- .bashrcや.zshrcの最初に `python3 ~/.agents/skills/terminal-boss-bgm-suggester/terminal_boss_bgm_suggester.py` を追加
- /skills menu から明示呼び出しも可能

# 注意点
- テキスト通知のみで音楽再生や外部API通信は行いません
- 状態ファイルが破損した場合は `reset` サブコマンドで初期化可能

# 設計方針
- 環境非依存・ローカル完結
- 1日1回のみ発動し、複数ターミナルでも重複通知なし
- 職場利用時は選曲内容・通知内容に注意