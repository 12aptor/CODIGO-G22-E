import { Router } from "express";
import * as messageResource from "../resources/message.resource";

export const messageRouter = Router();

messageRouter.get("/list/:channelId", messageResource.listMessages);