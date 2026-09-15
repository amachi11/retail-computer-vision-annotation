import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_video_annotations.json"
OUT = ROOT / "data" / "yolo_labels"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    width, height = data["image_width"], data["image_height"]
    OUT.mkdir(parents=True, exist_ok=True)

    for frame in data["frames"]:
        lines = []
        for ann in frame["annotations"]:
            x, y, w, h = ann["bbox"]
            x_center = (x + w / 2) / width
            y_center = (y + h / 2) / height
            lines.append(
                f"{ann['class_id']} {x_center:.6f} {y_center:.6f} {w/width:.6f} {h/height:.6f}"
            )
        output = OUT / f"{Path(frame['file_name']).stem}.txt"
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Exported YOLO labels for {len(data['frames'])} frames.")


if __name__ == "__main__":
    main()
