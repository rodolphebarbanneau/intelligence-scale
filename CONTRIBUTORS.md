# Contributing

This repository rates software an organization can adopt. It does not rate which foundation model is better. Two kinds of contribution keep that distinction intact.

## Project contributors

Project contributors change the rating system, the documentation, the skills, the command-line runner, the release workflow, or the report page.

That includes:

- [`docs/`](docs/)
- [`src/type.yaml`](src/type.yaml) and [`src/exec.yaml`](src/exec.yaml), the checks, caps, and gates behind every grade
- [`src/skills/`](src/skills/)
- [`src/config/models.txt`](src/config/models.txt), the models a release asks
- [`src/config/reference.json`](src/config/reference.json), the expected grades for the calibration anchors
- [`cli/`](cli/), the `intelligence-scale` command line: the rating loop and scorer in [`cli/rating/`](cli/rating/), the quadrant, the local server, and the mock fixture
- [`site/`](site/)

Open a pull request that explains what changed and why. A change to a rubric or a skill changes future ratings, so describe how scores would move. After editing `src/type.yaml` or `src/exec.yaml`, run `uv run intelligence-scale render-rubrics` to update the skills, then `uv run intelligence-scale self-check`. When a change is meant to move grades, run `uv run intelligence-scale mock --write-reference` only if the expected anchor grades should move too, and say so in the pull request.

## Spec representatives

A spec representative speaks for a technology that already has a file in [`src/specs/`](src/specs/).

Representatives may open an issue or a pull request to correct a factual error in that file: the wrong edition, an outdated capability, a broken source, or a missing supported feature. The pull request should change `src/specs/<slug>.md` and cite the source of the correction.

Representatives do not set scores. Do not edit [`output/`](output/). The next release reads the corrected spec and writes a new run.

A new dossier can ship as `draft: true` until it is ready for a published release. Draft specs can be rated in a local `test-` run. They do not appear in production output.

## How to send a change

1. Fork the repository and create a branch.
2. Edit the files that match your role. Project contributors stay out of a vendor's spec unless they are also correcting a cited fact. Spec representatives stay inside their own `src/specs/<slug>.md`.
3. Open a pull request. A representative's factual correction is reviewed the same way as any other factual edit.

Generated run files in `output/` are written by the release workflow. Pull requests should not hand-edit them.
