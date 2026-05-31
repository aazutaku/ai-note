---
name: desktop-mood-weather
description: デスクトップ上に完全ランダムな天気アイコンを表示することで、作業気分や実際の天気とは無関係な“気分天気”を演出します。画面端での理不尽な天気変化を楽しみたい、または会議や作業中にちょっとしたカオスを加えたい場合に自動発動します。キーワード例: デスクトップ通知, 天気, 気分, ランダム, アイコン表示。
---

# 機能概要
このSkillは、デスクトップの片隅に完全ランダムな“気分天気”アイコンを表示します。実際の天気やユーザーの本当の気分とは一切連動せず、毎回異なる天気（晴れ、曇り、雨、雷、大雪など）が表示されます。開発や会議中に理不尽な天気変化を演出し、ちょっとしたユーモアやカオスを日常に加えます。真面目な作業空間に突如現れる“あらし”や“大雪”アイコンが、思わずツッコミたくなる体験を提供します。

# 使い方
本Skillは明示的な呼び出し不要で、Antigravityエージェントが「デスクトップ通知」「気分」「天気」「ランダム表示」などのキーワードや状況を検知した際に自動発動します。スクリプトは常駐型で、一定時間ごとに天気をランダム更新します。明示呼び出し例はありませんが、Skillパッケージを有効化するだけで動作します。

# 出力例
（端末やログファイル例）
```
[INFO] mood-weather: Current mood weather is 'Thunderstorm'
[INFO] mood-weather: Displayed icon: thunderstorm.png at position (screen_width-120, screen_height-120)
[INFO] mood-weather: Next update in 10 minutes
[INFO] mood-weather: Current mood weather is 'Snow'
[INFO] mood-weather: Displayed icon: snow.png at position (screen_width-120, screen_height-120)
```
（デスクトップ右下に天気アイコンが表示されます）

# 注意点
- 実際の天気やユーザーの気分とは一切連動しません。
- アイコンはローカルに保存され、インターネット接続不要です。
- 複数起動時は前回と異なる天気が必ずしも保証されるわけではありません。
- 一部OSやデスクトップ環境では表示位置がずれる場合があります。

# 参考資料
- references/design_notes.md
- https://docs.python.org/ja/3/library/tkinter.html
- https://pillow.readthedocs.io/en/stable/reference/Image.html