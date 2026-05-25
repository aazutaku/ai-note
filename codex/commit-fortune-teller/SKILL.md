---
name: commit-fortune-teller
description: コミット時や/skills menu、commit-fortune-tellerの明示呼び出し時に発動。commit、push、fortune、運勢、占い、タロット等のキーワードやgit操作直後に反応。
---

# 機能概要
commit-fortune-tellerは、Gitコミットのたびにターミナルへランダムな“タロット風占い結果”を表示するジョーク系Skillです。作業の緊張感や重苦しさを和らげ、エンジニアの運命をコードではなく運に委ねるカオスな世界観を提供します。実用性はありませんが、日々の開発に笑いや話題をもたらします。

# 使い方
- 明示呼び出し例: `/skills menu` で選択、または `commit-fortune-teller` を直接指定
- 暗黙発動キーワード例: `commit`, `push`, `fortune`, `運勢`, `占い`, `タロット`, `git` などの操作直後

# 出力例
```
=== Commit Fortune Teller ===
今日の運勢: 大吉
このコミットは「太陽」…成功と喜びの暗示！
アドバイス: 迷わず進め、道は開かれる。
-----------------------------

=== Commit Fortune Teller ===
今日の運勢: 凶
このコミットは「塔」…思わぬバグに注意！
アドバイス: テストを怠るべからず。
-----------------------------
```

# 注意点
- 本SkillはGit操作の直後にのみ発動し、実際のコミット内容や履歴には影響しません。
- 出力は完全にランダムで、実際の運勢や成果とは無関係です。
- ローカル環境にログ等は保存されません。
- ジョーク用途のため、業務利用や真剣な判断には不向きです。

# 参考資料
- [Python random — 公式ドキュメント](https://docs.python.org/ja/3/library/random.html)
- references/design_notes.md も参照