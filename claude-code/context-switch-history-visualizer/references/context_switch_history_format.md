# Context Switch History 出力フォーマット

- 各 context 切替イベントを時系列で表示
- 1行: [時刻] path (滞在分数)
- directory/repository 境界の切替は明示
- 合計切替回数・平均滞在時間も表示
- node_modules, build, dist など無関係なパスは除外
- 機密情報・個人情報は絶対に含めないこと

## 例

[2024-06-10 10:03] /src/api/handlers (12分)
[2024-06-10 10:15] /src/utils (5分)
[2024-06-10 10:20] /docs/ (3分)
[2024-06-10 10:23] /src/api/handlers (7分)
[2024-06-10 10:30] /tests/integration (現在)