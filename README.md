# Evolutionary Marketing

Evolutionary Marketing is an innovative application that utilizes genetic algorithms and artificial intelligence to optimize and evolve ad variations for marketing campaigns. By leveraging the power of OpenAI's GPT-4 and DALL-E 2 models, this app generates ad copy and images, and optimizes them based on their performance scores.

## Features

- Generate ad copy using OpenAI's GPT-4 language model
- Generate ad images using OpenAI's DALL-E 2 image generation model
- Apply genetic algorithm techniques (selection, crossover, mutation) to evolve ad variations
- Optimize ad variations based on their performance scores
- Integrate with Google Analytics API to fetch real-time performance data (CPA)

## Requirements

- Python 3.x
- OpenAI API key
- Google Analytics API credentials

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/richardaragon/evolutionarymarketing.git
   ```

2. Install the required dependencies:
   ```
   pip install openai google-api-python-client
   ```

3. Set up your OpenAI API key:
   - Sign up for an OpenAI API key at [https://www.openai.com](https://www.openai.com)
   - Replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key in the code

4. Set up Google Analytics API credentials:
   - Follow the steps to create a Google Cloud Console project and enable the Google Analytics Reporting API
   - Generate the necessary credentials file (`credentials.json`) and place it in the project directory
   - Replace `'YOUR_VIEW_ID'` with your actual Google Analytics view ID in the code

## Usage

1. Define your initial ad variations in the `ad_variations` list, specifying the ad copy, image, and initial performance score (if available)

2. Run the genetic algorithm by calling the `genetic_algorithm_with_ai` function, specifying the number of generations and providing your OpenAI API key:
   ```python
   optimized_variations = genetic_algorithm_with_ai(ad_variations, generations=10, api_key='YOUR_OPENAI_API_KEY')
   ```

3. The optimized ad variations will be printed, including their ID, ad copy, image URL, and performance score

4. Integrate the optimized ad variations into your marketing campaigns and monitor their performance using Google Analytics

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The use of OpenAI's GPT-4 and DALL-E 2 models is subject to OpenAI's usage policies and terms of service. Make sure to comply with their guidelines and use the generated content responsibly.

Please note that the generated ad copy and images are based on AI models and may require manual review and adjustments before using them in actual marketing campaigns.
