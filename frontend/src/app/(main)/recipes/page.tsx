"use client";

import { RecipeCard } from "@/components/recipe-card";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { useRecipes } from "@/hooks/use-recipes";
import Link from "next/link";
import { Recipe } from "@/types";
export default function RecipesPage() {
  const { data: recipes, isLoading, error } = useRecipes();

  return (
    <div className="space-y-8">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Your Recipes</h1>
        <Button asChild>
          <Link href="/dashboard/recipes/new">Create New</Link>
        </Button>
      </div>

      {isLoading && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3].map((i) => (
            <Skeleton key={i} className="h-[200px] rounded-lg" />
          ))}
        </div>
      )}

      {error && (
        <div className="text-destructive">
          Error loading recipes: {error.message}
        </div>
      )}

      {recipes && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recipes.map((recipe:Recipe) => (
            <RecipeCard 
              key={recipe.id} 
              recipe={recipe}
              href={`/dashboard/recipes/${recipe.id}`}
            />
          ))}
        </div>
      )}
    </div>
  );
}