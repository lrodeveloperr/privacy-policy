#!/usr/bin/env python3
"""Validate locale coverage and current Apple/Google store field limits."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGUAGES = {"en", "es", "pt", "fr", "de", "it", "nl", "pl", "tr", "ro", "cs", "uk", "ru", "ar", "zh", "ja", "ko", "hi", "ur", "bn", "vi", "id", "th", "fil", "ms", "fi", "sv", "da", "nb", "el", "he"}
APPLE_EXPECTED = {"en-US", "en-CA", "en-GB", "es-MX", "es-ES", "pt-PT", "pt-BR", "fr-FR", "fr-CA", "de-DE", "it", "nl-NL", "pl", "tr", "ro", "cs", "uk", "ru", "ar", "zh-Hans", "zh-Hant", "ja", "ko", "hi", "vi", "id", "th", "ms", "fi", "sv", "da", "no", "el", "he"}
GOOGLE_EXPECTED = {"en-US", "en-CA", "en-GB", "es-419", "es-ES", "pt-PT", "pt-BR", "fr-FR", "fr-CA", "de-DE", "it-IT", "nl-NL", "pl-PL", "tr-TR", "ro", "cs-CZ", "uk", "ru-RU", "ar", "zh-CN", "zh-TW", "ja-JP", "ko-KR", "hi-IN", "ur", "bn-BD", "vi", "id", "th", "fil", "ms-MY", "fi-FI", "sv-SE", "da-DK", "no-NO", "el-GR", "iw-IL"}


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def nonempty(errors, platform, locale, field, value):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{platform}/{locale}/{field}: missing")


def main():
    apple = load("app-store.json")
    google = load("google-play.json")
    errors = []

    apple_locales = set(apple["locales"])
    google_locales = set(google["locales"])
    if apple_locales != APPLE_EXPECTED:
        errors.append(f"Apple locale mismatch: missing={sorted(APPLE_EXPECTED-apple_locales)} extra={sorted(apple_locales-APPLE_EXPECTED)}")
    if google_locales != GOOGLE_EXPECTED:
        errors.append(f"Google locale mismatch: missing={sorted(GOOGLE_EXPECTED-google_locales)} extra={sorted(google_locales-GOOGLE_EXPECTED)}")

    for locale, row in apple["locales"].items():
        for field in ("name", "subtitle", "promotional_text", "description", "keywords"):
            nonempty(errors, "apple", locale, field, row.get(field))
        limits = {"name": 30, "subtitle": 30, "promotional_text": 170, "description": 4000}
        for field, limit in limits.items():
            if len(row[field]) > limit:
                errors.append(f"apple/{locale}/{field}: {len(row[field])}>{limit} characters")
        keyword_bytes = len(row["keywords"].encode("utf-8"))
        if keyword_bytes > 100:
            errors.append(f"apple/{locale}/keywords: {keyword_bytes}>100 UTF-8 bytes")

    for locale, row in google["locales"].items():
        for field in ("app_name", "short_description", "full_description"):
            nonempty(errors, "google", locale, field, row.get(field))
        limits = {"app_name": 30, "short_description": 80, "full_description": 4000}
        for field, limit in limits.items():
            if len(row[field]) > limit:
                errors.append(f"google/{locale}/{field}: {len(row[field])}>{limit} characters")

    combined_langs = set(LANGUAGES)
    if len(combined_langs) != 31:
        errors.append(f"language registry count: {len(combined_langs)}!=31")

    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1

    print("PASS")
    print(f"31 product languages accounted for")
    print(f"{len(apple_locales)} App Store Connect localizations validated")
    print(f"{len(google_locales)} Google Play localizations validated")
    print("Apple: name<=30, subtitle<=30, promotional_text<=170, description<=4000, keywords<=100 UTF-8 bytes")
    print("Google Play: app_name<=30, short_description<=80, full_description<=4000")
    return 0


if __name__ == "__main__":
    sys.exit(main())
