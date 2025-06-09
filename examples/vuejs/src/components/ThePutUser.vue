<script setup lang="ts">
import { ref } from 'vue'
import { toTypedSchema } from '@vee-validate/zod'
import { z } from 'zod'
import { useForm } from 'vee-validate'
import {
  Card,
  CardHeader,
  CardTitle,
  CardFooter,
  CardDescription,
  CardContent,
} from '@/components/ui/card'
import type { User } from '@/types/models'
import { FormLabel, FormItem, FormControl, FormField, FormMessage } from '@/components/ui/form'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

const patchedUser = ref<User | null>(null)
const userId = ref<string>('')
const userFound = ref<boolean | null>(null)
const currentUser = ref<User | null>(null)
const errorMessage = ref<string | null>(null)

const patchUserSchema = toTypedSchema(
  z.object({
    id: z.string().min(1, 'User ID is required'),
    name: z.string().min(1, 'Name is required'),
    email: z.string().email('Invalid email address'),
  }),
)

const form = useForm({
  validationSchema: patchUserSchema,
})

const findUser = async () => {
  if (!userId.value) {
    errorMessage.value = 'Please enter a user ID'
    return
  }

  try {
    const response = await fetch(`http://localhost:8000/users/${userId.value}`)

    if (!response.ok) {
      userFound.value = false
      currentUser.value = null
      errorMessage.value = 'User not found'
      return
    }

    currentUser.value = await response.json()
    userFound.value = true
    errorMessage.value = null

    // Set form values
    form.setFieldValue('id', userId.value)
    form.setFieldValue('name', currentUser.value.name)
    form.setFieldValue('email', currentUser.value.email)
  } catch (error) {
    console.error('Error finding user:', error)
    userFound.value = false
    errorMessage.value = 'Error finding user'
    currentUser.value = null
  }
}

const onSubmit = form.handleSubmit(async (values) => {
  try {
    const { id, ...updateData } = values
    const response = await fetch(`http://localhost:8000/users/${id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(updateData),
    })

    if (!response.ok) {
      throw new Error('Failed to update user')
    }

    patchedUser.value = await response.json()
    errorMessage.value = null
  } catch (error) {
    console.error('Error updating user:', error)
    errorMessage.value = 'Failed to update user'
  }
})
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Update User</CardTitle>
      <CardDescription>Modify an existing user's information</CardDescription>
    </CardHeader>

    <CardContent>
      <div class="mb-4 flex gap-4">
        <Input type="text" placeholder="Enter user ID" v-model="userId" class="flex-grow" />
        <Button type="button" @click="findUser">Find User</Button>
      </div>

      <div v-if="errorMessage" class="mb-4 text-red-600">
        {{ errorMessage }}
      </div>

      <form v-if="userFound" @submit="onSubmit">
        <div class="grid grid-cols-2 gap-4">
          <FormField v-slot="{ componentField }" name="name">
            <FormItem>
              <FormLabel>Name</FormLabel>
              <FormControl>
                <Input type="text" placeholder="John Doe" v-bind="componentField" />
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>

          <FormField v-slot="{ componentField }" name="email">
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input type="email" placeholder="user@example.com" v-bind="componentField" />
              </FormControl>
              <FormMessage />
            </FormItem>
          </FormField>
        </div>
      </form>
    </CardContent>

    <CardFooter class="flex justify-between">
      <Button v-if="userFound" type="submit" @click="onSubmit">Update User</Button>
      <p v-if="patchedUser" class="text-green-600">
        User updated: {{ patchedUser.name }} ({{ patchedUser.email }})
      </p>
    </CardFooter>
  </Card>
</template>
