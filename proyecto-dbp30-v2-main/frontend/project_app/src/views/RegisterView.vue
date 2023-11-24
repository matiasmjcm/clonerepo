<template>
  <TheBackground></TheBackground>
  <div class="register-content">
    <h1 style="color: white; font-size: 40px">REGISTER PAGE</h1>
    <form method="POST" action="" @submit.prevent="handleSubmit">
      <label style="color: white" for="firstName"><b> First name </b></label>
      <input
        type="text"
        placeholder="Enter your first name"
        name="firstName"
        id="firstName"
        required
        class="input"
        v-model="first_name"
      />

      <label style="color: white" for="lastName"><b> Last name </b></label>
      <input
        type="text"
        placeholder="Enter your last name"
        name="lastName"
        id="lastName"
        required
        class="input"
        v-model="last_name"
      />

      <label style="color: white" for="username"><b> Username </b></label>
      <input
        type="text"
        placeholder="Enter your username"
        name="username"
        id="username"
        required
        class="input"
        v-model="username"
      />

      <label style="color: white" for="password"><b> Password </b></label>
      <input
        type="password"
        placeholder="Enter your password"
        name="password"
        id="password"
        required
        class="input"
        v-model="password"
      />

      <label style="color: white" for="email"><b> Email </b></label>
      <input
        type="email"
        placeholder="Enter your email"
        name="email"
        id="email"
        required
        class="input"
        v-model="email"
      />

      <div id="register-error" :class="hide_error === 'true' ? 'hidden' : ''">
        <p style="color: red; font-size: 24px">Username already exists!</p>
      </div>

      <button type="submit" class="registerButton">Register</button>

      <div id="server-error" class="hidden">
        <p style="color: red; font-size: 24px">
          Something went wrong! Try it later!
        </p>
      </div>
    </form>
  </div>
  <TheFooter></TheFooter>
</template>

<script>
import TheBackground from "@/components/TheBackground";
import TheFooter from "@/components/TheFooter";
import axios from "axios";

export default {
  name: "RegisterView",
  data() {
    return {
      first_name: "",
      last_name: "",
      username: "",
      password: "",
      email: "",
      hide_error: "true",
    };
  },
  components: { TheFooter, TheBackground },
  async beforeCreate() {
    this.hide_error = "true";
  },
  methods: {
    async handleSubmit() {
      await axios
        .post("/accounts", {
          first_name: this.first_name,
          last_name: this.last_name,
          username: this.username,
          password: this.password,
          email: this.email,
          number_of_sanctions: 0,
          is_active: false,
          is_admin: false,
        })
        .then((response) => {
          console.log(response);
          this.hide_error = "true";
        })
        .catch((error) => console.log(error), (this.hide_error = "false"));

      if (this.hide_error === "true") {
        window.location.href = "/";
      }
    },
  },
};
</script>

<style scoped>
.register-content {
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

.registerButton {
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
