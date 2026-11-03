# Lab 3 — CI/CD (Variant 2)

Простий калькулятор + GitHub Actions пайплайн з двома **паралельними** кроками:

1. **test** — запуск pytest
2. **lint** — перевірка стилю коду через Black

## Запуск локально

```bash
pip install -r requirements.txt
pytest -v
black --check .
```

## Автор

Касько Богдан Русланович, ІПЗ-26-1м
