import torch
from transformers import pipeline

from tqdm.auto import tqdm
tqdm.pandas(desc="Progress") # you can add a description for the progress bar

device = 'mps' if torch.backends.mps.is_available() else 'cuda' if torch.cuda.is_available() else 'cpu'

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True,
    device=device,
    truncation=True,
)

def get_max_sentiment(batch_preds, return_confidence=True):
    batch_labels = []
    batch_confidences = []
    for pred in batch_preds:
        max_score = max(pred, key=lambda x: x['score'])
        batch_labels.append(max_score['label'])
        if return_confidence: batch_confidences.append(max_score['score'])
    if return_confidence:
        return batch_labels, batch_confidences
    else:
        return batch_labels

def classify_sentiment_batch(batch_reviews):
    preds = sentiment_pipeline(batch_reviews)
    labels, confidences = get_max_sentiment(preds)
    return labels, confidences