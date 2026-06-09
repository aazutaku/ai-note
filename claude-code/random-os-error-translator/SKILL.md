---
name: random-os-error-translator
description: エラー発生時や例外検出時に自動で発動し、エラーメッセージを“別のOS風”にパロディ変換して表示します。明示的な /random-os-error-translator コマンドでも利用可能です。エラー、例外、permission denied、file not found などのキーワードに反応します。
---

# 機能概要
このSkillは、コマンドラインやターミナルで発生する各種エラーを、複数の“架空または懐かしのOS風”に自動変換して表示します。たとえば「Permission denied」を「このファイルは神聖にして侵入を禁ず（MS-DOS風）」や、「File not found」を「指定されたファイルは宇宙の彼方に消えました（国産OS風）」など、意味不明な演出で日常の作業に笑いとカオスをもたらします。元のエラー内容も簡単に参照できるので、実用性も確保しています。

# 使い方
- 明示呼び出し例: `/random-os-error-translator "Permission denied: 'test.txt'"`
- 暗黙発動キーワード例: `permission denied`, `file not found`, `is a directory`, `operation not permitted` などのエラー発生時に自動変換。

# 出力例
```
[OS風エラー演出: AmigaOS]
> ファイルへのアクセスは銀河評議会の承認が必要です。
[元のエラー]: Permission denied: 'test.txt'

[OS風エラー演出: MS-DOS]
> このファイルは神聖にして侵入を禁ず。
[元のエラー]: Permission denied: 'test.txt'

[OS風エラー演出: 謎の国産OS]
> 推奨されていない操作です。
[元のエラー]: Operation not permitted
```

# 注意点
- 本Skillはジョーク用途です。実際のエラー解決には元のエラーメッセージを参照してください。
- 一部のエラー内容は意図的に誇張・改変されています。
- ローカルにエラーログを保存する機能がありますが、個人情報や機密情報の取り扱いに注意してください。
- 除外パス: システムクリティカルなコマンドや管理者権限操作時は自動変換を抑制します。

# 参考資料
- 詳細な設計や演出パターンは `references/design_notes.md` を参照
- Python 標準の `os`, `random`, `argparse` などを活用
- 公式: https://ai-note.tech/skills/random-os-error-translator