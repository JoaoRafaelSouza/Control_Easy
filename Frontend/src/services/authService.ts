// src/services/authService.ts
import api from './api';

interface LoginPayload {
  email: string;
  password: string;
}

export async function login(payload: LoginPayload) {
  const response = await api.post('/login', payload);
  return response.data; 
}

export function logout() {
  localStorage.removeItem('token');
}