from tir import Webapp
import dados_Pedido  as CE
import dados_Prod as prod
import dados_teste as tst
from datetime import *
import unittest
import random 

data_atual = date.today()
data_atual_str = data_atual.strftime('%d/%m/%Y')#diretivas do objeto data_atual	
data_hora_atual = datetime.now()



class MODULO(unittest.TestCase):
	

	@classmethod
	def setUpClass(inst):

		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT',data_atual_str,'01','0101 ','99')

		inst.oHelper.Program('MATA410')
		# inst.oHelper.SetLateralMenu('Usuário > Senhas > Usuários')
		# inst.oHelper.SearchBrowse('000011')
		# inst.oHelper.SetButton('Outras Ações')
		# inst.oHelper.SetKey('DOWN',grid=False,grid_number=5)
		
	
	def test_MATA410(self):	

		linha_pedido = 0
		linha_produto = 0

		#numero de pedidos aleatorios a serem lançados 
		numero_pedidos = 2 #!!!!!!!!!!!!!!!!!!!!!!!!!!
		contador_pedidos = 0

		#self.oHelper.SetButton('Fechar')
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('0102')
		tst.atualizar_arquivo('teste_robo.txt','\n--------------------//--------------------\nTeste {}'.format(data_hora_atual))

		#while linha_pedido < CE.lin:
		while contador_pedidos < numero_pedidos:
    		
			linha_pedido = random.randint(1,CE.lin )

			#self.oHelper.SetButton('Ok')
			#self.oHelper.ClickFolder('Grupo')

			self.oHelper.SetValue(CE.CABECALHO[0],CE.COL_A[linha_pedido])
			#self.oHelper.SetValue(CE.CABECALHO[2],CE.COL_C[linha_pedido])
			self.oHelper.SetButton("Fechar")# erro aleatorio no ambiente 

			self.oHelper.SetValue(CE.CABECALHO[1],CE.COL_B[linha_pedido])
			self.oHelper.SetValue(CE.CABECALHO[3],CE.COL_D[linha_pedido])
			self.oHelper.SetValue(CE.CABECALHO[4],CE.COL_E[linha_pedido])
			self.oHelper.SetValue(CE.CABECALHO[5],CE.COL_F[linha_pedido])
			# self.oHelper.SetValue(CE.CABECALHO[6],CE.COL_G[linha_pedido])
			# self.oHelper.SetValue(CE.CABECALHO[7],CE.COL_H[linha_pedido])
			# self.oHelper.SetValue(CE.CABECALHO[8],CE.COL_I[linha_pedido])


			################# INSERIR PRODUTOS ####################
			#while linha_produto < prod.lin:

			#quantidade de produtos aleatorio entre 1 e 10
			numero_produto = random.randint(1,5) 
			contador_produto = 0

			tst.atualizar_arquivo('teste_robo.txt','\n	Nro. Pedido: {}'.format(self.oHelper.GetValue('C5_NUM')))
			tst.atualizar_arquivo('teste_robo.txt','\n		Nro. Cliente: {}'.format(CE.COL_A[linha_pedido]))
			tst.atualizar_arquivo('teste_robo.txt','\n		Qtd. Produtos: {}'.format(numero_produto))
			#tst.atualizar_arquivo('teste_robo.txt','\n    Nro. Pedido: {}\n    Nro. Cliente: {}\n    Qtd. Produtos: {}'.format(self.oHelper.GetValue('C5_NUM'),CE.CABECALHO[0],CE.COL_A[linha_pedido],numero_produto))

			while contador_produto < numero_produto:
    						
				linha_produto = random.randint(1,prod.lin -1)

				tst.atualizar_arquivo('teste_robo.txt','\n			{} - {}'.format((contador_produto+1),prod.COL_A[linha_produto]))
				#self.oHelper.ClickGridHeader(column_name = 'Produto' , grid_number =  1)

				self.oHelper.SetValue(prod.CABECALHO[0],prod.COL_A[linha_produto], grid=True)
				self.oHelper.SetValue(prod.CABECALHO[1],prod.COL_B[linha_produto], grid=True)
				#preço subiu automatico
				#self.oHelper.SetValue(prod.CABECALHO[2],prod.COL_C[linha_produto], grid=True)

				self.oHelper.SetValue(prod.CABECALHO[3],prod.COL_D[linha_produto], grid=True)
				self.oHelper.SetValue(prod.CABECALHO[4],prod.COL_E[linha_produto], grid=True)
				#self.oHelper.SetValue(prod.CABECALHO[5],prod.COL_F[linha], grid=True)
				# self.oHelper.SetValue(prod.CABECALHO[6],prod.COL_G[linha], grid=True)
				# self.oHelper.SetValue(prod.CABECALHO[7],prod.COL_H[linha], grid=True)
				
				self.oHelper.SetKey('DOWN', grid=True)
				#linha_produto = linha_produto + 1
				contador_produto = contador_produto +1 


			self.oHelper.LoadGrid()

			self.oHelper.SetButton("Salvar")
			self.oHelper.SetButton("Salvar")
			
			#linha_pedido = linha_pedido + 1
			contador_pedidos = contador_pedidos +1


		tempo_teste = datetime.now() - data_hora_atual
		tst.atualizar_arquivo('teste_robo.txt','\nTempo de exec: {}'.format(tempo_teste))
		# self.oHelper.SetValue('C5_VEND2','')

		# self.oHelper.SetButton('Outras Ações')

		self.oHelper.AssertTrue()

	
	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()