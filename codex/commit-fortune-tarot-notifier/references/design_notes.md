# 概要
commit-fortune-tarot-notifierは、Gitのコミット時に完全ランダムなタロットカード風メッセージを通知するジョークSkillです。開発現場の雰囲気を和ませるため、実用性よりも演出とネタ性を重視しています。

# 公式ドキュメント抜粋
- [subprocess — サブプロセス管理 — Python公式](https://docs.python.org/ja/3/library/subprocess.html)
- [Git Hooks — git-scm.com](https://git-scm.com/docs/githooks)

# 利用例
- チーム開発でコミットごとにタロット通知が流れることで、会話のきっかけやリラックス効果を期待
- 個人開発でも「今日はどんな運勢？」と気分転換に活用可能

# 注意点
- 通知内容は完全にランダムで、実際のコード品質や進捗とは無関係です
- デスクトップ通知はOS依存（Linux: notify-send, macOS: osascript, Windows: win10toast）
- 通知履歴は保存されません

# 設計方針
- Git commit時のフックや明示呼び出しの両方に対応
- 過度な作業阻害を避けるため、通知は1行・即時のみ
- 拡張性を考慮し、タロットメッセージは配列で管理