#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "${SCRIPT_DIR}/.venv/bin/python" ]]; then
  "${SCRIPT_DIR}/.venv/bin/python" "${SCRIPT_DIR}/alpha_s_bridge_holdout.py" "$@"
else
  python3 "${SCRIPT_DIR}/alpha_s_bridge_holdout.py" "$@"
fi
