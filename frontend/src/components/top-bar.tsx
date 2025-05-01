"use client";

import { Button } from "@/components/ui/button";
import { useAuthStore } from "@/stores/auth-store";
import Link from "next/link";

export function TopNav() {
  const { user, logout } = useAuthStore();
  
  return (
    <header className="border-b h-16 flex items-center px-6">
      <div className="flex justify-between items-center w-full">
        <span className="font-semibold">Recipe Manager</span>
        <div className="flex items-center gap-4">
          {user && <span className="text-sm">{user.email}</span>}
          <Button variant="outline" onClick={logout} asChild>
            <Link href="/login">Logout</Link>
          </Button>
        </div>
      </div>
    </header>
  );
}