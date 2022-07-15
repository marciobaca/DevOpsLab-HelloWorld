from app import app
import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        # cria uma instancia do unittest, precisa do nome "setUp"
        print ('setUp')
        self.app = app.test_client()

    def test_requisicao(self):
        # envia uma requisicao GET para a URL
        print ('test_requisicao')
        result = self.app.get('/')
        print (result.status_code)

        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(result.status_code, 200) 

    def test_conteudo(self):
        # envia uma requisicao GET para a URL
        print ('test_conteudo')
        result = self.app.get('/') 
        print (result.data.decode())
        # verifica o retorno do conteudo da pagina
        self.assertRegex(result.data.decode(), "Escreva uma Mensagem para o Cabecalho da Pagina.")


if __name__ == "__main__":
    print ('INICIANDO OS TESTES')
    print('----------------------------------------------------------------------')
    unittest.main(verbosity=2)