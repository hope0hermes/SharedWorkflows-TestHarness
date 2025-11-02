# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2025-11-02

### Changed
- feat: add is_published() helper to test complete publish pipeline (#11)


## [0.4.0] - 2025-11-02

### Changed
- feat: use PAT for release creation to trigger publish workflow (#9)


## [0.3.0] - 2025-11-02

### Changed
- feat: add get_version and get_info helper functions (#7)


## [0.2.0] - 2025-11-01

### Changed
- ci: add debug job and workflow_dispatch trigger to create-release (#5)
- fix: add required permissions to workflow jobs (#3)
- feat: initial test harness setup for SharedWorkflows (#1)
- ci: Initial repository setup and branch rules enforcement


### Added
- Initial test harness setup for SharedWorkflows
- Minimal Python package structure with version management
- Test workflows for SharedWorkflows reusable workflows
- Sample tests (passing and failing) for CI/CD validation
- Documentation for test harness purpose and usage
