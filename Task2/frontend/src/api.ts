import axios from "axios";

const API_URL = "http://localhost:8000";

export const scrapeBooks = async (url: string) => {
  return axios.post(`${API_URL}/scrape`, { url });
};

export const getBooks = async (filters?: { category?: string; title?: string }) => {
  let query = "";
  if (filters) {
    const params = new URLSearchParams();
    if (filters.category) params.append("category", filters.category);
    if (filters.title) params.append("title_contains", filters.title);
    query = "?" + params.toString();
  }
  const response = await axios.get(`${API_URL}/books${query}`);
  return response.data;
};
