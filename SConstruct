import os
import os.path
import logging
import random
import subprocess
import shlex
import gzip
import re
import functools
import time
import imp
import sys
import json
from steamroller import Environment


vars = Variables("custom.py")
vars.AddVariables(
    ("OUTPUT_WIDTH", "", 5000),
    ("DATA_ROOT", "", os.path.expanduser("~/corpora")),
    ("HATHITRUST_ROOT", "", "${DATA_ROOT}/hathitrust"),
    ("HATHITRUST_INDEX", "", "${HATHITRUST_ROOT}/hathi_index.tsv.gz"),
    ("HATHITRUST_MARC", "", "${HATHITRUST_ROOT}/hathi_marc.json.gz"),
)


env = Environment(
    variables=vars,
    ENV=os.environ,
    tools=[],
    
    BUILDERS={
        "FilterHathiTrust" : Builder(
            action="python scripts/filter_hathitrust.py --index ${HATHITRUST_INDEX} --marc ${HATHITRUST_MARC} --output ${TARGETS[0]}"
        )
    }
)

out = env.FilterHathiTrust(
    "work/filtered_index.txt.gz",
    [
        env["HATHITRUST_INDEX"],
        env["HATHITRUST_MARC"]
    ]
)
