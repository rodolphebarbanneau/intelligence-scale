# Contributing

This repository rates software an organization can adopt. It does not rate which foundation model is better. Two kinds of contribution keep that distinction intact.

## Project contributors

Project contributors change the rating system, the documentation, the skills, the command-line runner, the release workflow, or the report page.

That includes:

- [`docs/`](docs/)
- [`skills/`](skills/)
- [`report/`](report/)
- [`scripts/`](scripts/)

Open a pull request that explains what changed and why. A change to a skill changes future ratings, so describe how scores would move.

## Spec representatives

A spec representative speaks for a technology that already has a file in [`specs/`](specs/).

Representatives may open an issue or a pull request to correct a factual error in that file: the wrong edition, an outdated capability, a broken source, or a missing supported feature. The pull request should change `specs/<slug>.md` and cite the source of the correction.

Representatives do not set scores. Do not edit [`output/`](output/). The next release reads the corrected spec and writes a new run.

A new dossier can ship as `draft: true` until it is ready for a published release. Draft specs can be rated in a local `test-` run. They do not appear in production output.

## How to send a change

1. Fork the repository and create a branch.
2. Edit the files that match your role. Project contributors stay out of a vendor's spec unless they are also correcting a cited fact. Spec representatives stay inside their own `specs/<slug>.md`.
3. Open a pull request. A representative's factual correction is reviewed the same way as any other factual edit.

Generated run files in `output/` are written by the release workflow. Pull requests should not hand-edit them.
