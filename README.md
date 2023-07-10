 # Book Recommendation System using Collaborative Filtering

This project implements a book recommendation system based on collaborative filtering, a popular approach in recommendation systems. The system aims to provide personalized book recommendations to users by leveraging the preferences of similar users.

## Project Details

The book recommendation system is built using Python and consists of the following main components:

1. **Data Processing**: The system processes the raw book data to extract relevant features such as user preferences, book ratings, and item features. The data is typically in CSV format, with columns for `Books.csv`, `Ratings.csv`, and `Users.csv`.

2. **Collaborative Filtering Algorithm**: The algorithm utilizes user-based collaborative filtering to generate recommendations. It follows these steps:

   - **User Similarity Computation**: Similarity between users is calculated using a suitable metric such as cosine similarity or Pearson correlation coefficient. This step helps identify users with similar preferences.
   
   - **Finding Similar Users**: Users with similar preferences are identified based on their calculated similarity scores. This step forms the basis for generating personalized recommendations.
   
   - **Generating Recommendations**: The system generates recommendations for a target user by aggregating the preferences of similar users. Items highly rated by similar users but not yet seen by the target user are recommended.

3. **Deployment**: This model is deployed to render which is PaaS and UI has made with Streamlit

## Usage

To use the book recommendation system:

1. Clone the repository: `git clone https://github.com/your-username/Book-Recommendation-System---Collaborative-Filtering.git`.

2. Install dependencies: Navigate to the project directory and install the required dependencies using `pip install -r requirements.txt`.

3. Prepare the data: Ensure that you have the necessary book data in the expected format (CSV with columns for `user_id`, `book_id`, and `rating`).

4. Run the recommendation system: Execute the main script by running `app.py` and follow the instructions provided.

5. Get personalized recommendations: Once the system has processed the data and generated recommendations, you will receive a list of books recommended for you based on your preferences.


## Contributing

Contributions to this book recommendation system are welcome. If you encounter any issues, have suggestions, or want to contribute improvements, please open an issue or submit a pull request. When contributing, please adhere to the existing coding style and provide clear documentation for any changes or new features.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code for your own purposes.
