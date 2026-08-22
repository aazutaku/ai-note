# 概要
このSkillは、ユーザーの作業中に完全ランダムで“OSペット乱入”イベントを通知・出力することで、集中力のリセットや癒しを提供します。実際のデスクトップ描画は行わず、通知APIや端末出力のみを利用しています。

# 公式ドキュメント抜粋
- notify2: https://github.com/caronc/apprise
- Python random, argparse, time: https://docs.python.org/ja/3/library/

# 利用例
- `/random-os-fake-system-pet-interruption` コマンドで即時発動
- 長時間操作時に自動発動（autoモード）
- 履歴や集計コマンドで過去の癒しイベントを振り返る

# 注意点
- Linux/WSL/Macでのデスクトップ通知に対応。Windowsでは端末出力のみ。
- 実際のペット描画やアニメーション機能は含まれません。
- ログは ~/.os_pet_events.log に保存されます。

# 設計方針
- シンプルな構造と標準API活用で、どの環境でも動作することを重視。
- 完全ランダムな発動と多様なメッセージで飽きさせない体験を目指しました。