# Task -16 World Population Clock (pytest + Selenium + POM)

## Overview
Automates extraction of live population from:
https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live

## Features
- Page Object Model (POM)
- Explicit Wait + Expected Conditions
- XPath locators only
- Continuous extraction until CTRL+C
- pytest-html reporting

## Setup
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Run tests
```bash
pytest
```
Generates `report.html`.
