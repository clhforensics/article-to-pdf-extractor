# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-05-11

Initial public release.

### Added
- Bookmarklet workflow for capturing article content from authenticated browser sessions
- Saved HTML file upload (`.html`, `.htm`)
- Public URL fetching via CORS proxies (allorigins, corsproxy.io, thingproxy)
- Smart content extraction chain: JSON-LD `articleBody` → semantic selectors → paragraph aggregation
- Batch processing queue with mixed input types
- PDF generation via jsPDF with title, source URL, timestamp, and page numbers
- Plain text (`.txt`) export alongside PDFs
- Tab-based UI separating the three input workflows
- Drag-and-drop file upload supporting `.html`, `.htm`, and `.txt` (URL list)
- Auto-detection of pasted content type (bookmarklet JSON, raw HTML, or plain text)
- Toast notifications for user feedback
- Responsive design for mobile and desktop

### Security & Privacy
- No credentials are ever requested or stored
- No analytics, no tracking, no cookies
- The bookmarklet runs entirely in the user's authenticated browser tab; no data flows to this tool except via clipboard
