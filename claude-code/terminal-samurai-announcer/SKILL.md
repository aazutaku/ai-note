---
name: terminal-samurai-announcer
description: コマンド実行やシェル操作時に、侍風のナレーションをテキストで出力するSkillです。ls、git、vimなどの主要コマンドや明示的な/terminal-samurai-announcer呼び出し時に発動します。
---

# 機能概要
terminal-samurai-announcerは、ターミナルでコマンドを実行するたびに、時代劇の侍が現れ、進捗や状況を勇ましくナレーションするSkillです。lsやgit commitなど日常的な操作に「拙者、lsを実行仕る！」や「このcommit、見事なり！」といった侍風コメントを自動で添え、作業を劇場型に演出します。作業の緊張感を和らげ、日々のターミナルワークを楽しく彩ります。

# 使い方
本Skillは、主要なコマンド実行時（ls, cd, git, vim, mkdir, rm, cp, mv, cat, touch, python, pip, docker等）や、明示的な`/terminal-samurai-announcer`コマンドで発動します。SkillのON/OFFは`--samurai-on`/`--samurai-off`で切り替え可能です。明示呼び出し例:

```
/terminal-samurai-announcer ls -l
```

暗黙発動例:

```
git status
# => 拙者、git statusを見届け申す！
```

# 出力例
```
拙者、lsを実行仕る！
合計 8
-rw-r--r-- 1 user user  4096 Jun  1 09:00 README.md
-rw-r--r-- 1 user user  2048 Jun  1 09:01 main.py

このcommit、見事なり！
[main 1a2b3c4] fix: update logic
 2 files changed, 10 insertions(+), 2 deletions(-)

おお、catにて内容を吟味致す！
print("Hello, Samurai!")
```

# 注意点
- 本Skillはコマンドの標準出力・標準エラーを改変しません（侍コメントを前後に挿入するのみ）。
- 除外パス（.git/やnode_modules/等）では発動しません。
- ローカル環境にのみ影響し、外部には出力しません。
- ON/OFF切替はグローバル設定ファイルに保存されます。

# 参考資料
詳細仕様やカスタマイズ方法はreferences/design_notes.mdおよび公式bash/zshラッパー実装例（https://github.com/ohmyzsh/ohmyzsh/wiki）を参照してください。