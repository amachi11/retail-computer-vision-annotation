import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "retail_video_annotations.json"
OUTPUT = ROOT / "data" / "coco_annotations.json"


def polygon_area(points):
    coords = list(zip(points[0::2], points[1::2]))
    return abs(sum(x1*y2 - x2*y1 for (x1,y1),(x2,y2) in zip(coords, coords[1:]+coords[:1]))) / 2


def main():
    data = json.loads(SOURCE.read_text(encoding="utf-8"))
    images, annotations = [], []

    for frame in data["frames"]:
        images.append({
            "id": frame["frame_id"],
            "file_name": frame["file_name"],
            "width": data["image_width"],
            "height": data["image_height"]
        })
        for ann in frame["annotations"]:
            segmentation = ann.get("segmentation", [])
            area = polygon_area(segmentation[0]) if segmentation else ann["bbox"][2] * ann["bbox"][3]
            annotations.append({
                "id": ann["id"],
                "image_id": frame["frame_id"],
                "category_id": ann["class_id"],
                "bbox": ann["bbox"],
                "area": area,
                "segmentation": segmentation,
                "iscrowd": 0,
                "attributes": {
                    "track_id": ann["track_id"],
                    "occluded": ann["occluded"],
                    "truncated": ann["truncated"],
                    "state": ann["state"],
                    "confidence": ann["confidence"],
                    "needs_review": ann["needs_review"]
                }
            })

    categories = [
        {"id": int(class_id), "name": name}
        for class_id, name in data["classes"].items()
    ]

    output = {"images": images, "annotations": annotations, "categories": categories}
    OUTPUT.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Wrote {len(annotations)} annotations in COCO-style format to {OUTPUT}")


if __name__ == "__main__":
    main()
