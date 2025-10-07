# Prefix Demo

This is a simple Python demonstration project designed to showcase the use of PrefixAI, an on-call SRE agent.

## Overview

The project fetches the current Bitcoin price from the Coindesk API using a Python script (`app.py`).  
It includes an intentional error: the required dependency `requests` is not listed in [`requirements.txt`](requirements.txt), which will cause the workflow to fail. This is to demonstrate how PrefixAI can help diagnose and resolve such issues.

## Files

- [`app.py`](app.py): Fetches and prints the current Bitcoin price.
- [`requirements.txt`](requirements.txt): (Intentionally left empty for demo purposes.)
- [`.github/workflows/demo.yml`](.github/workflows/demo.yml): GitHub Actions workflow to run the demo.

## How to Run

1. Clone the repository.
2. Run the workflow via GitHub Actions or locally:
   ```sh
   pip install -r requirements.txt
   python app.py
   ```
   You will encounter an error due to the missing `requests` dependency.

## Purpose

This demo is intended to show how PrefixAI can assist in identifying and resolving errors in CI/CD pipelines and cloud platforms