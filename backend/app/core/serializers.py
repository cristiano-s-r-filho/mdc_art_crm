from rest_framework import serializers
from .models import User, Recipe, Ingredient, Menu

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ('recipe',)

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)
    
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('owner', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)
        return recipe

class MenuSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ('owner', 'created_at')