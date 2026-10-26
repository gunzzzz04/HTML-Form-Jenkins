# HTML Registration Form — Jenkins Pipeline Assignment

## Files
- `index.html`: Form with Name, Email, Contact Number and Submit.
- `tests/test_form.py`: Automated tests for form and fields.
- `Jenkinsfile`: Jenkins pipeline that checks out the repository and runs tests.

## Run tests locally on Windows
```bat
python -m unittest discover -s tests -p "test_*.py" -v
```

## Push to GitHub
Create a repository, then from this folder run:
```bat
git init
git add .
git commit -m "Add HTML registration form and tests"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the example remote URL with your actual repository URL.

## Jenkins
1. Ensure the Windows Jenkins agent has Git and Python installed and available on PATH.
2. Create New Item → Pipeline.
3. Under Pipeline, choose Pipeline script from SCM.
4. SCM: Git; Repository URL: your actual GitHub URL; Branch: `*/main`; Script Path: `Jenkinsfile`.
5. Save and click Build Now.
6. Open Console Output and capture the real run, including test results.

This Jenkinsfile uses `bat`, intended for a Windows Jenkins agent. For Linux, replace `bat` with `sh`.
