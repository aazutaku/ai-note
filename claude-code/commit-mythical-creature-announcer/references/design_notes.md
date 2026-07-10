# 概要
このSkillは、コミット作業や明示コマンド実行時に、神話生物（フェニックス・ユニコーン・ドラゴン等）のアスキーアートと理不尽な運勢コメントをランダム表示することで、開発現場にユーモアとカオスをもたらします。

# 公式ドキュメント抜粋
Git公式: https://git-scm.com/
Python argparse: https://docs.python.org/ja/3/library/argparse.html

# 利用例
- `python mythical_announcer.py` で神獣と運勢を表示
- `python mythical_announcer.py list` で神獣リストを参照
- Gitフック(pre-commit)に組み込むことで、毎回コミット時に発動

# 注意点
運勢や神獣は完全ランダムで、実際の開発状況や成果には一切影響しません。履歴保存や外部連携は行いません。

# 設計方針
アスキーアートと運勢コメントは拡張容易な構造で管理。CLIサブコマンドで柔軟に利用可能。Skill本体から直接呼び出される設計です。
