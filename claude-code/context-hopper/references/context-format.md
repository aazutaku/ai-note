# context-hopper context format

## 保存する内容
- directory: 対象ディレクトリのパス
- task: 進行中のタスク名・概要
- issues: 現在の課題・未解決トピック（配列）
- important_files: 注目すべきファイルリスト
- notes: 補足メモ・進捗

## 保存形式
- JSON (UTF-8, indent=2)
- context/[context_name].json で保存

## 利用例
{
  "directory": "./src/features/auth/",
  "task": "ログイン機能のバリデーション追加",
  "issues": ["email フォーマットのチェック実装中"],
  "important_files": ["validate.ts", "AuthForm.tsx"],
  "notes": "バリデーションエラー時のUI反映を未対応"
}