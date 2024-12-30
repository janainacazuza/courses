from rest_framework import serializers
from .models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, celular_invalido, nome_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ["id", "nome", "email", "cpf", "data_nascimento", "celular"] 
    
def validate(self, dados):
    if cpf_invalido(dados['cpf']):
        raise serializers.ValidationError({'cpf': 'O CPF deve um número válido'})
    if celular_invalido(dados['celular']):
        raise serializers.ValidationError({'celular': 'O numero de celular deve seguir o padrão XX XXXXX-XXXX respeitando o espaço e o hífen'})
    if nome_invalido(dados['nome']):
        raise serializers.ValidationError({'nome': 'O nome deve conter apenas caracteres alfabéticos'})
    return dados


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante.nome']

class EstudanteSerializerV2(serializers.ModelSerializer): 
    class Meta:
        model = Estudante
        ields = ["id", "nome", "email", "celular"] 
