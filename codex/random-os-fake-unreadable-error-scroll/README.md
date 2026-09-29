# random-os-fake-unreadable-error-scroll

> このSkillは、作業中に『謎のOS古代バグ巻物』風の意味不明なエラー通知を、ターミナルやデスクトップ上でランダムにスクロール表示します。trigger: エラー/クラッシュ/バグ報告・/skills menu・$skill-name mention など。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/fake_unreadable_error_scroll.py` - Random OS Fake Unreadable Error Scroll
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-unreadable-error-scroll の詳しい説明](https://ai-note.tech/random-os-fake-unreadable-error-scroll-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-unreadable-error-scroll-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-unreadable-error-scroll .agents/skills/random-os-fake-unreadable-error-scroll
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-unreadable-error-scroll .agents/skills/random-os-fake-unreadable-error-scroll
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
