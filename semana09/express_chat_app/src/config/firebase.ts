import { initializeApp } from "firebase/app";
import dotenv from "dotenv";

dotenv.config();

const firebaseConfig = {
  apiKey: process.env.FIREBASE_APIKEY,
  authDomain: "express-chat-app-a73f2.firebaseapp.com",
  projectId: "express-chat-app-a73f2",
  storageBucket: "express-chat-app-a73f2.firebasestorage.app",
  messagingSenderId: "161574250854",
  appId: "1:161574250854:web:031931574cf151f01900a7"
};

export const firebaseApp = initializeApp(firebaseConfig);