# Prototypes

This folder keeps early composition experiments that should not be included in
the production skin manifest.

The active composition entrypoints live in `src/panels/`.

Prototype panels are installed side by side through `src/prototypes/skin.xml`.
That manifest may use shared definitions from `src/defs.xml`, but prototype-only
classes and panels stay under `src/prototypes/` so `src/skin.xml` remains
production only.
