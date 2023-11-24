<template>
  <TheBackground></TheBackground>
  <div class="authors-content">
    <h1 style="color: white; font-size: 40px">ADD NEW AUTHOR</h1>
    <form id="addAuthorForm" @submit.prevent="handleSubmit">
      <label style="color: white" for="name"><b> NAME </b></label>
      <input
        type="text"
        placeholder="Enter the author's name"
        name="name"
        id="name"
        required
        v-model="name"
        class="input"
      />

      <label style="color: white" for="dob"><b> DATE OF BIRTH </b></label>
      <input
        type="date"
        placeholder="Enter the date of birth"
        name="dob"
        id="dob"
        required
        v-model="dob"
        class="input"
      />

      <div id="add-author-error" class="hidden">
        <p style="color: red; font-size: 24px">Author already exists!</p>
      </div>

      <button type="submit" class="addAuthorButton">Add author</button>

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
  name: "AddAuthorView",
  components: { TheFooter, TheBackground },
  data() {
    return {
      name: "",
      dob: "",
    };
  },
  beforeCreate() {
    if (sessionStorage.getItem("isAdmin") === "false") {
      window.location.href = "/";
    }
  },
  methods: {
    async handleSubmit() {
      await axios.post("authors", {
        name: this.name,
        dob: this.dob,
      });
      window.location.href = "/";
    },
  },
};
</script>

<style scoped>
.authors-content {
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

.addAuthorButton {
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
