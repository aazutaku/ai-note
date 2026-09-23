# 概要
本Skillは、作業中に突如として“謎のOS公式・古文書巻物通知”を画面端に表示し、集中力をブレイクするエンタメ演出を目的としています。Tkinterを使い、巻物風のUIで無意味な通知文をランダム生成します。

# 公式ドキュメント抜粋
TkinterはPython標準GUIライブラリで、`Tk()`によるウィンドウ生成や`Label`/`Frame`での装飾が可能です。
- [Tkinter公式](https://docs.python.org/ja/3/library/tkinter.html)

# 利用例
- `/random-os-fake-ancient-scroll-alert` コマンドで即時発動
- `scroll_alert.py alert` で手動通知
- `scroll_alert.py auto --interval 600` で10分ごと自動通知

# 注意点
- 通知内容は完全に無意味で、業務利用不可
- OS通知センター連携や履歴保存機能は未実装
- 他の通知や作業の邪魔になる場合があります

# 設計方針
- ランダム性と巻物風UIの徹底
- シンプルな依存（Tkinterのみ）
- ユーモアと集中力ブレイクを最優先