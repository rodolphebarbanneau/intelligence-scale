const QUADRANTS = {
  Leaders: "Agency can shift, and the product is a company surface, not a craft tool.",
  Challengers: "Company-wide, still human-operated. Many teams can put work on it. AI still assists rather than owns the process.",
  Visionaries: "Deep AI in one craft or function. Work can move toward AI inside a specialist lane. The rest of the company has no native path onto it.",
  Niche: "Thin on both scales. Limited agency shift, and limited organizational coverage.",
};

const CRITERIA = {
  "I.1": { name: "Routine AI assistance", blurb: "AI sits in normal work, not only as an experiment." },
  "I.2": { name: "Context and capability access", blurb: "AI can reach the data and tools real work needs." },
  "I.3": { name: "Bounded autonomous tasks", blurb: "AI can run a multi-step task inside a bounded objective." },
  "I.4": { name: "Human direction and review", blurb: "People can start, inspect, and correct the work." },
  "I.5": { name: "Repeatable organizational use", blurb: "The product supports ongoing use, not one-off demos." },
  "II.1": { name: "End-to-end process ownership", blurb: "A persistent AI actor can own a full process over time." },
  "II.2": { name: "Process-level execution", blurb: "AI progresses the process without a human at every step." },
  "II.3": { name: "Multi-capability execution", blurb: "The actor uses the tools needed to finish the process." },
  "II.4": { name: "Persistent AI actor", blurb: "A durable worker with identity, state, and permissions." },
  "II.5": { name: "Human supervision and exceptions", blurb: "People supervise and handle exceptions, not execute." },
  "II.6": { name: "Autonomous initiation and continuity", blurb: "Work can start or continue without a manual kickoff." },
  "II.7": { name: "Whole-process outcome", blurb: "Routine cases end in their outcome, not a draft a person finishes." },
  "III.1": { name: "Autonomous routine operations", blurb: "Whole processes run with no structural human step." },
  "III.2": { name: "Work determination and allocation", blurb: "AI decides what should happen next and who does it." },
  "III.3": { name: "AI-to-AI coordination", blurb: "Persistent actors coordinate without a human broker." },
  "III.4": { name: "Closed operational loop", blurb: "Detect, decide, execute, observe, and feed the next decision." },
  "III.5": { name: "Adaptive orchestration", blurb: "AI can change how work is organized when conditions change." },
  "III.6": { name: "Governance-level human role", blurb: "People govern through enforced policy, budgets, and risk limits." },
  "E.1": { name: "Domain span", blurb: "Whose work fits on the product as it ships." },
  "E.2": { name: "Shared work", blurb: "Several people, and an operator, can work on the same thing." },
  "E.3": { name: "System reach", blurb: "The product can read and write systems the company already runs." },
  "E.4": { name: "Extensible coverage", blurb: "Coverage can grow through an open catalog the product ships." },
  "E.5": { name: "Work surfaces", blurb: "Where that work can happen." },
  "E.6": { name: "Adoption path", blurb: "A team can put work on it without assembling the core system." },
  "E.7": { name: "Ready-made coverage", blurb: "A team reaches a working job without designing it by hand." },
};

const ROOT = /(?:^|\/)site\/[^/]*$/.test(location.pathname) ? "../" : "";

function fromRoot(path) {
  return ROOT + path;
}

const DOCS = [
  { id: "intelligence-scale", file: "intelligence-scale.md", label: "Intelligence Scale" },
  { id: "execution-scale", file: "execution-scale.md", label: "Execution Scale" },
  { id: "quadrant", file: "quadrant.md", label: "The quadrant" },
];

const SUN = '<svg class="sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4l1.4-1.4M17 7l1.4-1.4"></path></svg>';
const MOON = '<svg class="moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M16 3a8 8 0 1 0 5 14 7 7 0 0 1-5-14z"></path></svg>';

const themeButton = document.querySelector("#theme");
if (themeButton) {
  themeButton.innerHTML = SUN + MOON;
  syncThemeButton();
  themeButton.addEventListener("click", () => {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    localStorage.setItem("theme", next);
    syncThemeButton();
  });
}

