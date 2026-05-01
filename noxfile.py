import nox

# @nox.session
# def tests(session):
#     session.install("coverage")
#     session.install("pytest")

#     session.run("coverage", "run", "--source", "src", "-m", "pytest", "tests")
#     session.run("coverage", "report", "-m")


@nox.session
def lint(session):
    requirements = nox.project.load_toml("pyproject.toml")["tool"]["poetry"]["group"][
        "dev"
    ]["dependencies"]
    session.install(*requirements)

    # Install the local python package in editable mode
    session.install("-e", ".")
    session.run("pre-commit", "run", "--all-files")
