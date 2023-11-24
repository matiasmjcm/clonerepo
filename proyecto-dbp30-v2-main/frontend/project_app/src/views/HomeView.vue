<template>
  <TheBackground></TheBackground>
  <div class="home-content">
    <img alt="App logo" src="../assets/logo.png" />
    <h1>A BOOK FOR YOU</h1>
    <p>THE BEST BOOKSTORE IN THE WORLD</p>
    <router-link v-if="isLogged === 'false'" to="/register">
      <button>Register</button>
    </router-link>
    <router-link v-if="isLogged === 'false'" to="/login">
      <button>Log in</button>
    </router-link>
    <RouterLink to="/settings">
      <button v-if="isLogged === 'true'">Settings</button>
    </RouterLink>

    <div class="search-wrapper" v-if="isLogged === 'true'">
      <input
        type="search"
        placeholder="Search..."
        name="search"
        id="to-search"
        required
      />
    </div>

    <div
      class="book-cards"
      data-book-cards-container
      id="card"
      v-if="isLogged === 'true'"
    ></div>

    <br /><br />

    <div id="shopping-cart" v-if="isLogged === 'true'">
      <h2>Shopping Cart</h2>
      <div class="book-cards" data-book-cards-container id="card"></div>

      <br />

      <div
        v-for="book in books"
        class="book-cards"
        data-book-cards-container
        :key="book.id"
        id="card"
      >
        <div class="card">
          <div class="header" data-header>{{ "Title: " + book.title }}</div>
          <div class="price" data-price>
            {{ "Price: " + book.price }}
          </div>
          <div class="body" data-body>{{ book.id }}</div>
          <!-- <div class="author-name" data-author-name>
            {{ getBookAuthor(book.author_id) }}
          </div> -->
          <div class="due-date" data-due-date>"Due date: 7 days from now"</div>
          <div v-if="book.due_date === null">
            Rent
            <input
              type="checkbox"
              :ref="book.id.toString()"
              class="rent-button"
            />
          </div>
          <div v-else>
            Already rented!
            <input
              type="checkbox"
              :ref="book.id.toString()"
              class="rent-button"
              style="display: none"
            />
          </div>
        </div>
      </div>
      <form id="submit-rent" @submit.prevent="handleSubmit">
        <button type="submit">Rent</button>
      </form>
    </div>
    <router-link v-if="isLogged === 'true' && isAdmin === 'true'" to="/books">
      <button type="submit">Add a book</button>
    </router-link>
    <router-link v-if="isLogged === 'true' && isAdmin === 'true'" to="/authors">
      <button type="submit">Add an author</button>
    </router-link>
  </div>
  <TheFooter></TheFooter>
</template>

<script>
import TheBackground from "@/components/TheBackground";
import TheFooter from "@/components/TheFooter";
import axios from "axios";

export default {
  name: "HomeView",
  components: { TheFooter, TheBackground },
  data() {
    return {
      isLogged: sessionStorage.getItem("isLogged"),
      books: [],
      isAdmin: sessionStorage.getItem("isAdmin"),
      //   currentAuthorName: "",
    };
  },
  async beforeCreate() {
    if (sessionStorage.getItem("isLogged") !== "true") {
      sessionStorage.setItem("isLogged", "false");
      sessionStorage.setItem("currentUserId", "0");
      sessionStorage.setItem("isAdmin", "false");
    }
    this.books = await (await axios.get("/books")).data.books;
  },
  methods: {
    async handleSubmit() {
      this.books.forEach((book) => {
        let checkbox = this.$refs[book.id.toString()][0];
        console.log("Hola " + checkbox);
        if (checkbox.checked) {
          axios.patch(`/books/${book.id}`, {
            user_id: parseInt(sessionStorage.getItem("currentUserId")),
            borrowed_date:
              new Date().getFullYear() +
              "-" +
              (new Date().getMonth() + 1) +
              "-" +
              new Date().getDate(),
            due_date:
              new Date().getFullYear() +
              "-" +
              (new Date().getMonth() + 1) +
              "-" +
              (new Date().getDate() + 7),
          });
        }
        window.location.href = "/";
      });

      // async getBookAuthor(authorId) {
      //   this.currentAuthorName = await axios
      //     .post("/authors", {
      //       search_id: authorId,
      //     })
      //     .then((response) => {
      //       return response.data.author_name;
      //     });
      // },
    },
  },
  cardIsInCardContainer(card) {
    const bookCardContainer = document.querySelector(
      "[data-book-cards-container]"
    );

    for (var i = 0; i < bookCardContainer.children.length; i++) {
      let child = bookCardContainer.children[i];
      if (
        child.querySelector("[data-body]").textContent ==
        card.querySelector("[data-body]").textContent
      ) {
        if (
          child.querySelector("[data-header]").textContent ==
          card.querySelector("[data-header]").textContent
        ) {
          return true;
        }
      }
    }
    return false;
  },
};
</script>

<style scoped>
.home-content {
  width: 100%;
  position: absolute;
  text-align: center;
  color: whitesmoke;
  top: 40%;
  transform: translateY(-50%);
}

.card {
  font-family: "SansSerif", serif;
}

.home-content button {
  width: 21.55%;
  background-color: #04aa6d;
  color: white;
  padding: 15px;
  margin: 5px 5px 22px 5px;
  border: none;
  cursor: pointer;
  opacity: 0.9;
}

.home-content button:hover {
  background: #038455;
}

#submit-rent button {
  width: 21.55%;
  background-color: #04aa6d;
  color: white;
  padding: 15px;
  margin: 5px 0 22px 0;

  border: none;
  cursor: pointer;
  opacity: 0.9;
}

#submit-rent button:hover {
  background: #038455;
}

#search-form {
  margin: auto;
  max-width: 350px;
}

* {
  box-sizing: border-box;
}

/* Style the search field */
#search-form input[type="text"] {
  padding: 10px;
  font-size: 17px;
  border: 1px solid grey;
  float: left;
  width: 100%;
  background: #f1f1f1;
}

/* Clear floats */
#search-form::after {
  content: "";
  clear: both;
  display: table;
}

.hide {
  display: none;
}

.hidden {
  display: none;
}

/* book_cards */
input {
  font-size: 1rem;
}

.search-wrapper input {
  padding: 10px;
  font-size: 17px;
  border: 1px solid grey;
  float: initial;
  width: 20%;
  background: #f1f1f1;
}

.book-cards {
  display: inline-grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 0.25rem;
  margin-top: 1rem;
  margin-left: 5px;
  margin-right: 5px;
}

.card {
  border: 1px solid black;
  background-color: white;
  padding: 0.7rem;
  color: black;
  width: fit-content;
  margin: 1rem;
}

.card > .header {
  margin-bottom: 0.25rem;
}

/* .card>.body {
  font-size: .8rem;
  color: #777;
} */

.card > .body {
  display: none;
}
</style>
