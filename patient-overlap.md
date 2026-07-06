:root {
  --md-primary-fg-color: #0f766e;
  --md-primary-fg-color--light: #14b8a6;
  --md-primary-fg-color--dark: #115e59;
  --node-line: #99f6e4;
}

[data-md-color-scheme="slate"] {
  --md-primary-fg-color: #14b8a6;
  --node-line: #134e4a;
}

/* Signature: node-key badge used to tag each entity with its persistent identifier scheme */
.pid-badge {
  display: inline-block;
  font-family: "JetBrains Mono", monospace;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  padding: 0.08rem 0.5rem;
  border-radius: 999px;
  border: 1px solid var(--md-primary-fg-color--light);
  color: var(--md-primary-fg-color--dark);
  background: color-mix(in srgb, var(--md-primary-fg-color--light) 12%, transparent);
  white-space: nowrap;
}

[data-md-color-scheme="slate"] .pid-badge {
  color: var(--md-primary-fg-color--light);
}

/* Reference tables read as a schema, not prose */
.md-typeset table:not([class]) {
  font-size: 0.78rem;
}

.md-typeset table:not([class]) th {
  background: color-mix(in srgb, var(--md-primary-fg-color) 10%, transparent);
}

/* Layer stack on the overview */
.layer-stack {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  margin: 1.2rem 0;
}

.layer-stack .layer {
  border-left: 3px solid var(--md-primary-fg-color--light);
  padding: 0.5rem 0.9rem;
  background: color-mix(in srgb, var(--md-primary-fg-color) 5%, transparent);
  border-radius: 0 6px 6px 0;
}

.layer-stack .layer strong {
  color: var(--md-primary-fg-color--dark);
}

[data-md-color-scheme="slate"] .layer-stack .layer strong {
  color: var(--md-primary-fg-color--light);
}

/* Live feed cards */
.feed-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1.2rem 0;
}

.feed-panel {
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 10px;
  padding: 0.9rem 1rem 1rem;
  background: color-mix(in srgb, var(--md-primary-fg-color) 3%, transparent);
}

.feed-panel h3 {
  margin: 0 0 0.6rem;
  font-size: 0.9rem;
  letter-spacing: 0.02em;
  border-bottom: 2px solid var(--md-primary-fg-color--light);
  padding-bottom: 0.35rem;
}

.feed-body {
  max-height: 460px;
  overflow-y: auto;
}

.feed-item {
  padding: 0.5rem 0;
  border-bottom: 1px dashed var(--md-default-fg-color--lightest);
}

.feed-item:last-child { border-bottom: none; }

.feed-title {
  font-size: 0.82rem;
  font-weight: 600;
  line-height: 1.3;
}

.feed-meta {
  font-size: 0.72rem;
  color: var(--md-default-fg-color--light);
  margin-top: 0.2rem;
}

.feed-status {
  font-size: 0.78rem;
  color: var(--md-default-fg-color--light);
  font-style: italic;
}

.feed-live-link {
  margin: 0.6rem 0 0;
  font-size: 0.78rem;
}
