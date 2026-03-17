#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# Prefer Java 17 for AGP compatibility if it exists locally.
if command -v /usr/libexec/java_home &>/dev/null; then
  JAVA_17=$(/usr/libexec/java_home -v 17 2>/dev/null || true)
  if [[ -n "${JAVA_17:-}" ]]; then
    export JAVA_HOME="$JAVA_17"
    export PATH="$JAVA_HOME/bin:$PATH"
  fi
fi

# Ensure Gradle can write its wrapper cache even in restricted environments.
if [[ -z "${GRADLE_USER_HOME:-}" ]]; then
  DEFAULT_GRADLE_HOME="${HOME}/.gradle"
  mkdir -p "$DEFAULT_GRADLE_HOME" 2>/dev/null || true
  if [[ ! -w "$DEFAULT_GRADLE_HOME" ]]; then
    export GRADLE_USER_HOME="${ROOT_DIR}/.gradle-home"
    mkdir -p "$GRADLE_USER_HOME"
  fi
fi

echo "Using Java:"
java -version || true

echo
echo "Resetting stale Android generated intermediates..."
rm -rf \
  app/build/generated/data_binding_base_class_source_out \
  app/build/generated/source/buildConfig \
  app/build/generated/source/r \
  app/build/intermediates/compile_and_runtime_not_namespaced_r_class_jar \
  app/build/intermediates/runtime_symbol_list \
  app/build/intermediates/symbol_list_with_package_name

echo
echo "Building Android app (debug)..."
./gradlew clean assembleDebug

echo
echo "Running unit tests..."
./gradlew testDebugUnitTest
