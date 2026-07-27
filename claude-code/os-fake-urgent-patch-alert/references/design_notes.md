# 概要
このSkillは、開発現場に“謎の緊張感”と“笑い”をもたらすフェイク通知演出を目的としています。通知内容は完全にフィクションで、実害を与えない設計です。

# 公式ドキュメント抜粋
通知部分はPythonの`plyer.notification`を利用。クロスプラットフォーム対応で、macOS/Linux/Windowsの主要なデスクトップ通知APIをラップしています。詳細: https://plyer.readthedocs.io/en/latest/

# 利用例
- `/os-fake-urgent-patch-alert` で即座に通知
- CLI: `python fake_patch_alert.py log --count 3` で3回連続通知
- `python fake_patch_alert.py list` で履歴確認

# 注意点
- plyer未導入環境ではコンソール出力のみ
- 実際のシステムやファイルには一切影響なし
- ログはプロセス内のみ保持し、永続化なし

# 設計方針
- “意味のない通知”を毎回ランダム生成
- 実在APIのみ利用し、外部システムへの副作用ゼロ
- 履歴・サマリー機能もCLIでサポート