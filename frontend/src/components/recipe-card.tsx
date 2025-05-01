import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Recipe } from "@/types/index";
import { Link } from "lucide-react";
type RecipeCardProps = {
    recipe: Recipe;
    href?: string;  // Add href prop
};
export function RecipeCard({ recipe, href }: RecipeCardProps) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>
            {href ? (
              <Link href={href} className="hover:underline">
                {recipe.name}
              </Link>
            ) : (
              recipe.name
            )}
          </CardTitle>
        </CardHeader>
        <CardContent>
        <p className="text-sm text-muted-foreground">
          {recipe.ingredients.length} ingredients
        </p>
        <Button className="mt-4">View Recipe</Button>
      </CardContent>
      </Card>
  );
}