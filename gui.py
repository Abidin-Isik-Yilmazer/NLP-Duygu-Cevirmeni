import customtkinter as ctk
import os
import threading
from analyzer import SentimentAnalyzer

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SentimentApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI Duygu Analizi & Çeviri")
        self.geometry("650x700")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "icon.ico")
        try:
            self.iconbitmap(icon_path)
        except:
            pass

        self.configure(fg_color="#18181b")

        self.title_label = ctk.CTkLabel(self, text="İngilizce Metin Analizi",
                                        font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"))
        self.title_label.pack(pady=(25, 15))

        self.input_frame = ctk.CTkFrame(self, fg_color="#27272a", corner_radius=15)
        self.input_frame.pack(pady=10, padx=25, fill="x")

        self.textbox_input = ctk.CTkTextbox(self.input_frame, height=120, fg_color="transparent",
                                            font=ctk.CTkFont(size=14))
        self.textbox_input.pack(pady=15, padx=15, fill="x")

        self.textbox_input.insert("1.0",
                                  "Analiz edilecek İngilizce metni buraya yapıştırın\n(İşlemi başlatmak için Enter'a basabilirsiniz)")
        self.textbox_input.bind("<FocusIn>", self.clear_placeholder)
        self.textbox_input.bind("<Return>", self.run_analysis)
        self.placeholder_cleared = False

        # Buton oluşturulurken text_color_disabled="white" eklendi
        self.analyze_button = ctk.CTkButton(
            self,
            text="Analizi Başlat",
            height=45,
            corner_radius=22,
            font=ctk.CTkFont(size=15, weight="bold"),
            fg_color="#3b82f6",
            hover_color="#2563eb",
            text_color_disabled="white",
            command=self.run_analysis
        )
        self.analyze_button.pack(pady=15)

        self.output_frame = ctk.CTkFrame(self, fg_color="#27272a", corner_radius=15)
        self.output_frame.pack(pady=10, padx=25, fill="x")

        self.textbox_output = ctk.CTkTextbox(self.output_frame, height=250, fg_color="transparent",
                                             font=ctk.CTkFont(size=15), state="disabled")
        self.textbox_output.pack(pady=15, padx=15, fill="x")

        self.analyzer = SentimentAnalyzer()

    def clear_placeholder(self, event):
        if not self.placeholder_cleared:
            self.textbox_input.delete("1.0", "end")
            self.placeholder_cleared = True

    def run_analysis(self, event=None):
        input_text = self.textbox_input.get("1.0", "end-1c")

        if not input_text.strip() or not self.placeholder_cleared:
            return "break"

        # Kilitliyken arka plan rengi daha koyu bir mavi (#1d4ed8) yapıldı
        self.analyze_button.configure(text="⏳ İşleniyor", fg_color="#1d4ed8", state="disabled")
        self.update()

        threading.Thread(target=self.process_in_background, args=(input_text,), daemon=True).start()

        if event:
            return "break"

    def process_in_background(self, input_text):
        result = self.analyzer.analyze_and_summarize(input_text)

        self.textbox_output.configure(state="normal")
        self.textbox_output.delete("1.0", "end")
        self.textbox_output.insert("1.0", result)
        self.textbox_output.configure(state="disabled")

        # İşlem bitince buton rengi ve durumu normale dönüyor
        self.analyze_button.configure(text="Analizi Başlat", fg_color="#3b82f6", hover_color="#2563eb", state="normal")