# BugBug: GitHub Actions
#   - format
#   - linter
#   - pytest
# BugBug: Configure ruff linter

# Wheel names will be generated according to this value. Do not manually modify this value; instead
# update it according to committed changes by running this command from the root of the repository:
#
#   uv run python -m AutoGitSemVer.scripts.UpdatePythonVersion ./src/uvrepotemplate/__init__.py ./src
#
__version__ = "0.1.0"


def hello() -> str:
    return "Hello from uvrepotemplate!"


def Add(
    a: int,
    b: int,
) -> int:
    return a + b