const tip = document.querySelector("#tip");
if (tip) {
  document.addEventListener("click", (event) => {
    if (!tip.hidden && !event.target.closest(".quad-label, .dot, .mark-wrap")) {
      hideTip();
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") hideTip();
  });
}

if (document.querySelector("#ratings")) initIndex();
if (document.querySelector("#product")) initProduct();
if (document.querySelector("#docs")) initDocs();

function syncThemeButton() {
  if (!themeButton) return;
  const dark = document.documentElement.dataset.theme === "dark";
  themeButton.setAttribute("aria-label", dark ? "Use light theme" : "Use dark theme");
}

async function initIndex() {
  const runSelect = document.querySelector("#run");
  const status = document.querySelector("#status");
  const plot = document.querySelector("#plot");
  const chart = document.querySelector("#chart");
  const tableBar = document.querySelector("#table-bar");
  const tbody = document.querySelector("#ratings tbody");
  const empty = document.querySelector("#table-empty");
  const search = document.querySelector("#table-search");
  const quadrantFilter = document.querySelector("#quadrant-filter");
  const params = new URLSearchParams(location.search);
  const state = { specs: [], runId: "", sort: "score", dir: "desc", query: "", quadrant: "" };

  runSelect.addEventListener("change", () => {
    try {
      const url = new URL(location.href);
      url.searchParams.set("run", runSelect.value);
      history.replaceState(null, "", url);
    } catch (error) {
      // A page opened as a file cannot always rewrite its address.
    }
    loadRun(runSelect.value);
  });

  search.addEventListener("input", () => {
    state.query = search.value.trim().toLowerCase();
    renderTable();
    applyMatchState();
  });
  quadrantFilter.addEventListener("change", () => {
    state.quadrant = quadrantFilter.value;
    renderTable();
    applyMatchState();
  });
  document.querySelectorAll(".sort").forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.dataset.sort;
      if (state.sort === key) state.dir = state.dir === "asc" ? "desc" : "asc";
      else {
        state.sort = key;
        state.dir = key === "name" || key === "quadrant" ? "asc" : "desc";
      }
      renderTable();
    });
  });
  chart.querySelectorAll(".quad-label").forEach((button) => {
    const name = button.dataset.quad;
    button.addEventListener("pointerenter", () => showTip(button, `<strong>${escapeHtml(name)}</strong><p>${escapeHtml(QUADRANTS[name] || "")}</p>`));
    button.addEventListener("pointerleave", hideTip);
    button.addEventListener("focus", () => showTip(button, `<strong>${escapeHtml(name)}</strong><p>${escapeHtml(QUADRANTS[name] || "")}</p>`));
    button.addEventListener("blur", hideTip);
  });
  window.addEventListener("resize", () => placeLabels(chart));

  const published = await loadCatalog(fromRoot("output/index.json"));
  const tests = await loadCatalog(fromRoot("output/test-index.json"));
  if (!published && !tests) {
    status.textContent = "Could not read output/index.json.";
    return;
  }
  const runs = mergeRuns(published, tests);
  if (!runs.length) {
    status.textContent = "No runs yet. A published release writes the first folder under output/.";
    runSelect.disabled = true;
    return;
  }
  for (const run of runs) {
    const option = document.createElement("option");
    option.value = run.id;
    option.textContent = run.created ? `${run.id} · ${run.created}` : run.id;
    runSelect.append(option);
  }
  const requested = params.get("run");
  const initial = runs.some((run) => run.id === requested) ? requested : runs[0].id;
  runSelect.value = initial;
  await loadRun(initial);

  async function loadRun(id) {
    status.textContent = "Loading run…";
    plot.hidden = true;
    tableBar.hidden = true;
    chart.querySelectorAll(".mark-wrap").forEach((node) => node.remove());
    tbody.replaceChildren();
    state.specs = [];
    state.runId = id;
    let current;
    try {
      current = await loadRunFile(id);
    } catch (error) {
      status.textContent = "Could not read that run.";
      return;
    }
    setCommitStatus(status, current.git);
    state.specs = current.specs || [];
    for (const group of plotGroups(state.specs)) {
      const members = group.specs;
      const wrap = document.createElement("div");
      wrap.className = "mark-wrap";
      wrap.dataset.slugs = members.map((spec) => spec.slug).join(" ");
      wrap.style.left = `${clamp((Number(group.x) + 1) / 2 * 100)}%`;
      wrap.style.top = `${clamp((1 - Number(group.y)) / 2 * 100)}%`;
      const first = members[0];
      const typeValue = axisValue(first.type);
      const coverageValue = axisValue(first.exec);
      const type = typeValue != null ? typeValue.toFixed(2) : "—";
      const coverage = coverageValue != null ? coverageValue.toFixed(2) : "—";
      const score = specScore(first);
      const scoreText = score < 0 ? "—" : String(score);
      const names = members.map((spec) => spec.name || spec.slug);
      const slugs = members.map((spec) => spec.slug);
      const stacked = members.length > 1;
      const dot = document.createElement(stacked ? "button" : "a");
      dot.className = "dot";
      if (stacked) dot.type = "button";
      else dot.href = productUrl(id, first.slug);
      dot.setAttribute("aria-label", `${names.join(", ")}, score ${scoreText}, type ${type}, coverage ${coverage}, ${displayQuadrant(first.quadrant) || "unplotted"}`);
      const tipHtml = groupTip(members);
      const enter = () => {
        highlight(slugs);
        showTip(dot, tipHtml);
      };
      const leave = () => {
        highlight([]);
        hideTip();
      };
      dot.addEventListener("pointerenter", enter);
      dot.addEventListener("pointerleave", leave);
      dot.addEventListener("focus", enter);
      dot.addEventListener("blur", leave);
      const label = document.createElement("span");
      label.className = stacked ? "dot-label is-stack" : "dot-label";
      for (const spec of members) {
        const link = document.createElement("a");
        link.href = productUrl(id, spec.slug);
        link.textContent = spec.name || spec.slug;
        link.addEventListener("pointerenter", enter);
        link.addEventListener("pointerleave", leave);
        link.addEventListener("focus", enter);
        link.addEventListener("blur", leave);
        label.append(link);
      }
      wrap.append(dot, label);
      chart.append(wrap);
    }
    renderTable();
    plot.hidden = false;
    tableBar.hidden = false;
    requestAnimationFrame(() => placeLabels(chart));
  }

  function renderTable() {
    const visible = filteredSpecs(state);
    document.querySelectorAll(".sort").forEach((button) => {
      button.removeAttribute("aria-sort");
      if (button.dataset.sort === state.sort) button.setAttribute("aria-sort", state.dir === "asc" ? "ascending" : "descending");
    });
    tbody.replaceChildren();
    empty.hidden = visible.length > 0;
    for (const spec of visible) {
      const href = productUrl(state.runId, spec.slug);
      const row = document.createElement("tr");
      row.className = "spec";
      row.dataset.slug = spec.slug;
      const nameCell = document.createElement("td");
      const name = document.createElement("a");
      name.href = href;
      name.textContent = spec.name || spec.slug;
      nameCell.append(name);
      const quadrant = document.createElement("td");
      quadrant.innerHTML = `<span class="chip">${escapeHtml(displayQuadrant(spec.quadrant) || "Unplotted")}</span>`;
      const compound = document.createElement("td");
      compound.className = "compound";
      const score = specScore(spec);
      compound.textContent = score < 0 ? "—" : String(score);
      row.append(nameCell, quadrant, compound);
      row.append(scoreCell(spec.type, 3, 2));
      row.append(scoreCell(spec.exec, 1, 2));
      row.addEventListener("click", (event) => {
        if (event.target.closest("a")) return;
        location.href = href;
      });
      row.addEventListener("pointerenter", () => highlight(spec.slug));
      row.addEventListener("pointerleave", () => highlight(""));
      tbody.append(row);
    }
    applyMatchState();
  }

  function applyMatchState() {
    const matched = new Set(filteredSpecs(state).map((spec) => spec.slug));
    const filtering = Boolean(state.query || state.quadrant);
    chart.querySelectorAll(".mark-wrap").forEach((wrap) => {
      wrap.classList.toggle("is-dim", filtering && !wrapSlugs(wrap).some((slug) => matched.has(slug)));
    });
  }

  function highlight(slugOrSlugs) {
    const slugs = new Set(Array.isArray(slugOrSlugs) ? slugOrSlugs : slugOrSlugs ? [slugOrSlugs] : []);
    chart.querySelectorAll(".mark-wrap").forEach((wrap) => {
      wrap.classList.toggle("is-hot", wrapSlugs(wrap).some((slug) => slugs.has(slug)));
    });
    tbody.querySelectorAll("tr.spec").forEach((row) => {
      row.classList.toggle("is-hot", slugs.has(row.dataset.slug));
    });
  }
}

