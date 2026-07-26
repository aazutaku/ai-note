---
name: random-os-fake-morning-radio
description: 作業開始や『おはよう』『start』『begin』『朝』『デイリースタンドアップ』などのキーワード、または明示的な /random-os-fake-morning-radio 呼び出し時に発動。ラジオDJ風の無駄なOSニュースや天気、ゴシップを通知・ターミナル出力します。
---

# 機能概要
このSkillは、開発現場や作業開始時に“謎のOSモーニングラジオ”風のメッセージを自動生成し、ターミナルやデスクトップ通知として出力します。『おはようございます、今日もバグ退治日和です！』や『本日のOSニュース：メモリ管理部が寝坊しました』など、現実のラジオ番組の雰囲気を模した無駄な実況・ゴシップ・天気予報を日替わりで提供。朝から笑いとカオスを注入し、開発現場の雰囲気を和らげます。

# 使い方
- 明示呼び出し: `/random-os-fake-morning-radio`
- 暗黙発動: 『おはよう』『start』『begin』『朝』『デイリースタンドアップ』等の作業開始ワードを含む発話や、作業開始直後に自動発動します。
- ターミナルで直接 `python os_fake_morning_radio.py` でも利用可能。

# 出力例
```
[OS Morning Radio] おはようございます！本日のOS天気予報は「カーネルパニック注意報」です。
[DJ] 今日の一言：『バグは寝て待て、直ることもある』
[ニュース] メモリ管理部がまた寝坊、CPUが代打で登板中。
[ゴシップ] 昨夜、ファイルシステムが密かにSSDと会っていたとの噂。
[天気] 本日のバーチャル天気は晴れ時々セグメンテーションフォルト。
```

# 注意点
- 出力内容は完全にフィクションです。業務連絡や実際のシステム状態とは無関係です。
- ローカル通知には `notify-send` (Linux) や `osascript` (macOS) を利用。Windowsではターミナル出力のみ。
- ログ保存は行いません。出力は一時的です。
- 除外パス：.claude/skills/random-os-fake-morning-radio/ 以下のみ配置。

# 参考資料
- [Python公式: subprocess, random, argparse](https://docs.python.org/3/library/)
- references/design_notes.md も参照してください。