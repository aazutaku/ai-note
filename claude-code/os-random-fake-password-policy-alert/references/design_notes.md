# 概要
このSkillは、現場の緊張感を和らげるために、実際には存在しない理不尽なパスワードポリシー通知をランダムに表示するジョーク系ツールです。OSの設定やパスワード管理には一切影響しません。

# 公式ドキュメント抜粋
- Python subprocess: https://docs.python.org/3/library/subprocess.html
- Python random: https://docs.python.org/3/library/random.html
- Python argparse: https://docs.python.org/3/library/argparse.html

# 利用例
- チームのアイスブレイクや朝会のネタに
- セキュリティ研修の冒頭で緊張をほぐす小ネタとして
- CLIやデスクトップ通知の演出テスト用

# 注意点
- 実際のパスワードやセキュリティ設定には一切影響を与えません
- 通知内容は完全なジョークであり、業務には利用できません
- 通知履歴はユーザーホーム配下にのみ保存されます

# 設計方針
- クロスプラットフォームで動作する通知APIを選定
- 通知内容は日本語でバリエーション豊富に用意
- CLIサブコマンドで履歴管理やサマリー出力も可能に