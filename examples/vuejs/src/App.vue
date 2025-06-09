<script setup lang="ts">
import TheCreateUser from './components/TheCreateUser.vue';
import TheGetUserById from './components/TheGetUserById.vue';
import TheListUsers from './components/TheListUsers.vue';


</script> 

<template>
  <header class="p-8">
    <h1 class="text-3xl font-bold">Users API Client</h1>
  </header>

  <main class="p-8 space-y-8">
    <section>
      <TheListUsers />
    </section>
    <section>
      <TheCreateUser />
    </section>
    <section>
      <TheGetUserById />
    </section>
  </main>
</template>
