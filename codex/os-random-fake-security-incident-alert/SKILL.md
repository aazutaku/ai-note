---
name: os-random-fake-security-incident-alert
description: 作業中や会話中に「セキュリティ」「ウイルス」「インシデント」「OS」などのキーワードが出現した際、または/skillsメニューや明示的な呼び出しで、爆笑フェイクOSインシデント通知をランダムに生成・発火します。
---

# 機能概要
このSkillは、作業中や会話中に突如として“ありえないOSセキュリティインシデント”の通知をデスクトップやターミナルに表示します。通知内容は毎回ランダムで、「OSがピーマン型ウイルスに感染」「あなたの椅子が物理的に乗っ取られました」など、現実では絶対に起こりえない爆笑ネタばかり。生真面目なオフィスや開発現場の空気を一気に和ませ、コミュニケーションの潤滑油となります。本Skillは実際のシステム挙動やデータには一切影響を与えません。

# 使い方
- 明示呼び出し: `/skills menu` から `os-random-fake-security-incident-alert` を選択、または `$os-random-fake-security-incident-alert` と入力
- 暗黙発動: 「セキュリティ」「ウイルス」「インシデント」「OS」などの単語を含む会話やコマンド入力時、自動で発火

# 出力例
```
[ALERT] OS Security Incident Detected!
- Incident ID: #PPR-20240612-8721
- Description: 本日よりマウスが逆方向に動きます。OSは混乱しています。
- Recommendation: ピーマン型ウイルスにご注意ください。

[ALERT] OS Security Incident Detected!
- Incident ID: #CHR-20240612-0093
- Description: あなたの椅子が物理的に乗っ取られました。
- Recommendation: 立ち上がって深呼吸しましょう。
```

# 注意点
- 本Skillは完全なジョーク通知のみを生成し、実際のシステムやファイルには一切影響を与えません。
- ログや履歴はローカル保存されません。
- 本物のセキュリティアラートと混同しないようご注意ください。

# 参考資料
本SkillはPythonの標準ライブラリと`plyer`によるクロスプラットフォーム通知APIを利用しています。詳細はreferences/以下や[plyer公式ドキュメント](https://plyer.readthedocs.io/en/latest/)をご参照ください。