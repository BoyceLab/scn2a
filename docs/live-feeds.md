# Live feeds

This page pulls current SCN2A activity from public sources. Publications, preprints, and trials are queried live in your browser each time the page loads, so they are always current. News is refreshed on a schedule at build time.

!!! info "How the feeds work"
    PubMed, Europe PMC, and ClinicalTrials.gov all allow direct browser requests, so those three panels are genuinely live and require no server. The news panel reads a small file that a scheduled GitHub Action regenerates from a Google News query, which avoids the browser restrictions that block fetching news directly. Every panel falls back to a direct search link if a live request does not complete.

<div class="feed-grid" markdown="0">
  <div class="feed-panel">
    <h3>Latest publications (PubMed)</h3>
    <div class="feed-body" id="feed-pubmed"></div>
  </div>
  <div class="feed-panel">
    <h3>Preprints (Europe PMC)</h3>
    <div class="feed-body" id="feed-preprints"></div>
  </div>
  <div class="feed-panel">
    <h3>Clinical trials (ClinicalTrials.gov)</h3>
    <div class="feed-body" id="feed-trials"></div>
  </div>
  <div class="feed-panel">
    <h3>News</h3>
    <div class="feed-body" id="feed-news"></div>
  </div>
</div>

## Adding more sources

The same client-side pattern extends to any source that permits browser requests. Natural additions for a gene community:

- **NIH RePORTER** for federally funded grants mentioning the gene, through its public project API.
- **Europe PMC full text** searches, already used here for preprints, can also surface citing articles and grant links.
- **OpenAlex** for a broader works graph, including authors and institutions, which can feed the Person and Organization nodes of the portfolio directly.

## Feeding the portfolio graph

These feeds are not only for reading. Each publication, preprint, and trial carries the identifiers the schema uses as keys: PubMed IDs and DOIs for publications, DOIs for preprints, and NCT numbers for trials. A scheduled job can harvest these and create or update `Publication`, `ResearchActivity`, and `uses_dataset` nodes and edges automatically, which is exactly the self-population strategy described on the [Identifier and Standards Registry](identifiers.md) page.
