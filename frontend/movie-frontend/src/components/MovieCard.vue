<template>
    <div class="flex bg-gray-800 text-white rounded-lg shadow-lg overflow-hidden mb-6">
      <div class="w-1/4 h-auto">
        <img 
          :src="movie.poster" 
          alt="Movie Poster" 
          class="object-cover w-full h-full" 
        />
      </div>
      <div class="p-4 w-3/4">
        <h1 class="text-2xl font-bold mb-2">
          {{ movie.title }} <span class="text-gray-400">({{ movie.year }})</span>
        </h1>
        <p class="text-gray-400 mb-1"><strong>Genre:</strong> {{ movie.genre }}</p>
        <p class="text-gray-400 mb-1"><strong>Director:</strong> {{ movie.director }}</p>
        <p class="text-gray-400 mb-4"><strong>Plot:</strong> {{ movie.plot }}</p>
        <p class="text-yellow-400 font-bold mb-2">
          <strong>IMDB Rating:</strong> {{ movie.imdb_rating }}
        </p>
        <button
          @click="likeMovie"
          class="bg-blue-500 hover:bg-blue-700 text-white py-1 px-4 rounded"
        >
          Like
        </button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['movie'],
    methods: {
      likeMovie() {
        alert('You liked this movie!');
      },
    },
  };
  </script>
  
  <style scoped>
  /* Ensure uniform height and alignment for images */
  img {
    object-fit: cover;
    max-height: 200px; /* Ensures images have a consistent height */
  }
  
  /* Add hover effect for the card */
  div.flex:hover {
    transform: scale(1.02);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  
  /* Styling for consistent spacing */
  .flex {
    margin-bottom: 10px;
  }
  </style>
  