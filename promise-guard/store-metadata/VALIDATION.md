# Promise Guard metadata validation

**Validated:** 21 August 2026  
**Result:** PASS

## Coverage

| Target | Expected | Produced | Result |
|---|---:|---:|---|
| Selectable product languages | 31 | 31 | PASS |
| App Store Connect localizations | 34 | 34 | PASS |
| Google Play localizations | 37 | 37 | PASS |

## App Store Connect locales

`en-US`, `en-CA`, `en-GB`, `es-MX`, `es-ES`, `pt-PT`, `pt-BR`, `fr-FR`, `fr-CA`, `de-DE`, `it`, `nl-NL`, `pl`, `tr`, `ro`, `cs`, `uk`, `ru`, `ar`, `zh-Hans`, `zh-Hant`, `ja`, `ko`, `hi`, `vi`, `id`, `th`, `ms`, `fi`, `sv`, `da`, `no`, `el`, `he`.

The product registry records no exact App Store Connect listing locale for Urdu, Bengali or Filipino. Those remain localized inside the app; the App Store will display the configured primary localization where no localized product page is available.

## Google Play locales

`en-US`, `en-CA`, `en-GB`, `es-419`, `es-ES`, `pt-PT`, `pt-BR`, `fr-FR`, `fr-CA`, `de-DE`, `it-IT`, `nl-NL`, `pl-PL`, `tr-TR`, `ro`, `cs-CZ`, `uk`, `ru-RU`, `ar`, `zh-CN`, `zh-TW`, `ja-JP`, `ko-KR`, `hi-IN`, `ur`, `bn-BD`, `vi`, `id`, `th`, `fil`, `ms-MY`, `fi-FI`, `sv-SE`, `da-DK`, `no-NO`, `el-GR`, `iw-IL`.

## Automated field checks

| Store | Field | Limit checked | Result |
|---|---|---:|---|
| App Store | Name | 30 characters | PASS |
| App Store | Subtitle | 30 characters | PASS |
| App Store | Promotional text | 170 characters | PASS |
| App Store | Description | 4,000 characters | PASS |
| App Store | Keywords | 100 UTF-8 bytes | PASS |
| Google Play | App name | 30 characters | PASS |
| Google Play | Short description | 80 characters | PASS |
| Google Play | Full description | 4,000 characters | PASS |

Every required metadata field is non-empty. JSON parses successfully, locale sets match the locked registry exactly, and localized copy contains no explicit store price that could conflict with a storefront-localized price.

## Source hierarchy

- Apple, [App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information) — app name and subtitle limits.
- Apple, [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information) — promotional text, description, keyword-byte and Support URL requirements.
- Apple, [Creating your product page](https://developer.apple.com/app-store/product-page/) — metadata-writing and pricing-reference guidance.
- Google, [Create and set up your app](https://support.google.com/googleplay/android-developer/answer/9859152) — app name, short description and full description limits.

## Human release gates

Automated validation cannot certify how every localized listing appears beside final screenshots or whether every phrase is preferred by a native reviewer in every target market. Before public release, preview every listing in its store console, conduct native-speaker review for priority markets, and verify that screenshots match the final binary and localized UI.
