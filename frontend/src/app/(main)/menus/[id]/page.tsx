'use client';
import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import { api } from '@/lib/api/client';

interface Ingredient {
  name: string;
  quantity: number;
  unit: string;
  totalCost: number;
}

interface Recipe {
  id: number;
  name: string;
  ingredients: Ingredient[];
}

interface MenuData {
  id: number;
  name: string;
  recipes: Recipe[];
}

export default function MenuDetailPage() {
  const params = useParams();
  const [menu, setMenu] = useState<MenuData | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadMenu = async () => {
      try {
        const response = await api.get<MenuData>(`/menus/${params.id}/shopping-list`);
        setMenu(response.data);
      } catch (err) {
        setError('Failed to load menu');
      }
    };
    loadMenu();
  }, [params.id]);

  if (error) return <div>{error}</div>;
  if (!menu) return <div>Loading...</div>;
return(
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">{menu.name}</h1>
      
      <div className="space-y-6">
        {menu.recipes.map(recipe => (
          <div key={recipe.id} className="bg-white p-4 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-3">{recipe.name}</h2>
            <div className="space-y-2">
              {recipe.ingredients.map(ingredient => (
                <div key={ingredient.name} className="flex justify-between">
                  <span>{ingredient.quantity}{ingredient.unit} {ingredient.name}</span>
                  <span>${ingredient.totalCost.toFixed(2)}</span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}