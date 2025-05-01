"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/stores/auth-store";

export default function ProtectedRoute({
  children,
}: {
  children: React.ReactNode;
}) {
  const router = useRouter();
  const { token, hydrate } = useAuthStore();

  useEffect(() => {
    hydrate().then(() => {
      if (!token) router.push("/login");
    });
  }, [token, router, hydrate]);

  if (!token) return null;

  return <>{children}</>;
}