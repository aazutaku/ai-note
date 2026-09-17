---
name: os-random-fake-sudden-downtime-alert
description: 長時間の作業や集中状態、単調なコーディングセッション中に“緊急ダウンタイム通知”の演出で気分転換や遊び心を加えたい場合に発動。明示的な /os-random-fake-sudden-downtime-alert コマンドや「ダウンタイム」「メンテ」「OS異常」などのキーワードで自動発火します。
---

# 機能概要
このSkillは、作業中のあなたに突如「OS緊急ダウンタイム告知」をランダムな内容で表示するジョーク通知演出ツールです。実際のシステムやデータには一切影響を与えず、単調な作業空間に“謎の危機感”と笑いをもたらします。通知内容は毎回ランダム生成され、「理由: OSのやる気が低下」「対策: キーボードを褒め称えて延命可能」など、思わず二度見するフェイクメッセージが炸裂。気分転換やチームのアイスブレイク、集中しすぎた時のリフレッシュに最適です。

# 使い方
明示的には `/os-random-fake-sudden-downtime-alert` コマンドで即座に通知を発動できます。暗黙的には「ダウンタイム」「メンテ」「OS異常」「システム落ちそう」などのキーワードが会話やコードコメント中に現れると自動で発火します。CLIオプションで通知頻度や表示方法（デスクトップ/ターミナル）も制御可能です。

# 出力例
```
[ALERT] 緊急: このPCは15分後に謎のメンテナンスモードへ突入します
理由: OSのやる気が著しく低下
対策: キーボードを褒め称えて延命可能
キャンセル方法: 画面に向かって「ありがとうOS」と叫ぶ
---
[ALERT] Warning: Sudden downtime scheduled in 7 minutes
Reason: Unusual cosmic ray activity detected
Mitigation: Pet your mouse gently
```

# 注意点
本Skillは完全なフェイク通知のみを生成し、実際のOSやファイルには一切変更・ダメージを与えません。通知はローカル端末上にのみ表示され、ネットワーク送信やログ保存は行いません。悪用や誤解を招く環境（本番運用サーバ等）では使用を控えてください。

# 参考資料
詳細な設計方針や通知例は references/design_notes.md を参照。Pythonの標準通知API（notify2, plyer等）やターミナル出力の演出方法については公式ドキュメント（https://docs.python.org/ja/3/library/argparse.html, https://plyer.readthedocs.io/）もご覧ください。