"use client";

import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { api } from "@/lib/api/client";
import { useRouter } from "next/navigation";

const recipeSchema = z.object({
  name: z.string().min(3, "Name must be at least 3 characters"),
  description: z.string().optional(),
});

export default function NewRecipePage() {
  const router = useRouter();
  const form = useForm({
    resolver: zodResolver(recipeSchema),
    defaultValues: {
      name: "",
      description: "",
    },
  });

  const { mutate: createRecipe } = useMutation({
    mutationFn: (values: z.infer<typeof recipeSchema>) =>
      api.post("/recipes", values),
    onSuccess: () => {
      router.push("/dashboard/recipes");
    },
  });

  return (
    <div className="max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-8">Create New Recipe</h1>
      <Form {...form}>
        <form
          onSubmit={form.handleSubmit((values) => createRecipe(values))}
          className="space-y-6"
        >
          <FormField
            control={form.control}
            name="name"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Recipe Name</FormLabel>
                <FormControl>
                  <Input {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="description"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Description</FormLabel>
                <FormControl>
                  <Input {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />

          <div className="flex justify-end gap-4">
            <Button
              type="button"
              variant="outline"
              onClick={() => router.push("/dashboard/recipes")}
            >
              Cancel
            </Button>
            <Button type="submit">Create Recipe</Button>
          </div>
        </form>
      </Form>
    </div>
  );
}