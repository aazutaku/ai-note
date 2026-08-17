---
name: random-os-nap-detection-alert
description: ユーザーが30秒以上無操作状態になった場合に、ランダムな“お昼寝検出”メッセージをデスクトップ通知やターミナルに表示するSkillです。『うたた寝モード突入』などのツッコミ系通知で集中力低下やサボりを検出し、職場や作業現場で気まずい笑いを誘発します。コマンド入力やエディタ操作の監視がトリガー条件です。
---

# 機能概要
このSkillは、コマンドラインやエディタで作業中に30秒以上無操作状態が続くと、OSのデスクトップ通知やターミナルに「お昼寝検出」系のランダムなアラートを表示します。通知内容は毎回異なり、「検出：うたた寝モード突入」「OS推奨：夢の中でバグ修正」など、絶妙なツッコミで作業中のサボりや集中力低下をネタ化。職場での緊張感緩和や、気まずい空気を演出したい場合に最適です。

# 使い方
- 明示呼び出し例:
  - `/skills menu` から `random-os-nap-detection-alert` を選択
  - ターミナルで `python random_os_nap_detection_alert.py --start` を実行
- 暗黙発動キーワード例:
  - 「無操作」「サボり」「idle」「うたた寝」「集中力低下」などが含まれる文脈や、一定時間キーボード・マウス操作がない場合に自動発動します。

# 出力例
```
[OSお昼寝検出アラート] 検出：うたた寝モード突入
[OSお昼寝検出アラート] OS推奨：夢の中でバグ修正
[OSお昼寝検出アラート] 睡眠ログをクラウドにアップロード中...
[OSお昼寝検出アラート] 30秒以上操作がありません。お昼寝タイム？
[OSお昼寝検出アラート] 注意：作業効率が夢の中に突入しました
```

# 注意点
- 本Skillはユーザーのローカル環境でのみ動作し、ファイルや設定を破壊しません。
- 通知機能はLinux/macOSの`notify-send`や`osascript`を利用。Windowsでは`win10toast`等が必要です。
- 無操作検出は標準入力監視やイベントフックで実装していますが、全アプリケーションの操作を網羅するものではありません。
- 通知内容はローカルに保存されません。

# 参考資料
- [参考: references/design_notes.md](references/design_notes.md)
- [notify-send (Linux)](https://specifications.freedesktop.org/notification-spec/notification-spec-latest.html)
- [osascript (macOS)](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html)
- [win10toast (Windows)](https://pypi.org/project/win10toast/)