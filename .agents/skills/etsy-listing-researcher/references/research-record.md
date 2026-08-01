# Etsy research record

Use this schema internally or as an evidence appendix. Keep one row per unique listing; group same-shop variants when interpreting patterns.

## Listing record

| Field | What to record |
|---|---|
| listing_id | Etsy listing ID |
| url | Canonical public listing URL |
| query_route | Search phrase that surfaced it |
| cohort | evergreen or recent-demand |
| title | Visible listing title |
| category | Breadcrumb/category |
| item_signals | Bestseller, Etsy's Pick, Popular now, In demand, purchase prompt |
| item_reviews | Visible item review count and rating |
| favorites | Visible listing favorites |
| listing_date | Visible listed-on date |
| price | Visible price and sale state |
| shop_signals | Star Seller, shop rating, shop age, shop-wide sales |
| materials_size | Visible materials, dimensions, colors, hardware |
| functions | Keys, phone, camera, bag, jewelry, gift, etc. |
| description_terms | Product nouns, benefits, use cases, style terms |
| review_language | Short buyer phrases and themes |
| confidence | High/medium/low based on direct visibility |

## Phrase validation record

| Field | What to record |
|---|---|
| phrase | Candidate title/tag phrase |
| source | Listing titles, descriptions, reviews, Etsy search, filters, or autocomplete |
| competitor_coverage | Count of independent relevant listings using it |
| query_result_band | Visible Etsy result band; never call it exact search volume |
| top_evidence | URLs, ratings, favorites, badges, or purchase prompts |
| intent | Core product, material, function, style, recipient, or gift |
| fit | Exact/strong/weak match to user's product |
| decision | Title, tag, description only, or exclude |
| notes | Risks such as broad traffic, unsupported material, or personalization mismatch |

## Final evidence appendix

Summarize:

- research date and locale;
- user's product facts;
- number of unique evergreen and recent-demand pages deeply inspected;
- number of candidate phrases tested;
- top 5–10 evidence links;
- the 13 final tags with source and reason;
- excluded phrases and why;
- what Etsy did not expose, such as exact weekly orders, exact search volume, or private seller tags.
