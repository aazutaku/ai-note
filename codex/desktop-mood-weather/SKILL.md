---
name: desktop-mood-weather
description: デスクトップの片隅に完全ランダムな“気分天気”アイコンを表示したいとき、または「天気」や「気分」「演出」などのキーワードを含む会話や明示呼び出し時に発動します。実際の天気や気分とは無関係な演出が必要な場合に適しています。
---

# 機能概要
このSkillは、デスクトップの片隅に完全ランダムな“気分天気”アイコンを表示します。実際の天気やユーザーの気分状態とは一切連動せず、晴れ・曇り・雨・雷・雪などの天気アイコンが毎回ランダムで現れます。開発中や会議中、ふとした瞬間に理不尽な天気演出で画面に遊び心を加え、作業の気分転換や雑談のきっかけを提供します。

# 使い方
- 明示呼び出し例: `/skills menu` で「desktop-mood-weather」を選択、または `$desktop-mood-weather` と入力。
- 暗黙発動キーワード例: 「天気」「気分」「演出」「アイコン」「画面の端」「ランダム」などの語句を含む会話や説明文。
- Skillはsemantic-or-explicitトリガー型で、常時または明示的に呼び出せます。

# 出力例
```
[INFO] desktop-mood-weather: ランダム天気アイコン「雷」がデスクトップ右下に表示されました。
[INFO] desktop-mood-weather: 本日の気分天気は「雪」です。
[INFO] desktop-mood-weather: ウィンドウID=0x3e00007c, アイコン=rain.png, 位置=(screen_width-64, screen_height-64)
[INFO] desktop-mood-weather: 10分ごとに気分天気を再抽選します。
[INFO] desktop-mood-weather: 実際の天気や気分とは一切関係ありません。
```

# 注意点
- 実際の天候やユーザーの感情状態とは完全に無関係です。
- アイコン画像はローカル保存または一時生成されます。
- Windows/Mac/Linuxの主要デスクトップ環境で動作しますが、仮想環境やリモートデスクトップでは非対応の場合があります。
- 複数回起動時も毎回異なる天気が出る仕様です。

# 参考資料
- [PySimpleGUI公式](https://pysimplegui.readthedocs.io/)
- references/design_notes.md で設計方針や利用例を解説