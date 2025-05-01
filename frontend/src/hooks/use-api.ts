import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api/client";

// Fetch all recipes
export const useRecipes = () => {
  return useQuery({
    queryKey: ["recipes"],
    queryFn: async () => {
      const { data } = await api.get("/recipes");
      return data;
    },
  });
};

// Fetch shopping list
export const useShoppingList = (menuId: string) => {
  return useQuery({
    queryKey: ["shopping-list", menuId],
    queryFn: async () => {
      const { data } = await api.get(`/menus/${menuId}/shopping-list`);
      return data;
    },
  });
};