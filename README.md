# Bite_Plans
Custom Meal Planning

## Motivations
I need to take more control over my longterm nutrition. I've tried a couple of other solutions but I couldn't stick with anything. So, I will build it myself and hoping the time invested to build it just the way I want will entice me to commit. I enjoy cooking but, I find planning most meals tedious and a slough. I will automate that process. 

## Plans
1. Create a SurrealDB database that will run in memory and be saved to disk when not in use. This database will hold the recipes I upload, information about ingredients, local store prices, meals I've eaten recently, how well ingredients go together.
2. Create a routine that I can type a recipe into (Title, Description, Serving Size, Ingredients, Instructions, Cooking Time (Optional)
3. Scrape Publix's website for local prices on ingredients
4. Use Llama 3 8b to parse the descriptions of the listings on the website so I don't have to write a bunch of rules to attempt to parse it myself. (Also because I'd like to learn how to run a model locally)
5. Initial success will be successfully planning 3 days of Breakfast, Lunch, Snack, Dinner, Dessert
