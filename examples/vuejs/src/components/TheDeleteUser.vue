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
import { FormLabel, FormItem, FormControl, FormField } from '@/components/ui/form'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'

const deletedUserId = ref<string | null>(null)
const errorMessage = ref<string | null>(null)
const isDeleting = ref(false)

const deleteUserSchema = toTypedSchema(
  z.object({
    id: z.string().min(1, 'User ID is required'),
  }),
)

const form = useForm({
  validationSchema: deleteUserSchema,
})

const onSubmit = form.handleSubmit(async (values) => {
  try {
    isDeleting.value = true
    errorMessage.value = null

    const response = await fetch(`http://localhost:8000/users/${values.id}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })

    if (!response.ok) {
      throw new Error(`Failed to delete user: ${response.statusText}`)
    }

    deletedUserId.value = values.id
    form.resetForm()
  } catch (error) {
    console.error('Error deleting user:', error)
    errorMessage.value = error instanceof Error ? error.message : 'Failed to delete user'
  } finally {
    isDeleting.value = false
  }
})
</script>

<template>
  <Card>
    <CardHeader>
      <CardTitle>Delete User</CardTitle>
      <CardDescription>Enter a user ID to delete the user</CardDescription>
    </CardHeader>
    <form @submit="onSubmit">
      <CardContent>
        <div>
          <FormField v-slot="{ componentField }" name="id">
            <FormItem>
              <FormLabel>User ID</FormLabel>
              <FormControl>
                <Input type="text" placeholder="Enter user ID" v-bind="componentField" />
              </FormControl>
            </FormItem>
          </FormField>
        </div>
      </CardContent>
    </form>
    <CardFooter class="flex justify-between">
      <Button type="submit" class="bg-red-600 hover:bg-red-700" :disabled="isDeleting" @click="onSubmit">
        {{ isDeleting ? 'Deleting...' : 'Delete User' }}
      </Button>
      <p v-if="deletedUserId" class="text-green-600">
        User with ID "{{ deletedUserId }}" was successfully deleted
      </p>
      <p v-if="errorMessage" class="text-red-600">Error: {{ errorMessage }}</p>
    </CardFooter>
  </Card>
</template>
