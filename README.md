# TimeTrack Pro

## Overview

TimeTrack Pro is a simple command-line application developed as part of the DevOps 1 course. The application allows users to calculate daily working hours and total weekly working hours. The project demonstrates key DevOps practices such as version control with Git, branching strategies, pull requests, automated testing, and Continuous Integration (CI) using GitHub Actions.

The project was inspired by the RebTech AB case study, where a company needed a more structured and automated development workflow. The goal was not only to create a functional application but also to apply modern DevOps principles throughout the development process.

---

## Features

* Calculate working hours for a single workday
* Calculate total working hours for a week
* Simple command-line interface
* Automated unit tests using pytest
* Continuous Integration using GitHub Actions
* Git-based version control with feature branches and pull requests

---

## Project Structure

```text
timetrack-pro/
│
├── app.py
├── timetrack.py
├── test_timetrack.py
├── requirements.txt
├── README.md
│
└── .github/
    └── workflows/
        └── ci.yml
```

### File Descriptions

| File              | Purpose                                  |
| ----------------- | ---------------------------------------- |
| app.py            | Main application interface               |
| timetrack.py      | Contains business logic and calculations |
| test_timetrack.py | Automated unit tests                     |
| requirements.txt  | Python dependencies                      |
| ci.yml            | GitHub Actions CI pipeline               |
| README.md         | Project documentation                    |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/aamirashraf-dev/timetrack-pro.git
```

Navigate to the project folder:

```bash
cd timetrack-pro
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the application with:

```bash
python app.py
```

Example:

```text
TimeTrack Pro
=========================

Employee name: John
Start hour (24h format): 8
End hour (24h format): 17

Work Summary
-------------------------
Employee: John
Start time: 8
End time: 17
Hours worked: 9
```

---

## Running Automated Tests

To execute all tests:

```bash
python -m pytest
```

The tests verify that working hours and weekly hour calculations behave as expected.

---

## Branching Strategy

This project uses a simple feature branch workflow.

### Main Branch

The `main` branch contains stable and reviewed code.

### Feature Branches

New functionality is developed in separate feature branches before being merged into the main branch through Pull Requests.

Example:

```text
main
│
├── feature-timelog
└── feature-ci
```

### Why This Strategy Was Chosen

Using feature branches allows development work to be isolated from stable code. This reduces risk, improves collaboration, and makes code reviews easier. Pull Requests provide an opportunity to review and validate changes before they are merged.

---

## Continuous Integration (CI)

The project uses GitHub Actions to automatically validate code changes.

The CI pipeline is triggered whenever code is pushed to the `main` branch.

### Pipeline Steps

1. Checkout repository
2. Set up Python environment
3. Install project dependencies
4. Run Flake8 linting checks
5. Execute automated pytest tests

If any step fails, the pipeline reports the issue immediately, helping developers identify and fix problems early.

---

## Technologies Used

* Python 3
* Git
* GitHub
* GitHub Actions
* Pytest
* Flake8
* Visual Studio Code

---

## DevOps Practices Demonstrated

This project demonstrates several core DevOps principles:

* Version control using Git
* Branching and merging workflows
* Pull Requests for code review
* Automated testing
* Continuous Integration
* Documentation and traceability
* Incremental development through multiple commits

These practices help improve software quality, reduce manual work, and enable faster and more reliable delivery of software.

---

## Author

Aamir Ashraf