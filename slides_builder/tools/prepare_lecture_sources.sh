#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <lecture_dir>" >&2
  exit 1
fi

lecture_dir="$1"
batch_size="${BATCH_SIZE:-3}"
repo_root="$(cd "$(dirname "$0")/.." && pwd)"
download_script="${DOWNLOAD_SCRIPT:-$repo_root/tools/download_lecture_sources.sh}"
pdf_markdown_helper="${PDF_MARKDOWN_HELPER:-$repo_root/tools/extract_pdf_markdown.py}"
picaxe_home="${PICAXE_HOME:-/private/tmp/PicAxe/PicAxe-OCR}"
picaxe_python="${PICAXE_PYTHON:-/private/tmp/picaxe-venv/bin/python}"

papers_dir="$lecture_dir/papers"
literature_dir="$lecture_dir/literature"
bundle_dir="$literature_dir/picaxe-out"
batch_root="$bundle_dir/batches"
merged_images="$bundle_dir/extracted_images"
merged_tables="$bundle_dir/tables"
flat_images="$literature_dir/extracted_images"
flat_tables="$literature_dir/tables"
flat_papers="$literature_dir/papers"
flat_web="$literature_dir/web"

if [[ ! -x "$download_script" ]]; then
  echo "download helper not found: $download_script" >&2
  exit 1
fi

if [[ ! -f "$pdf_markdown_helper" ]]; then
  echo "PDF markdown helper not found: $pdf_markdown_helper" >&2
  exit 1
fi

if [[ ! -x "$picaxe_python" ]]; then
  echo "PicAxe python not found: $picaxe_python" >&2
  exit 1
fi

if [[ ! -d "$picaxe_home" ]]; then
  echo "PicAxe repo not found: $picaxe_home" >&2
  exit 1
fi

mkdir -p "$bundle_dir" "$batch_root" "$merged_images" "$merged_tables" "$flat_images" "$flat_tables" "$flat_papers" "$flat_web" \
  "$literature_dir/markdown" "$literature_dir/pdfimages"

"$download_script" "$lecture_dir"

if [[ -d "$papers_dir" ]]; then
  find "$papers_dir" -maxdepth 1 -type f -name '*.pdf' -exec cp -f {} "$flat_papers/" \;
fi

if [[ -d "$lecture_dir/web" ]]; then
  find "$lecture_dir/web" -maxdepth 1 -type f \( -name '*.html' -o -name '*.htm' \) -exec cp -f {} "$flat_web/" \;
fi

pdfs=()
while IFS= read -r pdf; do
  pdfs+=("$pdf")
done < <(find "$papers_dir" -maxdepth 1 -type f -name '*.pdf' | LC_ALL=C sort)

if [[ ${#pdfs[@]} -eq 0 ]]; then
  echo "no PDFs found in $papers_dir" >&2
  exit 1
fi

for pdf in "${pdfs[@]}"; do
  echo "markdown $pdf"
  python3 "$pdf_markdown_helper" --pdf "$pdf" --out-dir "$literature_dir"
done

batch_index=0
for ((i = 0; i < ${#pdfs[@]}; i += batch_size)); do
  batch_index=$((batch_index + 1))
  batch_dir="$(mktemp -d "${TMPDIR:-/private/tmp}/lecture_batch_${batch_index}.XXXXXX")"
  batch_output="$batch_root/batch_$(printf '%03d' "$batch_index")"
  mkdir -p "$batch_output"

  for pdf in "${pdfs[@]:i:batch_size}"; do
    cp "$pdf" "$batch_dir/"
  done

  echo "picaxe batch $batch_index: $(basename "$batch_output")"
  (
    cd "$picaxe_home"
    "$picaxe_python" main.py --input-dir "$batch_dir" --output-dir "$batch_output"
  )

  if [[ -d "$batch_output/extracted_images" ]]; then
    find "$batch_output/extracted_images" -type f -name '*.png' -exec cp -f {} "$merged_images/" \; -exec cp -f {} "$flat_images/" \;
  fi

  if [[ -d "$batch_output/tables" ]]; then
    find "$batch_output/tables" -type f -name '*.png' -exec cp -f {} "$merged_tables/" \; -exec cp -f {} "$flat_tables/" \;
  fi

  rm -rf "$batch_dir"
done

echo "done $bundle_dir"
