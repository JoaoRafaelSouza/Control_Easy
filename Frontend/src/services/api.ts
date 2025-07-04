// src/services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // URL do backend FastAPI
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;