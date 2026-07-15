# 概要
random-desktop-fake-os-memoは、ユーザーの作業環境に突発的な“謎のOSメモ”を通知することで、意図的な違和感や遊び心を演出するスキルです。集中しすぎた作業の合間や、単調なデスクトップにシュールな刺激を与えることを目的としています。

# 公式ドキュメント抜粋
- Linux: Freedesktop.org Notification Spec (https://specifications.freedesktop.org/notification-spec/latest/)
- Windows: win10toast (https://pypi.org/project/win10toast/)
- macOS: pync (https://pync.readthedocs.io/en/latest/)

# 利用例
- 長時間のコーディング時に、定期的に意味不明な通知が表示されることでリフレッシュ効果を狙う
- チームのデモや社内イベントで、デスクトップに混乱や笑いを起こす演出

# 注意点
- 通知内容は完全にランダムかつ非実用的であり、業務連絡などには一切利用できません
- 通知APIの仕様や環境依存で、通知が表示されない場合があります

# 設計方針
- 既存の通知APIのみを利用し、OSごとに最適な方法で通知を実装
- メモ内容はハードコーディングし、怪文書感を重視
- ログや履歴保存は行わず、あくまで“その瞬間”の演出に特化