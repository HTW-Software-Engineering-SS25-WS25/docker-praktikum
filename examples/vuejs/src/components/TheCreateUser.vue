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
import {
  FormLabel,
  FormItem,
  FormControl,
  FormField,
  FormMessage,
  FormDescription,
} from '@/components/ui/form'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

const createdUser = ref<User | null>(null)

const createUserSchema = toTypedSchema(
  z.object({
    name: z.string().min(1, 'Name is required'),
    email: z.string().email('Invalid email address'),
  }),
)

const form = useForm({
  validationSchema: createUserSchema,
})

const onSubmit = form.handleSubmit(async (values) => {
  try {
    const response = await fetch('http://localhost:8000/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(values),
    })

    if (!response.ok) {
      throw new Error('Failed to create user')
    }

    createdUser.value = await response.json()
  } catch (error) {
    console.error('Error creating user:', error)
  }
})
</script>
<template>
  <Card>
    <CardHeader>
      <CardTitle>Create a User</CardTitle>
      <CardDescription> Fill out the form below to create a new user. </CardDescription>
    </CardHeader>
    <form @submit="onSubmit">
      <CardContent>
        <div class="grid grid-cols-2 gap-4">
          <FormField v-slot="{ componentField }" name="name">
            <FormItem>
              <FormLabel>Name</FormLabel>
              <FormControl>
                <Input type="text" placeholder="John Doe" v-bind="componentField" />
              </FormControl>
            </FormItem>
          </FormField>

          <FormField v-slot="{ componentField }" name="email">
            <FormItem>
              <FormLabel>Email</FormLabel>
              <FormControl>
                <Input type="email" v-bind="componentField" />
              </FormControl>
            </FormItem>
          </FormField>
        </div>
      </CardContent>
    </form>
    <CardFooter class="flex justify-between">
      <Button type="submit" class="btn btn-primary" @click="onSubmit">Create User</Button>
      <p v-if="createdUser" class="mt-4 text-green-600">
        User created: {{ createdUser.name }} ({{ createdUser.email }})
      </p>
    </CardFooter>
  </Card>
</template>
