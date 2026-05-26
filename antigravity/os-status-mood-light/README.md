# os-status-mood-light

> 作業者の気分やコンディションを環境変数MOODやOSステータスバー、シェルプロンプト、Slack連携などで可視化したい場合に発動。環境変数変更や気分通知、日替わりネタ表示などのキーワードがトリガー。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_status_mood_light.py` - os-status-mood-light: 気分可視化スキル
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-status-mood-light の詳しい説明](https://ai-note.tech/os-status-mood-light-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-status-mood-light-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-status-mood-light .agent/skills/os-status-mood-light
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-status-mood-light .agent/skills/os-status-mood-light
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