function filteredSpecs(state) {
  const items = state.specs.filter((spec) => {
    const name = `${spec.name || ""} ${spec.slug || ""}`.toLowerCase();
    if (state.query && !name.includes(state.query)) return false;
    if (state.quadrant && displayQuadrant(spec.quadrant) !== state.quadrant) return false;
    return true;
  });
  const factor = state.dir === "asc" ? 1 : -1;
  return items.slice().sort((a, b) => {
    if (state.sort === "score") return factor * (specScore(a) - specScore(b));
    if (state.sort === "type") return factor * (sortValue(a.type) - sortValue(b.type));
    if (state.sort === "exec") return factor * (sortValue(a.exec) - sortValue(b.exec));
    const left = state.sort === "quadrant" ? displayQuadrant(a.quadrant) : a.name || a.slug || "";
    const right = state.sort === "quadrant" ? displayQuadrant(b.quadrant) : b.name || b.slug || "";
    return factor * left.localeCompare(right);
  });
}

function plotGroups(specs) {
  const groups = new Map();
  for (const spec of specs || []) {
    if (spec.x == null || spec.y == null) continue;
    const key = `${Number(spec.x)}:${Number(spec.y)}`;
    const group = groups.get(key) || { x: spec.x, y: spec.y, specs: [] };
    group.specs.push(spec);
    groups.set(key, group);
  }
  return [...groups.values()].map((group) => {
    group.specs.sort((a, b) => (a.name || a.slug || "").localeCompare(b.name || b.slug || ""));
    return group;
  });
}

