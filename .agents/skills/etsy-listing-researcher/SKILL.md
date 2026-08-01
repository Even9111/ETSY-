---
name: etsy-listing-researcher
description: Evidence-backed Etsy SEO research and listing creation for physical products. Use when Codex must study a user's Etsy product, inspect comparable and recently active listings, validate search terms on Etsy, and produce an optimized title, 13 tags, description, attributes, image plan, and competitive recommendations for products such as keychains, bag charms, phone straps, lanyards, jewelry, accessories, and gifts.
---

# Etsy Listing Researcher

## Objective

Turn a user's product link, photos, or description into Etsy listing materials aimed at organic discovery and conversion. Treat the work as an operator-led research task: independently choose search routes, inspect public evidence, compare cohorts, and make the final recommendation without requiring the user to specify every research step.

This skill applies to any physical Etsy product, not only keychain wristlets. Adapt the product vocabulary, buyer use cases, category, attributes, and competitor set to the actual item.

## Accepted inputs

- A local product image dragged into the chat: inspect the visible product directly and build the product brief before searching Etsy.
- Multiple local images: compare front, back, detail, color, packaging, and variant views; do not treat multiple photos of one item as separate products.
- An Etsy listing URL: read the public listing and use its verified facts as the product brief.
- An image plus short notes: use the image for visual facts and the notes for facts that cannot be confirmed visually, such as exact material, dimensions, or customization.
- One or more local product-folder paths pasted in chat: treat each direct child folder as one product unless the user explicitly says otherwise. Use the folder name as the product short name/SKU family label, inspect only supported image files inside that folder, and process folders independently.

When a local image does not establish an exact material, size, compatibility, or variant name, label it as unconfirmed and avoid using it as a hard SEO claim until the user confirms it.

## Batch folder mode

Activate batch mode when the user pastes two or more local folder paths, or explicitly asks to process a folder of product images. The user may paste paths separated by newlines, spaces, commas, or code fences.

For each folder:

1. Resolve and validate the exact folder path. Do not scan the entire home directory or workspace recursively.
2. Use the final folder name as the product short name. Keep the original folder and image filenames unchanged.
3. Read supported product images (`.jpg`, `.jpeg`, `.png`, `.webp`, `.avif`, `.heic`, `.heif`) and ignore hidden files, existing generated outputs, previews, and unrelated documents.
4. Treat all images in that folder as one product unless the user labels subfolders or filenames as separate variants/products. Use image filenames as optional variant clues, never as product facts by themselves.
5. Run the full research workflow independently for each product. Do not let one product's materials, colors, dimensions, or SEO terms leak into another product.
6. Save a copy-ready workbook back into the same product folder after research. Preferred filename: `<folder-name>_etsy_listing.xlsx`; if that file exists, create `<folder-name>_etsy_listing_v2.xlsx`, then increment the suffix rather than overwriting. Also save a compact `<folder-name>_etsy_listing.md` only when a plain-text backup is useful.
7. The workbook should contain, at minimum, these sheets: `上架资料`, `英文描述`, `13 Tags`, `SKU变体`, `竞品依据`, and `发布检查`. The `竞品依据` sheet must contain the full researched link set for that product, not only representative examples; include at least 30 unique public listing URLs when the research request calls for 30 listings, with source query, public signal, detail-page observations, evidence status, limitations, and URL columns.
8. Keep generated files inside the corresponding product folder. Never write generated files into the image folder's parent or another product's folder unless the user asks for a combined report.
9. In the chat response, provide a compact batch summary: folder name, image count, output workbook path, title/tag/SKU validation result, and any blocked or unconfirmed fields. The full copy remains in each workbook.

Batch safety and recovery:

- Never delete, rename, move, or overwrite the user's product images.
- If a folder contains no supported images, skip research for that folder and report the exact reason.
- If one folder fails, continue processing the remaining valid folders and report per-folder status.
- If a generated workbook is open or locked, save a suffixed copy and report it.
- Before writing, list the exact output path for each folder in the working notes; after writing, verify the file exists and inspect the workbook's key ranges and visual rendering.

## Evidence rules

