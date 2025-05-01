import { create } from "zustand";
import { persist } from "zustand/middleware";
import { api } from "@/lib/api/client";
type User = {
  id: number;
  email: string;
};

type AuthState = {
  token: string | null;
  user: User | null;
  login: (token: string, user: User) => void;
  logout: () => void;
  hydrate: () => Promise<void>;
};

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      user: null,
      login: (token, user) => {
        set({ token, user });
        localStorage.setItem("token", token);
      },
      logout: () => {
        set({ token: null, user: null });
        localStorage.removeItem("token");
      },
      hydrate: async () => {
        const token = localStorage.getItem("token");
        if (token) {
          // Verify token with backend
          try {
            const { data } = await api.get("/auth/me");
            set({ token, user: data.user });
          } catch {
            localStorage.removeItem("token");
          }
        }
      },
    }),
    {
      name: "auth-storage",
    }
  )
);
