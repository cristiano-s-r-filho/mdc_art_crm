"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Button } from "@/components/ui/button";
import { LayoutDashboard, Utensils, List } from "lucide-react";

export function Sidebar() {
  const pathname = usePathname();

  const navItems = [
    {
      href: "/dashboard",
      label: "Dashboard",
      icon: <LayoutDashboard className="h-4 w-4" />,
    },
    {
      href: "/dashboard/recipes",
      label: "Recipes",
      icon: <Utensils className="h-4 w-4" />,
    },
    {
      href: "/dashboard/menus",
      label: "Menus",
      icon: <List className="h-4 w-4" />,
    },
  ];

  return (
    <div className="w-64 border-r h-[calc(100vh-4rem)]">
      <div className="p-4 space-y-1">
        {navItems.map((item) => (
          <Button
            key={item.href}
            asChild
            variant={pathname === item.href ? "secondary" : "ghost"}
            className="w-full justify-start"
          >
            <Link href={item.href}>
              {item.icon}
              <span className="ml-2">{item.label}</span>
            </Link>
          </Button>
        ))}
      </div>
    </div>
  );
}
