from transformers import pipeline

# Load pre-trained emotion model
emotion_pipeline = pipeline("text-classification", 
                            model="j-hartmann/emotion-english-distilroberta-base",
                            return_all_scores=False)

def get_emotion(text):
    result = emotion_pipeline(text)[0]
    return result['label']