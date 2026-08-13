---
title: Privacy Policy for SupplyCheck Local
permalink: /supplycheck-local/privacy/
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

# Privacy Policy for SupplyCheck Local

**Effective date:** 12 August 2026  
**Last updated:** 13 August 2026

Lateef Razaq-Oyetola carrying on business as GoodUse Studios ("GoodUse Studios," "we," "us," or "our"), whose postal address is 36 Zorra Street, Toronto (Etobicoke), Ontario M8Z 0G5, Canada, publishes SupplyCheck Local (the "App"). This policy explains how the App handles information and how GoodUse Studios handles the limited information it actually receives.

## 1. Privacy summary

SupplyCheck is a local-first business utility. During ordinary core use, GoodUse Studios does not receive or store your orders, invoices, delivery records, photos, supplier notes, discrepancy records or recovery records. The App processes that operational content on your device.

The initial release has no SupplyCheck account, GoodUse Studios operational-data cloud database, advertising, behavioural analytics, tracking identifier, remote OCR, remote AI, supplier connection or simultaneous multi-device synchronization. It uses no third-party crash or analytics SDK. Platform services may separately process purchases or platform diagnostics under their settings, terms and privacy notices.

Operational content leaves the App only when a person using the device deliberately completes a previewed share, export, backup, copy or move and chooses a recipient, app, provider or destination. GoodUse Studios does not verify that person's identity or authority. V1 support does not ask for or accept operational records, images or backup files.

This local-first design reduces the information GoodUse Studios receives. It does not make the App or every use of it automatically compliant with every privacy, employment, records-management or other law.

## 2. Information processed locally

Depending on the features you use, the App may process locally:

- supplier and contact details;
- orders, invoices, delivery references, source documents and imported rows;
- item names, product identifiers, quantities, units, pack sizes, prices, currencies and tax scope;
- discrepancy, condition, substitution, damage and disposition information;
- delivery dates, check status, revision history and calculated comparison results;
- supplier follow-up, promised or received credit, refund or replacement information;
- notes, tasks, reminders, photos, attachments and locally retained source originals;
- generated PDFs, spreadsheets, readable exports and backup metadata;
- device labels, event history, conflict data, retention settings and local legal-notice history; and
- App settings and locally verified purchase-entitlement state.

Operational content can include personal or confidential information even when the App does not require it—for example names, signatures, faces, contact information, bank details or employee activity. Enter only information your organisation is authorized to use and avoid unnecessary sensitive content.

## 3. Limited content-free continuity data

SupplyCheck uses limited opaque local metadata to enforce the one-time five-delivery allowance, prevent duplicates or deleted records from silently reappearing when old packages are merged, and reject late file callbacks after deletion. This metadata is designed not to contain an organisation name, supplier, person, date, amount, attachment, note or other readable business content.

It can include:

- up to five opaque evaluation-claim tokens or anonymous conflict-family claim slots;
- a content-free marker recording that the five-use allowance has been exhausted;
- opaque deletion tombstones and a bounded identity-equivalence ledger; and
- content-free destruction-generation records used to reject stale callbacks.

The tokens and identity metadata may be correlatable with a matching old backup or package held by the customer. The exhaustion marker itself is only a monotonic status value and does not identify a delivery. This continuity data may remain in the App's private storage for the installation lifetime, including after **Delete all organisation data**, because deleting operational content does not restore the free allowance and an old package must not silently resurrect deleted content. Uninstalling or clearing all App storage may remove installation-local continuity data; a fresh installation without a SupplyCheck backup cannot consult data it does not have.

The complete installation-wide identity ledger and callback fence are excluded from the complete readable export and organisation backup. A machine-restorable package carries only the bounded continuity subset needed for safe restore: the exhaustion marker when set; no more than five per-claim equivalence entries; a capacity-bounded terminal-family projection of no more than 4,096 components and 16 MiB; and the minimum package-scoped identity and tombstone mapping needed for content in that package. These opaque mappings can relate packages to one another for deduplication and deletion continuity. They are not included in the human-readable export.

## 4. Information GoodUse Studios may receive

### App-store purchases

Apple or Google processes purchases under its terms and privacy notices. We do not receive your full payment-card or bank-account details. The Store and App may process limited information needed to verify or restore access, such as product, transaction or order reference, purchase status, paid-through or grace status, refund or revocation status, and storefront. Stores may provide GoodUse Studios with sales, tax and financial reports.

The initial App verifies entitlements through StoreKit or Google Play Billing and does not use a GoodUse Studios receipt server. Purchase restoration restores only an eligible entitlement; it does not restore or synchronize operational records.

