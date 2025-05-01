import { useQuery } from "@tanstack/react-query";
import { api } from "@/lib/api/client";

export const useRecipe = (id: string) => {
  return useQuery({
    queryKey: ["recipe", id],
    queryFn: async () => {
      const { data } = await api.get(`/recipes/${id}`);
      return data;
    },
  });
};

export const useRecipes = () => {
    return useQuery({
      queryKey: ['recipes'],
      queryFn: async () => {
        const { data } = await api.get('/recipes');
        return data;
      }
    });
  };