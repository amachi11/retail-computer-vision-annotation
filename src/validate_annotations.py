import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_video_annotations.json"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    width, height = data["image_width"], data["image_height"]
    valid_classes = {int(k) for k in data["classes"]}
    seen_ids, errors = set(), []

    for frame in data["frames"]:
        for ann in frame["annotations"]:
            prefix = f"frame={frame['frame_id']} annotation={ann['id']}"
            if ann["id"] in seen_ids:
                errors.append(f"{prefix}: duplicate annotation id")
            seen_ids.add(ann["id"])

            if ann["class_id"] not in valid_classes:
                errors.append(f"{prefix}: invalid class")

            x, y, w, h = ann["bbox"]
            if w <= 0 or h <= 0:
                errors.append(f"{prefix}: non-positive box size")
            if x < 0 or y < 0 or x + w > width or y + h > height:
                errors.append(f"{prefix}: box outside image boundaries")

            if not 0 <= ann["confidence"] <= 1:
                errors.append(f"{prefix}: confidence outside [0,1]")

            polygon = ann.get("segmentation", [[]])[0]
            if len(polygon) < 6 or len(polygon) % 2:
                errors.append(f"{prefix}: invalid polygon")

            if ann.get("needs_review") and ann["confidence"] > 0.98:
                errors.append(f"{prefix}: suspicious review/confidence combination")

    print(f"Frames checked: {len(data['frames'])}")
    print(f"Annotations checked: {len(seen_ids)}")

    if errors:
        print("Validation issues:")
        for error in errors:
            print(" -", error)
        raise SystemExit(1)

    print("PASS: annotation schema and geometry checks completed with no errors.")


if __name__ == "__main__":
    main()
