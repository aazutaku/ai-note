# 概要
このSkillは、実際のOSやファイルシステムには一切影響を与えず、ユーザーの作業環境に“謎のデスクトップペット進化通知”を疑似的に生成します。Python標準ライブラリのみで完結し、安全性とユーモア性を両立しています。

# 公式ドキュメント抜粋
- Python random: https://docs.python.org/ja/3/library/random.html
- Python argparse: https://docs.python.org/ja/3/library/argparse.html

# 利用例
- `/random-os-fake-desktop-pet-evolution-notifier` 実行で即時ランダム通知
- `python pet_evolution_notifier.py notify` でターミナル通知
- `python pet_evolution_notifier.py list` で履歴確認

# 注意点
- 実際のOS通知APIやファイル操作は一切使用していません。
- 出力は標準出力のみ、履歴もメモリ上のみで永続化されません。
- 業務利用時はジョーク通知であることを明示してください。

# 設計方針
毎回異なる進化・誕生パターンをランダム生成し、通知内容が重複しにくいよう工夫しています。CLIサブコマンドで履歴・サマリーも確認でき、AIエージェントからの明示・暗黙呼び出し両対応です。