# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

## [v1.1.1] - 2019-12-03

### Added

- **CUMULUS-1635** - Enhanced the messages logged by `CumulusLogger` to include
  the following additional information obtained from the CMA (if available):
  `asyncOperationId`, `granules` (granule IDs only), `parentArn`, and
  `stackName`

## [v1.1.0] - 2019-11-18

### Added

- **CUMULUS-1656** - Updated requirements to allow CMA 1.0.13 *or* the 1.1.x
  release branch of the CMA. It is expected that CMA 1.2.x will not be backward
  compatible with the 1.1.x client library.

- **CUMULUS-1488** - Updated CMA client to respect `CUMULUS_MESSAGE_ADAPTER_DIR`

## [v1.0.9] - 2019-09-16

### Added

- Updated CMA client to handle parameterized configuration, set execution env
  variable regardless of message format