- Use the public Etsy UI through the browser skill when live Etsy research is required. Do not bypass login, CAPTCHA, rate limits, paywalls, or hidden seller systems.
- Never claim access to a seller's private 13 tags unless the page visibly exposes them. Label outputs as `verified`, `observed`, or `recommended`.
- `verified`: directly visible on the user's page or a competitor page, such as title, category, material, price, badge, review count, favorites, purchase prompt, or description wording.
- `observed`: repeated across multiple real listings, search result cards, Etsy filters, visible autocomplete, or buyer reviews.
- `recommended`: an operator-selected phrase assembled from verified/observed evidence and matched to the user's actual product.
- Do not treat shop-wide sales as item sales. Report them as shop sales. Treat `In demand`, “bought this in the last 24 hours,” `Bestseller`, `Etsy's Pick`, `Popular now`, favorites, and item reviews as separate signals.
- Do not claim exact Etsy search volume when Etsy does not expose it. Use result-count bands, ranking, repeated appearance, badges, reviews, favorites, and relevance as proxies and state the limitation.
- Do not use a competitor's trademark, protected character, brand, or unsupported material/customization claim for the user's product.

## Research workflow

### 1. Build the product brief

Read the user's listing or inspect supplied photos before searching. Record:

- product type and likely Etsy category;
- construction, material, size, closure/hardware, colors, variants, and customization;
- real functions and use cases;
- style language supported by the product (for example boho, minimalist, cottagecore, vintage);
- gift audiences and occasions only when the product genuinely fits them;
- unsupported claims to exclude.

If the product page contradicts a user description, prefer the visible product facts and flag the conflict.

### 2. Generate independent search routes

Create several query families, not one guessed phrase:

1. Core product: what the item is.
2. Material/construction: what it is made from or how it is made.
3. Function/use case: what buyers attach, carry, or wear.
4. Style/aesthetic: how buyers describe its look.
5. Gift/recipient: only when supported.

Test Etsy's homepage search field where text suggestions are actually exposed. If the homepage only shows promotional category tiles or no stable text suggestions, record that fact and do not present the tiles as search keywords. Also test the selected queries on Etsy search result pages and record visible filters, result bands, ranking, and top-card language.

### 3. Build two competitor cohorts

Use public Etsy results to create two complementary cohorts:

- **Evergreen cohort:** roughly 15–30 unique, highly relevant listings with long-term signals such as high item reviews, favorites, Bestseller, Etsy's Pick, strong shop history, or repeated appearance across queries.
- **Recent-demand cohort:** when the user asks for current/weekly demand, screen at least 30 candidates and deeply inspect the strongest unique listings with recent listing dates, `In demand`, recent-purchase prompts, `Popular now`, new favorites, item reviews, or other visible activity. The public UI may not expose a true 7-day order ranking; report this as a recent-demand signal cohort, not a verified weekly sales leaderboard.

Deduplicate same-shop variants and near-identical listings when measuring common patterns. Keep the URLs for traceability even when variants are grouped.

### 4. Deeply inspect selected listing pages

Open each selected listing page, not only the result card. Capture a compact record containing:

- canonical URL, query route, title, and category/breadcrumbs;
- visible badges, item reviews, favorites, purchase prompts, listing date, price, discount, and shipping/return terms;
- shop name, Star Seller status, shop rating, shop age, and shop-wide sales, explicitly labeled;
- materials, dimensions, colors, hardware, personalization, and included components;
- the full description's product nouns, use cases, benefits, and buyer objections;
- a small set of buyer-review phrases and recurring themes when reviews are visible;
- image/alt-text clues only as supporting evidence, never as a substitute for visual product verification.

For fragile or dynamic pages, record what was visible and continue with the next page. Do not invent missing fields.

### 5. Score and compare evidence

Use judgment rather than a false precision ranking. A useful default is:

`relevance 30% + item-level demand signals 25% + review/favorite strength 20% + query coverage 15% + shop quality 10%`

Recent-demand scoring can add weight for a visible purchase prompt, recent listing date, or `Popular now`; evergreen scoring can add weight for item-review depth and repeated query placement. Keep shop-wide sales separate from item-level evidence.

