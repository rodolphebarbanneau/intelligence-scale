# The quadrant

The quadrant places a product on two independent scales at once.

The horizontal axis is the [Intelligence Scale](intelligence-scale.md): how far the product can shift operational agency from people to AI. The vertical axis is the [Execution Scale](execution-scale.md): how much of a company's work the product can carry as it ships.

The rated object is the **chassis**: the product an organization can adopt. The **motor** — the foundation model inside that product — is a separate question. Customer counts, funding, and vendor size are not on either axis.

A first-class wrap of another agent is part of the chassis as this product exposes it. Grade what a buyer can do while sitting in this product: the loop it surfaces, the automation it adds, and the work it hides or leaves on the other product's native UI. Do not copy a sibling product's scores. A thin wrap can score lower than the product it hosts. A harness that surfaces the agent and adds its own control plane can score as high or higher. Generic “attach anything” is not a wrap.

## What the axes measure

| Axis | Question | High score | Low score |
| --- | --- | --- | --- |
| **Type** (horizontal) | Who gets the work done? | AI can own and orchestrate work. People supervise or govern. | People still execute. AI assists inside a human-run process. |
| **Coverage** (vertical) | Whose work fits, and how far across the company can it go? | A company surface: several functions, shared work, systems of record, a catalog that grows coverage. | A craft tool or a blank canvas that one kind of specialist uses alone. |

A product can sit far along one axis and early on the other.

A coding agent that delegates a real engineering change sits to the right and stays low: deep agency, one craft. A company-wide assistant that only amplifies people sits high and stays left: broad coverage, human-executed work. Neither placement is a failure of the other scale.

## Where the lines sit

The Intelligence Scale runs from **0.0 to 3.0**. The vertical line is **1.5**, the middle of that range: Type I is complete and half of the way to Type II is covered. A product that has reached the Type II gate, at **2.0**, sits well to the right of the line. The chart maps a type score with:

```text
x = (type − 1.5) / 1.5
```

Type 0 sits at −1. Type 1.5 sits at 0. Type 3 sits at +1.

The Execution Scale runs from **0.00 to 1.00**. The horizontal line is **0.50**. A specialist-craft product cannot publish **0.50** or higher. The chart maps an execution score with:

```text
y = 2 × execution − 1
```

An execution score of 0 sits at −1. A score of 0.50 sits at 0. A score of 1 sits at +1.

A point that lands on a line belongs to the higher side. The exact center, where both scores sit on their midlines, is **Leaders**.

## The four quadrants

| Quadrant | Placement | What it means |
| --- | --- | --- |
| **Leaders** | At or right of center, and at or above center | Agency can shift, and the product is a company surface, not a craft tool. |
| **Challengers** | Left of center, and at or above center | Company-wide, still human-operated. People across functions can put work on it. AI still assists rather than owns the process. |
| **Visionaries** | At or right of center, and below center | Deep AI in one craft or one function. The product can shift work toward AI inside a specialist lane such as software engineering or customer support. The rest of the company has no native path onto it. |
| **Niche** | Left of center, and below center | Thin on both scales. Limited agency shift, and limited organizational coverage. |

Right of center does not mean Type II. It means the product has passed Type I and is well on the way: AI runs work on its own, started by triggers, with people supervising, even if no AI actor owns a whole process yet. Type II itself starts at **2.0**.

Examples of the split, not of a published score: a company-wide chat assistant that people prompt step by step belongs with the Challengers. A workspace product where agents run on schedules and events across many teams belongs with the Leaders, and moves further right when a persistent AI actor owns a process. A coding or support agent that carries its work end to end belongs with the Visionaries until other functions have a native path. A thin assistant or an unfinished prototype sits with Niche.

## What the dot is

Each release asks several models to rate every product. Each check is decided by a strict majority of the models that answered, so a 1-1 tie fails. The scorer grades that agreed checklist once, and the dot uses the resulting **consensus** score. One outlier model cannot move it, and the lowest and highest per-model scores stay visible as the spread.

The table beside the chart ranks products by a **score** from **0 to 100**. It is the geometric mean of the two published axis scores after each is mapped onto 0–1:

```text
score = 100 × √((type / 3) × coverage)
```

A geometric mean rewards products that are strong on both axes. Leaders tend to sit at the top. Niche sits at the bottom. A specialist that is deep on one axis and thin on the other stays in the middle.

Each axis column also keeps the **average**, **lowest**, and **highest** model scores, so a single outlier stays visible.

When fewer than half of the models return a score on an axis, that product stays in the table and stays off the chart. A missing evaluation is left blank. It is not treated as zero, and it is not filled in.
