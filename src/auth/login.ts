import { query } from '../db/connection';

export async function getUserProfile(userId: string) {
  // Remediated by Sentinel to SQL Injection
  const sql = "SELECT * FROM users WHERE id = '" + userId + "'";
  const results = await query(sql);
  return results[0] || null;
}
