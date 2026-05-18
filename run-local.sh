#!/bin/bash

# Shell script to run Flask app locally

set -o pipefail

PYTHON_IMAGE="ghcr.io/astral-sh/uv:0.11.16-python3.14-trixie-slim@sha256:56378b6ff601fc05ed4d0ef0de5772171427e5b8eff7b2045ac5d0c6db633616"

case "$1" in
  "start")
    if ! docker image inspect "$PYTHON_IMAGE" >/dev/null 2>&1; then
      echo "Image nicht vorhanden – wird gepullt..."
      docker pull "$PYTHON_IMAGE"
    else
      echo "Image bereits vorhanden – skip docker pull"
    fi

    echo "🚀 Starting infrastructure..."
    docker run -d -it --name kitchen-notes --rm \
    -p 5001:5000 \
    -v "$(pwd)":/app \
    -v "/mnt/ssd/kitchen-notes/kitnotes":/app/kitnotes \
    -v "/mnt/ssd/kitchen-notes/images":/app/images \
    -w /app \
    -e UV_PROJECT_ENVIRONMENT=/opt/venv \
    -e PATH="/opt/venv/bin:$PATH" \
    -e PYTHONPATH="/app/src" \
    "$PYTHON_IMAGE" \
    bash -c "uv sync && gunicorn -b 0.0.0.0:5000 wsgi:application"

    echo ""
    echo "✅ Container kitchen-notes is running."
    echo ""
    echo "🌐 Access:"
    echo " - KitchenNotes: http://$HOSTNAME:5001/"
    ;;

  "stop")
    docker stop kitchen-notes
    ;;

  "logs")
    docker logs -f kitchen-notes
    ;;

  *)
    echo "Usage: $0 start|stop|logs"
    exit 1
    ;;
esac
