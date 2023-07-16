#!/bin/bash

# Start frac-crawl.py
python3 frac-crawl.py

# Wait for frac-crawl.py to finish
wait

# Start frac-lattice.py
python3 frac-lattice.py

# Wait for frac-lattice.py to finish
wait

# Start frac-qr.py
python3 frac-qr.py

# Wait for frac-qr.py to finish
wait
