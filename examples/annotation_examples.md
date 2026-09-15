# Annotation Examples

## Example 1 — Product on Shelf
Frame 101 contains a clearly visible retail product and a customer hand approaching it.

- Product: class `product`, track `10`, state `on_shelf`
- Hand: class `hand`, track `20`, state `reaching`
- No review required

## Example 2 — Partial Occlusion
In frame 103, the hand overlaps the product while possession is visible.

- Product remains track `10`
- Product state changes to `held`
- `occluded=true`
- Segmentation follows only visible boundaries

## Example 3 — Review Queue
Frame 104 contains heavier overlap between the hand and product.

The product annotation is flagged `needs_review=true` because the visible boundary is less certain and the track should be checked for continuity before final approval.

## Example 4 — Product Placement
By frame 106, the product is placed in the basket.

- Product track remains `10`
- Product state becomes `in_basket`
- Hand state becomes `releasing`
- Basket remains persistent track `30`

## Annotation Principle
When object identity or geometry cannot be established confidently, flag it for review rather than inventing a label or boundary.
