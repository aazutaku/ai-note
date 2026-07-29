# 概要
このSkillは、コマンドやファイル保存などのアクション時に、完全に架空のOSパッチノートを自動生成し、通知またはターミナル出力するためのものです。ユーモアと遊び心で作業環境を和ませることを目的としています。

# 公式ドキュメント抜粋
- Python notify2: https://pypi.org/project/notify2/
- argparse: https://docs.python.org/ja/3/library/argparse.html
- random: https://docs.python.org/ja/3/library/random.html

# 利用例
- ターミナルで `python random_os_fake_patch_note_generator.py` を実行
- 明示的に `/random-os-fake-patch-note-generator` でSkill呼び出し
- log/summaryサブコマンドで過去の出力を確認

# 注意点
- 通知機能はLinux等のnotify2対応環境でのみ有効
- ログファイルはユーザーホームディレクトリ直下に保存
- 出力内容は完全なフィクションで、実際のOSや作業には影響しません

# 設計方針
- ユーザー体験を損なわないよう、頻度制御を実装
- 出力は毎回ユニークで、OSパッチノート風の文体を維持
- シンプルな構成で拡張・カスタマイズも容易