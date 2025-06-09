<script setup lang="ts">
import { ref } from 'vue'
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import type { User } from '@/types/models'

const users = ref<User[]>([])

const getUsers = async () => {
  const response = await fetch('http://localhost:8000/users')
  users.value = await response.json()
}
</script>
<template>
  <Card>
    <CardHeader>
      <CardTitle>List Users</CardTitle>
      <CardDescription> List all Users from the Backend API </CardDescription>
    </CardHeader>
    <CardContent>
      <ul class="list-disc pl-5">
        <li v-for="user in users" :key="user.id">{{ user.id }} {{ user.name }} ({{ user.email }})</li>
      </ul>
      <p v-if="users.length === 0">No users found.</p>
    </CardContent>
    <CardFooter>
      <Button @click="getUsers" class="btn btn-primary">Get Users</Button>
    </CardFooter>
  </Card>
</template>
