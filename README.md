# Article to PDF Extractor

A browser-based tool that converts web articles into clean PDFs, including articles you can legitimately access through an authenticated browser session.

No credentials. No backend. No server-side processing. No tracking. The app remains a single HTML file with no build step.

## Version 1.1.0

### Highlights
- Persistent queue stored in your browser
- Author and publication-date extraction when supplied by the source page
- Cleaner canonical URLs and duplicate prevention
- Improved PDF and TXT metadata
- Keyboard-accessible input tabs
- jsPDF updated to 4.2.1

## Use it

### Bookmarklet
1. Open the app.
2. Drag **Save Article to Extractor** to your bookmarks bar.
3. Open an article you are authorized to read.
4. Click the bookmarklet.
5. Return to the app, paste the copied data, and add it to the queue.

### Saved HTML
Save a page as **Webpage, HTML Only**, then upload the `.html` or `.htm` file.

### Public URL
Paste one or more public URLs. Public URL fetching uses third-party CORS proxies and may fail on bot-protected or login-required sites.

## Privacy
Bookmarklet captures and saved HTML are processed in the browser. The app does not request or store account credentials.

Public URL fetching sends the requested URL through a third-party CORS proxy. Do not use that mode for sensitive URLs.

## Limitations
- Text-first extraction; images and interactive embeds are not preserved.
- Lazy-loaded content may require scrolling through the source article before capture.
- Some sites use structures that browser extraction cannot fully see.
- Author/date metadata is included only when the page exposes it.

## Hosting
This project is designed for static hosting such as GitHub Pages. No build command is required.

## License
MIT
