import { z } from "zod";

export const channelSchema = z.object({
    name: z.string().trim(),
    type: z.enum(["TEXT", "VOICE"])
})