---
name: terminal-mood-indicator
description: このSkillは、MOODなどの環境変数が設定されている場合に発動し、ターミナル上に現在の気分マークや状態を自動表示します。コマンド実行時や/skills menu呼び出し時にも有効です。
---

# 機能概要
terminal-mood-indicatorは、ターミナルの環境変数（例: MOOD）に応じて、コマンド実行時に現在の気分や状態（例: 元気、だるい、やる気MAX、迷走中など）を自動的に表示するSkillです。作業開始時にMOODをセットするだけで、以降のプロンプトやコマンド実行時にその気分が演出として現れ、チーム内の雰囲気を和らげたり、コミュニケーションのきっかけを作ります。日々の気分の可視化により、開発現場の空気を柔らかくすることができます。

# 使い方
1. 明示呼び出し: `/skills menu` から本Skillを選択、または `terminal-mood-indicator` をメンション。
2. 暗黙発動: ターミナルで `export MOOD="やる気MAX"` のようにMOOD環境変数を設定し、以降のコマンド実行時に自動で気分が表示されます。
3. CLI: `python mood_indicator.py set "燃え尽き寸前"` でMOODをセット、`python mood_indicator.py show` で現在の気分を表示。

# 出力例
```
$ export MOOD="迷走中"
$ python mood_indicator.py show
[今日の気分] 迷走中
$ ls
[今日の気分] 迷走中
Documents  Downloads  mood_indicator.py
$ python mood_indicator.py set "やる気MAX"
[今日の気分] やる気MAX
```

# 注意点
- MOOD環境変数が未設定の場合は表示されません。
- 気分の履歴はローカルの~/.mood_indicator.jsonに保存されます。
- シェルのプロンプト自体を変更したい場合は、シェル設定ファイルへの追記が必要です。
- チーム共有には個別設定が必要です。

# 参考資料
- [公式ドキュメント](https://docs.python.org/3/library/os.html)
- references/design_notes.md も参照してください。