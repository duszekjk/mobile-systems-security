#!/usr/bin/env bash
set -euo pipefail

out_dir="${1:-research/2026-lecture-ai-vuln}"
papers_dir="$out_dir/papers"
web_dir="$out_dir/web"

mkdir -p "$papers_dir" "$web_dir"

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
download "https://arxiv.org/pdf/2403.18624.pdf" "$papers_dir/primevul.pdf"
download "https://arxiv.org/pdf/2411.17274.pdf" "$papers_dir/cleanvul.pdf"
download "https://arxiv.org/pdf/2407.08708.pdf" "$papers_dir/eyeballvul.pdf"
download "https://arxiv.org/pdf/2002.08155.pdf" "$papers_dir/codebert.pdf"
download "https://arxiv.org/pdf/2009.08366.pdf" "$papers_dir/graphcodebert.pdf"
download "https://arxiv.org/pdf/2205.12424.pdf" "$papers_dir/vulberta.pdf"
download "https://arxiv.org/pdf/2404.14719.pdf" "$papers_dir/vullmgnn.pdf"
download "https://arxiv.org/pdf/2406.03718.pdf" "$papers_dir/vulllm.pdf"
download "https://arxiv.org/pdf/2407.03093.pdf" "$papers_dir/realvul.pdf"
download "https://arxiv.org/pdf/2408.03489.pdf" "$papers_dir/llm_vuln_detection.pdf"
download "https://arxiv.org/pdf/2410.07573.pdf" "$papers_dir/realvul_php.pdf"
download "https://arxiv.org/pdf/2405.15690.pdf" "$papers_dir/vrpilot.pdf"
download "https://arxiv.org/pdf/2404.08144.pdf" "$papers_dir/one_day_exploit.pdf"
download "https://arxiv.org/pdf/2406.01637.pdf" "$papers_dir/zero_day_exploit.pdf"
download "https://nvlpubs.nist.gov/nistpubs/cswp/nist.cswp.41.pdf" "$papers_dir/lev_nist.pdf"

printf 'done %s\n' "$out_dir"
