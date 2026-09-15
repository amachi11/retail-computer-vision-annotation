# Retail Computer Vision Annotation Quality Report

## Dataset Overview

- Scenario: retail product/customer-hand interaction
- Frames represented: 6
- Total annotations represented: 14
- Object classes: product, hand, basket, shelf
- Persistent tracks: product `10`, hand `20`, basket `30`
- Geometry: bounding boxes + segmentation polygons
- Attributes: confidence, occlusion, truncation, interaction state, manual review

## Sequence Logic

The sample sequence follows a product through a realistic interaction lifecycle:

`on_shelf → reached for → held → moved → released → in_basket`

The same product and hand retain persistent track identities across frames.

## Quality Checks

- Unique annotation IDs
- Allowed class IDs
- Positive bounding-box dimensions
- Image-boundary checks
- Polygon structure validation
- Confidence range validation
- Track class consistency
- Frame ordering
- IoU-based temporal checks
- Manual review routing

## Difficult Case

Frame 104 contains significant product/hand overlap. The product is marked `needs_review=true` because its visible boundary is less certain during the interaction. This demonstrates review escalation rather than forced certainty.

## Export Support

The project includes:
- normalized YOLO bounding-box export;
- COCO-style bounding boxes and polygon segmentation;
- custom attributes preserving track IDs, state, occlusion, confidence, and review status.

## Portfolio Integrity

This is a synthetic portfolio project designed to demonstrate computer-vision annotation, tracking, export, and quality-control workflows. It does not use confidential client or employer imagery.
