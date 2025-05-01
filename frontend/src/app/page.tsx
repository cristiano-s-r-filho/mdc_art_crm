import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Utensils} from "lucide-react";
import Link from "next/link";
import { ShoppingCart } from "lucide-react";
import { DollarSign } from "lucide-react";
export default function HomePage() {
  return (
    <div className="min-h-screen flex flex-col">
      <nav className="flex justify-between items-center p-6 border-b">
        <span className="text-xl font-bold">RecipeMaster</span>
        <div className="space-x-4">
          <Button asChild variant="ghost">
            <Link href="/login">Login</Link>
          </Button>
          <Button asChild>
            <Link href="/register">Get Started</Link>
          </Button>
        </div>
      </nav>

      <main className="flex-1 flex items-center justify-center p-6">
        <Card className="w-full max-w-4xl">
          <CardHeader>
            <CardTitle className="text-3xl font-bold text-center">
              Transform Your Meal Planning
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-8">
            <div className="grid md:grid-cols-3 gap-8 text-center">
              <div className="space-y-2">
                <Utensils className="h-12 w-12 mx-auto" />
                <h3 className="text-xl font-semibold">Recipe Management</h3>
                <p className="text-muted-foreground">
                  Create, organize, and track your favorite recipes
                </p>
              </div>
              <div className="space-y-2">
                <ShoppingCart className="h-12 w-12 mx-auto" />
                <h3 className="text-xl font-semibold">Smart Shopping Lists</h3>
                <p className="text-muted-foreground">
                  Automatic ingredient aggregation
                </p>
              </div>
              <div className="space-y-2">
                <DollarSign className="h-12 w-12 mx-auto" />
                <h3 className="text-xl font-semibold">Cost Tracking</h3>
                <p className="text-muted-foreground">
                  Real-time meal cost calculations
                </p>
              </div>
            </div>

            <div className="text-center space-y-4">
              <Button asChild size="lg">
                <Link href="/register">Start Cooking Smarter</Link>
              </Button>
              <p className="text-sm text-muted-foreground">
                Already have an account?{' '}
                <Link href="/login" className="text-primary underline">
                  Sign in
                </Link>
              </p>
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  );
}