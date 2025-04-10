import { z } from "zod";

export const registerSchema = z.object({
  username: z.string().trim(),
  email: z.string().email().trim(),
  password: z.string().trim(),
});

export const loginSchema = z.object({
  email: z.string().email().trim(),
  password: z.string().trim()
})