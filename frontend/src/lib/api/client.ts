import axios from 'axios';

export const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
  headers: {
    'Content-Type': 'application/json',
  }
});

// Response interceptor
api.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error.response?.data?.message || 'Error')
);