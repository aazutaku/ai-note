# 概要
本Skillは、主要OSのデスクトップ通知APIを利用し、ユーザー体験を意図的に“うざく”演出するために設計されています。通知内容は実際のOSの小言やヘルプあるあるを参考に、イライラと笑いのバランスを追求しています。

# 公式ドキュメント抜粋
- Windows: win10toast (https://github.com/jithurjacob/Windows-10-Toast-Notifications)
- macOS: pync (https://github.com/setem/pync)
- Linux: notify2 (https://github.com/caronc/apprise/wiki/Notify2)

# 利用例
- 職場やリモートワーク中の“ネタ”として
- チームの朝会やイベントでのアイスブレイク
- OSの通知仕様を学ぶ教材として

# 注意点
- 通知の内容や頻度は、ユーザーの作業妨害になりすぎないよう自動で調整されています。
- 一部Linux環境ではnotify2の事前インストールやデスクトップ環境の対応が必要です。

# 設計方針
クロスプラットフォーム性と“うざさ”の絶妙なバランスを重視し、実際のOS通知APIのみを利用。CLIサブコマンドで手動テストやカスタマイズも可能です。