function displayQuadrant(name) {
  if (name === "Niche players") return "Niche";
  return name || "";
}

function wrapSlugs(wrap) {
  return (wrap.dataset.slugs || "").split(/\s+/).filter(Boolean);
}

function groupTip(members) {
  const first = members[0];
  const typeValue = axisValue(first.type);
  const coverageValue = axisValue(first.exec);
  const type = typeValue != null ? typeValue.toFixed(2) : "—";
  const coverage = coverageValue != null ? coverageValue.toFixed(2) : "—";
  const score = specScore(first);
  const scoreText = score < 0 ? "—" : String(score);
  const names = members.map((spec) => `<strong>${escapeHtml(spec.name || spec.slug)}</strong>`).join("");
  return `${names}<p>${escapeHtml(displayQuadrant(first.quadrant) || "Unplotted")}<br>Score ${escapeHtml(scoreText)} · Type ${escapeHtml(type)} · Coverage ${escapeHtml(coverage)}</p>`;
}

// The agreed score of an axis. Runs published before check voting only carry `median`.
function axisValue(axis) {
  if (!axis) return null;
  const value = axis.consensus != null ? axis.consensus : axis.median;
  return value != null ? Number(value) : null;
}

function sortValue(axis) {
  const value = axisValue(axis);
  return value != null ? value : -1;
}

function specScore(spec) {
  if (spec && spec.score != null) return Number(spec.score);
  const type = spec && axisValue(spec.type);
  const coverage = spec && axisValue(spec.exec);
  if (type == null || coverage == null) return -1;
  return Math.round(100 * Math.sqrt((Number(type) / 3) * Number(coverage)));
}

function axisStat(axis, key) {
  const aliases = { average: "mean", lowest: "min", highest: "max" };
  if (axis[key] != null) return Number(axis[key]);
  const legacy = aliases[key];
  return legacy && axis[legacy] != null ? Number(axis[legacy]) : null;
}

const LABEL_RADII = [10, 13, 16, 20];
const LABEL_STEPS = 16;
const LABEL_PAD = 2;

function placeLabels(chart) {
  const wraps = [...chart.querySelectorAll(".mark-wrap")];
  const chartBox = chart.getBoundingClientRect();
  const ranked = wraps
    .map((wrap) => {
      const label = wrap.querySelector(".dot-label");
      const stacked = label && label.classList.contains("is-stack");
      return { wrap, label, isolation: stacked ? Infinity : nearestDistance(wrap, wraps) };
    })
    .filter((item) => item.label)
    .sort((a, b) => b.isolation - a.isolation);
  ranked.forEach(({ label }) => resetLabelPose(label));
  const kept = [];
  for (const item of ranked) {
    const preferLeft = item.wrap.getBoundingClientRect().left > chartBox.left + chartBox.width * 0.5;
    const labels = kept.map((label) => label.getBoundingClientRect());
    const dots = wraps.filter((wrap) => wrap !== item.wrap).map((wrap) => expandBox(wrap.getBoundingClientRect(), 5));
    if (placeLabelAround(item.label, preferLeft, chartBox, labels, dots)) kept.push(item.label);
    else item.label.classList.add("is-hidden");
  }
}

function resetLabelPose(label) {
  label.classList.remove("is-hidden", "place-left", "place-center");
  label.style.left = "";
  label.style.top = "";
  label.style.right = "";
  label.style.transform = "";
}

function labelAngles() {
  const angles = [];
  for (let step = 0; step < LABEL_STEPS; step += 1) angles.push((step * 2 * Math.PI) / LABEL_STEPS);
  return angles;
}

