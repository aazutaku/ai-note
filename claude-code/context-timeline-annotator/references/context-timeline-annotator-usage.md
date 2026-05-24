# context-timeline-annotator Skill の使い方

## できること

- Claude Code の session 履歴や編集ログを時系列で一覧化し、各編集ステップに短い意図コメントを自動付与
- monorepo の複数 package を跨いだ作業履歴も directory ごとに整理
- onboarding や session 再開時に、過去の流れや decision の経緯を一目で把握

## 使い方

1. `.claude/skills/context-timeline-annotator/` 配下に Skill 一式を設置
2. Claude Code のチャットで `/context-timeline-annotator` を入力
3. 直近の履歴が時系列で注釈付きで表示される

## 出力例

[2024-06-14 13:02]  /packages/core/index.ts 編集  # API追加
[2024-06-14 13:10]  /packages/utils/helpers.ts 変更  # 共通関数を修正
[2024-06-14 13:15]  /packages/web/src/App.tsx 編集  # UIコンポーネント追加

## 注意点

- 履歴の改変・削除は一切行わない
- directory 増加や長時間 session では出力が多くなる場合あり