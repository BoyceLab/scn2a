# Live feeds

This page pulls current SCN2A activity from public sources. Publications, preprints, and trials are queried live in your browser each time the page loads, so they are always current. News is refreshed on a schedule at build time.

!!! info "How the feeds work"
    PubMed, Europe PMC, and ClinicalTrials.gov allow direct browser requests, so those panels are genuinely live and require no server. The Europe PMC full text panel surfaces articles across all sources, including full text matches, with a cited-by count and a link to the Europe PMC article page where citing articles and grant links live. The NIH RePORTER grants panel and the news panel are refreshed on a schedule at build time, because those services are better queried server side. Every panel falls back to a direct search link if a live request does not complete.

<div class="feed-grid" markdown="0">
  <div class="feed-panel">
    <h3>Latest publications (PubMed)</h3>
    <div class="feed-body" id="feed-pubmed"></div>
  </div>
  <div class="feed-panel">
    <h3>Full text and citations (Europe PMC)</h3>
    <div class="feed-body" id="feed-fulltext"></div>
  </div>
  <div class="feed-panel">
    <h3>Preprints (Europe PMC)</h3>
    <div class="feed-body" id="feed-preprints"></div>
  </div>
  <div class="feed-panel">
    <h3>Federal grants (NIH RePORTER)</h3>
    <div class="feed-body" id="feed-grants"></div>
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

## Sources behind these feeds

Each panel is a direct query against a public source. Follow any of them to search yourself:

- Publications: [PubMed](https://pubmed.ncbi.nlm.nih.gov/) via the [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) API.
- Full text, citations, and preprints: [Europe PMC](https://europepmc.org/) via its [REST API](https://europepmc.org/RestfulWebService).
- Federal grants: [NIH RePORTER](https://reporter.nih.gov/) via its [public project API](https://api.reporter.nih.gov/).
- Clinical trials: [ClinicalTrials.gov](https://clinicaltrials.gov/) via its [API v2](https://clinicaltrials.gov/data-api/api).
- News: a [Google News](https://news.google.com/) query fetched at build time.
- Researcher harvesting draws on [OpenAlex](https://openalex.org/). See the [Researchers](researchers.md) page.

For the full list of standards and data sources used across this site, see the [References](references.md) page.

## Feeding the portfolio graph

These feeds are not only for reading. Each publication, preprint, and trial carries the identifiers the schema uses as keys: PubMed IDs and DOIs for publications, DOIs for preprints, and NCT numbers for trials. A scheduled job can harvest these and create or update `Publication`, `ResearchActivity`, and `uses_dataset` nodes and edges automatically, which is exactly the self-population strategy described on the [Identifier and Standards Registry](identifiers.md) page.
