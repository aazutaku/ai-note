# 概要
本Skillは、毎回ランダムな“謎OSマスコット”名とセリフを生成し、notify2等の実在API経由でデスクトップ通知として表示する演出特化型ツールです。

# 公式ドキュメント抜粋
notify2 (https://pypi.org/project/notify2/)はLinuxデスクトップ通知の標準的Pythonライブラリで、クロスデスクトップ環境で動作します。Windows/Macでは標準通知APIへの移植が必要です。

# 利用例
- 明示: `python mascot_parade.py once` で1回だけ通知
- デーモン: `python mascot_parade.py daemon` で10分ごとに自動通知
- イベント連携: `python mascot_parade.py event --keyword=build` で特定作業時に通知

# 注意点
- 実用性は皆無で、作業の集中や効率化には寄与しません。
- 通知頻度は10分に1回まで自動制御し、うるさすぎない設計です。
- マスコット名・セリフは都度完全ランダム生成。

# 設計方針
- Skill本体はCLIサブコマンド形式で、明示/暗黙いずれの呼び出しにも対応。
- OS依存部分はnotify2等の実在APIのみを利用し、架空APIや関数は使用しません。