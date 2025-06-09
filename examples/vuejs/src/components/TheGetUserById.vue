<script setup lang="ts">
import { ref } from 'vue'
import {
  Card,
  CardHeader,
  CardTitle,
  CardFooter,
  CardDescription,
  CardContent,
} from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import type { User } from '@/types/models'
import { Input } from '@/components/ui/input'

const userId = ref<number | undefined>()
const foundUser = ref<User | null>(null)

const getUserById = async () => {
  if (!userId.value) return

  try {
    const response = await fetch(`http://localhost:8000/users/${userId.value}`)
    if (!response.ok) {
      throw new Error('User not found')
    }
    const user: User = await response.json()
    foundUser.value = user
  } catch (error) {
    console.error('Error fetching user:', error)
    alert('Error fetching user. Please check the console for details.')
  }
}
</script>
<template>
  <Card>
    <CardHeader>
      <CardTitle>Get User by ID</CardTitle>
      <CardDescription>Fetch a user by their ID from the Backend API</CardDescription>
    </CardHeader>
    <CardContent>
      <div class="grid grid-cols-2 gap-4">
        <Input
          v-model="userId"
          type="number"
          placeholder="Enter User ID"
          class="h-fit"
        />
        <div v-if="foundUser" class="p-4 bg-gray-100 rounded-md">
          <h3 class="text-lg font-semibold">User Details:</h3>
          <p><strong>ID:</strong> {{ foundUser.id }}</p>
          <p><strong>Name:</strong> {{ foundUser.name }}</p>
          <p><strong>Email:</strong> {{ foundUser.email }}</p>
        </div>
      </div>
    </CardContent>
    <CardFooter>
      <Button @click="getUserById" class="btn btn-primary" :disabled="!userId">Get User</Button>
    </CardFooter>
  </Card>
</template>
