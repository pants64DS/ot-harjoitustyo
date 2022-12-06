# Arkkitehtuurikuvaus

## Luokkarakenne

```mermaid
classDiagram
UI "1" -- "1" Table
Table "1" -- "*" Row
Table "1" -- "*" Column
Column "1" -- "0..1" SettingsWindow
SettingsWindow "1" -- "0..1" FloatingPointSettings

Row ..> Column
Column ..> Row
Column ..> Evaluator
Row ..> Evaluator
Table ..> Evaluator
```

## Toiminnallisuus

### Lausekkeen arvon laskeminen
Sekvenssikaavio tilaanteesta, jossa käyttäjä muuttaa lauseketta tekstikentässä, kun taulukossa on yksi rivi ja yksi sarake, joka käyttää 32-bittisiä liukulukuja:
```mermaid
sequenceDiagram
    actor Käyttäjä
    Käyttäjä ->> Row: muuttaa lausekkeen muotoon "1 + 2"
    activate Row
    Row ->> Row: get_expr()
    Row ->> Column: get_evaluator()
    activate Column
    Column ->> Evaluator: Evaluator(numpy.float32)
    Column -->> Row: Evaluator
    deactivate Column
    Row ->> Evaluator: evaluate_to_string('1 + 2')
    activate Evaluator
    Evaluator ->> Evaluator: evaluate('1 + 2')
    Evaluator -->> Row: '3'
    deactivate Evaluator
    Row -->> Käyttäjä: taulukon solussa näkyy luku 3
    deactivate Row
```
