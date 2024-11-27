import requests
x = 22091035
perfil = {"email": str(x) + "@alumno.utmetropolitana.edu.mx", "pass": str(x)}
response = requests.post('https://plataforma.utmetropolitana.edu.mx/ingresar.php', data=perfil,
                             allow_redirects=False)

print(response.cookies.__dict__)
# 110178lggdguu6j9vefpsq99v4
# sdtlh9b35afm24vvu3d672lrm3}