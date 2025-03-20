import { Router } from "express";
import * as channelResource from "../resources/channel.resource";

export const channelRouter = Router();

channelRouter.post("/create", channelResource.createChannel);
channelRouter.get("/list", channelResource.listChannels);