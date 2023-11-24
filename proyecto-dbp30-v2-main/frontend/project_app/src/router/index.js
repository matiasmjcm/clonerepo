import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegisterView from "@/views/RegisterView";
import LoginView from "@/views/LoginView";
import AuthorsView from "@/views/AuthorsView";
import BooksView from "@/views/BooksView";
import SettingsView from "@/views/SettingsView";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/authors",
    name: "authors",
    component: AuthorsView,
  },
  {
    path: "/books",
    name: "books",
    component: BooksView,
  },
  {
    path: "/settings",
    name: "settings",
    component: SettingsView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