Find common structures across both cohorts:

- words repeatedly used by strong listings;
- words that appear across independent search routes;
- buyer language that supports click and conversion;
- product attributes that distinguish high-performing listings;
- title order, clarity, and use-case coverage;
- pricing, shipping, photography, personalization, and gift positioning.

### 6. Validate the candidate search terms

Before finalizing 13 tags, search each candidate phrase on Etsy. For each phrase, record:

- visible result band (for example `1,000+ items`);
- whether the first relevant results include the user's product type;
- relevant top listings and their URLs;
- Bestseller, Etsy's Pick, Popular now, In demand, favorites, and review signals;
- whether the term is precise, broad, misleading, or dominated by another product class.

Keep a phrase when it has both evidence and product fit. Remove broad words that bring mostly unrelated products, even if they have large result counts. Keep style/gift terms secondary when they are useful for description or seasonal collections but weak as primary tags.

### 7. Generate the final listing package

Produce in Chinese explanation plus copy-ready English Etsy fields:

1. Product positioning in one sentence.
2. Recommended title, plus one alternate if materially useful. Put the strongest product phrase early, avoid repetitive stuffing, and do not use unsupported materials or personalization.
3. Exactly 13 tags, each mapped to evidence, intent, and product fit. Every tag must be 20 or fewer English characters including spaces. Do not pretend they are a competitor's private tags.
4. A SKU for every visible style/color/pattern variant. Derive it from the product family plus the actual visual variant (for example, `FLORAL-BLK-GOLD`), keep it unique within the listing, and keep it to 20 or fewer English letters, numbers, and hyphens.
5. Description with an opening keyword-rich but natural paragraph, features, use cases, materials, size, variants, included items, care/handmade notes, and gift positioning.
6. Category and attribute recommendations.
7. Price and shipping comparison, clearly labeled as market observation rather than a pricing mandate.
8. Photo and conversion recommendations based on competitor patterns and buyer-review objections.
9. Evidence appendix: research date, cohorts, top links, signals, keyword frequency/coverage, exclusions, and uncertainties.

Use the long-form description style in [references/description-template.md](references/description-template.md) unless the user requests a different format. Keep the user's preferred visual rhythm: an emoji-led headline, bold section headings, short benefit-led paragraphs, concrete use cases, construction details, dimensions, variants, what's included, important product-specific notes, and customer-service language. Select emojis from the actual product palette, motif, and aesthetic; use restrained, varied symbols rather than repeating a fixed emoji set. Never add a color, charm, material, safety claim, adjustment range, accessory, or defect note unless it is verified for the user's product.

## Hard length and naming constraints

- Make the final English title 135–140 characters inclusive. Aim for 137–139 characters, never exceed 140, and never pad with irrelevant repetition. Count letters, spaces, punctuation, and digits. If a natural title cannot reach 135 characters, add only verified product attributes, use cases, style, recipient, or gift context; do not invent claims.
- Provide exactly 13 English tags. Each tag must be 20 or fewer characters including spaces and punctuation. Prefer distinct search intents over repeated synonyms.
- Generate SKU names from the actual image-visible style, color, motif, hardware, or variant. Use short uppercase tokens separated by hyphens, such as `FLORAL-BLK-GOLD`, `RUFFLE-PINK-SILVER`, or `BOW-IVORY-ANTQ`. Keep each SKU at 20 or fewer characters and make sibling variants unique.
- Run the bundled validator [scripts/validate_listing_text.py](scripts/validate_listing_text.py) before delivery when producing a final package. If it reports an error, revise and rerun it.

## Output quality checklist

Before delivering, confirm:

- the title describes the user's actual product;
- all 13 tags are distinct, relevant, and supported by observed evidence;
- at least one core product phrase is validated through Etsy search and strong competitor pages;
- recent-demand and evergreen evidence are not conflated;
- shop sales are not reported as item sales;
- unavailable search volume or private tags are labeled unavailable;
- no competitor text is copied verbatim at material length;
- the final recommendation explains what to prioritize and what to avoid.

See [references/research-record.md](references/research-record.md) for the recommended per-listing record and final evidence table.
