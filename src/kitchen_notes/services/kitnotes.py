from pathlib import Path
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# -> kitchen-notes
BASE_DIR = Path(__file__).resolve().parents[3]
NOTES_DIR = BASE_DIR / "kitnotes"

logger.debug(f"Base directory: {BASE_DIR}")
logger.debug(f"Notes directory: {NOTES_DIR}")

def attach_image_url(note):
    if "bild" in note and note["bild"]:
        note["image_url"] = f"/images/{note['bild']}"
    return note


def get_all_notes():
    notes = []

    for file in NOTES_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            note = json.load(f)
            notes.append(attach_image_url(note))

    # optional: sort by id
    return sorted(notes, key=lambda r: r["id"])


def get_note_by_id(note_id: int):
    for file in NOTES_DIR.glob(f"{note_id}_*.json"):
        with open(file, "r", encoding="utf-8") as f:
            note = json.load(f)
            return attach_image_url(note)
    return None
