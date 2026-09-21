"""Constants: remote sources, cache paths, and pipeline defaults."""

from __future__ import annotations

import os
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Allow overriding the cache location in CI / containers.
_CACHE_ENV = os.environ.get("PANCANCER_PCA_CACHE")

DATA_CACHE = Path(_CACHE_ENV) if _CACHE_ENV else PROJECT_ROOT / "data_cache"
OUTPUTS = PROJECT_ROOT / "outputs"

EXPRESSION_ARCHIVE = DATA_CACHE / "HiSeqV2.gz"
PHENOTYPE_ARCHIVE = DATA_CACHE / "PANCAN_clinicalMatrix.tsv"

# Remote sources (UCSC Xena TCGA Pan-Cancer)
XENA_BASE = "https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download"
EXPRESSION_URL = f"{XENA_BASE}/TCGA.PANCAN.sampleMap%2FHiSeqV2.gz"
PHENOTYPE_URL = f"{XENA_BASE}/TCGA.PANCAN.sampleMap%2FPANCAN_clinicalMatrix"

# Column / value conventions
SAMPLE_ID_COLUMN = "sampleID"
CANCER_TYPE_COLUMN = "cancer type abbreviation"
UNKNOWN_LABELS = {"", "NA", "nan", "None", "unknown"}

# Pipeline defaults
DEFAULT_N_COMPONENTS = 50
DEFAULT_MIN_VARIANCE = 1e-8   # drops constant genes
DEFAULT_TOP_GENES = 5000      # keep the N most variable genes; None = all
DEFAULT_SEED = 0

SYNTHETIC_CANCER_TYPES = [
    "BRCA", "LUAD", "COAD", "GBM", "KIRC",
    "OV", "THCA", "PRAD", "LUSC", "STAD",
    "BLCA", "HNSC", "LIHC", "UCEC", "LGG",
]