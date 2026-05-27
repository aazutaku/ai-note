---
name: os-greeting-changer
description: ターミナルやコンソールを開いた際、または「起動」「OS」「ログイン」などのキーワードを含むプロンプトや明示的な /os-greeting-changer 呼び出し時に、現実には存在しない“偽OS起動メッセージ”を毎回ランダムに表示します。作業開始時の気分転換や遊び心を演出したい場合に自動発動します。
---

# 機能概要
`os-greeting-changer`は、ターミナルやコンソールの起動時や「起動」「ログイン」「OS」などのキーワードを含むプロンプト時に、現実には存在しない“偽OS起動メッセージ”を毎回ランダムに表示するスキルです。『Windows 99起動中…』や『Macintosh SE/30が時空を超えて復活』など、実在しないOSや理不尽な起動演出が混ざることで、日々の作業にちょっとしたユーモアと驚きを提供します。実用性はありませんが、開発や作業の合間に「なんだこれ」と一息つける遊び心を注入します。

# 使い方
- 明示呼び出し例: `/os-greeting-changer`
- 暗黙発動キーワード例: 「ターミナル起動」「OSを立ち上げ」「ログイン」「起動メッセージ」「システムスタート」など
- トリガータイプ: semantic-or-explicit

# 出力例
```
[Windows 99] 起動中... 未来への互換性を確認しています。
Macintosh SE/30が時空を超えて復活しました。
Linux UltraLite: コーヒータイム中、しばらくお待ち下さい。
AmigaOS 5.0 (幻覚モード) をロードしています。
BeOS Zeta: あなたのデータを踊らせます。
NeXTstep 4.2: ブラックキューブを回転中。
Solaris 13.1β: 仮想太陽を照射しています。
CP/M 4.4: パンチカードをスキャン中。
MS-DOS 11.0: メモリ管理AIが暴走開始。
OS/2 Warp 5: ワープゲートを開いています。
```

# 注意点
- 表示は標準出力のみで、ファイルやシステムには一切影響しません。
- 実在しないOS名や演出が含まれるため、実作業やログに混入しないよう注意してください。
- ローカル環境に保存や記録は行いません。
- ジョーク性が高いため、業務用途や自動化スクリプトには非推奨です。

# 参考資料
- references/design_notes.md を参照
- [UNIX fortune(1) マニュアル](https://man7.org/linux/man-pages/man6/fortune.6.html)
- [Wikipedia: List of operating systems](https://en.wikipedia.org/wiki/List_of_operating_systems)