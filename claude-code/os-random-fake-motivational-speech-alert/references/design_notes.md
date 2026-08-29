# 概要
このSkillは、コマンド実行や作業時に毎回異なる“OS公式”風やる気スピーチを通知することで、日常のコーディングにユーモアとエンタメ要素を加えることを目的としています。

# 公式ドキュメント抜粋
- [Python notifications](https://docs.python.org/3/library/subprocess.html)
- [notify-send (Linux)](https://wiki.archlinux.jp/index.php/Notify-send)
- [osascript (macOS)](https://ss64.com/osx/osascript.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)

# 利用例
- コマンド実行時に自動で通知を発火し、モチベーションを高める
- `/os-random-fake-motivational-speech-alert` で明示的に通知を受ける
- `--list` で過去の通知履歴を振り返る

# 注意点
- 通知は冗談目的であり、業務システムや本番環境では慎重に利用してください
- 履歴はユーザーホーム配下にのみ保存され、外部送信は一切ありません

# 設計方針
クロスプラットフォームな通知実装と、履歴管理・サマリ機能を組み合わせ、拡張性と安全性を両立しています。