function wrapAngle(angle) {
  const turn = Math.PI * 2;
  let value = angle % turn;
  if (value > Math.PI) value -= turn;
  if (value < -Math.PI) value += turn;
  return value;
}

function angleCost(angle, preferLeft) {
  const preferred = preferLeft ? Math.PI : 0;
  const opposite = preferLeft ? 0 : Math.PI;
  const toPreferred = Math.abs(wrapAngle(angle - preferred));
  const toOpposite = Math.abs(wrapAngle(angle - opposite));
  const toUp = Math.abs(wrapAngle(angle + Math.PI / 2));
  const toDown = Math.abs(wrapAngle(angle - Math.PI / 2));
  const toCardinal = Math.min(toPreferred, toOpposite, toUp, toDown);
  if (toPreferred < 0.2) return 0;
  if (toOpposite < 0.2) return 0.35;
  if (toUp < 0.2 || toDown < 0.2) return 0.7;
  return 1.1 + toCardinal;
}

function applyLabelPose(label, angle, radius) {
  const axisX = Math.cos(angle);
  const axisY = Math.sin(angle);
  const shiftX = axisX > 0.35 ? 0 : axisX < -0.35 ? -100 : -50;
  const shiftY = axisY > 0.35 ? 0 : axisY < -0.35 ? -100 : -50;
  label.style.left = `${axisX * radius}px`;
  label.style.top = `${axisY * radius}px`;
  label.style.right = "auto";
  label.style.transform = `translate(${shiftX}%, ${shiftY}%)`;
  label.classList.toggle("place-left", shiftX === -100);
  label.classList.toggle("place-center", shiftX === -50);
}

function placeLabelAround(label, preferLeft, chartBox, labelBoxes, dotBoxes) {
  const angles = labelAngles();
  let best = null;
  for (const radius of LABEL_RADII) {
    for (const angle of angles) {
      applyLabelPose(label, angle, radius);
      const box = label.getBoundingClientRect();
      const clipped = box.left < chartBox.left - 6 || box.right > chartBox.right + 6 || box.top < chartBox.top - 6 || box.bottom > chartBox.bottom + 6;
      if (clipped) continue;
      if (labelBoxes.some((other) => overlap(box, other, LABEL_PAD))) continue;
      const hitsDot = dotBoxes.some((other) => overlap(box, other, 0));
      const score = radius * 0.08 + angleCost(angle, preferLeft) + (hitsDot ? 3.5 : 0);
      if (!best || score < best.score) best = { angle, radius, score };
    }
  }
  if (!best) return false;
  applyLabelPose(label, best.angle, best.radius);
  return true;
}

function expandBox(box, pad) {
  return { left: box.left - pad, right: box.right + pad, top: box.top - pad, bottom: box.bottom + pad };
}

function nearestDistance(wrap, wraps) {
  const a = wrap.getBoundingClientRect();
  let best = Infinity;
  for (const other of wraps) {
    if (other === wrap) continue;
    const b = other.getBoundingClientRect();
    const dx = a.left - b.left;
    const dy = a.top - b.top;
    best = Math.min(best, Math.hypot(dx, dy));
  }
  return best;
}

function overlap(a, b, pad) {
  return !(a.right + pad < b.left || a.left - pad > b.right || a.bottom + pad < b.top || a.top - pad > b.bottom);
}

function showTip(anchor, html) {
  if (!tip) return;
  tip.innerHTML = html;
  tip.hidden = false;
  const rect = anchor.getBoundingClientRect();
  const width = tip.offsetWidth;
  const height = tip.offsetHeight;
  const left = Math.min(Math.max(12, rect.left + rect.width / 2 - width / 2), window.innerWidth - width - 12);
  const below = rect.bottom + 10;
  const top = below + height + 12 < window.innerHeight ? below : Math.max(12, rect.top - height - 10);
  tip.style.left = `${left}px`;
  tip.style.top = `${top}px`;
}

function hideTip() {
  if (tip) tip.hidden = true;
}

