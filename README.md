# Voucher Generator — PF Payment Voucher Builder

Pull participant data from Google Sheets, CSV, or PDF and lay it out like PF Payment Voucher template — ready to download as PDF.

## Quick start (Windows)
1. Double-click \Start Odyssey.cmd\ — opens http://127.0.0.1:xxxx/
2. Paste Google Sheet link (Anyone with the link → Viewer) and click **Import details & photos**
3. Review rows → Map fields → Template settings → Preview & export

## Files
- \Odyssey new version (1).html\ — single-file app (no build)
- \odyssey-local.py\ — localhost server so Google Sheets import works (file:// blocks it)
- \Start Odyssey.cmd\ — launcher (tries \python\ → \py\ → full path)

## Requirements
- Python 3.x (via \py\ launcher on Windows, 3.14 tested)
- Modern browser

## Google Sheet
Share → General access → Anyone with the link → Viewer. Link can be .../edit?usp=sharing without gid — app now handles missing gid correctly.

## License
Private
