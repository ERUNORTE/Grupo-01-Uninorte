from flask import Flask, render_template, blueprints, request
import utils
import yagmail


main = blueprints.Blueprint('main', __name__)

@main.route('/')
def index():

    return render_template("index.html")

@main.route('/BuscarAdministrador')
def BuscarAdministrador():

    return render_template("BuscarAdministrador.html")

@main.route('/BuscarCliente')
def BuscarCliente():

    return render_template("BuscarCliente.html")

@main.route('/ListaDeAdministradores')
def ListaDeAdministradores():

    return render_template("ListaDeAdministradores.html")

@main.route('/listaDeClientes')
def listaDeClientes():

    return render_template("listaDeClientes.html")

@main.route('/ListaDeHabitaciones')
def ListaDeHabitaciones():

    return render_template("ListaDeHabitaciones.html")

@main.route('/login')
def login():

    return render_template("login.html")

@main.route('/micuenta')
def micuenta():

    return render_template("micuenta.html")

@main.route('/mydata')
def mydata():

    return render_template("mydata.html")

@main.route('/NuevaHabitacion')
def NuevaHabitacion():

    return render_template("NuevaHabitacion.html")

@main.route('/NuevoAdministrador')
def NuevoAdministrador():

    return render_template("NuevoAdministrador.html")

@main.route('/terminosYcondiciones')
def terminos():

    return render_template("politicasdeprivacidad.html")

@main.route('/recuperar')
def recuperarContraseña():

    return render_template("recuperarcontraseña.html")

@main.route('/search')
def search():

    return render_template("search.html")



@main.route('/registro', methods=['GET', 'POST'])
def registro():

    if(request.method == 'POST'):

        correoUsuario=request.form['correo']
        nombreUsuario=request.form['nombre']
        claveUsuario=request.form['userPassword']

        if (not utils.isEmailValid(correoUsuario)):
            return "El correo {0}, no es correcto".format(correoUsuario)

        if(not utils.isPasswordValid(claveUsuario)):
            return "La clave no cumple con la seguridad mínima."

        cad="Hola {0}, este es un correo de pruba.".format(nombreUsuario)

            #Esto es solo una demo, Esto es seguro
        
        #try:
            #clienteMail = yagmail.SMTP("usuario@gmail.com","1234ABCDEF")
            #clienteMail.send(to=correoUsuario, subject="Activa tu cuenta", contents=cad )
        #except BaseException as e:
            #return "Error" + str(e)

        return render_template("login.html")


    return render_template("registro.html")