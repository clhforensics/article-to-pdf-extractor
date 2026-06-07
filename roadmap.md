# Article to PDF Extractor - Development Roadmap

This roadmap outlines the strategic feature pipeline for transforming the Article to PDF Extractor into a comprehensive, privacy-first Personal Knowledge Management (PKM) tool.

## Phase 1: Core UX and Privacy (Near-Term)
- [x] **Clean Room Extraction Mode:** Aggressively strip out all non-essential metadata, tracking tokens in URLs, and hidden `<iframe>` elements during DOM parsing to ensure an "air-gapped" and private document.
- [ ] **Code Block & Syntax Highlighting Preservation:** Retain formatting, monospace fonts, and background shading for `<pre>` and `<code>` tags, ensuring technical articles and documentation are rendered cleanly.
- [ ] **Adaptive Typographic Output ("Reading Lenses"):** Introduce distinct rendering styles before PDF generation:
  - *Bionic Reading Mode:* Bold initial letters to guide the eyes.
  - *Ink-Saver Mode:* Convert images to grayscale and use high-efficiency fonts.
  - *Deep Focus Mode:* Strip images, enlarge fonts, and widen margins.

## Phase 2: Workflow and Automation (Mid-Term)
- [ ] **Batch Processing Queue:** Allow multiple bookmarklet payloads to be stored in `localStorage`, enabling users to queue several articles and generate either a single multi-chapter PDF or trigger a bulk download.
- [ ] **The Executive AI Digest:** Integrate a lightweight API hook to process the extracted text and prepend a bulleted "Executive Summary" at the top of the generated document.
- [ ] **Automated Tagging & Metadata Injection:** Automatically generate topic tags based on article content and embed them directly into the PDF's internal metadata fields (Title, Author, Keywords) for seamless indexing by external search tools.

## Phase 3: Infrastructure and Integration (Long-Term)
- [ ] **Direct-to-Archive Pipeline:** Implement WebDAV or REST API endpoints within the UI settings to bypass local "Downloads" folders, automatically piping the generated PDF directly to a self-hosted environment or dedicated local NAS directory.
- [ ] **Progressive Web App (PWA) Conversion:** Wrap the single-file architecture in a basic Service Worker and Web App Manifest, allowing it to be installed locally on desktops and mobile devices for true offline capability.
