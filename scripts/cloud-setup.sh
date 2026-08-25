#!/usr/bin/env bash
# Idempotent environment bootstrap for the personal-ai-context knowledge base.
# Installs the docs toolchain (MkDocs Material) into a local virtualenv.
set -euo pipefail

cd "$(dirname "$0")/.."

# ensurepip / venv support is not in the base image; install it once.
if ! python3 -c "import ensurepip" >/dev/null 2>&1; then
  sudo apt-get update -qq
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq python3-venv
fi

# Create the virtualenv only if it does not already exist.
if [ ! -x ".venv/bin/python" ]; then
  python3 -m venv .venv
fi

.venv/bin/python -m pip install --quiet --upgrade pip
.venv/bin/python -m pip install --quiet -r requirements.txt

echo "Environment ready. MkDocs: $(.venv/bin/mkdocs --version)"
