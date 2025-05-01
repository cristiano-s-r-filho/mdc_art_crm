import { useMutation } from "@tanstack/react-query";
import { api } from "@/lib/api/client";

export const useLogin = () => {
  return useMutation({
    mutationFn: (credentials: { email: string; password: string }) =>
      api.post("/auth/login", credentials),
  });
};

export const useRegister = () => {
  return useMutation({
    mutationFn: (userData: { email: string; password: string }) =>
      api.post("/auth/register", userData),
  });
};