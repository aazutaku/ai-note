---
name: random-os-fake-system-astrology-alert
description: このSkillは、作業中やコマンド実行時などのタイミングで、ランダムな“OS公式・システム占星術通知”を表示します。明示呼び出し（/random-os-fake-system-astrology-alert）や、通知・運勢・占い・ラッキーコマンド等のキーワード出現時にも自動発動します。
---

# 機能概要
このSkillは、日常の開発作業やコマンド実行の合間に、架空のOS公式から届く“占星術風の謎通知”をランダムで表示します。通知内容は「今日のラッキーコマンド」「水星逆行中につきバグ注意」など、システムや作業内容と全く関係のないユーモラスなものばかり。真面目な作業の合間に、宇宙規模のどうでもいいアドバイスで思考をリフレッシュし、非日常感を演出します。通知はローカル環境のデスクトップ通知またはターミナル出力で安全に実行され、実データやシステムには一切影響しません。

# 使い方
- 明示呼び出し例: `/random-os-fake-system-astrology-alert`
- 暗黙発動: 「通知」「占い」「運勢」「ラッキーコマンド」「星座」などのキーワード出現時、または一定時間ごとに自動発動
- コマンドライン: `python astrology_alert.py --once` で即時通知、`python astrology_alert.py --daemon` で定期実行

# 出力例
```
[AstroSys Alert] 本日のあなたの守護惑星は木星です。大胆なリファクタリングに挑戦してみましょう。
[AstroSys Alert] 水星逆行中につき、git push の前に念のため diff を確認しましょう。
[AstroSys Alert] 今日のラッキーコマンドは: ls -l
[AstroSys Alert] あなたのシステムは現在、射手座モードです。新しいパッケージの導入に最適な日です。
[AstroSys Alert] バグは土星のせいかもしれません。深呼吸して再ビルドを。
```

# 注意点
- 出力は通知または標準出力のみ。ファイルやシステム設定は変更しません。
- ログや履歴はローカル保存されません。
- 本Skillはジョーク用途です。実際の占星術やOSの公式通知とは一切関係ありません。
- Linux/macOSの通知APIを利用。Windowsでは標準出力のみ対応。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- 公式API: [notify2 (Linux)](https://pypi.org/project/notify2/), [osascript (macOS)](https://ss64.com/osx/osascript.html)
