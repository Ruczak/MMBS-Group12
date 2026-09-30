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

#### 2. Comparing models with the brain

We compare each model RDM with the STG RDM using Spearman correlation. A higher score means that the model and brain rank sound differences more similarly. We use five runs per model and show averages with 95% confidence intervals across runs.

##### a) Effect of training

We compare the final layers of trained and untrained models. Waveform's average score rose slightly after training. The averages for Uninspired and Inspired fell. The corrected tests did not show a clear training effect in these runs.

##### b) Effect of model design

Inspired had the highest trained final-layer average (0.055), followed by Uninspired (0.029) and Waveform (-0.040). The corrected tests supported a difference between Inspired and each of the other two models. YAMNet scored 0.028 and is shown as a reference.

##### c) Effect of layer depth

The final layer scored higher than the first layer in all three trained models. However, Waveform and Uninspired had their highest average scores before the final layer. We show all extracted layers in the notebook.

We use Welch's t-tests and Holm correction for the six comparisons in 2a and 2b. We do not test differences between layers. The scores are small, and the brain data come from one person, so these results have limits.

## Use of AI

AI was used to help fix setup errors and draft explanations for Part I. This includes the trained-model and the comparisons in 2a, 2b, and 2c. Some code and text were inspired/corrected by AI. The conversation records this help.
[AI conversation PDF](rdm_conversation_exact_qa.pdf)
