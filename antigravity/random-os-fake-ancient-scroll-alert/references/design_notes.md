# 概要
このSkillは、作業現場に突如として“謎のOS古文書巻物通知”を爆誕させるエンタメ演出用です。集中力を破壊することが主目的で、実務的な通知とは一線を画します。

# 公式ドキュメント抜粋
- [plyer通知API](https://plyer.readthedocs.io/en/latest/): クロスプラットフォームなデスクトップ通知を実現。
- [subprocess](https://docs.python.org/ja/3/library/subprocess.html): OSごとの通知コマンド呼び出しに利用。

# 利用例
- ターミナルで `python ancient_scroll_alert.py --mode desktop --repeat 2 --interval 20` と実行すれば、20秒間隔で2回、巻物通知がランダム表示されます。
- `--list` オプションで登録済みフレーズ一覧も確認可能。

# 注意点
- 実用性はありません。通知内容は完全に無意味です。
- plyer未インストール時はOS標準通知コマンドにフォールバック。
- 通知履歴は保存されません。

# 設計方針
- 主要なOS（Linux, macOS, Windows）で通知が表示されるよう実装。
- フレーズは容易に追加・編集可能。
- Skill本体はCLIサブコマンド形式で拡張性を考慮。