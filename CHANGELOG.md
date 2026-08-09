# Changelog

All notable changes to this project will be documented in this file.

The project follows Semantic Versioning.

## [1.1.0] - 2026-08-08

### Added
- Persistent processing queue backed by browser `localStorage`
- Article author extraction from JSON-LD and common metadata fields
- Publication-date extraction from JSON-LD and common metadata fields
- Author and publication metadata in PDF and text exports
- Internal PDF document metadata
- Keyboard-accessible workflow tabs

### Changed
- Updated jsPDF from 2.5.1 to 4.2.1
- Canonical and cleaned URLs are preferred where available
- Bookmarklet payload format updated to version 3
- Saved HTML queue entries retain extracted content rather than the complete source HTML

### Fixed
- Duplicate URL detection is performed after tracking parameters and URL fragments are removed

## [1.0.0] - 2026-05-11

Initial public release.

### Added
- Bookmarklet workflow for authenticated browser sessions
- Saved HTML upload
- Public URL fetching via CORS proxies
- Smart text extraction
- Batch queue
- PDF and TXT exports
