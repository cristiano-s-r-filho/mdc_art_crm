import axios from "axios";
import { useAuthStore } from "@/stores/auth-store";
import { env } from "node:process";

export const api = axios.create({
    baseURL:"http://localhost:8000",
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().token;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});