#!/bin/zsh

set -eo pipefail

# python eplabel-multiline.py "$@" | tee /dev/tty | lpr -P "Zebra_LP2844_EPL2_CUPS" -o raw
python eplabel-multiline.py "$@" | tee /dev/tty | lpr -P "type2" -o raw
