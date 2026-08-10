---
name: os-fake-coffee-break-sound-effect
description: コマンド実行や作業中に、Codexがユーザーの集中状態や作業リズムを検知した際、または/skillsメニュー等で明示呼び出しされた際に発動。通知・サウンド演出による“強制コーヒーブレイク”を演出します。
---

# 機能概要
このSkillは、開発作業やコマンド実行の合間に、まるでOSが「コーヒーブレイクを強制したい」かのような、突発的なデスクトップ通知と“謎のコーヒー抽出音”などのサウンド演出を発動します。通知文言は完全ランダムで「あなたの集中はカフェイン不足です」「今こそ一服の時」などカオスな内容。開発現場に突然の休憩ムードをねじ込み、作業リズムを愉快に撹乱します。休憩のタイミングを自動で提案したい場合や、チームの雰囲気を和ませたい時に最適です。

# 使い方
- 明示呼び出し: `/skills menu` で「os-fake-coffee-break-sound-effect」を選択、または `$os-fake-coffee-break-sound-effect` を直接入力。
- 暗黙発動: 「コーヒー」「疲れ」「休憩」「集中」「カフェイン」などのキーワードを含む会話やコマンド実行時に自動発動。

# 出力例
```
[通知] 今こそ一服の時です。
[サウンド] ./sounds/coffee_pour.wav を再生中...

[通知] あなたの集中はカフェイン不足です。
[サウンド] ./sounds/cup_place.wav を再生中...

[通知] マシンも休みたい気分です。
[サウンド] ./sounds/coffee_steam.wav を再生中...
```

# 注意点
- サウンドファイルは `./sounds/` ディレクトリに配置してください。
- 通知表示は `notify-send` (Linux) または `osascript` (macOS) で実装。Windowsは `win10toast` 使用。
- 音声再生には `playsound` または `afplay`/`aplay` を利用。
- ローカル環境でのみ動作。リモートやサーバーでは通知・音声が再生されません。

# 参考資料
- [notify-send 公式](https://specifications.freedesktop.org/notification-spec/latest/)
- [playsound PyPI](https://pypi.org/project/playsound/)
- references/design_notes.md 参照