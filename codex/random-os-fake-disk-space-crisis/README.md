# random-os-fake-disk-space-crisis

> このSkillは、ターミナルやデスクトップ作業中に“ディスク残量危機”を装った現実離れしたジョーク通知をランダム生成し表示します。明示呼び出し（/skills menuやskill名メンション）や、disk/disk space/容量/空き/警告/残量/危機/alert/alert disk などのキーワード検出時に発動します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Codex** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_disk_space_crisis.py` - random-os-fake-disk-space-crisis: フェイクなディスク残量危機通知を炸裂させるジョークSkill
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Codex 向け random-os-fake-disk-space-crisis の詳しい説明](https://ai-note.tech/random-os-fake-disk-space-crisis-codex/)
- 動作手順: [Codex で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-disk-space-crisis-codex-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/codex/random-os-fake-disk-space-crisis .agents/skills/random-os-fake-disk-space-crisis
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/codex/random-os-fake-disk-space-crisis .agents/skills/random-os-fake-disk-space-crisis
```

配置後、Codex を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Codex: https://developers.openai.com/codex/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
