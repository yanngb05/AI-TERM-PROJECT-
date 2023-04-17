import re

def clean_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)   # remove URLs
    tweet = re.sub(r"@\S+", "", tweet)      # remove mentions
    tweet = re.sub(r"#\S+", "", tweet)      # remove hashtags
    tweet = re.sub(r"[^\w\s]", "", tweet)   # remove punctuation
    tweet = tweet.lower()                  # convert to lowercase
    return tweet

tweet1 = "It's March, and that means Brand Bracket is back — your chance to recognize the best brands on Twitter. We’ve picked 16 of our favorites that spark conversations, make us laugh, and connect to what’s happening — but now it’s time for you to decide the champ. Starting March 14, head to to vote for your favorite to advance and ultimately be crowned the Best Brand on Twitter. Meet all the brands competing in this year’s Brand Bracket below, and see why we think they’re championship-level contenders. Can’t get enough of Brand Bracket? You can play along by filling out your predictions here and Tweeting them to."
tweet2 = "Twitter is a social broadcast network that enables people and organizations to publicly share brief messages instantly around the world. This brings a variety of people with different voices, ideas, and perspectives. People are allowed to post content, including potentially inflammatory content, as long as they’re not violating the Twitter Rules. It’s important to know that Twitter does not screen content or remove potentially offensive content."

cleaned_tweet1 = clean_tweet(tweet1)
cleaned_tweet2 = clean_tweet(tweet2)

print(cleaned_tweet1)
print(cleaned_tweet2)