### Platform diagnostics

The App contains no third-party crash or analytics SDK. Apple or Google may make platform diagnostics available according to the device holder's and Store's settings. The App is designed not to put supplier names, filenames, notes, imported values, record identifiers, amounts, internal paths or photos in its logs or crash messages. GoodUse Studios must reassess this policy and the store declarations if production diagnostics or SDKs change.

### Support and privacy correspondence

If you contact us, we receive the contact details and neutral technical information you choose to provide. For support, send only the platform, device and operating-system version, App version, schema version, locale and neutral error code. Do not send screenshots, orders, invoices, supplier records, photos, databases, backups, payment-card details, passwords or other operational content. If operational content is sent contrary to these instructions, we will not use it as ordinary support input and will restrict or remove it subject to security, legal-preservation and incident-response duties.

We use correspondence to answer the request, troubleshoot using neutral information, handle purchase support, protect the App, meet legal obligations and establish, exercise or defend claims. Email providers may process correspondence outside your country. We retain it only as long as reasonably necessary for those purposes, subject to documented legal, tax, security and dispute-retention requirements.

## 5. Local storage and device security

Live operational data is kept in the operating system's app-private internal storage. The production design uses iOS file data protection and Android private credential-encrypted storage. Operational files are excluded from automatic operating-system/cloud App backup and automatic device-transfer paths; the complete organisation dataset moves only through a deliberate SupplyCheck backup or copy/move action.

SupplyCheck creates no App password, PIN, backup password, recovery key or separate live-database encryption credential. The operating system's device authentication normally controls device access. When native authentication is configured and available, the App requires it for complete readable export, complete backup, copy/move, restore/replace, Finish move, retention-policy changes or conflicts, and deletion of all organisation data. A failed, cancelled, timed-out or interrupted authentication attempt aborts the action. A strong consequence confirmation is used instead only when the operating system reports before prompting that native authentication is unsupported or not configured. Routine supplier sharing uses an exact preview and authority confirmation; per-record deletion uses a record-specific confirmation.

Use a strong device passcode, keep the operating system current and control physical access. GoodUse Studios is responsible for the App sandbox, permissions, temporary-file handling, dependencies, safe defaults and prevention of unintended disclosure caused by the software. The customer is responsible for device and staff access, lawful use, retention choices, selected recipients/providers and deliberate external copies.

No storage system is infallible. Device loss, failure, reset, uninstall, storage corruption or an incompatible update can cause data loss. GoodUse Studios cannot retrieve records that it never receives.

## 6. Photos, files and imports

The App uses system pickers so you select the photo or file to provide. Photos are re-encoded and location/EXIF metadata is removed when they enter the App. Crop and redaction tools are available, and photos are excluded from sharing by default. Keeping an untouched original is a separate, warned, off-by-default choice.

Imported files are treated as untrusted. The App validates supported formats and sizes, does not execute macros, formulas, links or external references, and does not modify or delete the original file in the location you selected. Temporary raw import copies, previews and share files are removed after success or cancellation where possible. Each is unusable no later than 24 hours after creation and is purged before normal use the next time the operating system executes the App. We do not claim physical deletion while the device does not run the App.

## 7. Sharing, exports, backup and device copies

The App distinguishes:

- supplier or internal PDF sharing;
- a filtered analysis spreadsheet;
- **Export all organisation data (readable)**, which produces a versioned ZIP with a canonical UTF-8 JSON dataset, convenience CSV tables and associated files; and
- a complete machine-restorable SupplyCheck backup or copy/move package.

Before a complete-data handoff, the App previews the scope and warns:

> SupplyCheck does not password-protect this file or transfer package. Anyone with access to the destination or file may be able to read it after handoff.

SupplyCheck adds no password or bespoke encryption to exported PDFs, spreadsheets, readable ZIPs, backups or local transfer packages. The system save/share interface hands the selected bytes to the destination you choose. After handoff, the recipient, file provider, messaging service, cloud-storage provider or other destination controls its copy under its terms and practices. The customer is responsible for that destination, authorized recipients, transfer duties, later copies and deletion from external systems. GoodUse Studios cannot recall or remotely delete those copies.

The App keeps a local backup inventory and outward-copy log to help you remember observed saves and handoffs. These observations are not proof that an external file still exists or was delivered, and the App does not claim to delete it. The initial release supports one intended active working copy at a time. A copied or restored package is not live synchronization; copies can diverge.

## 8. Retention inside the App

