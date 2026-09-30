# Multiscale Modeling of Biological Systems: Neuroscience (KEN3170)

## Setup

### Important - data

**Before starting** anything, **copy** `practical/data` **into** `assignment/data` and download model and data files specified in `assignment/README.md` and put them in `assignment/models` and `assignment/data` folders.

### Environment setup

#### uv - preferred way

Preferably, use `uv` tool inside `Assignment4` directory, with the following commands:

```bash
uv venv ./mmbs4
mmbs4/Scripts/activate
uv sync --locked --active
```

Also, if you're using Jupyter notebooks, install `ipykernel` with `uv pip install ipykernel`.

## Exercises

### Part I

#### 1. Constructing representational dissimilarity matrices (RDMs)

We created RDMs to compare how the brain and the different models represent the same sounds. Each row and column represents one sound, and the sounds are kept in the same order for all RDMs. We used correlation distance, \(1-r\), where \(r\) is the Pearson correlation between two sounds. A lower value means that two sounds are represented more similarly.

##### a) STG brain data

We loaded the brain data using `SantoroDataset()`. Each sound has a pattern of responses across the STG voxels. We calculated the correlation distance between these patterns to create the brain RDM. This RDM was then used as a reference to compare the different models.

##### b) Untrained models

We used the Waveform, Uninspired, and Inspired models without pretrained weights. For each sound, we extracted the activations using `extract_activations()` and turned them into feature vectors. We then created a separate RDM for each layer. This allowed us to see how the untrained models represent the sounds.

##### c) Trained models

We loaded the best model from each of the five training runs for every architecture. We used the same sound order and correlation distance as before and created an RDM for each layer and each run. We kept the runs separate so that we could compare them later, and we showed the first run of each model architecture.

For the Inspired model, `extract_activations()` treats the stacked GRU as one `rnn` representation. It uses the output of the final GRU layer instead of looking at the two GRU layers separately.

##### d) Pretrained YAMNet embeddings

We loaded the embeddings from the pretrained YAMNet model using `load_yamnet_activations(layer="embedding")`. The function averages the two embedding frames for each sound and keeps the sounds in the same order as `SantoroDataset()`.

We then created an RDM from these embeddings. This allowed us to compare YAMNet's sound representations with the STG brain data and the other three models.