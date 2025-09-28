from flask import Flask, request, jsonify, send_file
from io import BytesIO
from openpyxl import Workbook
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Permitir CORS para todas as rotas

@app.route("/")
def home():
      return jsonify({"message": "API do Sistema de Gestão Oncológica rodando com sucesso 🚀"})

@app.route("/login", methods=["POST"])
def login():
      data = request.get_json()
      username = data.get("username")
      password = data.get("password")

    # Credenciais configuráveis via variáveis de ambiente
      admin_user = os.environ.get("ADMIN_USER", "nathanyellmelo")
      admin_pass = os.environ.get("ADMIN_PASS", "oncologia2025")

    if username == admin_user and password == admin_pass:
              return jsonify({
                            "success": True, 
                            "token": "demo-token", 
                            "user": {"username": admin_user, "name": "Administrador"}
              })
else:
          return jsonify({"success": False, "message": "Credenciais inválidas"}), 401

@app.route("/dashboard/stats")
def get_dashboard_stats():
      return jsonify({
                "total_patients": 6,
                "scheduled_appointments": 0,
                "average_age": 46,
                "gender_distribution": {"male": 3, "female": 3}
      })

@app.route("/patients")
def get_patients():
      return jsonify([
                {"id": 1, "name": "João Silva", "zone": "Urbana", "age": 45, "gender": "Masculino", "cancer_type": "Próstata"},
                {"id": 2, "name": "Maria Santos", "zone": "Rural", "age": 33, "gender": "Feminino", "cancer_type": "Mama"},
                {"id": 3, "name": "Pedro Oliveira", "zone": "Urbana", "age": 67, "gender": "Masculino", "cancer_type": "Pulmão"},
                {"id": 4, "name": "Ana Costa", "zone": "Rural", "age": 52, "gender": "Feminino", "cancer_type": "Tireoide"},
                {"id": 5, "name": "Carlos Ferreira", "zone": "Urbana", "age": 41, "gender": "Masculino", "cancer_type": "Cólon"},
                {"id": 6, "name": "Lucia Almeida", "zone": "Rural", "age": 38, "gender": "Feminino", "cancer_type": "Ovário"}
      ])

@app.route("/appointments", methods=["GET"])
def get_appointments():
      return jsonify([])

@app.route("/appointments", methods=["POST"])
def create_appointment():
      data = request.get_json()
      # Simular criação de agendamento
      return jsonify({
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "patient_name": data.get("patient_name"),
          "doctor_name": data.get("doctor_name"),
          "appointment_date": data.get("appointment_date"),
          "appointment_time": data.get("appointment_time"),
          "notes": data.get("notes", "")
      })

@app.route("/export/excel")
def export_patients_to_excel():
      # Dados de demonstração (substituir por dados reais do banco de dados)
      patients_data = [
                {"id": "P001", "name": "Maria Silva Santos", "age": 58, "gender": "Feminino", "cancerType": "Mama", "stage": "Estágio II", "status": "Em Tratamento", "registrationDate": "2024-01-15", "lastConsultation": "2024-09-20", "hospital": "Hospital Regional", "zone": "Urbana", "city": "São José da Tapera", "neighborhood": "Centro", "phone": "(82) 99999-0001", "cpf": "123.456.789-01", "treatmentStartDate": "2024-02-01", "sessions": 12, "completedSessions": 8, "observations": "Paciente respondendo bem ao tratamento. Próxima consulta agendada.", "photo": None},
                {"id": "P002", "name": "João Santos Lima", "age": 65, "gender": "Masculino", "cancerType": "Próstata", "stage": "Estágio I", "status": "Curado", "registrationDate": "2023-11-10", "lastConsultation": "2024-09-19", "hospital": "Hospital Municipal", "zone": "Rural", "city": "São José da Tapera", "neighborhood": "Zona Rural", "phone": "(82) 99999-0002", "cpf": "234.567.890-12", "treatmentStartDate": "2023-12-01", "treatmentEndDate": "2024-06-15", "sessions": 20, "completedSessions": 20, "observations": "Tratamento concluído com sucesso. Paciente em remissão completa.", "photo": None},
                {"id": "P003", "name": "Ana Costa Oliveira", "age": 42, "gender": "Feminino", "cancerType": "Pulmão", "stage": "Estágio III", "status": "Em Tratamento", "registrationDate": "2024-03-20", "lastConsultation": "2024-09-18", "hospital": "Hospital Regional", "zone": "Ur
