<template>
  <TheBackground></TheBackground>
  <div class="login-content">
    <h1 style="color: white; font-size: 40px">LOGIN PAGE</h1>
    <form method="POST" action="" @submit.prevent="handleSubmit">
      <label style="color: white" for="username"><b> Username </b></label>
      <input
        type="text"
        placeholder="Enter your username"
        name="username"
        id="username"
        class="input"
        v-model="username"
        required
      />
      <label style="color: white" for="password"><b> Password </b></label>
      <input
        type="password"
        placeholder="Enter your password"
        name="password"
        id="password"
        class="input"
        v-model="password"
        required
      />
      <button type="submit" id="loginButton">Login</button>
    </form>
    <div id="register-error" :class="hide_error === 'true' ? 'hidden' : ''">
      <p style="color: red; font-size: 24px">User does not exists!</p>
    </div>
  </div>
  <TheFooter></TheFooter>
</template>

<script>
import TheBackground from "@/components/TheBackground";
import TheFooter from "@/components/TheFooter";
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      hide_error: "true",
    };
  },
  components: { TheFooter, TheBackground },
  methods: {
    async handleSubmit() {
      await axios
        .post("login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          sessionStorage.setItem("isLogged", response.data["is_logged"]);
          sessionStorage.setItem(
            "currentUserId",
            response.data["current_user_id"]
          );
          sessionStorage.setItem("isAdmin", response.data["is_admin"]);
        })
        .catch((error) => console.log(error), (this.hide_error = "false"));

      if (sessionStorage.getItem("isLogged") === "true") {
        window.location.href = "/";
      }
    },
  },
};
</script>

<style scoped>
.login-content {
  width: 100%;
  position: absolute;
  text-align: center;
  color: whitesmoke;
  top: 40%;
  transform: translateY(-50%);
}

.input {
  width: 20%;
  padding: 15px;
  display: block;
  margin: 0 auto;
  margin-bottom: 30px;
  border: none;
  background: #f1f1f1;
}

input:focus {
  background-color: #ddd;
  outline: none;
}

#loginButton {
  width: 21.55%;
  background-color: #04aa6d;
  color: white;
  padding: 15px;
  margin: 5px 5px 22px 5px;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.hidden {
  display: none;
}
</style>
