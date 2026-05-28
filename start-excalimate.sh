#!/usr/bin/env bash
# start-excalimate.sh
# Starts the Excalimate MCP server on localhost:3001.
# Run this before any Learn video work. Leave the terminal open.
#
# Usage:
#   ./start-excalimate.sh           # foreground, default port 3001
#   ./start-excalimate.sh 4000      # foreground on a different port
#
# To stop: Ctrl+C

set -euo pipefail

PORT="${1:-3001}"

# Check Node is installed
if ! command -v node >/dev/null 2>&1; then
  echo "❌ Node.js is not installed."
  echo "   Install with:  brew install node    (Mac)"
  echo "                  Or download from https://nodejs.org"
  exit 1
fi

NODE_MAJOR="$(node -v | sed 's/v//' | cut -d. -f1)"
if [ "$NODE_MAJOR" -lt 18 ]; then
  echo "❌ Node.js v18 or higher is required. You have $(node -v)."
  exit 1
fi

# Check if port is already in use
if lsof -i ":$PORT" >/dev/null 2>&1; then
  echo "⚠️  Port $PORT is already in use."
  echo "   Either Excalimate is already running, or another process is on this port."
  echo "   Check with:  lsof -i :$PORT"
  echo "   To kill it:  kill -9 \$(lsof -t -i :$PORT)"
  exit 1
fi

echo "▶️  Starting Excalimate MCP server on http://localhost:$PORT/mcp"
echo "    Open https://app.excalimate.com and click Live to connect"
echo "    Press Ctrl+C to stop"
echo ""

# Run in foreground so Ctrl+C stops it cleanly
exec npx @excalimate/mcp-server --port "$PORT"