#!/usr/bin/env bash
set -euo pipefail

out_dir="${1:-research/2026-lecture-ai-vuln-core}"
papers_dir="$out_dir/papers"
mkdir -p "$papers_dir"

download() {
  local url="$1"
  local dest="$2"
  if [[ -f "$dest" ]]; then
    printf 'skip %s\n' "$dest"
    return 0
  fi
  printf 'fetch %s\n' "$url"
  curl -fL --retry 3 --retry-delay 2 --connect-timeout 20 \
    -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" \
    "$url" -o "$dest"
}

download "https://arxiv.org/pdf/1801.01681.pdf" "$papers_dir/vuldeepecker.pdf"
download "https://arxiv.org/pdf/1909.03496.pdf" "$papers_dir/devign.pdf"
download "https://arxiv.org/pdf/2106.10478.pdf" "$papers_dir/ivdetect.pdf"
download "https://arxiv.org/pdf/2203.05181.pdf" "$papers_dir/linevd.pdf"
download "https://arxiv.org/pdf/2107.08760.pdf" "$papers_dir/cvefixes.pdf"
download "https://arxiv.org/pdf/2304.00409.pdf" "$papers_dir/diversevul.pdf"
download "https://arxiv.org/pdf/2002.08155.pdf" "$papers_dir/codebert.pdf"
download "https://arxiv.org/pdf/2009.08366.pdf" "$papers_dir/graphcodebert.pdf"

printf 'done %s\n' "$out_dir"
