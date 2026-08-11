# 概要
このSkillは、実用性を完全に排除した“気分天気”バーをOS風に演出するための設計です。職場や自宅のPC環境で、唐突に謎の気分天気を表示し、会話や雰囲気を和ませることを目的としています。

# 公式ドキュメント抜粋
- [Python tkinter公式ドキュメント](https://docs.python.org/ja/3/library/tkinter.html)
- [win10toast (Windows通知)](https://pypi.org/project/win10toast/)

# 利用例
- コード実行時や会話の合間に自動/手動でバーを表示
- 「今日の気分は？」と聞かれた時に即時ランダム天気を出す

# 注意点
- 表示は完全にランダムで、実際の気分や天候とは無関係
- Mac/Linuxはtkinter、Windowsはwin10toastを利用
- 他の通知系Skillと同時利用時は競合に注意

# 設計方針
- 100%ランダム生成で、履歴や記録は一切残さない
- OSごとに最適な通知方法を選択（tkinter/タスクバー）
- CLIサブコマンドで柔軟な呼び出しに対応