# Arkkitehtuurikuvaus

## Luokkarakenne

```mermaid
classDiagram
UI "1" -- "1" Table
Table "1" -- "*" Column
Table "1" -- "*" Row
Row ..> Column
Column ..> Row
Column ..> Evaluator
```
