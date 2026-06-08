---
name: terminal-samurai-weathercaster
description: ターミナル起動時や /skills menu、terminal-samurai-weathercaster の明示呼び出し時に発動。天気APIや現実の天候参照は一切せず、毎回異なる侍風コメントをランダム生成し、作業開始気分を演出する際に利用。
---

# 機能概要
terminal-samurai-weathercasterは、ターミナルを開くたびに“侍”が登場し、その日の作業気分を天気予報風に斬り捨て御免する演出系Skillです。現実の天気やAPI参照は一切行わず、完全にランダムな天気・侍コメントを生成。作業開始の緊張感やマンネリを和らげ、開発現場にユーモアと意外性をもたらします。

# 使い方
- 明示呼び出し: `/skills menu` から本Skillを選択、または `terminal-samurai-weathercaster` を直接呼び出し
- 暗黙発動: ターミナル起動時、または「天気」「侍」「気分」「演出」などのキーワードを含む状況で自動発動

# 出力例
```
【侍の気分天気予報】
本日快晴、コードも冴え渡るでござる！
------------------------------
侍より一言: 「エラーも恐れず、進むがよい！」

【侍の気分天気予報】
雷注意報、バグの嵐到来か？
------------------------------
侍より一言: 「バグ斬り捨て御免！」
```

# 注意点
- 現実の天気やAPI参照は一切行いません
- 出力は毎回完全ランダムです
- ローカル環境での利用を前提とし、外部サーバー等へのデータ送信はありません
- 侍コメントはジョーク要素を含みますが、業務利用時はご注意ください

# 参考資料
- references/design_notes.md を参照
- 公式: [Python random](https://docs.python.org/ja/3/library/random.html), [argparse](https://docs.python.org/ja/3/library/argparse.html)
