#!/usr/bin/env bash
# make-learn-video.sh
# One-command setup for a Phlo Learn video recording session.
#
# What it does:
#   1. Verifies Node and Claude Code CLI are installed
#   2. Starts Excalimate MCP server in the background if not running
#   3. Opens the Excalimate live canvas in your default browser
#   4. Launches Claude Code in the phlo-learn project directory
#
# Usage:
#   ./make-learn-video.sh
#
# To clean up at the end of a session:
#   ./make-learn-video.sh --stop

set -euo pipefail

# === Config ===
PORT=3001
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CANVAS_URL="https://app.excalimate.com"
MCP_URL="http://localhost:$PORT/mcp"
PID_FILE="/tmp/phlo-excalimate.pid"

# === Helpers ===
log()  { printf "\033[1;36m▶\033[0m %s\n" "$*"; }
ok()   { printf "\033[1;32m✓\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m!\033[0m %s\n" "$*"; }
fail() { printf "\033[1;31m✗\033[0m %s\n" "$*" >&2; exit 1; }

open_url() {
  local url="$1"
  if command -v open >/dev/null 2>&1; then
    open "$url"                # macOS
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$url" >/dev/null 2>&1 &  # Linux
  elif command -v start >/dev/null 2>&1; then
    start "$url"               # Windows Git Bash / WSL
  else
    warn "Couldn't auto-open browser. Open this manually: $url"
  fi
}

# === Stop mode ===
if [ "${1:-}" = "--stop" ]; then
  if [ -f "$PID_FILE" ]; then
    PID=$(cat "$PID_FILE")
    if kill -0 "$PID" 2>/dev/null; then
      log "Stopping Excalimate (PID $PID)..."
      kill "$PID"
      rm "$PID_FILE"
      ok "Stopped."
    else
      warn "PID file exists but process isn't running. Cleaning up."
      rm "$PID_FILE"
    fi
  else
    warn "No Excalimate process tracked. Checking port $PORT..."
    if lsof -i ":$PORT" >/dev/null 2>&1; then
      warn "Something is on port $PORT but not started by this script."
      echo "    To kill it manually:  kill -9 \$(lsof -t -i :$PORT)"
    else
      ok "Nothing to stop. Port $PORT is free."
    fi
  fi
  exit 0
fi

# === Prerequisites ===
log "Checking prerequisites..."

command -v node >/dev/null 2>&1 || fail "Node.js not found. Install from https://nodejs.org (need v18+)"
NODE_MAJOR=$(node -v | sed 's/v//' | cut -d. -f1)
[ "$NODE_MAJOR" -ge 18 ] || fail "Node.js v18+ required. You have $(node -v)."

command -v claude >/dev/null 2>&1 || fail "Claude Code CLI not found. Install: npm install -g @anthropic-ai/claude-code"

[ -d "$PROJECT_DIR/.claude/skills/phlo-learn-videos" ] \
  || fail "Phlo Learn skill not found at $PROJECT_DIR/.claude/skills/phlo-learn-videos"

ok "Node $(node -v), Claude $(claude --version 2>/dev/null | head -1)"
ok "Project directory: $PROJECT_DIR"

# === Start Excalimate if not running ===
if lsof -i ":$PORT" >/dev/null 2>&1; then
  ok "Excalimate already running on port $PORT"
else
  log "Starting Excalimate MCP server on port $PORT..."
  # Launch in background, write PID, redirect logs
  npx @excalimate/mcp-server --port "$PORT" >/tmp/phlo-excalimate.log 2>&1 &
  echo $! > "$PID_FILE"

  # Wait up to 15s for it to come up
  for i in $(seq 1 15); do
    if lsof -i ":$PORT" >/dev/null 2>&1; then
      ok "Excalimate running (PID $(cat "$PID_FILE"))"
      break
    fi
    sleep 1
    if [ "$i" -eq 15 ]; then
      fail "Excalimate didn't start in 15s. Check /tmp/phlo-excalimate.log"
    fi
  done
fi

# === Register MCP with Claude Code (idempotent) ===
log "Ensuring Claude Code knows about Excalimate..."
# Try to add it; if it already exists, claude mcp add will fail harmlessly
if claude mcp list 2>/dev/null | grep -q "excalimate"; then
  ok "Excalimate already registered with Claude Code"
else
  if claude mcp add --transport http excalimate "$MCP_URL" >/dev/null 2>&1; then
    ok "Registered Excalimate MCP with Claude Code"
  else
    warn "Couldn't register MCP automatically. Run manually:"
    echo "    claude mcp add --transport http excalimate $MCP_URL"
  fi
fi

# === Open the canvas ===
log "Opening Excalimate canvas at $CANVAS_URL"
log "  → Click the 'Live' button in the top right to connect to localhost:$PORT"
open_url "$CANVAS_URL"

# === Launch Claude Code ===
log "Launching Claude Code in $PROJECT_DIR"
echo ""
echo "    Ready to record. Suggested first prompt:"
echo "    \"Using the phlo-learn-videos skill, [your topic here]\""
echo ""
echo "    When done, run:  $0 --stop"
echo ""

cd "$PROJECT_DIR"
exec claude