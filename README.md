# 🛒 Shopping Mart

Shopping Mart is a product recommendation system designed to assist users in finding the best products based on their preferences and queries. It utilizes Prolog for recommendation engine and NLTK with Python for Natural Language Processing to enhance the user experience.

## Features

- **Product Recommendation System**: Shopping Mart employs a recommendation engine written in [Prolog](https://www.swi-prolog.org/) to execute inferences and provide product recommendations.

- **Web Scraped Dataset**: The system utilizes a web scraped Flipkart Dataset, consisting of over 4,300 products, to build its product database.

- **Natural Language Processing (NLP) Layer**: We have integrated a layer of NLP using [NLTK](https://www.nltk.org/) and Python to extract keywords from user queries, such as categories, budget, and product names, and match them with the product database.

- **Top-Rated Product Recommendations**: By leveraging the NLP layer, Shopping Mart recommends the top 5 highest-rated products based on user-specified filters and preferences.

## How it Works

1. User submits a query, including categories, budget, and other relevant information.
2. The NLP layer processes the query, extracting key information.
3. The NLP layer triggers the Prolog engine to execute inferences and recommend the top 5 highest-rated products that match the user's criteria.

## Usage

1. Clone this repository.
2. Install the required dependencies, including Prolog and NLTK.
3. Run the Shopping Mart application.

## Dependencies

- [Prolog (SWI-Prolog)](https://www.swi-prolog.org/)
- [NLTK](https://www.nltk.org/)
- Python

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to reach out with any questions or suggestions!
