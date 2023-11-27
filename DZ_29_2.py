class RecipeModel(object):
    def __init__(self, author, types, description, link_to_video, ingredients, name_of_the_cuisine):
        self.author = author
        self.types = types
        self.description = description
        self.link_to_video = link_to_video
        self.ingredients = ingredients
        self.name_of_the_cuisine = name_of_the_cuisine


class RecipeView(object):
    @staticmethod

    def display_recipe(recipe):
        print(f'Author: {recipe.author}\nTypes: {recipe.types}'
              f'\nDescription: {recipe.description}\nLink to video: {recipe.link_to_video}'
              f'\nIngredients: {recipe.ingredients}\nName of the cuisine: {recipe.name_of_the_cuisine}')

class RecipeController(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view




    def display_view(self):
        self.view.display_recipe()


if __name__ == '__main__':
    recipe1 = RecipeModel('Alexandra Sedova', 'salad', 'Salad with chicken, arugula and tangerine', 'https://art-lunch.ru/recipe/salat-s-kuricej-rukoloj-i-mandarinom_foto/', 'chicken fillet, arugula, tangerines, cucumbers, feta cheese, soy sauce, olive oil', 'Russian')
    recipe2 = RecipeModel('Women', 'Shoes', 'Red', '400$', 'Gucсi', '7')

    controller_1 = RecipeController(recipe1)
    controller_1.display_view()