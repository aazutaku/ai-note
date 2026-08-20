# 概要
random-os-fake-boss-keyは、伝統的な「ボスキー」を現代のCLI/AIワークフロー向けに再設計したパロディSkillです。業務画面風のダミー出力を即座に生成し、緊急時の“仕事中”演出を支援します。

# 公式ドキュメント抜粋
- [Boss key - Wikipedia](https://en.wikipedia.org/wiki/Boss_key)
- curses: https://docs.python.org/3/library/curses.html

# 利用例
- チャットで「上司が来た」と発言→自動でダミー画面表示
- CLIで `python fake_boss_key.py --show` 実行→即座に切り替え

# 注意点
- 本Skillは実データを一切使用せず、完全なランダム生成のみ
- ローカル端末のみに影響し、クラウドや他ユーザーには非表示
- 保存や履歴機能はありません

# 設計方針
- 発動速度と演出のリアルさを重視
- CLI/AI連携両対応
- 画面復帰はEscキー/明示コマンドで即座に可能