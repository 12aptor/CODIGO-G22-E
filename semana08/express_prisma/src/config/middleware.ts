import type { Request, Response, NextFunction } from "express";

export const authMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const token = req.headers.authorization;

  if (!token) {
    res.status(401).json({
      object: "auth",
      error: "Unauthorized",
    });
  }

  // Lógica para verificar la validez del token

  next();
};
