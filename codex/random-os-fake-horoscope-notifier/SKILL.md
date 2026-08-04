---
name: random-os-fake-horoscope-notifier
description: 作業開始や/skills menuコマンド、random-os-fake-horoscope-notifierへの明示呼び出し時など、セッション開始・ターミナル起動・新規作業開始などのキーワードを検知した際に発動します。1日1回、ランダムな“OS風星占い”通知を表示します。
---

# 機能概要
このSkillは、開発者の作業開始やセッション起動時に、完全ランダムな“OS星占い”通知をデスクトップまたはターミナルへ1日1回表示します。内容は「今日のラッキーコマンドはls」や「運勢：バグ回避率上昇」など、根拠のない占い風アドバイスで、開発のスタートをユーモラスに演出します。日々のコーディングにちょっとした遊び心を加え、気分転換やチームの会話のきっかけにもなります。

# 使い方
- 明示呼び出し例：
  - `/skills menu` から `random-os-fake-horoscope-notifier` を選択
  - `$ random-os-fake-horoscope-notifier notify`
- 暗黙発動キーワード例：
  - 「作業開始」「新規ターミナル」「start coding」などのセッション開始時
  - Codexが「今日もよろしく」「build start」などを検知した場合

# 出力例
```
=== OS Horoscope Notifier ===
運勢: 今日は「ls」コマンドが幸運を呼びます。
バグ回避率が12%上昇。
注意: 仕様変更星が逆行中。こまめなgit commit推奨。
ラッキーアイテム: マグカップ
===========================
```

# 注意点
- 通知は1日1回のみ表示されます（ローカルに記録）
- 内容は完全ランダムで、実際の運勢や開発結果には影響しません
- デスクトップ通知はLinux/macOSのみ対応（notify-sendまたはosascript利用）
- ローカル環境のみに保存され、クラウド連携や個人情報送信はありません

# 参考資料
- references/design_notes.md
- https://docs.python.org/ja/3/library/random.html
- https://wiki.archlinux.jp/index.php/Desktop_notifications