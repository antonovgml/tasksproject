from django.test import TestCase
from tasksapp.models import Task

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import sys

# Create your tests here.

def p(data):
    sys.stderr.write('vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n')
    sys.stderr.write(repr(data) + '\n')
    sys.stderr.write('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')


class TaskModelTestCase(TestCase):


    def setUp(self):        
        return


    def test_model_create_task(self):
        self.task_title = "Task1234"
        old_cnt = Task.objects.count()
        self.task = Task(title=self.task_title)
        self.task.save()
        new_cnt = Task.objects.count()

        self.assertEqual(new_cnt - old_cnt, 1, "Wrong creating Task")



    def tearDown(self):
        pass



class ViewTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.API_URL = 'http://localhost:8000/api/tasks/'



    def test_api_can_create_task(self):
        task_data = {'title':'title1', 'details': 'perform title1'}

        response = self.client.post(
            self.API_URL,
            task_data,
            format="json"
        )

        p(response)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "API was unable to create a task")

    def test_api_can_get_tasks_list(self):

        p('Start test_api_can_get_tasks_list')

        tasks = Task.objects.get()
        p('retrieved tasks')
        response = self.client.get(
            self.API_URL + tasks.id,
            format='json'
        )    

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertContains(response, tasks)


    def test_api_can_update_task(self):
        tasks = Task.objects.get()
        change_task = {'title': 'Updated title'}
        res = self.client.put(
            reverse('details', kwargs = {'pk': tasks.id}),
            change_task,
            format='json'
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_delete_task(self):
        p('Start test_api_can_delete_task')
        tasks = Task.objects.get()
        p(tasks)
        response = self.client.delete(
            self.API_URL+tasks.id,            
            format='json',
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)



    def tearDown(self):
        pass

