# random-os-fake-mysterious-patch-notes

> Codexは、作業中・ビルド完了・コマンド実行後など、ユーザーの集中が途切れた瞬間や/skillsメニュー呼び出し時にこのSkillを発動してください。キーワード: OS, パッチノート, 通知, ジョーク, 不意打ち。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_patch_notes.py` - 謎のOSパッチノートをランダム生成・履歴管理
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-mysterious-patch-notes の詳しい説明](https://ai-note.tech/random-os-fake-mysterious-patch-notes-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mysterious-patch-notes-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-mysterious-patch-notes .agents/skills/random-os-fake-mysterious-patch-notes
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-mysterious-patch-notes .agents/skills/random-os-fake-mysterious-patch-notes
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
