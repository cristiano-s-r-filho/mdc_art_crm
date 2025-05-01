export type Recipe = {
    id: number;
    name: string;
    description?: string;
    ingredients: Ingredient[];
};
  
export type Ingredient = {
    id: number;
    name: string;
    quantity: number;
    unit: string;
    unit_cost: number;  
};
  
export type Menu = {
    id: number;
    name: string;
    recipes: Recipe[];
};