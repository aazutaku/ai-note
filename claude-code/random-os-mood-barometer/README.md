# random-os-mood-barometer

> ターミナルやエディタでコマンド実行時、または /random-os-mood-barometer 明示呼び出し時に、画面端やメニューバー風の“謎のOS気分バロメーター”をランダム表示します。生産性や気分の根拠なき演出で、作業体験をカオスに彩ります。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Claude Code** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/mood_barometer.py` - 謎のOS風気分バロメーター
- `references/design_notes.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Claude Code 向け random-os-mood-barometer の詳しい説明](https://ai-note.tech/random-os-mood-barometer-claude-code/)
- 動作手順: [Claude Code で実際に動かす手順と検証](https://ai-note.tech/random-os-mood-barometer-claude-code-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/claude-code/random-os-mood-barometer .claude/skills/random-os-mood-barometer
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/claude-code/random-os-mood-barometer .claude/skills/random-os-mood-barometer
```

配置後、Claude Code を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Claude Code: https://code.claude.com/docs/ja/skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
