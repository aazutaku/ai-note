---
name: random-os-error-kaiseki
description: コマンド実行時にエラーが発生した場合、CodexはこのSkillを発動し、エラー内容を“OS風カタカナ謎解説”としてデスクトップ通知します。trigger: error, exception, fail, crash, notify。
---

# 機能概要
random-os-error-kaisekiは、コマンドやスクリプト実行時に発生したエラーを、技術者風の意味不明なカタカナ造語で“解説”し、デスクトップ通知として演出するジョーク系Skillです。通常のエラーメッセージでは味わえない、開発現場に混乱と笑いをもたらすことを目的としています。バグやクラッシュ時に、システム管理者やエンジニアの疲れた心を強制リフレッシュします。

# 使い方
- 明示呼び出し: `/skills random-os-error-kaiseki` またはスキルメニューから選択
- 暗黙発動: コマンド実行時に `error`, `exception`, `fail`, `crash`, `notify` などのキーワードが含まれるエラーが発生した場合、自動で発動します。

# 出力例
```
$ python broken_script.py
Traceback (most recent call last):
  File "broken_script.py", line 1, in <module>
    raise ValueError("バグ発生！")
ValueError: バグ発生！

[通知] パケット・シンフォニーがバッファ・カタストロフを検出しました
[通知] デジタル・アンビエントがオーバーフローしました
[通知] システム・パラダイムのカーネル・リゾナンスが不正です
[通知] メモリ・エクリプスがプロトコル・フラクタルを阻害しました
```

# 注意点
- 通知はローカル環境のデスクトップ通知APIを利用します。SSHやヘッドレス環境では表示されません。
- 実際のエラー内容は標準出力にそのまま表示され、通知とは別に確認可能です。
- 通知文は毎回ランダム生成されますが、内容に技術的な意味はありません。
- Windows/macOS/Linuxの主要デスクトップ環境で動作確認済み。

# 参考資料
- [Python公式: notifications](https://docs.python.org/ja/3/library/subprocess.html)
- references/design_notes.md も参照