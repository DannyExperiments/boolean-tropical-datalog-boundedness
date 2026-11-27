# Explore the tropical path trace

[Download the offline explorer ZIP](https://raw.githubusercontent.com/DannyExperiments/boolean-tropical-datalog-boundedness/v1.0.0/visualization/boolean-tropical-datalog-boundedness-explorer.zip), extract it, and open index.html. Move the round slider to see the Boolean and tropical values at the first vertex. Drag Rotate to turn the chart.

The four path edges have numeric weight zero. Guards have weights 81, 27, 9, 3 and 1. A derivation that stops at vertex j uses all prior guard weights once and the guard at j twice. The exact successive costs are 162, 135, 126, 123 and 122. Their first rounds are 2, 3, 4, 5 and 6. The chart compares bar heights relative to the largest cost and highlights the selected round. The earlier rounds 0 and 1 have no proof yet.

The five bars show one worked case. The paper proves the same round growth for arbitrary path length.

To render the illustration, use an existing Python environment with Pillow and Arial or DejaVu Sans.

    python3 visualization/render.py
