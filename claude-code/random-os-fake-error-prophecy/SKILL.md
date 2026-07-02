---
name: random-os-fake-error-prophecy
description: このSkillは、Claude Codeでターミナル操作やエディタコマンド実行時などの作業フロー中に、ランダムな“未来予言型OSエラーメッセージ”を表示します。triggerType: always/semantic-or-explicit。明示コマンド /random-os-fake-error-prophecy でも発動。
---

# 機能概要
`random-os-fake-error-prophecy`は、作業中に突如として“未来を予言するOS風エラーメッセージ”をランダム表示するSkillです。実用性はありませんが、日々のコーディング作業に絶妙な不安や笑いをもたらし、マンネリ化した作業リズムをリセットします。表示されるメッセージは「明日3回pushに失敗します」「警告: 来週GitHubが逆行します」など、根拠のない予言ばかり。実際のエラーと混同しない演出で、作業の邪魔にならない頻度・タイミングで発動します。

# 使い方
- 明示的な呼び出し: `/random-os-fake-error-prophecy` コマンドを実行
- 暗黙発動: ターミナルやエディタで`git push`、`npm install`、`code`、`make`などのコマンド実行時や、ファイル保存・ビルド・デバッグなどの操作時に自動発動

# 出力例
```
エラー: 明日あなたは3回pushに失敗します
警告: 来週GitHubが逆行します
注意: コードレビューで哲学的質問を受けます
予言: 2日後にnpm installが謎の失敗をします
警告: あなたのエディタが突然詩的になります
```

# 注意点
- 本Skillは実際のエラー通知ではありません。内容は完全なフィクションです。
- メッセージはランダム生成され、実際の作業やリポジトリには影響しません。
- ローカルに履歴や個人情報は保存しません。
- 頻度や内容はカスタマイズ可能です。

# 参考資料
- references/design_notes.md を参照
- 公式Python randomモジュール: https://docs.python.org/3/library/random.html
