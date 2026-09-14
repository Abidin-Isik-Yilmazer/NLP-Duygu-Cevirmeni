from transformers import pipeline
from deep_translator import MyMemoryTranslator
import warnings
import re
import textwrap

warnings.filterwarnings("ignore")


class SentimentAnalyzer:
    def __init__(self):
        print("Yapay zeka modeli yükleniyor, lütfen bekleyin...")
        self.nlp_model = pipeline("sentiment-analysis",
                                  model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
        self.translator = MyMemoryTranslator(source='english', target='turkish')
        print("Sistem hazır!")

    def get_sentiment(self, text):
        # Yapay zeka modelinin de (distilbert) kendi içinde 512 kelimelik bir sınırı vardır.
        # Hata vermemesi için analize giden metni baştan sınırlandırıyoruz.
        short_text = text[:1500]
        result = self.nlp_model(short_text)[0]
        return result['label'], result['score']

    def get_translation(self, text):
        # 500 karakter sınırını aşmamak için metni 450 karakterlik parçalara bölüyoruz
        chunks = textwrap.wrap(text, width=450, break_long_words=False)
        translated_chunks = []

        for chunk in chunks:
            try:
                # Her parçayı çevir ve listeye ekle
                translated_chunks.append(self.translator.translate(chunk))
            except:
                pass

        # Çevrilen parçaları aralarına boşluk koyarak tek bir metin haline getir
        return " ".join(translated_chunks)

    def get_word_analysis(self, text):
        clean_text = re.sub(r'[^\w\s]', '', text).lower()
        words = list(dict.fromkeys(clean_text.split()))

        word_list_str = "\n\n📖 Kelime Kelime Analiz:\n"
        for word in words:
            if word.strip():
                try:
                    tr_word = self.get_translation(word)
                    word_list_str += f"▪ {word} : {tr_word}\n"
                except:
                    pass
        return word_list_str

    def analyze_and_summarize(self, english_text):
        label, score = self.get_sentiment(english_text)
        turkish_label = "Olumlu" if label == "POSITIVE" else "Olumsuz"
        confidence_percentage = round(score * 100, 2)

        translated_text = self.get_translation(english_text)
        word_analysis = self.get_word_analysis(english_text)

        summary = (
            f"🎯 Duygu Durumu: {turkish_label}\n"
            f"📊 Eminlik Oranı: %{confidence_percentage}\n"
            f"🌍 Metnin Çevirisi: {translated_text}"
            f"{word_analysis}"
        )
        return summary