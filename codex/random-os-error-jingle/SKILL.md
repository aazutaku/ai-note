---
name: random-os-error-jingle
description: コマンド実行時にエラー（例外・非ゼロ終了コード）が発生した場合、必ずランダムな“OSエラージングル”サウンドを再生する。エラー検知・通知・演出用途で発動。
---

# 機能概要
`random-os-error-jingle`は、コマンドやスクリプト実行時にエラー（例外発生や非ゼロ終了コード）を検知すると、即座にランダムな“OSエラージングル”サウンド（WAV/MP3/OGG対応）を再生するSkillです。音源は自作の短いWAVやレトロなファミコン風ファイルなど自由に追加・差し替え可能。エラー発生時の通知・演出を強化し、開発現場や作業空間にユーモラスかつ怪しげな雰囲気を演出します。

# 使い方
- 明示呼び出し例: `/skills random-os-error-jingle run --cmd "python myscript.py" --jingles ./jingles/ --volume 0.8`
- 暗黙発動キーワード例: "エラー発生時にジングル再生", "失敗時に音で通知", "コマンド失敗時のサウンド演出"
- 音源ディレクトリに好きなファイルを追加・交換可能
- `--mute`で一時的にサウンド無効化、`--volume`で音量調整

# 出力例
```
$ python random_os_error_jingle.py run --cmd "ls not_exist_dir" --jingles ./jingles/
[INFO] 実行: ls not_exist_dir
[ERROR] コマンドが失敗しました (終了コード: 2)
[INFO] ジングル再生: ./jingles/famicom_fail.wav
```

# 注意点
- サウンド再生にはOSの標準機能またはPythonの`playsound`/`pygame`を利用
- 音源ファイルはローカルに保存・管理、著作権に注意
- サーバーや無音環境では効果が発揮されません
- コマンド実行はサンドボックス外で行われるため、セキュリティリスクに注意

# 参考資料
- [Python subprocess documentation](https://docs.python.org/ja/3/library/subprocess.html)
- [playsound PyPI](https://pypi.org/project/playsound/)
- references/design_notes.md も参照