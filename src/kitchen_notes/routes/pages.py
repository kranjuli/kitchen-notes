from flask import Blueprint, render_template, send_from_directory
from pathlib import Path
from kitchen_notes.services.kitnotes import get_all_notes, get_note_by_id

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

pages_bp = Blueprint("pages", __name__)

BASE_DIR = Path(__file__).resolve().parents[3]  # -> kitchen-notes
IMAGE_DIR = BASE_DIR / "images"

logger.debug(f"Base directory: {BASE_DIR}")
logger.debug(f"Image directory: {IMAGE_DIR}")

@pages_bp.route("/")
def home():
    kitchen_notes = get_all_notes()
    return render_template("index.html", active_page="home", notes=kitchen_notes)

@pages_bp.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

@pages_bp.route("/note/<int:note_id>")
def note_detail(note_id):
    kit_note = get_note_by_id(note_id)
    logger.debug(f"Retrieved note: {kit_note}")
    if not kit_note:
        return "Kitchen Note not found", 404

    return render_template("note.html", note=kit_note)
