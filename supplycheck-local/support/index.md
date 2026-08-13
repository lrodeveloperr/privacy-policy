---
title: Support and Data Deletion for SupplyCheck
permalink: /supplycheck-local/support/
lang: en
---

<style>
:root { color-scheme: light dark; }
body { box-sizing: border-box; max-width: 980px; margin: 0 auto; padding: 28px 22px 56px; font: 17px/1.62 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #172033; background: #ffffff; }
a { color: #0759b8; }
h1, h2, h3 { line-height: 1.25; color: #0b2345; }
h1 { margin-top: 1.2rem; }
blockquote { margin-left: 0; padding: .75rem 1rem; border-left: 4px solid #4b78a8; background: #f4f7fb; }
table { display: block; max-width: 100%; overflow-x: auto; border-collapse: collapse; }
th, td { padding: .55rem; border: 1px solid #ccd5e0; text-align: left; vertical-align: top; }
.legal-nav { display: flex; flex-wrap: wrap; gap: .55rem 1rem; padding-bottom: 1rem; border-bottom: 1px solid #d7dee8; }
.legal-meta { color: #48566a; }
.legal-footer { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #d7dee8; color: #48566a; }
@media (prefers-color-scheme: dark) {
  body { color: #e8edf5; background: #111827; }
  h1, h2, h3 { color: #f5f8fc; }
  a { color: #82b7ff; }
  blockquote { background: #1d2a3a; }
  th, td, .legal-nav, .legal-footer { border-color: #425069; }
  .legal-meta, .legal-footer { color: #b8c3d4; }
}
</style>

<nav class="legal-nav" aria-label="SupplyCheck legal documents">
  <a href="{{ '/supplycheck-local/' | relative_url }}">Overview</a>
  <a href="{{ '/supplycheck-local/privacy/' | relative_url }}">Privacy</a>
  <a href="{{ '/supplycheck-local/terms/' | relative_url }}">Terms</a>
  <a href="{{ '/supplycheck-local/purchases/' | relative_url }}">Purchases</a>
  <a href="{{ '/supplycheck-local/refunds/' | relative_url }}">Refunds</a>
  <a href="{{ '/supplycheck-local/support/' | relative_url }}">Support & deletion</a>
  <a href="{{ '/supplycheck-local/disclaimer/' | relative_url }}">Disclaimer</a>
</nav>

<p class="legal-meta"><strong>Lateef Razaq-Oyetola carrying on business as GoodUse Studios</strong> · 36 Zorra Street, Toronto (Etobicoke), Ontario M8Z 0G5, Canada · Privacy Officer: Lateef Razaq-Oyetola · <a href="mailto:lrodeveloperr@gmail.com">lrodeveloperr@gmail.com</a> · Version 13 August 2026</p>

# Support and Data Deletion for SupplyCheck

**Last updated:** 13 August 2026

## 1. Support

**Operator:** Lateef Razaq-Oyetola carrying on business as GoodUse Studios  
**Postal address:** 36 Zorra Street, Toronto (Etobicoke), Ontario M8Z 0G5, Canada  
**Privacy Officer:** Lateef Razaq-Oyetola  
**Email:** lrodeveloperr@gmail.com

For support, include only:

- Android or iOS;
- device model and operating-system version;
- SupplyCheck version;
- schema version and locale, if shown; and
- the neutral error code and steps that produced it.

For purchase support, you may include a redacted Store order or transaction reference.

Do **not** send screenshots, supplier or employee names, order or invoice references, prices, notes, photos, source documents, exported reports, databases, backup files, passwords, PINs, recovery keys or payment-card details. V1 support does not accept operational records or images. If an email includes them contrary to these instructions, GoodUse Studios will restrict or remove that content subject to security, legal-preservation and incident-response duties.

SupplyCheck has no account and no GoodUse Studios cloud database containing your operational records. We cannot view, retrieve, edit, restore or remotely delete records stored only on your device.

## 2. Export before deletion

If you need a human-readable copy, use:

**Settings → Data & Continuity → Export all organisation data (readable)**

The readable ZIP contains a canonical UTF-8 JSON dataset, convenience CSV tables and associated organisation files. It is for access and portability and is not the machine-restorable backup. Saving it does not cancel or extend a Pending-deletion deadline.

The file is not password-protected or separately encrypted by SupplyCheck. Anyone with access to the file or chosen destination may be able to read it. Secure the destination and delete external copies separately when no longer needed.

## 3. Delete a record

Use **Permanently delete** on the relevant record and confirm the exact scope. This removes the record's content-bearing local history and derivatives, including revisions, recovery events, photos, retained originals, exact PDFs marked shared, indexes, previews and temporary share files.

Deleting an incomplete free Draft releases its unused reservation. Deleting a completed record does not restore a consumed free delivery.

A minimal opaque tombstone, evaluation token and identity-continuity mapping may remain where needed to prevent an old backup from resurrecting a deletion or counting one delivery more than once. It contains no readable supplier, person, date, amount, attachment or note.

## 4. Delete all organisation data in the App

Use:

**Settings → Data & Continuity → Delete all organisation data**

The App shows the scope and local backup/outward-copy observations before final confirmation. When native device authentication is configured and available, it must succeed; cancel, failure, lockout, timeout or backgrounding aborts the action. A strong confirmation fallback is used only if the operating system reports before prompting that native authentication is unsupported or not configured.

The action removes the live organisation database and content-bearing local derivatives, including attachments, retained originals, temporary files, indexes, local checkpoints, local backup inventory and outward-copy log. Destruction is crash-resumable and is reported complete only after the App verifies the local scope is empty.

The following content-free continuity data remains in app-private storage for the installation lifetime:

- up to five opaque evaluation-claim tokens or anonymous conflict-family slots;
- the marker that the historical five-use allowance has been exhausted, when applicable;
- a bounded opaque identity-equivalence ledger needed to deduplicate old packages and apply deletion markers correctly; and
- content-free destruction-generation records needed to reject stale callbacks.

This data contains no organisation, supplier, person, date, amount, attachment, task or note, but an opaque token may correlate with a matching old backup held by the customer. It is retained so deletion does not reset the free allowance and old packages cannot silently duplicate or resurrect records. It is excluded from the complete readable export. A bounded subset can travel in a machine-restorable SupplyCheck package as described in the [Privacy Policy]({{ '/supplycheck-local/privacy/' | relative_url }}).

## 5. Operating-system removal

### Android

The in-App **Delete all organisation data** action is the preferred route because it applies the App's deletion and continuity rules. Android's **Settings → Apps → SupplyCheck → Storage → Clear storage/data** control or deleting the App can remove the App container, including installation-local continuity metadata. Menu wording varies by device.

The production configuration excludes operational files from Android automatic App backup and automatic device transfer. A complete SupplyCheck backup or export saved to Files, cloud storage or another provider is outside the App container and is not removed by clearing App data or uninstalling.

### iOS

The in-App **Delete all organisation data** action is the preferred route. Deleting SupplyCheck removes its local App container. Do not choose **Offload App** if your goal is deletion because offloading can preserve documents and data for later reinstallation.

The production configuration excludes operational files from automatic iOS App backup and automatic device transfer. A complete SupplyCheck backup or export saved to Files, iCloud Drive or another provider is outside the App container and is not removed by deleting the App.

## 6. External and older copies

SupplyCheck cannot recall or remotely delete:

- a PDF already sent;
- a readable export or analysis spreadsheet;
- a complete backup or transfer package in a user-selected destination;
- a recipient or provider-held copy;
- an old customer-controlled backup; or
- data on another device.

Delete each external copy from its destination and, where relevant, trash/deleted-items folders, synced devices and backups. Ask recipients to delete their copies where appropriate.

An isolated device restoring a backup created before a later deletion may reintroduce the older content because it has no newer tombstone. SupplyCheck shows package age and this limitation before restore. It does not claim forensic erasure from device storage.

## 7. Retention and automatic local deletion

- Temporary import, preview and share files are removed after success or cancellation where possible. They become unusable no later than 24 hours after creation and are purged the next time the App executes.
- A Draft enters seven-day Pending deletion after 90 days without edit or **Keep draft**.
- Record-bound import staging follows its parent record. An unattached or supplier-template staging session enters seven-day **Pending deletion** after 90 days without **Resume import** or **Keep staging**; either action resets its activity anchor.
- Completed records without open recovery follow the selected 1-year, 3-year, 7-year or Manual-deletion-only choice. Until the organisation chooses, completed records do not auto-delete. For a record without follow-up, a fixed period runs from the latest substantive completed revision; for a recovery case, it runs from the later of the latest substantive revision and latest resolution or closure. Display-label changes, task/reminder/share status, exports and UI changes do not reset that anchor.
- Open recoveries and unresolved conflicts are not automatically deleted.
- Archive does not override retention.
- Exporting does not cancel a deadline.

## 8. Information held by GoodUse Studios

For personal information GoodUse Studios actually holds, such as support or privacy correspondence, you may request access, correction or deletion by emailing lrodeveloperr@gmail.com from the same address where practical. We may verify the request and may retain limited information required for legal, tax, accounting, security, fraud-prevention or unresolved-dispute purposes.

Deleting local App data does not delete Store transaction records held by Apple or Google. Contact the applicable Store regarding its records.

## 9. Purchases after deletion

Deleting local data or uninstalling the App does not cancel an Android subscription. Cancel through [Google Play subscriptions](https://play.google.com/store/account/subscriptions) if you do not want future renewal.

An eligible purchase may be restored through the purchasing Store account. Entitlement restoration does not restore or synchronize operational records. iOS and Android purchases do not transfer between platforms.


<footer class="legal-footer">
SupplyCheck · © 2026 Lateef Razaq-Oyetola carrying on business as GoodUse Studios · <a href="mailto:lrodeveloperr@gmail.com">lrodeveloperr@gmail.com</a> · Version 13 August 2026
</footer>
