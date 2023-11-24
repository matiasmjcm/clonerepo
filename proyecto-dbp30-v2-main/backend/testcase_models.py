from turtle import update
import unittest
from flask_sqlalchemy import SQLAlchemy

from server import create_app
from models import Account, Book, Author, setup_db

import json
import datetime
import random

class ProjectAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        #change password for your sqlserver
        self.database_name = 'proyecto_dbp30_final_version_test'
        self.database_path='postgresql://{}:{}@{}/{}'.format('postgres', 'hola', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_account = {
            'first_name' : 'new_name',
            'last_name' : 'new_lastname',
            'username' : 'new_username',
            'password' : 'new_password',
            'number_of_sanctions' : 0,
            'is_active' : False,
            'is_admin' : False,
            'email' : 'new_email'
        }
        self.new_author = {
            'name' : 'new_name',
            'dob' : datetime.datetime.now().date()
        }
        self.new_book = {
            'ISBN' : 'new_ISBN',
            'title' : 'new_title',
            'subject' : 'new_subject',
            'language' : 'new_language',
            'number_of_pages' : 100,
            'publication_date' : datetime.datetime.now().date(),
            'publisher' : 'new_publisher',
            'price' : 120,
            'due_date' : datetime.datetime.now().date(),
            'borrowed_date' : datetime.datetime.now().date(),
            'user_id' : None,
            'author_id' : None
        }

    
    
      
################## ACCOUNT ##################

    #LOGIN
    #PASS
    def test_login_success(self):
        res = self.client().post('/accounts', json=self.new_account)
        data = json.loads(res.data)

        res_login = self.client().post('/login', json={"username" : "new_username", "password" : "new_password"})
        data_login = json.loads(res_login.data)

        self.assertEqual(res_login.status_code, 200)
        self.assertEqual(data_login['is_logged'], True)
        self.assertTrue(data_login['current_user_id'])

    #POST ACCOUNT
    #PASS
    def test_register_success(self):
        #insert data
        res = self.client().post('/accounts', json=self.new_account)
        data = json.loads(res.data)

        #test endpoint
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['accounts']))

        # recover database integrity        
        self.client().delete(f'/accounts/{data["created"]}')

    #PASS
    def test_register_failed(self):
        #insert data
        res = self.client().post('/accounts', json = {})
        data = json.loads(res.data)

        #test endpoint
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'unprocessable')

    #GET ACCOUNT
    #PASS
    def test_get_account_success(self):
        #insert data
        res = self.client().post('/accounts', json=self.new_account)
        data = json.loads(res.data)
        id_to_deleted = data['created']

        #test endpoint
        res = self.client().get('/accounts')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_accounts'])   
        self.assertTrue(len(data['accounts']))

        #recover database integrity
        res = self.client().delete('/accounts/' + str(id_to_deleted))

    #PASS
    def test_get_account_failed(self):
        # test endpoint
        res = self.client().get('/accounts?page=9999999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404) 
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    #UPDATE ACCOUNT
    #FAILED
    def test_update_account_for_id_success(self):
        #insert data
        res = self.client().post('/accounts', json = self.new_account)
        data = json.loads(res.data)
        id_to_deleted = updated_id = data['created']

        #test endpoint
        res = self.client().patch('/accounts/{}'.format(updated_id), json = {"first_name" : "update_first_name"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['id'])
        self.assertEqual(data['id'], str(updated_id))

        #recover database intedrity
        res = self.client().delete('/accounts/' + str(id_to_deleted))

    #PASS
    def test_update_account_for_id_failed(self):
        res = self.client().patch('/accounts/9999999', json={
            "first_name": "update_first_name"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    #DELETE ACCOUNT
    #PASS REVISADO
    def test_delete_account_for_id_success(self):
        res = self.client().post('/accounts', json=self.new_account)
        data = json.loads(res.data)
        deleted_id = data['created']
        self.id_delete_sala = deleted_id

        res = self.client().delete('/accounts/' + str(deleted_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], str(deleted_id))

    #PASS
    def test_delete_account_for_id_failed(self):
        res = self.client().delete('/accounts/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

################## AUTHOR ##################
    #POST AUTHOR
    #PASS
    def test_create_author_success(self):
         #insert data
        res = self.client().post('/authors', json=self.new_author)
        data = json.loads(res.data)

        #test endpoint
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['authors']))

        # recover database integrity        
        self.client().delete(f'/accounts/{data["created"]}')

    #PASS
    def test_create_author_failed(self):
        #insert data
        res = self.client().post('/authors', json = {})
        data = json.loads(res.data)

        #test endpoint
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'unprocessable')

    #GET AUTHOR
    #PASS
    def test_get_author_success(self):
        #insert data
        res = self.client().post('/authors', json=self.new_author)
        data = json.loads(res.data)
        id_to_deleted = data['created']

        #test endpoint
        res = self.client().get('/authors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_authors'])   
        self.assertTrue(len(data['authors']))

        #recover database integrity
        res = self.client().delete('/authors/' + str(id_to_deleted))

    #PASS
    def test_get_author_failed(self):
        # test endpoint
        res = self.client().get('/authors?page=9999999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404) 
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    #UPDATE AUTHOR
    #FAILED
    def test_update_author_for_id_success(self):
        #insert data
        res = self.client().post('/authors', json = self.new_author)
        data = json.loads(res.data)
        id_to_deleted = updated_id = data['created']

        #test endpoint
        res = self.client().patch('/authors/{}'.format(updated_id), json = {"name" : "update_name"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['id'])
        self.assertEqual(data['id'], str(updated_id))

        #recover database intedrity
        res = self.client().delete('/authors/' + str(id_to_deleted))

    #PASS
    def test_update_author_for_id_failed(self):
        res = self.client().delete('/authors/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    #DELETE AUTHOR
    #FAILED REVISADO
    def test_delete_author_for_id_success(self):
        res = self.client().post('/authors', json=self.new_author)
        data = json.loads(res.data)
        deleted_id = data['created']

        res = self.client().delete('/authors/' + str(deleted_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], str(deleted_id))

    #PASS
    def test_delete_author_for_id_failed(self):
        res = self.client().delete('/authors/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')


################## BOOK ##################
    #POST BOOK
    #PASS
    def test_create_book_success(self):
        res_account = self.client().post('/accounts', json=self.new_account)
        data_account = json.loads(res_account.data)
        res_author = self.client().post('/authors', json=self.new_author)
        data_author = json.loads(res_author.data)

        self.new_book["author_id"] = data_author['created']
        self.new_book["user_id"] = data_account['created']

        res = self.client().post('/books', json=self.new_book)
        data = json.loads(res.data)
        id_to_deleted = data['created']

        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_books'])   
        self.assertTrue(len(data['books']))

        # recover database integrity
        res = self.client().delete('/accounts/' + str(id_to_deleted))
        res = self.client().delete('/authors/' + str(data_account['created']))
        res = self.client().delete('/books/' + str(data_author['created']))

    #FAILED
    def test_create_book_failed(self):
        res = self.client().post('/books', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'unprocessable')

    #GET BOOK
    #PASS
    def test_get_book_success(self):
        res_account = self.client().post('/accounts', json=self.new_account)
        data_account = json.loads(res_account.data)
        res_author = self.client().post('/authors', json=self.new_author)
        data_author = json.loads(res_author.data)

        self.new_book["author_id"] = data_author['created']
        self.new_book["user_id"] = data_account['created']

        res = self.client().post('/books', json=self.new_book)
        data = json.loads(res.data)
        id_to_deleted = data['created']

        #test endpoint
        res = self.client().get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])   
        self.assertTrue(len(data['books']))

        # recover database integrity
        res = self.client().delete('/accounts/' + str(id_to_deleted))
        res = self.client().delete('/authors/' + str(data_account['created']))
        res = self.client().delete('/books/' + str(data_author['created']))

    #PASS
    def test_get_book_failed(self):
        res = self.client().get('/books/page=100000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405) 
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'method not allowed')
    
    
    #UPDATE BOOK
    #FAILED
    def test_update_book_for_id_success(self):
        res_account = self.client().post('/accounts', json=self.new_account)
        data_account = json.loads(res_account.data)
        res_author = self.client().post('/authors', json=self.new_author)
        data_author = json.loads(res_author.data)

        self.new_book["author_id"] = data_author['created']
        self.new_book["user_id"] = data_account['created']

        res = self.client().post('/books', json=self.new_book)
        data = json.loads(res.data)
        id_to_deleted = updated_id =data['created']

        #test endpoint
        res = self.client().patch('/accounts/{}'.format(updated_id), json={'title' : 'update_title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['id'])
        self.assertEqual(data['id'], str(updated_id))

        # recover database integrity
        res = self.client().delete('/accounts/' + str(id_to_deleted))
        res = self.client().delete('/authors/' + str(data_account['created']))
        res = self.client().delete('/books/' + str(data_author['created']))


    #PASS
    def test_update_book_for_id_failed(self):
        res = self.client().patch('/books/9999999', json={'title' : 'update_title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    #DELETE BOOK
    #FAILED
    def test_delete_book_for_id_success(self):
        res_account = self.client().post('/accounts', json=self.new_account)
        data_account = json.loads(res_account.data)
        res_author = self.client().post('/authors', json=self.new_author)
        data_author = json.loads(res_author.data)

        self.new_book["author_id"] = data_author['created']
        self.new_book["user_id"] = data_account['created']

        res_book = self.client().post('/books', json=self.new_book)
        data = json.loads(res_book.data)
        id_to_deleted = updated_id =data['created']

        #test endpoint 
        res_book = self.client().delete('/books/' + str(id_to_deleted))
        data_book = json.loads(res_book.data)

        self.assertEqual(res_book.status_code, 200)
        self.assertEqual(data_book['success'], True)
        self.assertEqual(data_book['deleted'], str(id_to_deleted))
 
        # recover database integrity
        res = self.client().delete('/accounts/' + str(data_account['created']))
        res = self.client().delete('/authors/' + str(data_author['created']))
    
    #PASS
    def test_delete_book_for_id_failed(self):
        res = self.client().delete('/books/99999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        self.assertEqual(data['message'], 'resource not found')

    def tearDown(self):
        pass