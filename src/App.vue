<template>
  <div id = "app">
    <nav>
      <ul class="nav">
        <li class="nav-item">
          <router-link to="/">Hello world page</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/login">Login page</router-link>
        </li>

      </ul>
    </nav>
    <router-view/>
  </div>

  
</template>

<script>
export default {
  name:"App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
