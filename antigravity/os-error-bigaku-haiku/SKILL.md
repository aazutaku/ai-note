---
name: os-error-bigaku-haiku
description: ターミナルやシェルでコマンド実行時にOSエラー（例: Permission denied, FileNotFoundError, Segmentation fault等）が発生した場合、そのエラーメッセージを和風俳句に変換・表示する際に発動。エラー検出・エラー内容の俳句化がキーワード。
---

# 機能概要
このSkillは、ターミナルやシェル上でコマンド実行時に発生する各種OSエラー（例：Permission denied、FileNotFoundError、Segmentation faultなど）を検知し、その内容を和風の“エラー俳句”として表示します。無機質なエラーメッセージを文学的な俳句に変換することで、失敗時のストレスや落胆を和らげ、思わず笑ってしまう体験に変えます。日々の開発や運用の中で、エラーを前向きに受け止めるためのユーモアあふれるスキルです。

# 使い方
このSkillは明示的な呼び出しは不要で、コマンド実行時に自動的に発動します。例えば、`ls /root`や`cat nofile.txt`など、エラーが発生する操作を行った際に、俳句化されたエラーメッセージがターミナルに表示されます。暗黙発動キーワード例："Permission denied", "No such file or directory", "Segmentation fault" など。

# 出力例
```
[元エラー] Permission denied: '/root/secret.txt'
[俳句]   Permission denied
          心閉ざして
          春霞

[元エラー] FileNotFoundError: 'nofile.txt' not found
[俳句]   ファイルなし
          探し求めて
          夕暮れ時

[元エラー] Segmentation fault (core dumped)
[俳句]   セグメンテーション
          記憶の彼方
          絶望感
```

# 注意点
- すべてのOSエラーが俳句化されるわけではなく、主要なエラーのみ対応しています。
- 俳句はエラー内容ごとに変化しますが、完全な意味合いの一致を保証するものではありません。
- 俳句生成のためにローカルにエラーログや履歴を保存することはありません。
- 本Skillはジョーク・パロディ用途です。実運用環境での利用は推奨しません。

# 参考資料
詳細はreferences/以下やPython公式の例外ハンドリングドキュメント（https://docs.python.org/3/library/exceptions.html）を参照してください。