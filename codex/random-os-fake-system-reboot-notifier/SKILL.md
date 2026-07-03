---
name: random-os-fake-system-reboot-notifier
description: 作業中や集中タイム、または『再起動』『OS』『通知』などのキーワードが会話やコマンドに含まれる場合、または/skillsメニューやrandom-os-fake-system-reboot-notifierの明示呼び出し時に発動します。唐突なシステム再起動予告を演出します。
---

# 機能概要
このSkillは、ユーザーの作業中に突然“謎のOSシステム再起動予告”をデスクトップ通知として表示します。『5分後にシステムは謎の理由で再起動します』や『理由：カーネルの気まぐれ』など、内容は毎回ランダム生成され、実際には何も起きません。チーム内の雰囲気を一瞬ピリッとさせつつ、即座にネタだと分かる脱力系通知で、オフィスやリモートワークの話題作り・アイスブレイクに最適です。

# 使い方
- 明示呼び出し: `/skills random-os-fake-system-reboot-notifier` または `$random-os-fake-system-reboot-notifier`
- 暗黙発動: 「再起動」「OS」「システム通知」「shutdown」などのキーワードを含む会話やコマンド時に自動発動

# 出力例
```
[通知] 重要なお知らせ: 5分後にシステムは謎の理由で再起動します。
理由: カーネルの気まぐれ

[通知] システムメンテナンス: 3分後に全プロセスが一時停止されます。
理由: メモリの気分転換

[通知] OSアップデート: 10分後に再起動が予定されています。
理由: 不明なエラーコード 0xDEADBEEF
```

# 注意点
- 通知はユーザーのローカル環境にのみ表示され、実際の再起動やシステム操作は一切行いません。
- 通知内容は毎回ランダムに生成されます。
- ログや履歴はローカルには保存されません。
- Linux/macOS/Windowsの主要デスクトップ通知APIに対応していますが、仮想環境や一部リモート環境では通知が表示されない場合があります。

# 参考資料
- references/design_notes.md に設計方針・API選定理由を記載
- 公式: [Python plyer通知API](https://plyer.readthedocs.io/en/latest/)
- [Windows Toast通知](https://learn.microsoft.com/en-us/windows/uwp/design/shell/tiles-and-notifications/)
- [Linux notify-send](https://specifications.freedesktop.org/notification-spec/)