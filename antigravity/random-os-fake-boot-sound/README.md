# random-os-fake-boot-sound

> ターミナルやエディタの起動時、または作業開始時などのセッション開始イベント（例: terminal open, editor launch, workspace attach）で自動的に発動し、毎回異なるランダムなサウンドを再生して疑似的な“OS起動音”を演出します。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/random_os_fake_boot_sound.py` - random-os-fake-boot-sound: ランダムなOS起動音を再生するスクリプト
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け random-os-fake-boot-sound の詳しい説明](https://ai-note.tech/random-os-fake-boot-sound-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/random-os-fake-boot-sound-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/random-os-fake-boot-sound .agent/skills/random-os-fake-boot-sound
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/random-os-fake-boot-sound .agent/skills/random-os-fake-boot-sound
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
