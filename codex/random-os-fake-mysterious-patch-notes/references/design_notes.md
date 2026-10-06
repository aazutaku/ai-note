# 概要
このSkillは、開発現場での“OSアップデート通知”の演出をパロディ化し、現実には存在しない機能や不可解なバグ修正をユーモラスに通知します。ユーザーの集中を一瞬だけ和らげ、チーム内の話題や気分転換に役立ちます。

# 公式ドキュメント抜粋
実在するOSのパッチノート例: [Windows Release Notes](https://learn.microsoft.com/en-us/windows/release-health/release-information/)、[macOS Release Notes](https://support.apple.com/en-us/HT201222)。

# 利用例
- ビルド完了時やコマンド実行後に自動発動
- `/skills random-os-fake-mysterious-patch-notes` で明示呼び出し
- チーム内で「今日の謎パッチノート」を共有

# 注意点
- 通知内容は現実のOSやプロジェクトとは無関係です。
- 履歴はユーザーホームの `~/.random_os_patch_notes_history` に保存されます。
- 履歴が不要な場合はファイルを削除してください。

# 設計方針
- 毎回異なる内容をランダム生成
- 実在しない機能・バグ修正を必ず混在
- CLIで履歴参照やサマリー表示が可能
- シンプルな構造で他Skillとの連携や拡張も容易