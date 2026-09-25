---
name: pr-comment-ninja-translator
description: Pull Requestのコメントが投稿・編集される際や、/pr-comment-ninja-translator コマンドで明示的に呼び出された場合に発動。キーワード: PRコメント, 忍者口調, ジョーク, 変換, レビュー。
---

# 機能概要
このSkillは、Pull Requestのコメント文を自動で“忍者口調”に変換し、開発現場にユーモアをもたらします。通常のレビューコメントが「拙者思うに…」「ござる」などの忍者ワールドに早変わり。真剣な議論も一瞬で和み、チームの雰囲気が柔らかくなります。エンタメ枠として、日々の開発の息抜きやアイスブレイクに最適です。

# 使い方
- 明示的な呼び出し例：
  `/pr-comment-ninja-translator この変数名は分かりにくいです。`
- 暗黙発動キーワード例：
  PRコメント投稿時に「忍者」「ござる」「拙者」などの単語が含まれる場合、またはSkill設定で自動変換をONにしている場合に自動発動します。

# 出力例
```terminal
> /pr-comment-ninja-translator この関数はバグがあります
拙者申す、この関数、バグの術にござる。修正の巻、お願い仕る。

> /pr-comment-ninja-translator 変数名をもっと分かりやすくしてください
拙者思うに、この変数名、影の如く分かりにくき候。分かりやすき名へと変えるのが良きと存ずる。

> /pr-comment-ninja-translator テストが落ちています
ござる…テスト、落ちてしまったでござる。
```

# 注意点
- 原文の意味を大きく損なわない範囲で忍者口調へ変換しますが、完全な意図伝達は保証されません。
- 機密情報や真面目な議論には適用しないよう注意してください。
- ローカルには変換ログ等は保存しません。
- 既存コメントの編集にも適用可能ですが、元文書のバックアップは自動で取得されません。

# 参考資料
- references/design_notes.md に設計方針や利用例を記載
- 公式GitHub API: https://docs.github.com/en/rest/issues/comments
- 日本語自然言語処理: https://github.com/megagonlabs/ginza
