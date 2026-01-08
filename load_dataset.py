from datasets import load_dataset

def load_amazon_reviews(language="hi", samples=1000):
    """
    Loads Amazon Multilingual Reviews dataset.
    """
    dataset = load_dataset(
        "mteb/amazon_reviews_multi",
        language,
        split=f"train[:{samples}]"
    )
    return dataset


if __name__ == "__main__":
    data = load_amazon_reviews()
    print(data[0])
