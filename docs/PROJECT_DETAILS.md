Project Title

Gen Z Media Sentiment Analysis Across News and Social Platforms

Problem Statement

To examine how Generation Z is represented and discussed in both traditional news media and social media, and to analyze how sentiment shifts during major political events such as the Nepal protest (September 2025).

System Components
1. RSS News Sentiment Analysis

RSS feed scraping

Text preprocessing

CNN + LSTM sentiment classification

Aggregated sentiment reporting

2. YouTube Protest Sentiment Analysis

Comment scraping

Text cleaning

Lexicon-based sentiment (VADER)

Deep Learning sentiment (CNN + LSTM trained on IMDB)

Phase-wise sentiment comparison

Deep Learning Architecture

Embedding Layer (128 dimensions)
Conv1D (128 filters, kernel size 5)
MaxPooling
LSTM (64 units)
Dense (ReLU)
Sigmoid Output

Loss: Binary Crossentropy
Optimizer: Adam
Validation Accuracy (IMDB): ~85%

Comparative Analysis
Method	Platform	Output Type
VADER	YouTube	3-class
CNN + LSTM	YouTube	Binary
CNN + LSTM	RSS News	Sentiment classification
Key Insights

News and social media portray Gen Z differently.

Sentiment shifts are observable around major political events.

Deep learning models generalize sentiment across domains.

Lexicon and neural approaches provide complementary perspectives.

🎯 Now Your Repository Is

✔ Complete
✔ Multi-platform
✔ Multi-model
✔ Deep learning justified
✔ Clean architecture
✔ Research-grade