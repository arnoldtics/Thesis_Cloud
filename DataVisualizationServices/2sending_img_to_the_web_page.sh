#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
IMAGE_PATH="$SCRIPT_DIR/Number_of_theses_published_per_year.png"
DEST_DIR="../ThesisCloud/microservice/static/img"

if [ -f "$IMAGE_PATH" ]; then
    cp "$IMAGE_PATH" "$DEST_DIR"
    echo "Action completed: $DEST_DIR"
else
    echo "File not found"
fi
