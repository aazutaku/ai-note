# random-desktop-fake-os-memo

> 作業中や定期的なタイミングで、Codexがユーザーのデスクトップに意味不明な“謎OSメモ”を通知する際に発動。通知・演出・OS連携カテゴリのタスクや、/skills menuやrandom-desktop-fake-os-memoの明示呼び出し時も対応。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_desktop_fake_os_memo.py` - 謎のOSメモをデスクトップ通知で表示するスキル (random-desktop-fake-os-memo)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-desktop-fake-os-memo の詳しい説明](https://ai-note.tech/random-desktop-fake-os-memo-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-desktop-fake-os-memo-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-desktop-fake-os-memo .agents/skills/random-desktop-fake-os-memo
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-desktop-fake-os-memo .agents/skills/random-desktop-fake-os-memo
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
