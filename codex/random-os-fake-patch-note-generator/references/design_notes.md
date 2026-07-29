# 概要
このSkillは、開発作業の合間に“偽のOSパッチノート”を自動生成し、通知やターミナルに表示することで、作業空間にユーモアとリラックスをもたらすことを目的としています。

# 公式ドキュメント抜粋
- plyer通知API: https://plyer.readthedocs.io/en/latest/
- argparse: https://docs.python.org/ja/3/library/argparse.html

# 利用例
- `/skills menu`で明示呼び出し
- コマンド実行やファイル保存時に自動発動
- `python random_os_fake_patch_note_generator.py log --notify` で即時通知

# 注意点
- 通知はplyerがインストールされている場合のみ有効
- 履歴は同ディレクトリの`os_fake_patch_note_history.log`に保存
- 実際のOSや作業には一切影響しません

# 設計方針
- パッチノート文体を厳密に模倣しつつ、内容は完全に現実離れしたジョーク要素で構成
- 頻度制御や履歴管理機能を備え、過剰な出力を抑制
- CLIサブコマンドで用途に応じた柔軟な利用が可能