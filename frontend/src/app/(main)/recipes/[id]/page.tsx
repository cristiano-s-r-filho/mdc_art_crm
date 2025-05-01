"use client";

import { Button } from "@/components/ui/button";
import { useRecipes } from "@/hooks/use-recipes";
import { useRouter } from "next/navigation";
import { Skeleton } from "@/components/ui/skeleton";
import { api } from "@/lib/api/client";
import { Ingredient } from "@/types";
export default function RecipeDetailPage({ params }: { params: { id: string } }) {
  const router = useRouter();
  const { data: recipe, isLoading, error } = useRecipes();

  const handleDelete = async () => {
    if (confirm("Are you sure you want to delete this recipe?")) {
      await api.delete(`/recipes/${params.id}`);
      router.push("/dashboard/recipes");
    }
  };

  if (isLoading) return <Skeleton className="h-[400px] w-full" />;
  if (error) return <div>Error loading recipe</div>;

  return (
    <div className="max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-2xl font-bold">{recipe?.name}</h1>
        <div className="flex gap-4">
          <Button
            variant="outline"
            onClick={() => router.push(`/dashboard/recipes/${params.id}/edit`)}
          >
            Edit
          </Button>
          <Button variant="destructive" onClick={handleDelete}>
            Delete
          </Button>
        </div>
      </div>

      {recipe?.description && (
        <p className="text-muted-foreground mb-6">{recipe.description}</p>
      )}

      <div className="space-y-4">
        <h2 className="text-xl font-semibold">Ingredients</h2>
        <ul className="space-y-2">
          {recipe?.ingredients?.map((ingredient:Ingredient) => (
            <li key={ingredient.id} className="flex justify-between items-center">
              <span>
                {ingredient.quantity} {ingredient.unit} {ingredient.name}
              </span>
              <span className="text-muted-foreground">
                ${(ingredient.quantity * ingredient.unit_cost).toFixed(2)}
              </span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}