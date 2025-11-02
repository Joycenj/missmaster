import axios from "axios";
const API_BASE = process.env.NEXT_PUBLIC_API_BASE || "http://127.0.0.1:8000";

export const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
  headers: { "Content-Type": "application/json" },
});

export async function listCandidates(category){
  const url = category ? `/api/candidates/?category=${encodeURIComponent(category)}` : "/api/candidates/";
  const { data } = await api.get(url);
  return data;
}
export async function getCandidate(slug){
  const { data } = await api.get(`/api/candidates/${slug}/`);
  return data;
}
export async function createVoteIntent(payload){
  const { data } = await api.post(`/api/vote-intents/`, payload);
  return data;
}
export async function getVoteIntent(id){
  const { data } = await api.get(`/api/vote-intents/${id}/`);
  return data;
}
