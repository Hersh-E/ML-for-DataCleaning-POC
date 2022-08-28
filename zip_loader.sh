#!/bin/bash

zip -r ml4c_v1_0_1.zip ./ -x "__MAC*" -x "test.py" -x "zip_loader.sh" -x "*.zip" -x "*.DS_Store*" -x ".git*" -x "README.md" -x "cache*" -x "*__pycache__*" -x "docs*"
