---
name: random-os-fake-telepathic-command-alert
description: 作業中やコマンド実行の合間、または明示的な /random-os-fake-telepathic-command-alert 呼び出し時に、OSが“読心術”で検出したかのような架空コマンド通知をランダム表示。通知・演出・OS連携カテゴリ向け。
---

# 機能概要
このSkillは、あなたの作業中やコマンド実行の合間に、OSがまるで“読心術”を身につけたかのようなフェイク通知をランダムに表示します。通知内容は毎回異なり、「あなたが心で考えたコマンドをOSが検出しました：'make coffee'」や「念波キャッチ：'deploy to mars'」など、絶対に実行されない妄想コマンドばかり。これにより、真面目な作業空間に不条理な笑いと現実逃避の余白をもたらします。実際のシステムコマンドやデータには一切触れず、安全性とユーモアを両立しています。

# 使い方
- 明示呼び出し例:
  `/random-os-fake-telepathic-command-alert`
- 暗黙発動キーワード例:
  - "コマンド実行待ち"
  - "作業中断"
  - "集中力低下"
  - "エディタ切替"
Skillはこれらの状況で自動的に発動し、ランダムなテレパシー通知を表示します。

# 出力例
```
[Telepathic OS Alert]
あなたが心の中で考えたコマンドを検出しました: 'brew install happiness'

[Telepathic OS Alert]
念波キャッチ: 'sudo teleport /workspace moon_base'

[Telepathic OS Alert]
OSがあなたの妄想コマンドを感知: 'git push --force-to-parallel-universe'

[Telepathic OS Alert]
読心術発動: 'make coffee'

[Telepathic OS Alert]
未知のコマンドが念波で伝わりました: 'deploy to mars'
```

# 注意点
- 実在のコマンドやデータ、ファイルには一切アクセスしません。
- 通知内容は完全にランダム生成され、実行されることはありません。
- ローカル保存や履歴管理は行いません。
- 本Skillはユーモア・演出目的であり、業務用途には適しません。

# 参考資料
- [references/design_notes.md](references/design_notes.md)
- [Python公式: notifications/OS通知API](https://docs.python.org/3/library/subprocess.html)
- [OS通知の実装例](https://github.com/jithurjacob/Windows-10-Toast-Notifications)