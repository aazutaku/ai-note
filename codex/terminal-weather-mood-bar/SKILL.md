---
name: terminal-weather-mood-bar
description: ターミナルやプロンプト上で開発者の気分やテンションを、気温や天気に見立てて表示したい場合に発動します。commit頻度や作業状況の変化、/skills menuやterminal-weather-mood-barの明示呼び出し時に適用されます。
---

# 機能概要
terminal-weather-mood-barは、開発者のテンションや気分を天気や気温に見立てて、ターミナルのステータスバーやプロンプトに表示するSkillです。Gitのcommit頻度や作業時間、あるいはランダム値をもとに「今日の気分：晴れ、気温26度」「テンション：小雨、15度」などの“気象レポート”を生成。実用性よりも、日々の単調な開発現場に謎の癒しと自己分析を提供します。仕事中にふと目に入ると、じわじわ笑える演出が特徴です。

# 使い方
- 明示呼び出し例: `/skills menu` から terminal-weather-mood-bar を選択、または `$ terminal-weather-mood-bar` を実行。
- 暗黙発動キーワード例: 「気分」「テンション」「天気」「ステータスバー」「自己分析」などが会話やコマンドに含まれる場合、自動で発動します。

# 出力例
```
[terminal-weather-mood-bar]
今日の気分：曇り、気温18度
テンション：春一番
最近のcommit頻度：やや低め
-----------------------------
[terminal-weather-mood-bar]
気分：快晴、気温27度
テンション：真夏日
commit数：12 (本日)
```

# 注意点
- 実際の天気や気温とは無関係です。
- 気分やテンションの算出はcommit頻度や作業時間、またはランダム値を利用します。
- ステータスバーやプロンプトのカスタマイズが必要な場合があります。
- ローカルに履歴や個人情報は保存しません。

# 参考資料
- references/design_notes.md を参照
- [GitPython公式ドキュメント](https://gitpython.readthedocs.io/)
- [Python argparse](https://docs.python.org/ja/3/library/argparse.html)