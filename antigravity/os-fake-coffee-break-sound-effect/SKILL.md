---
name: os-fake-coffee-break-sound-effect
description: このSkillは、Antigravityがコマンド実行や作業中に“コーヒーブレイク”を演出したい場合に発動します。トリガー条件は「休憩」「集中」「疲労」「カフェイン」「リフレッシュ」などのキーワードや、連続作業・長時間稼働時です。
---

# 機能概要
このSkillは作業中やコマンド実行時に、まるでOSが強制的に“コーヒーブレイク”を推奨してくるかのような演出を提供します。実行時にデスクトップ通知とともに「コーヒー抽出音」「カップを置く音」などの効果音を再生し、通知文言も「あなたの集中はカフェイン不足です」「今こそ一服の時」など毎回ランダムで変化します。開発現場や作業環境に謎の休憩ムードを注入し、単調なリズムを愉快に撹乱します。

# 使い方
このSkillは明示的な呼び出しは不要で、Antigravityのsemantic-match-onlyトリガーにより自動発動します。たとえば「休憩したい」「集中力が切れた」「カフェインが必要」などの発話や、長時間連続作業時に自動的に通知＋サウンドが発動します。ローカルで明示的にスクリプトを実行したい場合は `python coffee_break_notifier.py` で手動テストも可能です。

# 出力例
```
[通知] 今こそ一服の時。
[サウンド再生] ./sounds/coffee_pour.wav
[通知] あなたの集中はカフェイン不足です。
[サウンド再生] ./sounds/cup_put.wav
[通知] マシンも休みたい気分。
[サウンド再生] ./sounds/coffee_machine.wav
```

# 注意点
- サウンドファイルは ./sounds/ ディレクトリにwav/mp3形式で保存してください。
- 通知機能はWindows/macOS/Linux(通知API対応)で動作しますが、環境によっては追加パッケージが必要です。
- 効果音や通知文言はカスタマイズ可能です。
- 明示的なCLIオプションや関数は使用していません。

# 参考資料
- [plyer通知公式](https://plyer.readthedocs.io/en/latest/)
- [playsound公式](https://github.com/TaylorSMarks/playsound)
- references/design_notes.md 参照