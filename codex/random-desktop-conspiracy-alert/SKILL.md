---
name: random-desktop-conspiracy-alert
description: 作業やコーディング中、または /skills メニューや skill名への明示的な呼び出し時に、意味不明で根拠のない陰謀論アラートをデスクトップ通知で発生させます。trigger キーワード: 通知、アラート、陰謀論、気分転換。
---

# 機能概要
このSkillは、開発現場や作業中のデスクトップに突如として意味不明な陰謀論アラートを表示し、現場に一瞬の混乱と笑いをもたらします。通知内容は完全ランダムで「Wi-Fiの波動が干渉しています」「コードレビューは宇宙人の監視下にあります」など、全く根拠のない怪しさ満点のメッセージです。集中力を微妙に妨害しつつも、気分転換や場の和み、チームのコミュニケーション促進に役立ちます。

# 使い方
- 明示呼び出し例: `/skills random-desktop-conspiracy-alert` または スキル名へのメンション
- 暗黙発動キーワード例: 「通知」「アラート」「陰謀論」「気分転換」などが会話やコマンドに含まれる場合、自動発動します。
- CLIサブコマンド: `python conspiracy_alert.py send` で即時通知、`python conspiracy_alert.py list` で過去の通知メッセージ一覧、`python conspiracy_alert.py summary` で発生履歴要約。

# 出力例
```
[通知] Wi-Fiの波動が干渉しています。
[通知] コードレビューは宇宙人の監視下にあります。
[通知] 本日15時、全てのバグが覚醒します。
[通知] あなたのマウスは政府の追跡装置です。
[通知] デプロイのたびに時空が歪みます。
```

# 注意点
- 通知はローカルOSの通知APIを利用します（Linux: notify-send, Windows: win10toast, macOS: osascript）。
- 通知頻度は過剰にならないよう調整されていますが、連続発動にはご注意ください。
- メッセージ内容は完全なフィクションであり、実際の事実とは一切関係ありません。
- ログはスクリプトのディレクトリに保存されます。

# 参考資料
- references/design_notes.md に設計方針や参考リンクを記載
- 公式ドキュメント: [Python win10toast](https://pypi.org/project/win10toast/), [notify-send](https://man7.org/linux/man-pages/man1/notify-send.1.html), [osascript](https://ss64.com/osx/osascript.html)