# 概要
terminal-samurai-announcerは、日々のターミナル作業を時代劇風に実況することで、作業の緊張感を和らげ、楽しい演出を提供するSkillです。コマンド実行時に標準出力へ侍風メッセージを毎回ランダムに挿入します。

# 公式ドキュメント抜粋
本SkillはPython標準のrandom, subprocess, argparseモジュールのみを利用し、外部依存なく動作します。ON/OFF状態はユーザーホームディレクトリの隠しファイルで管理します。

# 利用例
- `python samurai_announcer.py on` で有効化
- `python samurai_announcer.py run ls -l` で実況付きls
- ON状態で `python samurai_announcer.py git status` など任意コマンドをラップ実行

# 注意点
コマンドの実際の出力や挙動には干渉せず、標準出力にメッセージを追加するだけです。パイプや複雑なシェル構文には未対応。

# 設計方針
SkillのON/OFF切替は明示的に可能とし、既存作業フローの邪魔をしません。実況文はテンプレート+コマンド名を埋め込む方式で多様性を確保しています。