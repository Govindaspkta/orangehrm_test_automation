# Test Plan - OrangeHRM Demo

**Application under test:** OrangeHRM (https://opensource-demo.orangehrmlive.com)
**Tester:** Govinda
**Version:** 1.0 | **Date:** <fill>

## 1. Objective
Verify that the main user flows of OrangeHRM work correctly, find defects, and document the results.

## 2. Scope
**In scope:** login, dashboard, PIM, Admin, Leave, My Info, Directory, UI
**Out of scope:** load/performance testing, security/penetration testing, third-party integrations.

## 3. Test Approach
- **Manual:** functional, negative, boundary, UI and exploratory testing.
- **Automation:** Playwright (Python) with pytest for stable, high-priority flows.
- **Defects:** logged in the Bug Reports sheet with steps, expected vs actual, severity and priority.

## 4. Test Environment
| Item | Details |
|---|---|
| URL | https://opensource-demo.orangehrmlive.com |
| Browser | Chrome (latest), Firefox for compatibility checks |
| Devices | Desktop 1920x1080, mobile viewport 375x667 (DevTools) |
| Tools | Excel/Google Sheets, Chrome DevTools, Playwright, pytest |

## 5. Entry / Exit Criteria
- **Entry:** site reachable, test data prepared, test cases written.
- **Exit:** all High-priority cases executed and every defect logged.

## 6. Defect Severity
- **Critical:** crash, data loss, blocks a main flow
- **High:** major feature broken, no workaround
- **Medium:** feature works with issues or a workaround
- **Low:** cosmetic or minor

## 7. Risks
- Public site: other users may change shared data, and the site may be slow or down.
- Solo tester with limited time.

## 8. Deliverables
Test plan, test cases, bug reports, test summary report, automation scripts.
