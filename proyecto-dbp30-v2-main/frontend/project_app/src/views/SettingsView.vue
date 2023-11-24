<template>
  <TheBackground></TheBackground>
  <div class="settings-content">
    <h1 style="color: white; font-size: 40px">ACCOUNT SETTINGS</h1>
    <form id="newpassword-form" @submit.prevent="handleUpdate">
      <h3>UPDATE PASSWORD</h3>
      <input
        type="password"
        id="new-password"
        name="newPassword"
        style="text-align: center"
        placeholder="Enter your new password"
        v-model="newPassword"
        required
      />
      <button type="submit" value="Change">Change password</button>
    </form>

    <form id="delete-form" @submit.prevent="handleDelete">
      <h3>DELETE ACCOUNT</h3>
      <button type="submit" id="deleteAccountBtn">Delete all your data</button>
    </form>
  </div>
  <TheFooter></TheFooter>
</template>

<script>
import TheBackground from "@/components/TheBackground";
import TheFooter from "@/components/TheFooter";
import axios from "axios";

export default {
  name: "SettingsView",
  components: { TheFooter, TheBackground },
  data() {
    return {
      newPassword: "",
    };
  },
  methods: {
    async handleUpdate() {
      await axios.patch(
        `/accounts/${sessionStorage.getItem("currentUserId")}`,
        {
          password: this.newPassword,
        }
      );
      window.location.href = "/";
    },
    async handleDelete() {
      await axios.delete(
        `/accounts/${sessionStorage.getItem("currentUserId")}`
      );
      sessionStorage.setItem("isLogged", "false");
      sessionStorage.setItem("currentUserId", "0");
      sessionStorage.setItem("isAdmin", "false");
      window.location.href = "/";
    },
  },
};
</script>

<style scoped>
p,
h2,
h3 {
  color: white;
}

.settings-content {
  width: 100%;
  position: absolute;
  text-align: center;
  color: whitesmoke;
  top: 40%;
  transform: translateY(-50%);
}

input {
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

form button {
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

.home-content {
  position: absolute;
  text-align: center;
  color: whitesmoke;
  top: 40%;
  transform: translateY(-50%);
}
</style>
