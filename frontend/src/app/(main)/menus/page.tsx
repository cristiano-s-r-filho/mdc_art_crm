'use client'
import { useState } from 'react';
import useSWR from 'swr';
import { api } from '../../../lib/api/client';
import { Button } from '@/components/ui/button';

interface Recipe {
  id: number;
  name: string;
  ingredients: Array<{ id: number }>;
}

export default function Menus() {
    const { data: recipes } = useSWR<{ data: Recipe[] }>('/recipes', api.get);
    const [selectedRecipes, setSelectedRecipes] = useState<number[]>([]);
  
    const createMenu = async () => {
      await api.post('/menus', { recipe_ids: selectedRecipes });
    };
  
    return (
      <div className="max-w-2xl mx-auto p-4">
        <h1 className="text-2xl font-bold mb-6">Create Menu</h1>
        <div className="space-y-2">
          {recipes?.data.map((recipe: Recipe) => (
            <label key={recipe.id} className="flex items-center space-x-2 p-2 hover:bg-gray-100 rounded-lg">
              <input
                type="checkbox"
                onChange={(e) => setSelectedRecipes(
                  e.target.checked 
                    ? [...selectedRecipes, recipe.id] 
                    : selectedRecipes.filter((id: number) => id !== recipe.id)
                )}
              />
              <span>{recipe.name}</span>
            </label>
          ))}
        </div>
        <Button onClick={createMenu} className="mt-4">Create Menu</Button>
      </div>
    );
}