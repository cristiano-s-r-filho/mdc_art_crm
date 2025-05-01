'use client'
import { useState } from 'react';
import { Button } from '../../components/Button';
import { Input } from '../../components/Input';
import { api } from '../../lib/utils/api';

interface Ingredient {
    name: string;
    quantity: number;
    unit: string;
    price: number;
  }

  export default function Recipes() {
    const [ingredients, setIngredients] = useState<Ingredient[]>([
      { name: '', quantity: 0, unit: 'g', price: 0 }
    ]);
  
    const addIngredient = () => setIngredients([...ingredients, { name: '', quantity: 0, unit: 'g', price: 0 }]);
  
    const submitRecipe = async (e: React.FormEvent) => {
      e.preventDefault();
      const formData = new FormData(e.currentTarget as HTMLFormElement);
      await api.post('/recipes', {
        name: formData.get('name'),
        ingredients: ingredients.map(ing => ({
          name: ing.name,
          quantity: ing.quantity,
          unit: ing.unit,
          price_per_unit: ing.price
        }))
      });
    };
  
    return (
      <div className="max-w-2xl mx-auto p-4">
        <h1 className="text-2xl font-bold mb-6">Create Recipe</h1>
        <form onSubmit={submitRecipe} className="space-y-4">
          <Input name="name" placeholder="Recipe name" required />
          {ingredients.map((ing, i) => (
            <div key={i} className="flex gap-2">
              <Input
                value={ing.name}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                  const newIngredients = [...ingredients];
                  newIngredients[i].name = e.target.value;
                  setIngredients(newIngredients);
                }}
                placeholder="Ingredient"
              />
              <Input
                type="number"
                value={ing.quantity}
                onChange={(e: React.ChangeEvent<HTMLInputElement>) => {
                  const newIngredients = [...ingredients];
                  newIngredients[i].quantity = parseFloat(e.target.value);
                  setIngredients(newIngredients);
                }}
              />
            </div>
          ))}
          <Button type="button" onClick={addIngredient}>+ Add Ingredient</Button>
          <Button type="submit">Save Recipe</Button>
        </form>
      </div>
    );
  }
