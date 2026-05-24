# prompt-branch-suggester

> 作業ブランチ名やコミットメッセージ、直前のファイル差分などのキーワードを検出した際に、Antigravityが最適な指示ファイルやプロンプト分岐案を自動生成・提案するSkillです。semantic-match-only条件で発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/prompt_branch_suggester.py` - 実行スクリプト
- `references/design_notes.md` - 参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け prompt-branch-suggester の詳しい説明](https://ai-note.tech/prompt-branch-suggester-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/prompt-branch-suggester-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/prompt-branch-suggester .agent/skills/prompt-branch-suggester
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/prompt-branch-suggester .agent/skills/prompt-branch-suggester
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
