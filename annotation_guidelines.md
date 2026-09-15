# Retail Image & Video Annotation Guidelines

## Bounding Boxes
Draw the smallest axis-aligned rectangle containing all visible pixels of the target object. Avoid extra background. If an object is partially hidden, annotate only the visible extent and mark `occluded=true`. If it extends beyond the frame, mark `truncated=true`.

## Segmentation
Segmentation polygons should follow visible boundaries. Do not invent hidden boundaries behind another object. Use enough vertices to represent meaningful shape changes without unnecessary points.

## Tracking
The same physical object keeps the same `track_id` across consecutive frames. Track IDs must never be reused for another object in the same sequence. Maintain identity through short occlusions only when motion, location, appearance, and context support the match. If identity becomes uncertain, start a new track and flag the transition for review.

## Product States
- `on_shelf`
- `held`
- `in_basket`
- `unknown`

## Hand Actions
- `reaching`
- `holding`
- `releasing`
- `other`

A product changes from `on_shelf` to `held` only when there is visual evidence of possession. Proximity alone is not enough.

## Review Rules
Set `needs_review=true` for severe occlusion, uncertain class, overlapping objects that cannot be separated confidently, possible track-ID switches, motion blur, or unclear interaction state.

## Final QA Checklist
1. Correct class on every object.
2. Tight boxes within frame boundaries.
3. Valid polygons.
4. Consistent track IDs.
5. Correct occlusion and truncation flags.
6. Interaction states supported by visible evidence.
7. Uncertain cases flagged rather than guessed.
