# Promise Guard store metadata package

This package contains reviewed App Store Connect and Google Play listing drafts for the 31-language Promise Guard catalogue.

## Deliverables

- `app-store.json`: 34 App Store Connect localizations.
- `google-play.json`: 37 Google Play localizations.
- `commercial-model.json`: locked platform-specific product model and reference prices.
- `VALIDATION.md`: field-limit and coverage results.
- `SUBMISSION-CHECKLIST.md`: fields that depend on the final binaries or verified publisher details.
- `generate_metadata.py`: reviewed localization source and deterministic JSON builder.
- `validate_metadata.py`: repeatable locale and length validation.

Run:

```bash
python3 generate_metadata.py
python3 validate_metadata.py
```

The English legal documents in the parent directory are authoritative. Localized listing copy is a marketing translation, not a localized legal instrument.
