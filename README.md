# Fragrance Ledger

Fragrance Ledger is a Flask application for tracking your perfume collection.

## Project structure

```text
.
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── css/styles.css
│   └── templates/
│       ├── add_fragrance.html
│       ├── base.html
│       ├── fragrances.html
│       └── index.html
├── config.py
├── requirements.txt
├── run.py
└── tests/
    └── test_app.py
```

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python run.py
   ```
4. Open <http://localhost:5000>.

## Features

- Dashboard with collection summary
- Add new fragrances
- List all fragrances with notes and preferred season