function scoreCell(axis, scaleMax, places) {
  const cell = document.createElement("td");
  const consensus = axisValue(axis);
  const average = consensus != null ? consensus : axis ? axisStat(axis, "average") : null;
  const lowest = axis ? axisStat(axis, "lowest") : null;
  const highest = axis ? axisStat(axis, "highest") : null;
  if (average == null || lowest == null || highest == null) {
    cell.textContent = "—";
    return cell;
  }
  const wrap = document.createElement("div");
  wrap.className = "score";
  const avg = document.createElement("div");
  avg.className = "score-avg";
  avg.textContent = average.toFixed(places);
  const bar = document.createElement("div");
  bar.className = "score-bar";
  const low = document.createElement("span");
  low.className = "score-end";
  low.innerHTML = `<small>Lowest</small>${lowest.toFixed(places)}`;
  const high = document.createElement("span");
  high.className = "score-end score-end-high";
  high.innerHTML = `<small>Highest</small>${highest.toFixed(places)}`;
  const track = document.createElement("div");
  track.className = "track";
  const range = document.createElement("div");
  range.className = "range";
  range.style.left = percent(lowest, scaleMax);
  range.style.width = percent(Math.max(0, highest - lowest), scaleMax);
  track.append(range);
  for (const [value, kind] of [[lowest, "low"], [average, "avg"], [highest, "high"]]) {
    const mark = document.createElement("span");
    mark.className = `mark ${kind}`;
    mark.style.left = percent(value, scaleMax);
    track.append(mark);
  }
  bar.append(low, track, high);
  wrap.append(avg, bar);
  cell.append(wrap);
  return cell;
}

async function initProduct() {
  const params = new URLSearchParams(location.search);
  const run = params.get("run");
  const slug = params.get("spec");
  const status = document.querySelector("#status");
  const root = document.querySelector("#product");
  if (!run || !slug) {
    status.textContent = "Missing run or spec.";
    return;
  }
  let data;
  try {
    data = await loadRunFile(run);
  } catch (error) {
    status.textContent = "Could not read that run.";
    return;
  }
  const spec = (data.specs || []).find((item) => item.slug === slug);
  if (!spec) {
    status.textContent = "That spec is not in this run.";
    return;
  }
  document.title = `${spec.name} · Intelligence Scale`;
  document.querySelector("#title").textContent = spec.name;
  renderScorecard(document.querySelector("#meta"), spec);
  setCommitStatus(status, data.git);
  const toc = [{ id: "overview", label: "Scores" }];
  const typeSection = criteriaTable("Type criteria", spec.type, "type-criteria");
  const coverageSection = criteriaTable("Coverage criteria", spec.exec, "coverage-criteria");
  if (typeSection) {
    root.append(typeSection);
    toc.push({ id: "type-criteria", label: "Type criteria" });
  }
  if (coverageSection) {
    root.append(coverageSection);
    toc.push({ id: "coverage-criteria", label: "Coverage criteria" });
  }
  const models = Object.keys((spec.type && spec.type.models) || {});
  if (models.length) {
    const analysis = document.createElement("section");
    analysis.className = "analysis-block";
    analysis.id = "analysis";
    const heading = document.createElement("h2");
    heading.textContent = "Analysis";
    analysis.append(heading);
    toc.push({ id: "analysis", label: "Analysis" });
    for (const model of models) {
      const section = document.createElement("section");
      const sectionId = `analysis-${safeAnchor(model)}`;
      section.className = "model-block";
      section.id = sectionId;
      const subheading = document.createElement("h3");
      subheading.textContent = model;
      const prose = document.createElement("div");
      prose.className = "prose";
      const report = (spec.type.models[model] && spec.type.models[model].report) || ((spec.exec.models || {})[model] || {}).report;
      section.append(subheading);
      if (!report) {
        prose.textContent = (spec.type.models[model] && spec.type.models[model].error) || "No written analysis.";
      } else {
        try {
          const markdown = await fetchText(fromRoot(`output/${encodeURIComponent(run)}/${report.split("/").map(encodeURIComponent).join("/")}`));
          prose.innerHTML = renderMarkdown(markdown);
        } catch (error) {
          prose.textContent = "Could not read the written analysis.";
        }
      }
      section.append(prose);
      analysis.append(section);
      toc.push({ id: sectionId, label: model, child: true });
    }
    root.append(analysis);
  }
  bindToc(toc);
}

