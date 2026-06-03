#!/usr/bin/env bash
# Copia CSVs do material da faculdade para data/csv_fonte
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/DOCS-FACUL/Arquivos_CSV-69fa4f2fb9482"
DEST="$ROOT/data/csv_fonte"
mkdir -p "$DEST"
cp -v "$SRC"/*.csv "$DEST/"
echo "OK: $(ls -1 "$DEST" | wc -l) arquivos em data/csv_fonte"
