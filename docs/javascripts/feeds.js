/* Live feeds for the SCN2A example page.
   PubMed, Europe PMC, and ClinicalTrials.gov are queried live in the
   visitor's browser (all three send CORS headers). News is read from a
   JSON file refreshed at build time by a scheduled GitHub Action. */

const GENE = "SCN2A";

function el(tag, cls, html) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (html !== undefined) e.innerHTML = html;
  return e;
}

function esc(s) {
  return (s == null ? "" : String(s)).replace(/[&<>"]/g, c =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

function statusMsg(node, text) {
  node.innerHTML = "";
  node.appendChild(el("p", "feed-status", esc(text)));
}

function feedItem(title, href, meta) {
  const item = el("div", "feed-item");
  const a = el("a", "feed-title", esc(title));
  a.href = href;
  a.target = "_blank";
  a.rel = "noopener";
  item.appendChild(a);
  if (meta) item.appendChild(el("div", "feed-meta", esc(meta)));
  return item;
}

async function loadPubMed(node) {
  statusMsg(node, "Loading latest PubMed articles...");
  try {
    const base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/";
    const term = encodeURIComponent(GENE);
    const s = await fetch(`${base}esearch.fcgi?db=pubmed&term=${term}&sort=date&retmax=15&retmode=json`);
    const ids = (await s.json()).esearchresult.idlist || [];
    if (!ids.length) { statusMsg(node, "No results returned."); return; }
    const d = await fetch(`${base}esummary.fcgi?db=pubmed&id=${ids.join(",")}&retmode=json`);
    const res = (await d.json()).result;
    node.innerHTML = "";
    ids.forEach(id => {
      const r = res[id];
      if (!r) return;
      const authors = (r.authors || []).slice(0, 3).map(a => a.name).join(", ")
        + ((r.authors || []).length > 3 ? ", et al." : "");
      const meta = [r.source, r.pubdate, authors].filter(Boolean).join("  \u00b7  ");
      node.appendChild(feedItem(r.title, `https://pubmed.ncbi.nlm.nih.gov/${id}/`, meta));
    });
  } catch (e) {
    statusMsg(node, "Live PubMed request failed. ");
    const a = el("a", null, "Open this search on PubMed");
    a.href = `https://pubmed.ncbi.nlm.nih.gov/?term=${encodeURIComponent(GENE)}&sort=date`;
    a.target = "_blank"; a.rel = "noopener";
    node.appendChild(a);
  }
}

async function loadPreprints(node) {
  statusMsg(node, "Loading preprints from Europe PMC...");
  try {
    const q = encodeURIComponent(`${GENE} AND SRC:PPR`);
    const url = `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=${q}&format=json&pageSize=15&sort=${encodeURIComponent("P_PDATE_D desc")}`;
    const r = await fetch(url);
    const results = ((await r.json()).resultList || {}).result || [];
    if (!results.length) { statusMsg(node, "No preprints returned."); return; }
    node.innerHTML = "";
    results.forEach(p => {
      const href = p.doi ? `https://doi.org/${p.doi}`
        : `https://europepmc.org/article/${p.source}/${p.id}`;
      const meta = [p.bookOrReportDetails && p.bookOrReportDetails.publisher, p.pubType, p.firstPublicationDate, p.authorString]
        .filter(Boolean).join("  \u00b7  ");
      node.appendChild(feedItem(p.title, href, meta));
    });
  } catch (e) {
    statusMsg(node, "Live Europe PMC request failed. ");
    const a = el("a", null, "Open preprint search on Europe PMC");
    a.href = `https://europepmc.org/search?query=${encodeURIComponent(GENE + " AND SRC:PPR")}`;
    a.target = "_blank"; a.rel = "noopener";
    node.appendChild(a);
  }
}

async function loadTrials(node) {
  statusMsg(node, "Loading clinical trials...");
  try {
    const url = `https://clinicaltrials.gov/api/v2/studies?query.term=${encodeURIComponent(GENE)}&pageSize=15&sort=LastUpdatePostDate:desc`;
    const r = await fetch(url);
    const studies = (await r.json()).studies || [];
    if (!studies.length) { statusMsg(node, "No trials returned."); return; }
    node.innerHTML = "";
    studies.forEach(s => {
      const p = s.protocolSection || {};
      const idm = p.identificationModule || {};
      const status = (p.statusModule || {}).overallStatus;
      const phases = ((p.designModule || {}).phases || []).join(", ");
      const meta = [status, phases, idm.nctId].filter(Boolean).join("  \u00b7  ");
      node.appendChild(feedItem(idm.briefTitle || idm.officialTitle || idm.nctId,
        `https://clinicaltrials.gov/study/${idm.nctId}`, meta));
    });
  } catch (e) {
    statusMsg(node, "Live ClinicalTrials.gov request failed. ");
    const a = el("a", null, "Open trial search on ClinicalTrials.gov");
    a.href = `https://clinicaltrials.gov/search?term=${encodeURIComponent(GENE)}`;
    a.target = "_blank"; a.rel = "noopener";
    node.appendChild(a);
  }
}

async function loadNews(node) {
  statusMsg(node, "Loading news...");
  try {
    const r = await fetch("data/scn2a_news.json", { cache: "no-store" });
    const data = await r.json();
    const items = data.items || [];
    if (!items.length) {
      statusMsg(node, "No news items yet. The news feed populates at build time.");
    } else {
      node.innerHTML = "";
      if (data.generated) {
        node.appendChild(el("p", "feed-status", "Updated " + esc(data.generated)));
      }
      items.slice(0, 15).forEach(n => {
        const meta = [n.source, n.published].filter(Boolean).join("  \u00b7  ");
        node.appendChild(feedItem(n.title, n.link, meta));
      });
    }
  } catch (e) {
    statusMsg(node, "News file not available yet.");
  }
  const live = el("p", "feed-live-link");
  const a = el("a", null, "Open a live Google News search for " + GENE);
  a.href = `https://news.google.com/search?q=${encodeURIComponent(GENE)}`;
  a.target = "_blank"; a.rel = "noopener";
  live.appendChild(a);
  node.appendChild(live);
}

async function loadResearchers(node) {
  statusMsg(node, "Loading researchers...");
  try {
    const r = await fetch("data/scn2a_researchers.json", { cache: "no-store" });
    const data = await r.json();
    const people = data.researchers || [];
    if (!people.length) {
      statusMsg(node, "No researchers yet. The list populates at build time from OpenAlex.");
      return;
    }
    node.innerHTML = "";
    const head = el("p", "feed-status",
      `${data.researchers_with_orcid} researchers with ORCID from ${data.total_works_scanned} works`
      + (data.generated ? "  \u00b7  updated " + esc(data.generated) : ""));
    node.appendChild(head);
    people.forEach(p => {
      const item = el("div", "feed-item");
      const a = el("a", "feed-title", esc(p.name || p.orcid));
      a.href = p.orcid_url; a.target = "_blank"; a.rel = "noopener";
      item.appendChild(a);
      const bits = [];
      bits.push(p.works_count + (p.works_count === 1 ? " work" : " works"));
      if (p.institutions && p.institutions.length) bits.push(p.institutions[0]);
      if (p.orcid) bits.push(p.orcid);
      item.appendChild(el("div", "feed-meta", esc(bits.join("  \u00b7  "))));
      node.appendChild(item);
    });
  } catch (e) {
    statusMsg(node, "Researcher list not available yet.");
  }
}

function initFeeds() {
  const map = {
    "feed-pubmed": loadPubMed,
    "feed-preprints": loadPreprints,
    "feed-trials": loadTrials,
    "feed-news": loadNews,
    "feed-researchers": loadResearchers,
  };
  Object.keys(map).forEach(id => {
    const node = document.getElementById(id);
    if (node) map[id](node);
  });
}

/* Works with Material instant navigation and plain page loads. */
if (typeof document$ !== "undefined" && document$.subscribe) {
  document$.subscribe(initFeeds);
} else {
  document.addEventListener("DOMContentLoaded", initFeeds);
}
