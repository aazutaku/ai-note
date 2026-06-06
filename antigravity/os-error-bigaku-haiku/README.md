# os-error-bigaku-haiku

> ターミナルやシェルでコマンド実行時にOSエラー（例: Permission denied, FileNotFoundError, Segmentation fault等）が発生した場合、そのエラーメッセージを和風俳句に変換・表示する際に発動。エラー検出・エラー内容の俳句化がキーワード。

このSkillは [ai-note.tech](https://ai-note.tech) の Skill 提案媒体で設計され、**Antigravity** 向けに最適化したものです。

## ファイル構成

- `SKILL.md` - Skill本体 (frontmatter + 指示)
- `scripts/os_error_bigaku_haiku.py` - エラーメッセージから主要なエラータイプを抽出
- `references/reference.md` - 概要 をまとめた参考資料

## 関連記事

- スキル詳細説明: [Antigravity 向け os-error-bigaku-haiku の詳しい説明](https://ai-note.tech/os-error-bigaku-haiku-antigravity/)
- 動作手順: [Antigravity で実際に動かす手順と検証](https://ai-note.tech/os-error-bigaku-haiku-antigravity-log/) (公開準備中の場合あり)

## 配置方法

degit で一発:

```bash
npx degit aazutaku/ai-note/antigravity/os-error-bigaku-haiku .agent/skills/os-error-bigaku-haiku
```

または git clone してコピー:

```bash
git clone --depth 1 https://github.com/aazutaku/ai-note.git
cp -r ai-note/antigravity/os-error-bigaku-haiku .agent/skills/os-error-bigaku-haiku
```

配置後、Antigravity を再起動するか自動検出を待つと利用できるようになります。

## 公式ドキュメント

- Antigravity: https://codelabs.developers.google.com/getting-started-with-antigravity-skills

## 注意

このSkillは ai-note.tech が提供するサンプルで、動作保証はありません。各自の環境で検証の上、ご利用ください。
