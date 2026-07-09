---
name: os-command-drumroll-alert
description: git push、rm、npm publish などの重大コマンドを実行する直前に、Antigravity が自動でドラムロール音とOS通知を発動。コマンド実行前の緊張感を演出し、操作ミスや事故を防止するための演出系スキル。trigger: semantic-match-only。
---

# 機能概要
このSkillは、エンジニアがターミナルやエディタで重大なコマンド（例: `git push`, `rm`, `npm publish` など）を実行しようとした際、直前に“OS風ドラムロール”サウンドを鳴らし、さらにデスクトップ通知で「運命の選択が迫る！」「本当に実行しますか？」などの演出メッセージを表示します。普段の作業フローに緊張感とユーモアを加え、重大操作の前に注意を促すことで、ミスの抑止や気分転換にも役立ちます。

# 使い方
このSkillは明示的な呼び出しを必要とせず、`git push`, `rm -rf`, `npm publish`, `docker system prune` などのコマンドを実行しようとした際に自動発動します。Antigravityがコマンド内容をセマンティックに解析し、該当する場合にのみ演出を挿入します。

## 暗黙発動キーワード例
- git push
- rm -rf
- npm publish
- docker system prune
- systemctl restart

# 出力例
```
[ドラムロール音が鳴る]
[デスクトップ通知] 運命の選択が迫る！本当に git push を実行しますか？
[ターミナル出力] Drumroll... Are you sure you want to proceed with 'rm -rf ./build'?
[選択肢] Yes / No
```

# 注意点
- サウンド再生・通知機能はOS依存（Linux: notify-send, aplay / macOS: osascript, afplay / Windows: powershell通知）
- コマンド実行の遅延や割り込みを最小限に抑えますが、演出が不要な場合はSkillを無効化してください
- 通知・サウンドは複数パターンをランダム表示
- ローカル環境に一時的なサウンドファイルを保存します

# 参考資料
- [Python: subprocess, os, random, platform, plyer, playsound](https://docs.python.org/3/library/)
- references/design_notes.md を参照