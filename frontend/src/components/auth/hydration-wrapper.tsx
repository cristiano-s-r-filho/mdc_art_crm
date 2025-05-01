"use client";

import { useEffect } from "react";
import { useAuthStore } from "@/stores/auth-store";

export function HydrationWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  const { hydrate } = useAuthStore();

  useEffect(() => {
    hydrate();
  }, [hydrate]);

  return <>{children}</>;
}