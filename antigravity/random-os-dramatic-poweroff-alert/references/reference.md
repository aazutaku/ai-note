# 概要
このSkillは、クロスプラットフォームなデスクトップ通知API（主にPythonのplyer, win10toast）を活用し、実際のシャットダウン操作を一切伴わずに“壮大な電源オフ予告”を演出します。通知内容は毎回ランダム生成され、OSごとに適切な通知方式を選択します。

# 公式ドキュメント抜粋
- plyer: https://plyer.readthedocs.io/en/latest/
- win10toast: https://github.com/jithurjacob/Windows-10-Toast-Notifications

# 利用例
作業中に突如「OSカーネル、最後の咆哮をあげよ！」等の通知が表示され、緊張感が一気に和らぎます。明示的にCLIから `python dramatic_poweroff_alert.py loop --count 3` のように実行することも可能です。

# 注意点
通知はローカル環境でのみ表示され、実際のシステム操作は行いません。plyer/win10toastのインストールが必要です。

# 設計方針
安全性を最優先し、OSやユーザーデータに一切影響を与えない設計としています。通知内容の多様性・ユーモア性を重視し、繰り返し利用しても飽きない工夫を施しています。