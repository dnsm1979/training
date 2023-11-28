class RecipeModel(object):
    def __init__(
        self,
        author,
        types,
        description,
        link_to_video,
        ingredients,
        name_of_the_cuisine,
    ):
        self.author = author
        self.types = types
        self.description = description
        self.link_to_video = link_to_video
        self.ingredients = ingredients
        self.name_of_the_cuisine = name_of_the_cuisine


class RecipeView(object):
    def __init__(self, model):
        self.model = model

    def display_recipe(recipe):
        print(
            f"Author: {recipe.model.author}\nTypes: {recipe.model.types}"
            f"\nDescription: {recipe.model.description}\nLink to video: {recipe.model.link_to_video}"
            f"\nIngredients: {recipe.model.ingredients}\nName of the cuisine: {recipe.model.name_of_the_cuisine}"
        )


class RecipeController(object):
    def __init__(self, model):
        self.model = model
        self.view = RecipeView(self.model)

    def display_view(self):
        self.view.display_recipe()


if __name__ == "__main__":
    recipe1 = RecipeModel(
        "Alexandra Sedova",
        "salad",
        "Salad with chicken, arugula and tangerine",
        "https://art-lunch.ru/recipe/salat-s-kuricej-rukoloj-i-mandarinom_foto/",
        "chicken fillet, arugula, tangerines, cucumbers, feta cheese, soy sauce, olive oil",
        "Russian",
    )

    controller_1 = RecipeController(recipe1)
    controller_1.display_view()