function criteriaTable(title, axis, id) {
  if (!axis) return null;
  const models = Object.keys(axis.models || {});
  const keys = [];
  for (const model of models) {
    for (const key of Object.keys((axis.models[model].criteria) || {})) {
      if (!keys.includes(key)) keys.push(key);
    }
  }
  if (!keys.length) return null;
  const section = document.createElement("section");
  section.className = "criteria-block";
  section.id = id;
  const heading = document.createElement("h2");
  heading.textContent = title;
  const table = document.createElement("table");
  table.className = "criteria";
  const head = document.createElement("tr");
  head.innerHTML = `<th>Criterion</th><th class="crit-consensus">Consensus</th>${models.map((model) => `<th>${escapeHtml(model)}</th>`).join("")}`;
  table.append(head);
  for (const key of keys) {
    const meta = CRITERIA[key] || { name: key, blurb: "" };
    const row = document.createElement("tr");
    const agreed = axis.criteria ? axis.criteria[key] : null;
    const consensusCell = `<td class="crit-grade crit-consensus">${agreed == null ? "—" : escapeHtml(formatGrade(agreed))}</td>`;
    const grades = models.map((model) => {
      const value = axis.models[model].criteria ? axis.models[model].criteria[key] : null;
      const differs = value != null && agreed != null && Number(value) !== Number(agreed);
      return `<td class="crit-grade${differs ? " crit-differs" : ""}">${value == null ? "—" : escapeHtml(formatGrade(value))}</td>`;
    }).join("");
    row.innerHTML = `<th><span class="crit-id">${escapeHtml(key)}</span><span class="crit-name">${escapeHtml(meta.name)}</span><span class="crit-blurb">${escapeHtml(meta.blurb)}</span></th>${consensusCell}${grades}`;
    table.append(row);
  }
  section.append(heading, table);
  return section;
}

function renderScorecard(root, spec) {
  if (!root) return;
  root.id = "overview";
  root.replaceChildren();
  const quadrant = displayQuadrant(spec.quadrant) || "Unplotted";
  const score = specScore(spec);
  const type = axisValue(spec.type);
  const coverage = axisValue(spec.exec);
  root.append(statCard("Quadrant", `<span class="chip">${escapeHtml(quadrant)}</span>`));
  root.append(statCard("Score", score < 0 ? "—" : `<strong>${score}</strong><span class="stat-scale">0–100</span>`));
  root.append(statCard("Type", type == null ? "—" : `<strong>${type.toFixed(2)}</strong><span class="stat-scale">0–3</span>${miniTrack(type, 3)}`));
  root.append(statCard("Coverage", coverage == null ? "—" : `<strong>${coverage.toFixed(2)}</strong><span class="stat-scale">0–1</span>${miniTrack(coverage, 1)}`));
  if (spec.url) {
    const link = document.createElement("a");
    link.className = "stat stat-link";
    link.href = spec.url;
    link.innerHTML = `<small>Product</small><span>Open site</span>`;
    root.append(link);
  }
}

function statCard(label, html) {
  const card = document.createElement("div");
  card.className = "stat";
  card.innerHTML = `<small>${escapeHtml(label)}</small><div class="stat-value">${html}</div>`;
  return card;
}

function miniTrack(value, scaleMax) {
  return `<div class="track" aria-hidden="true"><span class="mark avg" style="left:${percent(value, scaleMax)}"></span></div>`;
}

function setCommitStatus(status, git) {
  if (!status) return;
  if (!git) {
    status.replaceChildren();
    return;
  }
  const badge = document.createElement("span");
  badge.className = "chip commit";
  badge.textContent = `Commit ${String(git).slice(0, 7)}`;
  status.replaceChildren(badge);
}

function bindToc(items) {
  const nav = document.querySelector("#toc");
  if (!nav || items.length < 2) return;
  nav.hidden = false;
  nav.replaceChildren();
  const title = document.createElement("p");
  title.className = "toc-title";
  title.textContent = "On this page";
  const list = document.createElement("div");
  list.className = "toc-list";
  for (const item of items) {
    const link = document.createElement("a");
    link.href = `#${item.id}`;
    link.textContent = item.label;
    if (item.child) link.classList.add("is-child");
    list.append(link);
  }
  nav.append(title, list);
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (!visible.length) return;
    const id = visible[0].target.id;
    list.querySelectorAll("a").forEach((link) => link.classList.toggle("is-active", link.hash === `#${id}`));
  }, { rootMargin: "-15% 0px -65% 0px", threshold: 0 });
  for (const item of items) {
    const target = document.getElementById(item.id);
    if (target) observer.observe(target);
  }
}

function safeAnchor(value) {
  return String(value).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "section";
}

function formatGrade(value) {
  const number = Number(value);
  return Number.isNaN(number) ? String(value) : number.toFixed(2);
}

async function initDocs() {
  const root = document.querySelector("#docs");
  const toc = [];
  for (const doc of DOCS) {
    const section = document.createElement("section");
    section.className = "doc-block";
    section.id = doc.id;
    const prose = document.createElement("div");
    prose.className = "prose";
    try {
      prose.innerHTML = renderMarkdown(await fetchText(fromRoot(`docs/${encodeURIComponent(doc.file)}`)));
    } catch (error) {
      prose.textContent = `Could not read docs/${doc.file}.`;
    }
    section.append(prose);
    root.append(section);
    toc.push({ id: doc.id, label: doc.label });
  }
  bindToc(toc);
  const hash = location.hash.slice(1);
  if (hash) {
    const target = document.getElementById(hash);
    if (target) target.scrollIntoView();
  }
}

