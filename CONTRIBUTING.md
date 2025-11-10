# Contributing Guide

## Branch-to-Milestone Mapping

### Task 1: Git & Environment Setup
**Branch:** `setup-task`
- **Milestone:** Project initialization and CI/CD setup
- **Commits:**
  - `[TASK-1] init: add .gitignore`
  - `[TASK-1] add requirements`
  - `[TASK-1] add project structure and workflows`
  - `[TASK-1] add documentation for folders`
  - `[TASK-1] add unit tests workflow`

### Task 2: Data Profiling, Cleaning & EDA
**Branches:** `eda-benin`, `eda-sierraleone`, `eda-togo`
- **Milestone:** Exploratory Data Analysis for each country
- **Commits:**
  - `[TASK-2] add benin eda notebook`
  - `[TASK-2] add sierra leone eda notebook`
  - `[TASK-2] add togo eda notebook`
  - `[TASK-2] complete eda analysis with results`

### Task 3: Cross-Country Comparison
**Branch:** `compare-countries`
- **Milestone:** Statistical comparison and ranking
- **Commits:**
  - `[TASK-3] add cross country comparison notebook`
  - `[TASK-3] update comparison with statistical tests`

### Bonus: Interactive Dashboard
**Branch:** `dashboard-dev`
- **Milestone:** Streamlit dashboard development and deployment
- **Commits:**
  - `[BONUS] add dashboard documentation`
  - `[BONUS] update streamlit dashboard`
  - `[BONUS] deploy to streamlit cloud`

## Commit Message Convention

Use the following format for all commits:
```
[TASK-X] type: brief description

Examples:
[TASK-1] feat: add GitHub Actions workflow
[TASK-2] analysis: complete benin eda
[TASK-3] docs: add comparison insights
[BONUS] deploy: configure streamlit app
```

### Commit Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `analysis`: Data analysis updates
- `test`: Adding or updating tests
- `deploy`: Deployment configurations
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

## Development Workflow

### 1. Create Feature Branch
```bash
git checkout main
git pull origin main
git checkout -b <branch-name>
```

### 2. Make Changes
- Write clean, documented code
- Follow PEP 8 style guide for Python
- Add docstrings to functions
- Update notebooks with insights

### 3. Commit with Labels
```bash
git add <files>
git commit -m "[TASK-X] type: description"
```

### 4. Push and Create PR
```bash
git push -u origin <branch-name>
```
Then create a Pull Request on GitHub with:
- Clear title with task label
- Description of changes
- Link to related issue (if any)

### 5. Code Review
- Address reviewer comments
- Update PR with additional commits
- Ensure CI/CD passes

### 6. Merge
- Squash and merge or regular merge
- Delete branch after merge

## Project Structure

```
solar-challenge-week0/
├── .github/workflows/      # CI/CD pipelines
├── app/                    # Streamlit dashboard
├── data/                   # Data files (gitignored)
├── notebooks/              # Jupyter notebooks for EDA
├── scripts/                # Python utility scripts
├── tests/                  # Unit tests
├── .gitignore
├── requirements.txt
├── README.md
└── CONTRIBUTING.md
```

## Data Guidelines

### DO NOT Commit:
- Raw CSV files
- Cleaned data files
- Large datasets
- API keys or credentials

### DO Commit:
- Notebooks with analysis
- Code and scripts
- Documentation
- Configuration files

## Testing

Run tests before committing:
```bash
python -m unittest discover tests/
```

## Questions?

Contact the project maintainers or open an issue on GitHub.

## Acknowledgments

This project is part of the 10 Academy Week 0 Challenge for Solar Data Analysis.
