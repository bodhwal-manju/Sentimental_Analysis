#!/usr/bin/env python3
"""
Create a simplified word index for sentiment analysis that works offline
"""

def create_simple_word_index():
    """
    Create a basic word index with common English words
    This allows the app to work without requiring IMDB dataset downloads
    """
    
    # Common positive and negative sentiment words
    positive_words = [
        'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'brilliant', 
        'outstanding', 'superb', 'magnificent', 'terrific', 'awesome', 'perfect',
        'beautiful', 'incredible', 'marvelous', 'spectacular', 'impressive',
        'good', 'nice', 'fine', 'pleasant', 'enjoyable', 'delightful', 'charming',
        'lovely', 'attractive', 'appealing', 'satisfying', 'refreshing', 'exciting'
    ]
    
    negative_words = [
        'terrible', 'awful', 'horrible', 'bad', 'worst', 'disappointing', 
        'boring', 'dull', 'poor', 'weak', 'mediocre', 'pathetic', 'useless',
        'annoying', 'irritating', 'frustrating', 'confusing', 'ridiculous',
        'stupid', 'silly', 'nonsense', 'waste', 'pointless', 'meaningless',
        'unpleasant', 'ugly', 'disgusting', 'revolting', 'repulsive', 'offensive'
    ]
    
    # Common neutral words
    common_words = [
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
        'before', 'after', 'above', 'below', 'over', 'under', 'between', 'among',
        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
        'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
        'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them',
        'my', 'your', 'his', 'her', 'its', 'our', 'their', 'this', 'that', 'these', 'those',
        'movie', 'film', 'actor', 'actress', 'director', 'plot', 'story', 'character',
        'scene', 'dialogue', 'script', 'acting', 'performance', 'cinematography',
        'soundtrack', 'music', 'visual', 'effects', 'special', 'action', 'drama',
        'comedy', 'thriller', 'horror', 'romance', 'adventure', 'fantasy', 'science',
        'fiction', 'documentary', 'animation', 'family', 'musical', 'mystery',
        'watch', 'watched', 'watching', 'see', 'seen', 'seeing', 'show', 'shows',
        'time', 'times', 'year', 'years', 'minute', 'minutes', 'hour', 'hours',
        'first', 'second', 'third', 'last', 'next', 'previous', 'new', 'old',
        'long', 'short', 'big', 'small', 'large', 'little', 'high', 'low',
        'much', 'many', 'more', 'most', 'less', 'least', 'some', 'any', 'all',
        'every', 'each', 'other', 'another', 'same', 'different', 'similar'
    ]
    
    # Combine all words and create index
    all_words = positive_words + negative_words + common_words
    
    # Create word index (starting from index 3 to match IMDB format)
    word_index = {}
    for i, word in enumerate(all_words, start=3):
        word_index[word] = i
    
    # Add special tokens
    word_index['<PAD>'] = 0
    word_index['<START>'] = 1
    word_index['<UNK>'] = 2
    
    return word_index

if __name__ == "__main__":
    word_index = create_simple_word_index()
    print(f"Created word index with {len(word_index)} words")
    
    # Save to file
    import pickle
    with open('simple_word_index.pkl', 'wb') as f:
        pickle.dump(word_index, f)
    print("Word index saved to 'simple_word_index.pkl'")
    
    # Test some words
    test_words = ['great', 'terrible', 'movie', 'unknown_word']
    for word in test_words:
        idx = word_index.get(word, 2)  # 2 is <UNK>
        print(f"'{word}' -> {idx}")