from flask import request
from flask_jwt_simple import create_jwt
from flask_restful import Resource
from models.insured import InsuredModel
from models.provider import ProviderModel
from models.user    import UserModel
from os import environ
from datetime import date, datetime


class AuthenticationResource(Resource):

    def post(self):
        data = request.get_json()
        email = data['email'].strip()
        password = data['password']
        insured = InsuredModel.authenticate(email, password)
        provide = ProviderModel.authenticate(email, password)
        user    = UserModel.authenticate(email, password)

        if insured:
            access = create_jwt({
                'id_insured':   insured.id,
                'email':        insured.email,
                'first_name':   insured.first_name,
                'last_name':    insured.last_name,
                'cpf':          insured.cpf,
                'tel':          insured.tel,
                'cel':          insured.cel,
                'status':       insured.status
            })

            return {
                'id_insured': insured.id,
                'email': insured.email,
                'first_name': insured.first_name,
                'last_name': insured.last_name,
                'cpf': insured.cpf,
                'tel': insured.tel,
                'cel': insured.cel,
                'status': insured.status,
                'jwt': access
            }, 200

        elif provide:
            access = create_jwt({
                'id_provide': provide.id,
                'business_name':provide.business_name,
                'fantasy_name': provide.fantasy_name,
                'email': provide.email,
                'cnpj': provide.cnpj,
                'tel': provide.tel,
                'cel': provide.cel,
                'status': provide.status,
                })
            return {
                'id_provide': provide.id,
                'business_name':provide.business_name,
                'fantasy_name': provide.fantasy_name,
                'email': provide.email,
                'cnpj': provide.cnpj,
                'tel': provide.tel,
                'cel': provide.cel,
                'status': provide.status,
                'jwt': access
            }, 200
            
        elif user:
            access = create_jwt({
                'id_user': user.id,
                'first_name':user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'status': user.status,
                })
            return {
                'id_user': user.id,
                'first_name':user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'status': user.status,
                'jwt': access
            }, 200
        else:
            return {'message': 'Invalid credentials'}, 400
