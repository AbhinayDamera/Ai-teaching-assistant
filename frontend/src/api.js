import axios from 'axios';

// In production, REACT_APP_API_URL points to your Render backend URL
// In development, empty string uses the proxy in package.json
const BASE_URL = process.env.REACT_APP_API_URL || '';

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 30000,
});

export default api;
