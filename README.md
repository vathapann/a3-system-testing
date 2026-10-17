# Assignment 3: System Testing (32571 Enterprise Software Testing)

Automated system tests for https://ecommerce-playground.lambdatest.io
using **Python + Behave (BDD/Gherkin) + Selenium WebDriver**.

## Who tested what

| Function | Name | Tester | Feature file |
|---|---|---|---|
| F1 | User Registration | Sovatha Pann | `features/f1_register.feature` |
| F2 | User Login | Sovatha Pann | `features/f2_login.feature` |
| F3 | Forgotten Password | Sovatha Pann | `features/f3_forgotten_password.feature` |
| F4 | Product Search | Tiwat Thiplakha | `features/f4_search.feature` |
| F5 | Wishlist | Tiwat Thiplakha | `features/f5_wishlist.feature` |
| F6 | Product Compare | Tiwat Thiplakha | `features/f6_compare.feature` |
| F7 | Shopping Cart | Yiyang Chen | `features/f7_cart.feature` |
| F8 | Checkout | Yiyang Chen | `features/f8_checkout.feature` |
| F9 | Contact Us | Yiyang Chen | `features/f9_contact.feature` |

Step definitions: `features/steps/fN_<name>_steps.py`. Shared steps: `features/steps/common_steps.py`.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Google Chrome must be installed. Selenium Manager downloads ChromeDriver automatically.

## Run

```bash
behave                                   # all tests
behave features/f2_login.feature         # one function
behave --format plain features/          # simpler output for screenshots
```

Screenshots of each scenario are saved to `screenshots/`.

## Rules for the team

1. Work on your own branch (`member-a`, `member-b`, `member-c`) and open a pull request.
2. Only edit your own feature and step files. Changes to `helper/`, `environment.py`
   or `common_steps.py` need a quick message to the group first.
3. Never reuse a fixed email for registration; use `unique_email()`.
