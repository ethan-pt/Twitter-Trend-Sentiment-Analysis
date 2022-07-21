from twitter import TwitterData
from sentiment import SentimentAnalysis
import tkinter as tk
from tkinter.ttk import Combobox


class App:
    def __init__(self, root):
        self.root = root
        self.twitter_data = TwitterData()
        self.sentiment_analysis = SentimentAnalysis()
        self.trend_names = self.twitter_data.get_trend_names()

        # Tells window how to handle being resized
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(3, weight=3)

        # Add frames to separate different sections
        self.frame_trends = tk.Frame(root)
        self.frame_score = tk.Frame(root)

        # Add choose trend label
        self.label_choose = tk.Label(self.frame_trends, text='Choose trend...')

        # Add score labels
        self.label_score = tk.Label(self.frame_score, text='Score', font=('Arial', 15), padx=20)
        self.score = tk.Label(self.frame_score, text='0', fg='#c91e1e', font=('Arial', 12))

        # Add and configure trends combo box to change based on selection
        self.combo = Combobox(self.frame_trends, values=self.trend_names)
        self.combo.set('Trends')
        self.combo.bind('<<ComboboxSelected>>', self.trend_changed)

        # Place label and combobox in frame_trends
        self.label_choose.grid(column=0, row=0)
        self.combo.grid(column=0, row=1)

        # Place labels in frame_score
        self.label_score.grid(column=0, row=0)
        self.score.grid(column=0, row=1)

        # Place frames in window
        self.frame_trends.grid(column=1, row=0)
        self.frame_score.grid(column=2, row=0)

    # Changes score based on trend selected
    def trend_changed(self, event):
        score = self.sentiment_analysis.analyze_sentiment(self.combo.get())
        self.score.config(text=int(score * 100))

    # Requests trend data from twitter.py
    def get_trends(self):
        return self.twitter_data.get_trend_data()

    # Requests sentiment from sentiment.py
    def get_sentiment(self, trend_name):
        return self.sentiment_analysis.analyze_sentiment(trend_name)


def main():
    root = tk.Tk()
    root.title('Twitter Trend Sentiment Analysis')

    window = App(root)

    root.mainloop()

if __name__ == '__main__':
    main()