# Chatbot Testing — Manual + Automation

**Project:** Testing Conversational AI Chatbot — Manual and Automation Approach

## Overview
This project demonstrates manual test case design and a beginner-friendly automation framework for testing conversational AI APIs and flows. It includes API tests (pytest + requests), guidelines for manual test cases, and CI to run automated tests on GitHub Actions.

## What I tested
- Conversation flows (expected bot responses)
- API correctness (status codes, JSON schema, response fields)
- Regression smoke tests for critical endpoints

## Tools / Tech
- Python 3.8+
- pytest
- requests
- jsonschema
- Postman (optional)
- GitHub Actions (CI)

## How to run locally
1. Create virtual env:

output
python -m venv venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows

2. Install dependencies:
pip install -r requirements.txt

3. Edit `tests/test_chatbot_api.py` and set `BASE_URL` to the API you will test.

4. Run tests:
pytest -q

## Files
- `tests/test_chatbot_api.py` — basic API tests
- `.github/workflows/python-tests.yml` — CI to run pytest
- `postman/` — Postman collection and manual test cases (optional)

## How to present this in interviews
- Show test cases and test run logs.
- Explain manual testing + Postman usage and automation with pytest.
- Mention bug reporting template (Google Sheet / Jira).