function renderMarkdown(source) {
  const lines = source.replaceAll("\r\n", "\n").split("\n");
  const html = [];
  let index = 0;
  while (index < lines.length) {
    const line = lines[index];
    if (!line.trim()) {
      index += 1;
      continue;
    }
    if (line.startsWith("```")) {
      const fence = [];
      index += 1;
      while (index < lines.length && !lines[index].startsWith("```")) {
        fence.push(escapeHtml(lines[index]));
        index += 1;
      }
      if (index < lines.length) index += 1;
      html.push(`<pre><code>${fence.join("\n")}</code></pre>`);
      continue;
    }
    if (line.startsWith("|")) {
      const rows = [];
      while (index < lines.length && lines[index].startsWith("|")) {
        if (!/^\|\s*-+/.test(lines[index])) rows.push(splitRow(lines[index]));
        index += 1;
      }
      html.push(`<table>${rows.map((row, rowIndex) => `<tr>${row.map((cell) => `<${rowIndex === 0 ? "th" : "td"}>${inline(cell)}</${rowIndex === 0 ? "th" : "td"}>`).join("")}</tr>`).join("")}</table>`);
      continue;
    }
    const heading = /^(#{1,4})\s+(.*)$/.exec(line);
    if (heading) {
      const level = heading[1].length + 1;
      html.push(`<h${level}>${inline(heading[2])}</h${level}>`);
      index += 1;
      continue;
    }
    if (line.startsWith("> ")) {
      const quote = [];
      while (index < lines.length && lines[index].startsWith("> ")) {
        quote.push(lines[index].slice(2));
        index += 1;
      }
      html.push(`<blockquote><p>${inline(quote.join(" "))}</p></blockquote>`);
      continue;
    }
    if (/^[-*]\s+/.test(line)) {
      const items = [];
      while (index < lines.length && /^[-*]\s+/.test(lines[index])) {
        items.push(`<li>${inline(lines[index].replace(/^[-*]\s+/, "").replace(/^\[ \]\s+/, ""))}</li>`);
        index += 1;
      }
      html.push(`<ul>${items.join("")}</ul>`);
      continue;
    }
    const paragraph = [];
    while (index < lines.length && lines[index].trim() && !lines[index].startsWith("|") && !lines[index].startsWith("#") && !lines[index].startsWith("> ") && !lines[index].startsWith("```") && !/^[-*]\s+/.test(lines[index])) {
      paragraph.push(lines[index]);
      index += 1;
    }
    html.push(`<p>${inline(paragraph.join(" "))}</p>`);
  }
  return html.join("");
}

function splitRow(line) {
  return line.replace(/^\|/, "").replace(/\|$/, "").split("|").map((cell) => cell.trim());
}

function inline(text) {
  return escapeHtml(text)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '<a href="$2">$1</a>')
    .replace(/\[([^\]]+)\]\((#[^)]+)\)/g, '<a href="$2">$1</a>')
    .replace(/\[([^\]]+)\]\(((?:[\w./-]+)\.md)\)/g, (_, label, file) => {
      const slug = file.replace(/^.*\//, "").replace(/\.md$/, "");
      return `<a href="#${slug}">${label}</a>`;
    });
}

function productUrl(run, slug) {
  return fromRoot(`site/product.html?run=${encodeURIComponent(run)}&spec=${encodeURIComponent(slug)}`);
}

function percent(value, scaleMax) {
  return `${Math.min(100, Math.max(0, (Number(value) / scaleMax) * 100))}%`;
}

function clamp(value) {
  return Math.min(96, Math.max(4, value));
}

function mergeRuns(published, tests) {
  const byId = new Map();
  for (const run of [...((published && published.runs) || []), ...((tests && tests.runs) || [])]) {
    if (run && run.id) byId.set(run.id, run);
  }
  return [...byId.values()].sort((a, b) => String(b.created || "").localeCompare(String(a.created || "")));
}

async function loadCatalog(path) {
  try {
    return await fetchJson(path);
  } catch (error) {
    return null;
  }
}

async function loadRunFile(id) {
  return fetchJson(fromRoot(`output/${encodeURIComponent(id)}/ratings.json`));
}

async function fetchJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(response.statusText);
  return response.json();
}

async function fetchText(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(response.statusText);
  return response.text();
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}
