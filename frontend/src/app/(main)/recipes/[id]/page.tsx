interface Props {
    params: { id: string };
  }
  
  export default function RecipeDetailPage({ params }: Props) {
    return (
      <div>
        <h1 className="text-2xl font-bold">Recipe {params.id}</h1>
        {/* Recipe details */}
      </div>
    );
  }