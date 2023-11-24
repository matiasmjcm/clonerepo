<template>
  <div id="nav">
    <ul class="nav-links">
      <li class="links">
        <router-link to="/">Home</router-link>
      </li>
      <li class="links">
        <router-link to="/contact">Contact</router-link>
      </li>
      <a v-if="this.isLogged === 'true'" v-on:click="handleLogout" href="/login"
        >Logout</a
      >
    </ul>
  </div>
</template>

<script>
export default {
  name: "TheNavigation",
  data() {
    return {
      isLogged: sessionStorage.getItem("isLogged"),
    };
  },
  methods: {
    // Log out user
    handleLogout() {
      sessionStorage.setItem("isLogged", "false");
      sessionStorage.setItem("currentUserId", "0");
      sessionStorage.setItem("isAdmin", "false");
      this.isLogged = "false";
    },
  },
};
</script>

<style scoped>
#nav {
  display: flex;
  background-color: #04aa6d;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

#nav a.router-link-exact-active {
  color: whitesmoke;
}

.nav-links {
  display: flex;
  margin-left: auto;
  font-size: large;
}

.links {
  padding-right: 20px;
  list-style: none;
}

.logo {
  font-size: 20px;
}
</style>
