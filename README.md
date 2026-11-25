# OrangeHRM Demo - QA Project

Manual and automated testing of **OrangeHRM** (https://opensource-demo.orangehrmlive.com), a public practice site.

## What's inside
| Folder | Content |
|---|---|
| `docs/test-plan.md` | Scope, approach, environment, risks, schedule |
| `docs/test-summary-report.md` | Results report (fill in after execution) |
| `manual/orangehrm-test-cases.xlsx` | 37 test cases, bug reports, auto-calculated summary |
| `automation/` | Playwright (Python) + pytest, 19 automated tests |
| `.github/workflows/` | GitHub Actions workflow (manual trigger) |

## Tools
Excel / Google Sheets, Chrome DevTools, Playwright (Python), pytest, GitHub Actions.

## Run the automated tests
```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env              # optional, defaults already work
pytest --headed                   # remove --headed for a faster run
```
Screenshots of failed tests are saved to `test-results/`.

The tests use the demo admin login that OrangeHRM publishes on its own login page (Admin / admin123). The demo is shared and resets regularly, so tests only create new records and never edit existing ones.

## Results
- Manual: 37 test cases written, `<N>` executed, `<P>` passed, `<F>` failed
- Defects logged: `<D>` (see the Bug Reports sheet)
- Automation: 19 tests, `<X>` passing

## Notes
This is a public practice site. Tests only use normal user flows, with no load or security testing.
