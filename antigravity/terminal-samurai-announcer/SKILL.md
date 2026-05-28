---
name: terminal-samurai-announcer
description: ターミナルでコマンド実行時に、侍風の時代劇ナレーションをテキストで表示したい場合に発動します。コマンド実行・進捗・通知・演出・実況・侍・時代劇などのキーワードや、作業の雰囲気を盛り上げたい時に適しています。
---

# 機能概要
terminal-samurai-announcerは、ターミナルでコマンドを実行するたびに、侍が現れて時代劇風のナレーションを高らかに読み上げる（テキスト出力する）スキルです。lsやgit commitなど、どんなコマンドにも毎回異なる侍のセリフが添えられ、作業が一気にチャンバラ劇場に変貌します。コマンドの緊張感や単調さを和らげ、作業のモチベーションや周囲の注目度も向上します。

# 使い方
このSkillは、ターミナルでコマンドを実行する際に自動で発動します。明示的な呼び出しは不要です。暗黙発動キーワード例：ls、cd、git、make、python、npm、docker、vim、sudo、rm、cat など、一般的なコマンド全般。
ON/OFF切り替えは `samurai_announce.py toggle` で可能です。

# 出力例
```
$ ls
拙者、lsの術を披露仕る！
Desktop  Documents  Downloads
$ git commit -m "fix bug"
このcommit、まこと見事なり！
[main 1a2b3c4] fix bug
$ rm -rf temp/
おぬし、temp/を消し去る覚悟、しかと見届けた！
$ python script.py
拙者、script.pyを走らせ候！
```

# 注意点
- 本Skillは標準出力に侍風セリフを付加するのみで、コマンドの実行結果自体は変更しません。
- ローカル環境でのみ動作を保証します。
- ON/OFF切替は設定ファイル（~/.samurai_announcer_state）で管理されます。
- 除外パスや特定コマンドの除外設定も可能です。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- [Python subprocess公式](https://docs.python.org/3/library/subprocess.html)
- [shlex公式](https://docs.python.org/3/library/shlex.html)
- [os.path公式](https://docs.python.org/3/library/os.path.html)