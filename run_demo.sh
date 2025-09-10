#!/usr/bin/env bash
set -e
echo "Starting ClinicAssist demo server on http://localhost:8000"
uvicorn server:app --host 0.0.0.0 --port 8000
