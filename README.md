# SharedWorkflows Test Harness

**A dedicated testing repository for [SharedWorkflows](https://github.com/hope0hermes/SharedWorkflows) reusable workflows and composite actions.**

[![Tests](https://github.com/hope0hermes/SharedWorkflows-TestHarness/actions/workflows/tests.yml/badge.svg)](https://github.com/hope0hermes/SharedWorkflows-TestHarness/actions/workflows/tests.yml)

## Purpose

This repository exists solely to test changes to SharedWorkflows **without polluting production repositories** with test/debug commits.

### Problem It Solves

Testing SharedWorkflows changes used to require:
1. Making changes in SharedWorkflows
2. Creating a PR in SharedWorkflows
3. Pushing test commits to production repos (StravaAnalyzer, StravaFetcher, etc.)
4. Debugging by going back and forth between repositories
5. **Polluting production commit history** with test/debug commits

### Solution

This test harness provides:
- ✅ **Clean separation**: Keep test commits out of production repos
- ✅ **Fast iteration**: Quick feedback loop for workflow development
- ✅ **Comprehensive testing**: Test all workflow scenarios without risk
- ✅ **Safe experimentation**: Break things without consequences

---

## Structure

```
SharedWorkflows-TestHarness/
├── .github/
│   └── workflows/
│       ├── tests.yml              # Tests reusable-tests workflow
│       ├── release.yml            # Tests reusable-release workflow
│       ├── create-release.yml     # Tests reusable-create-release workflow
│       ├── publish.yml            # Tests reusable-publish workflow
│       └── commitlint.yml         # Tests reusable-commitlint workflow
├── src/
│   └── testharness/
│       └── __init__.py            # Minimal package with version
├── tests/
│   ├── conftest.py                # Pytest fixtures
│   ├── test_passing.py            # Tests that pass
│   └── test_failing.py            # Tests that fail (for testing CI)
├── CHANGELOG.md                   # For testing changelog updates
├── pyproject.toml                 # Minimal Python project config
├── LICENSE                        # MIT License
└── README.md                      # This file
```

---

## How It Works

### 1. Testing Workflow Changes

When developing new features in SharedWorkflows:

```bash
# 1. Make changes in SharedWorkflows
cd SharedWorkflows
git checkout -b feat/new-feature
# ... make changes ...

# 2. Test in this repository
cd ../SharedWorkflows-TestHarness
git checkout -b test/new-feature

# 3. Update workflow to use your branch
# In .github/workflows/tests.yml, change:
# uses: hope0hermes/SharedWorkflows/.github/workflows/reusable-tests.yml@main
# to:
# uses: hope0hermes/SharedWorkflows/.github/workflows/reusable-tests.yml@feat/new-feature

# 4. Push and observe results
git add .
git commit -m "test: verify new SharedWorkflows feature"
git push origin test/new-feature

# 5. Check GitHub Actions results
# If tests pass, your SharedWorkflows change is ready!
```

### 2. Test Scenarios

This repository tests:

- **Reusable Tests Workflow** (`reusable-tests.yml`)
  - Linting with ruff
  - Running pytest
  - Coverage reporting
  - Python version matrix
  - Passing and failing tests

- **Reusable Release Workflow** (`reusable-release.yml`)
  - Version bump detection from conventional commits
  - CHANGELOG updates
  - PR creation with version bumps
  - Hatch version management

- **Reusable Create Release Workflow** (`reusable-create-release.yml`)
  - GitHub Release creation
  - Tag creation
  - Release notes generation

- **Reusable Publish Workflow** (`reusable-publish.yml`)
  - Package building with hatch
  - Publishing to GitHub Packages
  - Version extraction

- **Reusable Commitlint Workflow** (`reusable-commitlint.yml`)
  - Conventional commit validation
  - PR title checking

---

## Usage

### For SharedWorkflows Developers

**Testing a new SharedWorkflows feature:**

1. Create feature branch in SharedWorkflows
2. Create test branch in this repo
3. Update workflow references to point to your branch
4. Push and verify in GitHub Actions
5. Once confirmed working, merge SharedWorkflows PR
6. Update this repo's workflows back to `@main`

**Testing specific scenarios:**

```bash
# Test failing tests
git commit --allow-empty -m "test: trigger failing test scenario"

# Test version bump (patch)
git commit --allow-empty -m "fix: test patch version bump"

# Test version bump (minor)
git commit --allow-empty -m "feat: test minor version bump"

# Test version bump (major)
git commit --allow-empty -m "feat!: test major version bump"

# Test no version bump
git commit --allow-empty -m "docs: test no version bump"
```

### For New Projects

If you're setting up a new project using SharedWorkflows, reference the workflows here as examples:

- See `.github/workflows/tests.yml` for how to call `reusable-tests.yml`
- See `.github/workflows/release.yml` for how to call `reusable-release.yml`
- See `.github/workflows/publish.yml` for how to call `reusable-publish.yml`

---

## Workflows

### Tests Workflow

Runs on every push and PR:
```yaml
uses: hope0hermes/SharedWorkflows/.github/workflows/reusable-tests.yml@main
with:
  python-version: "3.12"
  package-name: "sharedworkflows-testharness"
  coverage-threshold: 0
  run-lint: true
  run-tests: true
```

### Release Workflow

Creates version bump PRs when changes are merged to main:
```yaml
uses: hope0hermes/SharedWorkflows/.github/workflows/reusable-release.yml@main
with:
  package-path: "src/testharness/__init__.py"
secrets:
  PAT_TOKEN: ${{ secrets.PAT_TOKEN }}
```

### Create Release Workflow

Creates GitHub releases after version bump PRs are merged:
```yaml
uses: hope0hermes/SharedWorkflows/.github/workflows/reusable-create-release.yml@main
```

### Publish Workflow

Publishes package to GitHub Packages after release:
```yaml
uses: hope0hermes/SharedWorkflows/.github/workflows/reusable-publish.yml@main
with:
  registry: github
secrets:
  PUBLISH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## Testing Philosophy

### What This Repo Tests

✅ **Workflow integration**: Do the reusable workflows work correctly?  
✅ **Version management**: Does version bumping work?  
✅ **Release automation**: Do releases get created properly?  
✅ **Publishing**: Does package publishing work?  
✅ **Error handling**: Do workflows fail gracefully?  

### What This Repo Doesn't Test

❌ **Production code**: No real functionality here, just stubs  
❌ **Complex logic**: Keep it minimal, focus on workflow testing  
❌ **Long-running processes**: Fast tests only  

---

## Contributing

This repository is primarily for testing SharedWorkflows. Contributions should:

1. **Keep it minimal**: Only add what's needed to test workflows
2. **Document changes**: Update README when adding new test scenarios
3. **Follow conventions**: Use conventional commits (they're tested here!)
4. **Don't add features**: This isn't a real package, just a test harness

---

## Related Projects

- **[SharedWorkflows](https://github.com/hope0hermes/SharedWorkflows)**: Reusable CI/CD workflows and composite actions
- **[StravaAnalyzer](https://github.com/hope0hermes/StravaAnalyzer)**: Production project using SharedWorkflows
- **[StravaFetcher](https://github.com/hope0hermes/StravaFetcher)**: Production project using SharedWorkflows

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

- **Author**: Israel Barragan
- **Email**: abraham0vidal@gmail.com
- **GitHub**: [@hope0hermes](https://github.com/hope0hermes)

---

**This is a test harness. For real functionality, see the projects listed above.**