SupplyCheck applies these local retention choices:

- Temporary quarantine, preview and share files are deleted after success or cancellation where possible and have a maximum 24-hour logical lifetime plus purge on the next App execution.
- A Draft enters a seven-day **Pending deletion** state after 90 days without an edit or a **Keep draft** action, then is permanently deleted on the next safe App run unless kept, edited or completed.
- Record-bound import staging follows its parent record. An unattached or supplier-template staging session enters seven-day **Pending deletion** after 90 days without **Resume import** or **Keep staging**; either action resets its activity anchor.
- After the first completion, the organisation chooses a default of 1 year, 3 years, 7 years or **Manual deletion only** for completed records without open recovery. Until a choice is made, completed records are not automatically deleted. For a record without follow-up, a fixed period runs from the latest substantive completed revision; for a recovery case, it runs from the later of the latest substantive revision and latest resolution or closure. Display-label changes, task/reminder/share status, exports and UI changes do not reset that anchor. An individual record can use the organisation policy or one of the same override choices.
- A fixed-period completed or archived record enters **Pending deletion** seven days before its scheduled deletion. Exporting does not cancel or extend the deadline. **Keep and choose retention** changes the applicable choice.
- Open recovery matters and unresolved conflicts are not automatically deleted.
- Photos, retained originals and exact PDFs marked shared inherit the parent record's retention. Archiving does not stop the retention clock.

Changing a retention choice can make old content immediately eligible for the seven-day Pending-deletion period. The App shows the affected scope before deletion.

## 9. Access, correction and deletion

Because operational content remains under the customer's control on its device, local tools provide the practical access, correction, export and deletion routes:

- search and review records and their history;
- correct a completed record through a traceable revision;
- export all organisation data in the complete readable format;
- permanently delete an individual record and its content-bearing derivatives; or
- use **Delete all organisation data** to remove the live organisation dataset and local content-bearing derivatives.

Deletion cannot recall PDFs, spreadsheets, recipient copies, provider-held exports, old customer-controlled backups or copies on another device. An isolated device restoring a backup made before a later deletion may reintroduce older content because it cannot know the deletion occurred. SupplyCheck does not claim forensic erasure from flash storage. The limited content-free continuity data described in section 3 survives Delete all organisation data.

For records held only by a customer organisation, a person seeking privacy rights should ordinarily contact that organisation. GoodUse Studios cannot search, correct or delete operational content it never received. For personal information GoodUse Studios actually holds, such as support or privacy correspondence, you may request access, correction or deletion, withdraw consent or object where applicable law provides that right. We may verify the request and may retain limited information where required by law or needed for security or legal claims.

You may also have a right to complain to the privacy regulator in your jurisdiction.

## 10. Sale, advertising and tracking

GoodUse Studios does not sell or rent operational content. The App has no ads, behavioural analytics or cross-app tracking and does not share operational content with advertising networks.

## 11. International processing

GoodUse Studios is based in Ontario, Canada. Apple, Google, email providers and destinations you independently select may process the limited information they receive in Canada, the United States or other countries under their own terms, privacy notices and transfer mechanisms. Laws in those places may differ from those where you live.

## 12. Children

The App is a business utility and is not directed to children. We do not knowingly solicit personal information from children through the App. A person who cannot legally agree to the Terms of Use must not purchase or use the App without an authorized adult's involvement.

## 13. Legal disclosures

We may use or disclose information we actually possess when reasonably necessary to comply with law or valid legal process, protect rights or safety, investigate fraud or security incidents, or establish, exercise or defend legal claims. This does not give GoodUse Studios access to operational records held only on a customer's device.

## 14. Changes

We may update this policy when the App, data flows, providers or legal requirements change. We will change the date above and provide any additional notice required for a material change. We will not describe an acknowledgement of this notice as blanket consent for unrelated processing.

## 15. Contact

**Operator:** Lateef Razaq-Oyetola carrying on business as GoodUse Studios  
**Postal address:** 36 Zorra Street, Toronto (Etobicoke), Ontario M8Z 0G5, Canada  
**Privacy Officer:** Lateef Razaq-Oyetola  
**Email:** lrodeveloperr@gmail.com

© 2026 Lateef Razaq-Oyetola carrying on business as GoodUse Studios


<footer class="legal-footer">
SupplyCheck Local · © 2026 Lateef Razaq-Oyetola carrying on business as GoodUse Studios · <a href="mailto:lrodeveloperr@gmail.com">lrodeveloperr@gmail.com</a> · Version 13 August 2026
</footer>
