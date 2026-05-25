# ai-note

[ai-note.tech](https://ai-note.tech) が毎朝 5:00 JST に1ネタずつ提案している、AI Coding Agent 向け Skill のカタログリポジトリです。Claude Code / Codex / Antigravity の3製品向けに、エンタメ寄りの Skill (commit時に猫が鳴く、ファイル名で相性占い 等) を中心に並んでいきます。

> このリポジトリの Skill は ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。

## このリポジトリは何

ai-note.tech の n8n ワークフローが、毎朝 5:00 JST に「今日の Skill ネタ」を AI に提案させて、Claude Code / Codex / Antigravity 各製品向けに3バリエーション展開し、ここに自動 commit しています。

媒体方針: **エンタメ:実用 = 8:2**。8割は「これ作るやつ正気か?」みたいな遊びネタ、2割が真面目なワークフロー Skill です。

サイト側 (ai-note.tech) には Skill ごとに2記事が連動しています:

- **スキル詳細説明**: 「Skills ラボ」カテゴリの記事
- **動作手順**: 「AI実験ログ」カテゴリの記事 (著者が実際に動かしてレビューした記録)

## 構成

```
ai-note/
├── README.md
├── claude-code/
│   └── <skill-name>/
│       ├── README.md
│       ├── SKILL.md
│       ├── scripts/
│       └── references/
├── codex/
│   └── <skill-name>/
└── antigravity/
    └── <skill-name>/
```

各 Skill フォルダは独立パッケージ。フォルダ内の README.md に詳細・関連記事リンクがまとまっています。

## 使い方

degit でフォルダ単位で取れます。

```bash
# Claude Code の場合
npx degit aazutaku/ai-note/claude-code/<skill-name> ~/.claude/skills/<skill-name>

# Codex の場合 (.agents は複数形)
npx degit aazutaku/ai-note/codex/<skill-name> ~/.agents/skills/<skill-name>

# Antigravity の場合 (.agent は単数形)
npx degit aazutaku/ai-note/antigravity/<skill-name> ~/.gemini/antigravity/skills/<skill-name>
```

Codex (`.agents`) と Antigravity (`.agent`) の単複違いにご注意。混同すると Skill が認識されません。

## 配置パスまとめ

| 製品 | プロジェクト単位 | グローバル |
|---|---|---|
| Claude Code | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` |
| Codex | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` |
| Antigravity | `.agent/skills/<name>/` | `~/.gemini/antigravity/skills/<name>/` |

公式仕様:

- [Claude Code Skills](https://code.claude.com/docs/ja/skills)
- [Codex Skills](https://developers.openai.com/codex/skills)
- [Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills)

## 自動生成について

このリポジトリのコミットは、ai-note.tech の n8n ワークフローによる自動 push です。

- 毎朝 5:00 JST に発火
- 1ネタを Claude Code / Codex / Antigravity の3製品分に展開 (最大3 Skill / 日)
- Git Trees API で1コミットにまとめて push
- 過去30件と被らないように AI が考慮 (完全一致回避は無し、似た方向の被りはあり得る)

## 関連

- サイト: [ai-note.tech](https://ai-note.tech)
- 著者: [@aazutaku](https://github.com/aazutaku)

## 注意

このリポジトリの Skill は ai-note.tech が提供するサンプルで、動作保証はありません。再配布・改変・商用利用は自由ですが、利用は自己責任でお願いします。
