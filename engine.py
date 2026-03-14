from transformers import pipeline

class IntentEngine:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        print(f"Initializing engine with {model_name}...")
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, text):
        results = self.classifier(text)
        return results

if __name__ == "__main__":
    engine = IntentEngine()
    test_text = "The new simulation model is performing exceptionally well!"
    print(f"Analysis for: '{test_text}'")
    print(engine.analyze(test_text))
