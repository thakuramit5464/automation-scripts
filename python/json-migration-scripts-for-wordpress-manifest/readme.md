# Manifest Language Grouping Script

This Python script transforms a Curious Reader container `manifest.json` by grouping `web_apps` into an `appLanguages` object based on `languageInEnglishName`.

Each language group gets its own list of apps, and **`appId` numbering restarts from `0` for every language**.

---

## ✨ What This Script Does

### Input

- Reads a standard `manifest.json` file
- Uses the existing `web_apps` array
- Keeps `web_apps` unchanged

### Output

- Adds a new top-level key: `appLanguages`
- Groups apps by `languageInEnglishName` (lowercased)
- Generates a **language-scoped `appId`** starting from `0`
- Writes the updated manifest to `manifest_updated.json`
