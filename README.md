# Retail Computer Vision Annotation & Tracking Portfolio

A production-style portfolio project demonstrating image and video annotation for retail computer-vision systems. The project focuses on accurate object labeling, segmentation, multi-object tracking, difficult-case review, and automated quality control.

## Project Scenario

This project simulates annotation work for a retail store camera system that needs to understand products and customer interactions across video frames.

Objects are annotated using:
- Bounding boxes
- Segmentation polygons
- Class labels
- Persistent track IDs across frames
- Occlusion and truncation attributes
- Interaction states
- Confidence scores
- Manual review flags

## Object Classes

| Class ID | Label | Description |
|---|---|---|
| 0 | product | Retail merchandise or packaged goods |
| 1 | hand | Customer or employee hand |
| 2 | basket | Shopping basket |
| 3 | shelf | Shelf or product display region |

## Interaction States

### Products
- `on_shelf`
- `held`
- `in_basket`
- `unknown`

### Hands
- `reaching`
- `holding`
- `releasing`
- `other`

## Advanced Skills Demonstrated

- Image annotation
- Video-frame annotation
- Bounding-box labeling
- Segmentation-mask / polygon annotation
- Object classification
- Multi-object tracking
- Persistent track-ID management
- Occlusion and truncation handling
- Retail product-hand interaction labeling
- Annotation QA and review workflows
- IoU-based temporal consistency checks
- COCO-style annotation structure
- YOLO label conversion
- Dataset statistics and class-balance reporting
- Review queue generation

## Repository Structure

```text
retail-computer-vision-annotation/
├── README.md
├── annotation_guidelines.md
├── requirements.txt
├── data/
│   ├── classes.json
│   ├── retail_video_annotations.json
│   ├── review_queue.csv
│   └── coco_annotations.json
├── examples/
│   └── annotation_examples.md
├── src/
│   ├── validate_annotations.py
│   ├── track_quality_control.py
│   ├── convert_to_yolo.py
│   ├── generate_coco.py
│   └── dataset_statistics.py
└── reports/
    └── quality_report.md
```

## Annotation Workflow

1. Review the full image or video frame before drawing labels.
2. Identify all target objects using the approved class list.
3. Draw tight bounding boxes around visible object extents.
4. Create visible-boundary segmentation polygons for selected objects.
5. Assign persistent `track_id` values across adjacent frames.
6. Record occlusion, truncation, interaction state, and confidence.
7. Flag uncertain annotations using `needs_review=true` rather than guessing.
8. Run schema and geometry validation.
9. Run temporal track-quality checks to detect possible ID switches.
10. Export training-ready labels and generate a final QC report.

## Quality-Control Philosophy

High-quality computer-vision annotation requires more than drawing a box. Box geometry, class identity, object continuity, segmentation boundaries, and interaction labels must all be consistent. Difficult examples are explicitly routed for review instead of forcing certainty.

This portfolio uses synthetic annotation metadata so the complete workflow can be demonstrated without using confidential client or employer imagery.

## Run the Project

```bash
python src/validate_annotations.py
python src/track_quality_control.py
python src/convert_to_yolo.py
python src/generate_coco.py
python src/dataset_statistics.py
```

No external Python packages are required.

## Author

**Amanda Eze**  
AI Data Annotation • Computer Vision Labeling • Data Quality
