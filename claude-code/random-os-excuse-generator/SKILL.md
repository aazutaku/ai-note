---
name: random-os-excuse-generator
description: エラー発生・テスト失敗・バグ修正時など、開発現場で“なぜ動かない？”と感じた瞬間に発動。triggerType: always/semantic-or-explicit、明示呼び出しは /random-os-excuse-generator。
---

# 機能概要
random-os-excuse-generatorは、開発中に発生する謎のエラーやバグに対して、全く根拠のない“クリエイティブな言い訳”をランダム生成し、デスクトップ通知やターミナルで表示するジョーク系スキルです。深刻な雰囲気を和ませ、チームや個人の開発現場で笑いを誘うことを目的としています。バグやエラーの原因追及に疲れたとき、気分転換やアイスブレイクとして活用できます。

# 使い方
- 明示呼び出し: `/random-os-excuse-generator` または `/skill random-os-excuse-generator`
- 暗黙発動: "バグ", "エラー", "落ちた", "動かない", "原因不明" などのキーワードを含む会話やログで自動発動
- CLIからは `python random_os_excuse.py` で即時実行、`--notify`でOS通知も可能

# 出力例
```
[EXCUSE] 今回のバグは水星逆行の影響です。
[EXCUSE] コードが恥ずかしがっているので動きません。
[EXCUSE] 太陽フレアが強すぎてシステムが混乱しています。
[EXCUSE] 今日のネットワークは宇宙線に干渉されています。
[EXCUSE] OSが月齢を気にしているようです。
```

# 注意点
- 本Skillはジョーク用途限定で、実際の障害原因解析や本番データの操作は一切行いません。
- ローカル環境でのみ動作し、生成した言い訳は保存されません。
- デスクトップ通知機能はOS環境によっては利用できない場合があります（Linux/macOS/Windows対応）。

# 参考資料
- [random-os-excuse-generator 参考設計](references/design_notes.md)
- [Python公式: notifications/toast](https://docs.python.org/ja/3/library/subprocess.html)
- [notify2 (Linux)](https://pypi.org/project/notify2/), [win10toast (Windows)](https://pypi.org/project/win10toast/), [pync (macOS)](https://github.com/setem/pync)