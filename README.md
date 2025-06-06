# Unifize Discount Service

This project implements a modular discount calculation system for an e-commerce platform, supporting brand, category, bank, and voucher-based offers.

---

## 🚀 Features

* Modular service for brand & category discounts
* Bank-specific discount service
* Voucher code validation logic
* Clean interface via `DiscountService`

---

## 🧱 Project Structure

```
unifize-discount-service/
├── README.md
├── pyproject.toml
├── poetry.lock
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── fake_data.py
│   └── service/
│       ├── __init__.py
│       └── discount_service.py
├── tests/
│   ├── __init__.py
│   └── test_discount_service.py
```

---

## ⚙️ Setup Instructions

### Prerequisites

* Python 3.10+
* Poetry

### Installation

```bash
git clone <your-repo-url>
cd unifize-discount-service
poetry install
```

### Run the App

```bash
poetry run python src/main.py
```

### Run Tests

```bash
PYTHONPATH=src poetry run pytest
```

---

## 🔍 Assumptions

* Discounts apply in this order: brand → category → voucher → bank
* `SUPER69` is only valid on non-premium brands
* Dummy scenario involves a single PUMA T-shirt with stacked offers

---

## 📦 Example Scenario

* **Product**: PUMA T-shirt
* **Brand Discount**: 40%
* **Category Discount**: 10%
* **Bank Offer**: 10% via ICICI card
* **Expected Price**: ₹486 from ₹1000 base

---

## 🛠 Tech Stack

* Python 3.10+
* Poetry
* Pytest
* `decimal.Decimal` for money-safe math

---

## 📩 Contributing

For suggestions or bugs, feel free to raise an issue or pull request.

---

