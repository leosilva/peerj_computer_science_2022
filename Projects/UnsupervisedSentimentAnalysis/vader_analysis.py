from leia.leia import SentimentIntensityAnalyzer


# Declare variables for summary printing
positive_list = []
negative_list = []
neutral_list = []


def perform_vader_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    analysis_result = analyzer.polarity_scores(text)

    return analysis_result


def print_summary_analysis(analysis_results_for_summary):
    for analysis_result in analysis_results_for_summary:
        compound = analysis_result["compound"]
        pos = analysis_result["pos"]
        neu = analysis_result["neu"]
        neg = analysis_result["neg"]

        if compound == 0.0:
            neutral_list.append(neu)
        elif compound > 0.0:
            positive_list.append(pos)
        elif compound < 0.0:
            negative_list.append(neg)

    print(f"Positive: {len(positive_list)}")
    print(f"Negative: {len(negative_list)}")
    print(f"Neutral: {len(neutral_list)}")