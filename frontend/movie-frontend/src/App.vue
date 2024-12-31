<template>
  <div id="app" class="bg-gray-900 text-white min-h-screen p-6">
    <h1 class="text-4xl font-bold text-center mb-8">Movies</h1>
    <div v-if="loading" class="text-center text-gray-400">Loading...</div>
    <div v-if="!loading && movies.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
    <div v-if="!loading && !movies.length" class="text-center text-gray-400">
      <p>No movies found.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import MovieCard from './components/MovieCard.vue';

export default {
  name: 'App',
  components: {
    MovieCard,
  },
  data() {
    return {
      movies: [],
      loading: true,
    };
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/api/posts/') // Replace with your API endpoint
      .then((response) => {
        this.movies = response.data.results;
        this.loading = false;
      })
      .catch((error) => {
        console.error(error);
        this.loading = false;
      });
  },
};
</script>
