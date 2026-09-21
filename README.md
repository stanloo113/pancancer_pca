# Pan-Cancer PCA

Principal Component Analysis on the [TCGA-PANCAN HiSeq gene expression dataset](https://archive.ics.uci.edu/dataset/401/gene+expression+cancer+rna+seq) — 801 tumour samples × 20,531 genes across 5 cancer types (BRCA, KIRC, LUAD, PRAD, COAD).

The goal is simple: **do different cancer types form distinct clusters in an unsupervised 2D/3D projection of their transcriptomes?**

If the UCI download fails (offline, mirror down), the pipeline transparently falls back to a synthetic 5-class dataset so the code always runs.

## Results preview

Running the pipeline produces three figures in `outputs/`:

| File | What it shows |
|---|---|
| `pca_2d.png` | Static PC1 vs PC2 scatter, colour-coded by cancer type, with class centroids |
| `pca_3d.html` | Interactive PC1/PC2/PC3 scatter (open in a browser) |
| `scree.png` | Per-PC and cumulative explained variance |

Plus console output: explained variance ratios, silhouette score, and the top-10 loading genes on PC1 and PC2.
