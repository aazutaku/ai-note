# random-os-fake-mascot-parade

> 作業中やコマンド実行時など、Antigravityがユーザーの集中や手が空いたタイミングを検知した際に、ランダムな“謎のOSマスコット”によるデスクトップ通知を発生させる。通知内容・キャラ名・セリフは毎回完全ランダム生成され、主に『応援』『警告』『意味不明な助言』などが含まれる。triggerType: always, semantic-match-only。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mascot_parade.py` - 謎のOSマスコット大行進 (通知ジョークSkill)
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-mascot-parade の詳しい説明](https://ai-note.tech/random-os-fake-mascot-parade-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-mascot-parade-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-mascot-parade .agent/skills/random-os-fake-mascot-parade
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-mascot-parade .agent/skills/random-os-fake-mascot-parade
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
