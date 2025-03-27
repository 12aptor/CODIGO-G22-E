import { Router } from "express";
import * as userResources from "../resources/user.resource";

export const userRouter = Router();

userRouter.get("/", userResources.getUsers);
userRouter.post("/", userResources.createUser);