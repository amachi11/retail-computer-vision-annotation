import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "retail_video_annotations.json"


def iou(a, b):
    ax1, ay1, aw, ah = a
    bx1, by1, bw, bh = b
    ax2, ay2 = ax1 + aw, ay1 + ah
    bx2, by2 = bx1 + bw, by1 + bh
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    union = aw * ah + bw * bh - inter
    return inter / union if union else 0.0


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    tracks = defaultdict(list)

    for frame in data["frames"]:
        for ann in frame["annotations"]:
            tracks[ann["track_id"]].append((frame["frame_id"], ann))

    flags = []
    for track_id, items in tracks.items():
        items.sort(key=lambda x: x[0])
        classes = {ann["class_id"] for _, ann in items}
        if len(classes) > 1:
            flags.append((track_id, "CLASS_SWITCH", "Track changes class"))

        for (f1, a1), (f2, a2) in zip(items, items[1:]):
            score = iou(a1["bbox"], a2["bbox"])
            if f2 <= f1:
                flags.append((track_id, "FRAME_ORDER", f"{f1}->{f2}"))
            if f2 == f1 + 1 and score < 0.12:
                flags.append((track_id, "LOW_TEMPORAL_IOU", f"frames {f1}-{f2}, IoU={score:.3f}"))

    print(f"Tracks checked: {len(tracks)}")
    if flags:
        print("Track review queue:")
        for flag in flags:
            print(" -", flag)
    else:
        print("PASS: no track consistency warnings.")


if __name__ == "__main__":
    main()
