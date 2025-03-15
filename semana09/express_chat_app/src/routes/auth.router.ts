import { Router } from "express";
import * as authResource from "../resources/auth.resource";
import multer from "multer";

const storage = multer.memoryStorage();
const upload = multer({ storage });

export const authRouter = Router();

authRouter.post("/register", upload.single("avatar"), authResource.register);
