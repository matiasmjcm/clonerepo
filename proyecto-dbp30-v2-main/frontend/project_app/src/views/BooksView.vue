<template>
  <TheBackground></TheBackground>
  <div class="books-content">
    <h1 style="color: white; font-size: 40px">ADD NEW BOOK</h1>
    <form id="addBookForm" @submit.prevent="handleSubmit">
      <label style="color: white" for="ISBN"><b> ISBN </b></label>
      <input
        type="text"
        placeholder="Enter the ISBN"
        name="ISBN"
        id="ISBN"
        required
        class="input"
        v-model="ISBN"
      />

      <label style="color: white" for="title"><b> TITLE </b></label>
      <input
        type="text"
        placeholder="Enter the title"
        name="title"
        id="title"
        required
        v-model="title"
        class="input"
      />

      <label style="color: white" for="subject"><b> SUBJECT </b></label>
      <input
        type="text"
        placeholder="Enter the subject"
        name="subject"
        id="subject"
        required
        v-model="subject"
        class="input"
      />

      <label style="color: white" for="language"><b> LANGUAGE </b></label>
      <input
        type="text"
        placeholder="Enter the language"
        name="language"
        id="language"
        required
        v-model="language"
        class="input"
      />

      <label style="color: white" for="number_of_pages"
        ><b> NUMBER OF PAGES </b></label
      >
      <input
        type="number"
        placeholder="Enter the number of pages"
        name="number_of_pages"
        id="number_of_pages"
        required
        v-model="number_of_pages"
        class="input"
      />

      <label style="color: white" for="publication_date"
        ><b> PUBLICATION DATE </b></label
      >
      <input
        type="date"
        placeholder="Enter the publication date"
        name="publication_date"
        id="publication_date"
        required
        v-model="publication_date"
        class="input"
      />

      <label style="color: white" for="publisher"><b> PUBLISHER </b></label>
      <input
        type="text"
        placeholder="Enter the publisher"
        name="publisher"
        id="publisher"
        required
        v-model="publisher"
        class="input"
      />

      <label style="color: white" for="price"><b> PRICE </b></label>
      <input
        type="number"
        placeholder="Enter the price"
        name="price"
        id="price"
        required
        v-model="price"
        class="input"
      />

      <label style="color: white" for="author"><b> AUTHOR </b></label>
      <select
        name="author"
        id="author"
        required
        v-model="author_name"
        class="input"
      >
        <option
          v-for="author in authors"
          :key="author.id"
          class="author-option"
        >
          {{ author.name }}
        </option>
      </select>

      <div id="add-book-error" class="hidden">
        <p style="color: red; font-size: 24px">Book already exists!</p>
      </div>

      <button type="submit" class="addBookButton">Add book</button>

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
  name: "addBookView",
  components: { TheFooter, TheBackground },
  data() {
    return {
      ISBN: "",
      title: "",
      subject: "",
      language: "",
      number_of_pages: 0,
      publication_date: "",
      publisher: "",
      price: 0,
      author_name: "",
      author_id: 0,
      authors: [],
    };
  },
  async beforeCreate() {
    if (sessionStorage.getItem("isAdmin") === "false") {
      window.location.href = "/";
    }
    this.authors = await (await axios.get("/authors")).data.authors;
  },
  methods: {
    async handleSubmit() {
      this.author_id = await axios
        .post("/authors", {
          search_name: this.author_name,
        })
        .then((response) => {
          return response.data.author_id;
        });

      await axios.post("books", {
        ISBN: this.ISBN,
        title: this.title,
        subject: this.subject,
        language: this.language,
        number_of_pages: this.number_of_pages,
        publication_date: this.publication_date,
        publisher: this.publisher,
        price: this.price,
        author_id: this.author_id,
      });
      window.location.href = "/";
    },
  },
};
</script>

<style scoped>
.books-content {
  width: 100%;
  position: absolute;
  text-align: center;
  color: whitesmoke;
  top: 50%;
  transform: translateY(-50%);
}

.container {
  position: absolute;
  padding: 15px;
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

.addBookButton {
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
