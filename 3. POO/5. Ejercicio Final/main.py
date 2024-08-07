from textblob import TextBlob

class Feeling:
    def get_polarity(self, text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        return round(polarity, 1)
    
class FeelingAnalyzer:
    def __init__(self, ranges):
        self.ranges = ranges

    def analyse_feeling(self, polarity):
        for range, feeling in self.ranges:
            if range[0] >=  polarity >= range[1]:
                return feeling



def main():
    #Create the ranges for the Feeling Analizer
    ranges = [
        ((1, 0.6), ("Very Positive")),
        ((0.5, 0.2), ("Positive")), 
        ((0.1, -0.1), ("Neutral")),
        ((-0.1, -0.4), ("Negative")),
        ((-0.5, -1), ("Very Negative")),
    ]

    while True:
        print("Feeling Analyzer...")

        #Create the Feeling() object and get it's polarity
        feeling = Feeling()
        polarity = feeling.get_polarity(input("Enter a text: "))

        #Create FeelingAnalizer() object, analyse the feeling, and print the result
        analizer = FeelingAnalyzer(ranges)
        analysis = analizer.analyse_feeling(polarity)
        print(f"{analysis}\n")

if __name__ == "__main__":
    main()
        
      
