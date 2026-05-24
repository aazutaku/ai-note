# 概要
prompt-branch-suggesterは、作業ブランチやコミット内容・diffをもとに、AIエージェント向けの指示ファイル分岐案や一時的プロンプトセットを自動生成するSkillです。編集者の手間を省き、作業内容に即した指示を迅速に得ることを目的としています。

# 公式ドキュメント抜粋
- [GitPython](https://gitpython.readthedocs.io/): Pythonからgitリポジトリ情報を安全に取得。
- [OpenAI Codex](https://platform.openai.com/docs/guides/code): 指示ファイル設計やプロンプト分岐のベストプラクティス。

# 利用例
feature/add-loginブランチで大きなdiffが発生した際、`/skills prompt-branch-suggester suggest`を実行すると、login機能向けの指示ファイル分岐や一時的なプロンプト案が提案されます。

# 注意点
- 既存指示ファイルは上書きせず、分岐ファイルや一時ファイルとして保存。
- 巨大なdiffや曖昧なブランチ名の場合、一般的な提案となる場合があります。

# 設計方針
安全性と拡張性を重視し、git情報の取得・ファイル保存時の競合回避・既存ファイル保護を徹底しています。