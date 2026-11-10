# Equipe 5 — Validação de pagamento de benefício

## Organização

- `modelos.py`: enumeração de entidades pagadoras e dados de atestados.
- `blockchain.py`: interface de consulta e simulação da blockchain.
- `pagamento.py`: validação da regra de negócio.
- `main.py`: demonstração com cinco cenários.
- `test_pagamento.py`: testes automatizados da regra de negócio.

## Execução

Requer Python 3.9 ou superior. No terminal, dentro da pasta do projeto:

```bash
python main.py
```

## Testes

Os testes utilizam apenas a biblioteca padrão do Python:

```bash
python -m unittest -v test_pagamento
```
