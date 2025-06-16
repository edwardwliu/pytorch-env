#!/bin/bash
if [ ! -z "$VIRTUAL_ENV" ]; then
  deactivate
fi
rm -rf pytorch-env
python3 -m venv pytorch-env
source pytorch-env/bin/activate
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
fi
python3 test_torch.py